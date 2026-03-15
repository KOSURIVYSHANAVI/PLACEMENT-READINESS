from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
from werkzeug.utils import safe_join
import bcrypt
import random
from datetime import datetime, timezone
import os

app = Flask(__name__)
CORS(app)

# -------------------------------
# Serve React frontend
# -------------------------------
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    build_dir = os.path.join(os.path.dirname(__file__), 'frontend_build')
    if path != "" and os.path.exists(safe_join(build_dir, path)):
        return send_from_directory(build_dir, path)
    return send_from_directory(build_dir, 'index.html')

# -------------------------------
# MongoDB Connection
# -------------------------------
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.server_info()
    print("MongoDB connected successfully!")
except Exception as e:
    print("MongoDB connection failed:", e)

# -------------------------------
# Databases & Collections
# -------------------------------
db1 = client['placement_readiness_module1']
db2 = client['placement_readiness_module2']
db4 = client['placement_readiness_module4']

students_col = db1['students']
questions_col = db1['questions']
test_results_col = db1['test_results']

roadmaps_col = db2['roadmaps']
job_roles_col = db2['job_roles']
company_col = db2['company_eligibility']

admins_col = db4['admins']
subjects_col = db4['subjects']

# -------------------------------
# Index creation
# -------------------------------
students_col.create_index('email', unique=True)
questions_col.create_index('category')
test_results_col.create_index([('student_id', 1), ('submitted_at', -1)])
roadmaps_col.create_index('category')
job_roles_col.create_index('required_skills')
company_col.create_index('min_score')
admins_col.create_index('email', unique=True)
subjects_col.create_index('key', unique=True)

# -------------------------------
# MODULE 1 - STUDENT REGISTRATION / LOGIN / TESTS
# -------------------------------
@app.route('/api/student/register', methods=['POST'])
def register():
    data = request.json
    if students_col.find_one({'email': data['email']}):
        return jsonify({'error': 'Email already exists'}), 400
    hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    result = students_col.insert_one({
        'name': data['name'],
        'email': data['email'],
        'password': hashed,
        'created_at': datetime.now(timezone.utc)
    })
    return jsonify({'message': 'Registration successful', 'student_id': str(result.inserted_id)}), 201

@app.route('/api/student/login', methods=['POST'])
def login():
    data = request.json
    student = students_col.find_one({'email': data['email']})
    if not student or not bcrypt.checkpw(data['password'].encode('utf-8'), student['password']):
        return jsonify({'error': 'Invalid credentials'}), 401
    return jsonify({'message': 'Login successful', 'student_id': str(student['_id']), 'name': student['name']}), 200

@app.route('/api/questions/<category>', methods=['GET'])
def get_questions(category):
    questions = list(questions_col.find(
        {'category': category},
        {'_id': 1, 'question_text': 1, 'option_a': 1, 'option_b': 1, 'option_c': 1, 'option_d': 1}
    ))
    for q in questions:
        q['id'] = str(q['_id'])
        del q['_id']
    random.shuffle(questions)
    return jsonify(questions[:10]), 200

@app.route('/api/test/submit', methods=['POST'])
def submit_test():
    data = request.json
    answers = data['answers']
    question_ids = [ObjectId(a['question_id']) for a in answers]
    questions = {str(q['_id']): q for q in questions_col.find({'_id': {'$in': question_ids}})}

    score = sum(1 for a in answers if questions.get(a['question_id'], {}).get('correct_answer') == a['selected_answer'])
    total = len(answers)
    percentage = (score / total * 100) if total > 0 else 0
    readiness_score = percentage * 0.8

    test_results_col.insert_one({
        'student_id': data['student_id'],
        'category': data['category'],
        'score': score,
        'total': total,
        'percentage': percentage,
        'readiness_score': readiness_score,
        'submitted_at': datetime.now(timezone.utc)
    })
    return jsonify({'score': score, 'total': total, 'percentage': percentage, 'readiness_score': readiness_score}), 200

@app.route('/api/results/<student_id>', methods=['GET'])
def get_results(student_id):
    results = list(test_results_col.find({'student_id': student_id}))
    for r in results:
        r['id'] = str(r['_id'])
        del r['_id']
        r['submitted_at'] = r['submitted_at'].strftime('%Y-%m-%d %H:%M:%S')
    return jsonify(results), 200

# -------------------------------
# MODULE 2 - CAREER GUIDANCE
# -------------------------------
@app.route('/api/guidance/roadmap/<student_id>', methods=['GET'])
def get_personalized_roadmap(student_id):
    results = list(test_results_col.find({'student_id': student_id}))
    weak_areas = [r['category'] for r in results if r['percentage'] < 60]
    if not weak_areas:
        return jsonify({'message': 'No weak areas found', 'roadmaps': [], 'weak_areas': []})
    roadmaps = list(roadmaps_col.find({'category': {'$in': weak_areas}}))
    return jsonify({
        'weak_areas': weak_areas,
        'roadmaps': [{'id': str(r['_id']), 'category': r['category'], 'title': r['title'],
                      'description': r['description'], 'resources': r['resources'],
                      'duration': r['duration'], 'learning_path': r.get('learning_path', [])} for r in roadmaps]
    })

@app.route('/api/guidance/job-roles/<student_id>', methods=['GET'])
def get_suitable_job_roles(student_id):
    results = list(test_results_col.find({'student_id': student_id}))
    strong_skills = [r['category'] for r in results if r['percentage'] >= 70]
    if not strong_skills:
        return jsonify({'message': 'Complete more assessments', 'job_roles': [], 'strong_skills': []})
    job_roles = list(job_roles_col.find({'required_skills': {'$in': strong_skills}}))
    return jsonify({
        'strong_skills': strong_skills,
        'job_roles': [{'id': str(j['_id']), 'title': j['title'], 'description': j['description'],
                       'required_skills': j['required_skills'], 'salary_range': j.get('salary_range', 'Not specified')} for j in job_roles]
    })

@app.route('/api/guidance/company-eligibility/<student_id>', methods=['GET'])
def check_company_eligibility(student_id):
    pipeline = [{'$match': {'student_id': student_id}}, {'$group': {'_id': None, 'avg_score': {'$avg': '$percentage'}}}]
    result = list(test_results_col.aggregate(pipeline))
    if not result:
        return jsonify({'message': 'No test results found', 'eligible_companies': []})
    avg_score = result[0]['avg_score']
    eligible = list(company_col.find({'min_score': {'$lte': avg_score}}, {'name': 1, 'min_score': 1, 'roles': 1, 'package': 1}))
    return jsonify({
        'average_score': avg_score,
        'eligible_companies': [{'name': c['name'], 'min_score': c['min_score'], 'roles': c.get('roles', []), 'package': c.get('package', 'Not specified')} for c in eligible],
        'total_eligible': len(eligible)
    })

# -------------------------------
# MODULE 3 - ANALYTICS
# -------------------------------
@app.route('/api/analytics/dashboard/<student_id>', methods=['GET'])
def get_analytics_dashboard(student_id):
    pipeline = [
        {'$match': {'student_id': student_id}},
        {'$group': {'_id': None, 'total_tests': {'$sum': 1}, 'average_score': {'$avg': '$percentage'},
                    'highest_score': {'$max': '$percentage'}, 'lowest_score': {'$min': '$percentage'},
                    'categories': {'$addToSet': '$category'}}}
    ]
    result = list(test_results_col.aggregate(pipeline))
    if not result:
        return jsonify({'message': 'No data available', 'total_tests': 0, 'average_score': 0, 'highest_score': 0, 'lowest_score': 0})
    d = result[0]
    return jsonify({
        'total_tests': d['total_tests'],
        'average_score': round(d['average_score'], 2),
        'highest_score': round(d['highest_score'], 2),
        'lowest_score': round(d['lowest_score'], 2),
        'categories_attempted': len(d['categories'])
    })

@app.route('/api/analytics/chart/<student_id>', methods=['GET'])
def get_chart_data(student_id):
    results = list(test_results_col.find({'student_id': student_id}))
    categories, scores = [], []
    for r in results:
        if r['category'] not in categories:
            categories.append(r['category'])
            scores.append(r['percentage'])
    return jsonify({'categories': categories, 'scores': scores, 'chart_type': 'bar'})

@app.route('/api/analytics/timeline/<student_id>', methods=['GET'])
def get_readiness_timeline(student_id):
    results = list(test_results_col.find({'student_id': student_id}).sort('submitted_at', 1))
    return jsonify({
        'timeline': [{'date': r['submitted_at'].strftime('%Y-%m-%d %H:%M'), 'category': r['category'],
                      'readiness_score': r.get('readiness_score', 0), 'percentage': r['percentage']} for r in results]
    })

@app.route('/api/analytics/comparison/<student_id>', methods=['GET'])
def compare_scores(student_id):
    results = list(test_results_col.find({'student_id': student_id}).sort('submitted_at', -1))
    comparisons = {}
    for r in results:
        cat = r['category']
        if cat not in comparisons:
            comparisons[cat] = {'current': r['percentage'], 'previous': None, 'improvement': 0}
        else:
            comparisons[cat]['previous'] = r['percentage']
            comparisons[cat]['improvement'] = comparisons[cat]['current'] - r['percentage']
    return jsonify({'comparisons': comparisons})

# -------------------------------
# MODULE 4 - ADMIN
# -------------------------------
@app.route('/api/admin/login', methods=['POST'])
def login_admin():
    data = request.json
    if data['email'] == 'admin@placement.com' and data['password'] == 'admin123':
        return jsonify({'message': 'Login successful', 'admin_id': 'admin_001', 'name': 'Admin'}), 200
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/api/admin/analytics', methods=['GET'])
def get_system_analytics():
    total_students = students_col.count_documents({})
    total_tests = test_results_col.count_documents({})
    total_questions = questions_col.count_documents({})
    total_roadmaps = roadmaps_col.count_documents({})
    result = list(test_results_col.aggregate([{'$group': {'_id': None, 'avg': {'$avg': '$percentage'}}}]))
    avg_performance = round(result[0]['avg'], 2) if result else 0
    category_stats = list(test_results_col.aggregate([
        {'$group': {'_id': '$category', 'avg_score': {'$avg': '$percentage'}, 'count': {'$sum': 1}}}
    ]))
    return jsonify({
        'total_students': total_students,
        'total_tests': total_tests,
        'total_questions': total_questions,
        'total_roadmaps': total_roadmaps,
        'avg_performance': avg_performance,
        'category_stats': [{'category': s['_id'], 'avg_score': round(s['avg_score'], 2), 'attempts': s['count']} for s in category_stats]
    })

@app.route('/api/admin/questions', methods=['POST'])
def add_question():
    data = request.json
    questions_col.insert_one({**data, 'created_at': datetime.now(timezone.utc)})
    return jsonify({'message': 'Question added successfully'}), 201

@app.route('/api/admin/questions', methods=['GET'])
def get_all_questions():
    questions = list(questions_col.find())
    return jsonify([{'id': str(q['_id']), 'category': q['category'],
                     'question_text': q['question_text'], 'correct_answer': q['correct_answer']} for q in questions])

@app.route('/api/admin/questions/count', methods=['GET'])
def get_question_counts():
    counts = list(questions_col.aggregate([{'$group': {'_id': '$category', 'count': {'$sum': 1}}}]))
    return jsonify([{'category': c['_id'], 'count': c['count']} for c in counts])

@app.route('/api/admin/roadmaps', methods=['POST'])
def add_roadmap():
    data = request.json
    roadmaps_col.insert_one({**data, 'created_at': datetime.now(timezone.utc)})
    return jsonify({'message': 'Roadmap added successfully'}), 201

@app.route('/api/admin/roadmaps', methods=['GET'])
def get_all_roadmaps():
    roadmaps = list(roadmaps_col.find())
    return jsonify([{'id': str(r['_id']), 'category': r['category'], 'title': r['title'],
                     'description': r['description'], 'resources': r['resources'], 'duration': r['duration']} for r in roadmaps])

@app.route('/api/admin/companies', methods=['POST'])
def add_company():
    data = request.json
    company_col.insert_one({**data, 'created_at': datetime.now(timezone.utc)})
    return jsonify({'message': 'Company added successfully'}), 201

@app.route('/api/admin/subjects', methods=['POST'])
def add_subject():
    data = request.json
    subjects_col.insert_one({**data, 'created_at': datetime.now(timezone.utc)})
    return jsonify({'message': 'Subject added successfully'}), 201

@app.route('/api/admin/subjects', methods=['GET'])
def get_all_subjects():
    subjects = list(subjects_col.find())
    return jsonify([{'id': str(s['_id']), 'key': s['key'], 'name': s['name'], 'icon': s.get('icon', '📚')} for s in subjects])


    students = list(students_col.find())
    result = []
    for s in students:
        student_id = str(s['_id'])
        results = list(test_results_col.find({'student_id': student_id}))
        avg = round(sum(r['percentage'] for r in results) / len(results), 2) if results else 0
        result.append({
            'id': student_id,
            'name': s['name'],
            'email': s['email'],
            'tests_taken': len(results),
            'average_score': avg,
            'readiness_status': 'Ready' if avg >= 70 else 'Needs Improvement',
            'registered_at': s['created_at'].strftime('%Y-%m-%d')
        })
    return jsonify({'students': result, 'total': len(result)})

# -------------------------------
# Run Server
# -------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)