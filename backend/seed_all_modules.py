from pymongo import MongoClient

# Connect to MongoDB
import os
MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://kosurivyshnavi2006_db_user:kFUrh0fPGrgGwEhi@cluster0.dx2e3xi.mongodb.net/?appName=Cluster0")
client = MongoClient(MONGO_URI)

# Module 1 Database - Questions
module1_db = client['placement_readiness_module1']
questions_collection = module1_db['questions']

# Module 2 Database - Roadmaps
module2_db = client['placement_readiness_module2']
roadmaps_collection = module2_db['roadmaps']
company_eligibility_collection = module2_db['company_eligibility']

# Clear existing data
questions_collection.delete_many({})
roadmaps_collection.delete_many({})
company_eligibility_collection.delete_many({})

# Sample Questions
quantitative_questions = [
    {
        'category': 'quantitative',
        'question_text': 'If 20% of a number is 50, what is the number?',
        'option_a': '200',
        'option_b': '250',
        'option_c': '300',
        'option_d': '350',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'A train travels 120 km in 2 hours. What is its speed?',
        'option_a': '50 km/h',
        'option_b': '60 km/h',
        'option_c': '70 km/h',
        'option_d': '80 km/h',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'What is 15% of 200?',
        'option_a': '25',
        'option_b': '30',
        'option_c': '35',
        'option_d': '40',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'If x + 5 = 12, what is x?',
        'option_a': '5',
        'option_b': '6',
        'option_c': '7',
        'option_d': '8',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'The average of 10, 20, and 30 is:',
        'option_a': '15',
        'option_b': '20',
        'option_c': '25',
        'option_d': '30',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'What is the square root of 144?',
        'option_a': '10',
        'option_b': '11',
        'option_c': '12',
        'option_d': '13',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'If a product costs $80 after a 20% discount, what was the original price?',
        'option_a': '$90',
        'option_b': '$95',
        'option_c': '$100',
        'option_d': '$105',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'What is 25% of 80?',
        'option_a': '15',
        'option_b': '20',
        'option_c': '25',
        'option_d': '30',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'If 3x = 27, what is x?',
        'option_a': '7',
        'option_b': '8',
        'option_c': '9',
        'option_d': '10',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'The ratio of 15 to 45 is:',
        'option_a': '1:2',
        'option_b': '1:3',
        'option_c': '1:4',
        'option_d': '1:5',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'What is 10% of 500?',
        'option_a': '40',
        'option_b': '45',
        'option_c': '50',
        'option_d': '55',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'If a = 5 and b = 3, what is 2a + 3b?',
        'option_a': '17',
        'option_b': '18',
        'option_c': '19',
        'option_d': '20',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'What is the value of 5²?',
        'option_a': '20',
        'option_b': '25',
        'option_c': '30',
        'option_d': '35',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'If 40% of a number is 80, what is the number?',
        'option_a': '180',
        'option_b': '200',
        'option_c': '220',
        'option_d': '240',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'What is 30% of 150?',
        'option_a': '40',
        'option_b': '45',
        'option_c': '50',
        'option_d': '55',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'The sum of angles in a triangle is:',
        'option_a': '90°',
        'option_b': '180°',
        'option_c': '270°',
        'option_d': '360°',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'If x - 8 = 15, what is x?',
        'option_a': '21',
        'option_b': '22',
        'option_c': '23',
        'option_d': '24',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'What is 50% of 200?',
        'option_a': '90',
        'option_b': '95',
        'option_c': '100',
        'option_d': '105',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'The LCM of 4 and 6 is:',
        'option_a': '10',
        'option_b': '12',
        'option_c': '14',
        'option_d': '16',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'If 2x + 5 = 15, what is x?',
        'option_a': '3',
        'option_b': '4',
        'option_c': '5',
        'option_d': '6',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'What is the cube of 3?',
        'option_a': '9',
        'option_b': '18',
        'option_c': '27',
        'option_d': '36',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'The perimeter of a square with side 5 cm is:',
        'option_a': '15 cm',
        'option_b': '20 cm',
        'option_c': '25 cm',
        'option_d': '30 cm',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'What is 75% of 80?',
        'option_a': '55',
        'option_b': '60',
        'option_c': '65',
        'option_d': '70',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'If 5x = 45, what is x?',
        'option_a': '7',
        'option_b': '8',
        'option_c': '9',
        'option_d': '10',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'The area of a rectangle with length 10 and width 5 is:',
        'option_a': '40',
        'option_b': '45',
        'option_c': '50',
        'option_d': '55',
        'correct_answer': 'C'
    },
    {
        'category': 'quantitative',
        'question_text': 'What is 20% of 250?',
        'option_a': '45',
        'option_b': '50',
        'option_c': '55',
        'option_d': '60',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'The HCF of 12 and 18 is:',
        'option_a': '4',
        'option_b': '6',
        'option_c': '8',
        'option_d': '10',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'If x/4 = 5, what is x?',
        'option_a': '15',
        'option_b': '20',
        'option_c': '25',
        'option_d': '30',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'What is 60% of 50?',
        'option_a': '25',
        'option_b': '30',
        'option_c': '35',
        'option_d': '40',
        'correct_answer': 'B'
    },
    {
        'category': 'quantitative',
        'question_text': 'The value of 8 × 7 is:',
        'option_a': '54',
        'option_b': '56',
        'option_c': '58',
        'option_d': '60',
        'correct_answer': 'B'
    }
]



# Logical Reasoning - 30 Questions
reasoning_questions = [
    {'category': 'reasoning', 'question_text': 'If all roses are flowers and some flowers are red, then:', 'option_a': 'All roses are red', 'option_b': 'Some roses may be red', 'option_c': 'No roses are red', 'option_d': 'All flowers are roses', 'correct_answer': 'B'},
    {'category': 'reasoning', 'question_text': 'Find the odd one out: 2, 4, 6, 9, 10', 'option_a': '2', 'option_b': '4', 'option_c': '9', 'option_d': '10', 'correct_answer': 'C'},
    {'category': 'reasoning', 'question_text': 'Complete the series: 2, 4, 8, 16, __', 'option_a': '20', 'option_b': '24', 'option_c': '28', 'option_d': '32', 'correct_answer': 'D'},
    {'category': 'reasoning', 'question_text': 'If A is taller than B, and B is taller than C, then:', 'option_a': 'C is tallest', 'option_b': 'A is tallest', 'option_c': 'B is tallest', 'option_d': 'Cannot determine', 'correct_answer': 'B'},
    {'category': 'reasoning', 'question_text': 'Find the next number: 1, 4, 9, 16, __', 'option_a': '20', 'option_b': '25', 'option_c': '30', 'option_d': '36', 'correct_answer': 'B'},
    {'category': 'reasoning', 'question_text': 'If CAT = 24, DOG = 26, then BAT = ?', 'option_a': '20', 'option_b': '22', 'option_c': '23', 'option_d': '24', 'correct_answer': 'C'},
    {'category': 'reasoning', 'question_text': 'Complete: ACE, BDF, CEG, __', 'option_a': 'DFH', 'option_b': 'DEF', 'option_c': 'EFG', 'option_d': 'FGH', 'correct_answer': 'A'},
    {'category': 'reasoning', 'question_text': 'If BOOK is coded as CPPL, then WORD is:', 'option_a': 'XPSE', 'option_b': 'XQSE', 'option_c': 'WQSE', 'option_d': 'WPRD', 'correct_answer': 'A'},
    {'category': 'reasoning', 'question_text': 'Find odd one: Apple, Banana, Carrot, Mango', 'option_a': 'Apple', 'option_b': 'Banana', 'option_c': 'Carrot', 'option_d': 'Mango', 'correct_answer': 'C'},
    {'category': 'reasoning', 'question_text': 'Complete: 5, 10, 20, 40, __', 'option_a': '60', 'option_b': '70', 'option_c': '80', 'option_d': '90', 'correct_answer': 'C'},
    {'category': 'reasoning', 'question_text': 'If Monday is 2 days after today, what day is today?', 'option_a': 'Wednesday', 'option_b': 'Thursday', 'option_c': 'Friday', 'option_d': 'Saturday', 'correct_answer': 'D'},
    {'category': 'reasoning', 'question_text': 'Find the missing number: 3, 6, 12, 24, __', 'option_a': '36', 'option_b': '42', 'option_c': '48', 'option_d': '54', 'correct_answer': 'C'},
    {'category': 'reasoning', 'question_text': 'If RAIN is coded as 1234, then TRAIN is:', 'option_a': '51234', 'option_b': '61234', 'option_c': '71234', 'option_d': '81234', 'correct_answer': 'A'},
    {'category': 'reasoning', 'question_text': 'Complete: AB, CD, EF, __', 'option_a': 'FG', 'option_b': 'GH', 'option_c': 'HI', 'option_d': 'IJ', 'correct_answer': 'B'},
    {'category': 'reasoning', 'question_text': 'Find odd one: 11, 13, 17, 18, 19', 'option_a': '11', 'option_b': '13', 'option_c': '17', 'option_d': '18', 'correct_answer': 'D'},
    {'category': 'reasoning', 'question_text': 'If 2 + 3 = 10, 3 + 4 = 14, then 4 + 5 = ?', 'option_a': '18', 'option_b': '20', 'option_c': '22', 'option_d': '24', 'correct_answer': 'B'},
    {'category': 'reasoning', 'question_text': 'Complete: 1, 1, 2, 3, 5, 8, __', 'option_a': '11', 'option_b': '12', 'option_c': '13', 'option_d': '14', 'correct_answer': 'C'},
    {'category': 'reasoning', 'question_text': 'If BLUE is coded as CMVF, then RED is:', 'option_a': 'SFE', 'option_b': 'SDE', 'option_c': 'TFE', 'option_d': 'TDE', 'correct_answer': 'A'},
    {'category': 'reasoning', 'question_text': 'Find the next: 100, 50, 25, __', 'option_a': '10', 'option_b': '12.5', 'option_c': '15', 'option_d': '20', 'correct_answer': 'B'},
    {'category': 'reasoning', 'question_text': 'If all birds can fly and penguin is a bird, then:', 'option_a': 'Penguin can fly', 'option_b': 'Penguin cannot fly', 'option_c': 'Statement is contradictory', 'option_d': 'Cannot determine', 'correct_answer': 'C'},
    {'category': 'reasoning', 'question_text': 'Complete: 2, 6, 12, 20, __', 'option_a': '28', 'option_b': '30', 'option_c': '32', 'option_d': '34', 'correct_answer': 'B'},
    {'category': 'reasoning', 'question_text': 'Find odd one: Circle, Square, Triangle, Rectangle', 'option_a': 'Circle', 'option_b': 'Square', 'option_c': 'Triangle', 'option_d': 'Rectangle', 'correct_answer': 'A'},
    {'category': 'reasoning', 'question_text': 'If A = 1, B = 2, then Z = ?', 'option_a': '24', 'option_b': '25', 'option_c': '26', 'option_d': '27', 'correct_answer': 'C'},
    {'category': 'reasoning', 'question_text': 'Complete: 10, 20, 30, 40, __', 'option_a': '45', 'option_b': '50', 'option_c': '55', 'option_d': '60', 'correct_answer': 'B'},
    {'category': 'reasoning', 'question_text': 'If MOTHER is coded as NPUIFS, then FATHER is:', 'option_a': 'GBUIFS', 'option_b': 'GBUIFS', 'option_c': 'GBUIFS', 'option_d': 'GBUIFS', 'correct_answer': 'A'},
    {'category': 'reasoning', 'question_text': 'Find the next: 3, 9, 27, 81, __', 'option_a': '162', 'option_b': '243', 'option_c': '324', 'option_d': '405', 'correct_answer': 'B'},
    {'category': 'reasoning', 'question_text': 'Complete: A1, B2, C3, __', 'option_a': 'D3', 'option_b': 'D4', 'option_c': 'E4', 'option_d': 'E5', 'correct_answer': 'B'},
    {'category': 'reasoning', 'question_text': 'Find odd one: 5, 10, 15, 22, 25', 'option_a': '5', 'option_b': '10', 'option_c': '22', 'option_d': '25', 'correct_answer': 'C'},
    {'category': 'reasoning', 'question_text': 'If DESK is coded as EFSL, then CHAIR is:', 'option_a': 'DIBJS', 'option_b': 'DIBJR', 'option_c': 'CIBJS', 'option_d': 'CIBJR', 'correct_answer': 'A'},
    {'category': 'reasoning', 'question_text': 'Complete: 7, 14, 28, 56, __', 'option_a': '84', 'option_b': '98', 'option_c': '112', 'option_d': '126', 'correct_answer': 'C'}
]

# Verbal Ability - 30 Questions
verbal_questions = [
    {'category': 'verbal', 'question_text': 'Synonym of HAPPY:', 'option_a': 'Sad', 'option_b': 'Joyful', 'option_c': 'Angry', 'option_d': 'Tired', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Antonym of DIFFICULT:', 'option_a': 'Hard', 'option_b': 'Tough', 'option_c': 'Easy', 'option_d': 'Complex', 'correct_answer': 'C'},
    {'category': 'verbal', 'question_text': 'Choose correct spelling:', 'option_a': 'Accomodate', 'option_b': 'Accommodate', 'option_c': 'Acomodate', 'option_d': 'Acommodate', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Synonym of BRAVE:', 'option_a': 'Coward', 'option_b': 'Fearful', 'option_c': 'Courageous', 'option_d': 'Weak', 'correct_answer': 'C'},
    {'category': 'verbal', 'question_text': 'Antonym of ANCIENT:', 'option_a': 'Old', 'option_b': 'Modern', 'option_c': 'Historic', 'option_d': 'Traditional', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Fill in the blank: She is good __ mathematics.', 'option_a': 'in', 'option_b': 'at', 'option_c': 'on', 'option_d': 'with', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Synonym of QUICK:', 'option_a': 'Slow', 'option_b': 'Fast', 'option_c': 'Lazy', 'option_d': 'Tired', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Antonym of BEAUTIFUL:', 'option_a': 'Pretty', 'option_b': 'Lovely', 'option_c': 'Ugly', 'option_d': 'Attractive', 'correct_answer': 'C'},
    {'category': 'verbal', 'question_text': 'Choose correct sentence:', 'option_a': 'He go to school', 'option_b': 'He goes to school', 'option_c': 'He going to school', 'option_d': 'He gone to school', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Synonym of INTELLIGENT:', 'option_a': 'Dumb', 'option_b': 'Smart', 'option_c': 'Foolish', 'option_d': 'Stupid', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Antonym of STRONG:', 'option_a': 'Powerful', 'option_b': 'Mighty', 'option_c': 'Weak', 'option_d': 'Robust', 'correct_answer': 'C'},
    {'category': 'verbal', 'question_text': 'Fill in: I have been waiting __ two hours.', 'option_a': 'since', 'option_b': 'for', 'option_c': 'from', 'option_d': 'at', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Synonym of LARGE:', 'option_a': 'Small', 'option_b': 'Tiny', 'option_c': 'Big', 'option_d': 'Little', 'correct_answer': 'C'},
    {'category': 'verbal', 'question_text': 'Antonym of RICH:', 'option_a': 'Wealthy', 'option_b': 'Poor', 'option_c': 'Affluent', 'option_d': 'Prosperous', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Choose correct: Neither of them __ present.', 'option_a': 'are', 'option_b': 'is', 'option_c': 'were', 'option_d': 'been', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Synonym of ANGRY:', 'option_a': 'Happy', 'option_b': 'Furious', 'option_c': 'Calm', 'option_d': 'Peaceful', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Antonym of HOT:', 'option_a': 'Warm', 'option_b': 'Burning', 'option_c': 'Cold', 'option_d': 'Heated', 'correct_answer': 'C'},
    {'category': 'verbal', 'question_text': 'Fill in: She is afraid __ dogs.', 'option_a': 'from', 'option_b': 'of', 'option_c': 'with', 'option_d': 'by', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Synonym of FAMOUS:', 'option_a': 'Unknown', 'option_b': 'Renowned', 'option_c': 'Obscure', 'option_d': 'Hidden', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Antonym of LOVE:', 'option_a': 'Like', 'option_b': 'Adore', 'option_c': 'Hate', 'option_d': 'Cherish', 'correct_answer': 'C'},
    {'category': 'verbal', 'question_text': 'Choose correct: The news __ good.', 'option_a': 'are', 'option_b': 'is', 'option_c': 'were', 'option_d': 'been', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Synonym of CLEAN:', 'option_a': 'Dirty', 'option_b': 'Spotless', 'option_c': 'Messy', 'option_d': 'Filthy', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Antonym of DARK:', 'option_a': 'Black', 'option_b': 'Dim', 'option_c': 'Light', 'option_d': 'Shadowy', 'correct_answer': 'C'},
    {'category': 'verbal', 'question_text': 'Fill in: He is senior __ me.', 'option_a': 'than', 'option_b': 'to', 'option_c': 'from', 'option_d': 'with', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Synonym of SMALL:', 'option_a': 'Large', 'option_b': 'Tiny', 'option_c': 'Big', 'option_d': 'Huge', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Antonym of EARLY:', 'option_a': 'Soon', 'option_b': 'Prompt', 'option_c': 'Late', 'option_d': 'Quick', 'correct_answer': 'C'},
    {'category': 'verbal', 'question_text': 'Choose correct: One of the boys __ absent.', 'option_a': 'are', 'option_b': 'is', 'option_c': 'were', 'option_d': 'been', 'correct_answer': 'B'},
    {'category': 'verbal', 'question_text': 'Synonym of QUIET:', 'option_a': 'Loud', 'option_b': 'Noisy', 'option_c': 'Silent', 'option_d': 'Boisterous', 'correct_answer': 'C'},
    {'category': 'verbal', 'question_text': 'Antonym of TRUE:', 'option_a': 'Correct', 'option_b': 'Right', 'option_c': 'False', 'option_d': 'Accurate', 'correct_answer': 'C'},
    {'category': 'verbal', 'question_text': 'Fill in: I am looking forward __ meeting you.', 'option_a': 'for', 'option_b': 'to', 'option_c': 'at', 'option_d': 'in', 'correct_answer': 'B'}
]



dbms_questions = [
    {'category': 'dbms', 'question_text': 'What does DBMS stand for?', 'option_a': 'Data Base Management System', 'option_b': 'Database Management Software', 'option_c': 'Data Binary Management System', 'option_d': 'Database Manipulation System', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Which SQL command is used to retrieve data?', 'option_a': 'GET', 'option_b': 'SELECT', 'option_c': 'RETRIEVE', 'option_d': 'FETCH', 'correct_answer': 'B'},
    {'category': 'dbms', 'question_text': 'Primary key must be:', 'option_a': 'Unique', 'option_b': 'Null', 'option_c': 'Duplicate', 'option_d': 'Optional', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Which is not a DDL command?', 'option_a': 'CREATE', 'option_b': 'ALTER', 'option_c': 'SELECT', 'option_d': 'DROP', 'correct_answer': 'C'},
    {'category': 'dbms', 'question_text': 'Foreign key is used for:', 'option_a': 'Uniqueness', 'option_b': 'Referential integrity', 'option_c': 'Indexing', 'option_d': 'Sorting', 'correct_answer': 'B'},
    {'category': 'dbms', 'question_text': 'Which normal form removes transitive dependency?', 'option_a': '1NF', 'option_b': '2NF', 'option_c': '3NF', 'option_d': 'BCNF', 'correct_answer': 'C'},
    {'category': 'dbms', 'question_text': 'ACID properties include:', 'option_a': 'Atomicity', 'option_b': 'Consistency', 'option_c': 'Isolation', 'option_d': 'All of the above', 'correct_answer': 'D'},
    {'category': 'dbms', 'question_text': 'Which command is used to delete a table?', 'option_a': 'DELETE', 'option_b': 'REMOVE', 'option_c': 'DROP', 'option_d': 'TRUNCATE', 'correct_answer': 'C'},
    {'category': 'dbms', 'question_text': 'JOIN is used to:', 'option_a': 'Combine rows from tables', 'option_b': 'Delete rows', 'option_c': 'Update rows', 'option_d': 'Create tables', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Which is not a type of JOIN?', 'option_a': 'INNER JOIN', 'option_b': 'OUTER JOIN', 'option_c': 'CROSS JOIN', 'option_d': 'PARALLEL JOIN', 'correct_answer': 'D'},
    {'category': 'dbms', 'question_text': 'Index is used for:', 'option_a': 'Faster retrieval', 'option_b': 'Data storage', 'option_c': 'Data deletion', 'option_d': 'Data backup', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Which is a DML command?', 'option_a': 'CREATE', 'option_b': 'INSERT', 'option_c': 'ALTER', 'option_d': 'DROP', 'correct_answer': 'B'},
    {'category': 'dbms', 'question_text': 'Candidate key is:', 'option_a': 'Minimal superkey', 'option_b': 'Foreign key', 'option_c': 'Composite key', 'option_d': 'Alternate key', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Which clause is used with SELECT to filter?', 'option_a': 'FILTER', 'option_b': 'WHERE', 'option_c': 'HAVING', 'option_d': 'CONDITION', 'correct_answer': 'B'},
    {'category': 'dbms', 'question_text': 'GROUP BY is used with:', 'option_a': 'Aggregate functions', 'option_b': 'JOIN', 'option_c': 'INDEX', 'option_d': 'VIEW', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Which is not an aggregate function?', 'option_a': 'COUNT', 'option_b': 'SUM', 'option_c': 'AVG', 'option_d': 'SELECT', 'correct_answer': 'D'},
    {'category': 'dbms', 'question_text': 'Transaction ends with:', 'option_a': 'COMMIT or ROLLBACK', 'option_b': 'START', 'option_c': 'BEGIN', 'option_d': 'END', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'View is a:', 'option_a': 'Physical table', 'option_b': 'Virtual table', 'option_c': 'Index', 'option_d': 'Key', 'correct_answer': 'B'},
    {'category': 'dbms', 'question_text': 'Which key can have NULL values?', 'option_a': 'Primary key', 'option_b': 'Foreign key', 'option_c': 'Candidate key', 'option_d': 'Super key', 'correct_answer': 'B'},
    {'category': 'dbms', 'question_text': 'Normalization is used to:', 'option_a': 'Reduce redundancy', 'option_b': 'Increase redundancy', 'option_c': 'Delete data', 'option_d': 'Backup data', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Which is not a constraint?', 'option_a': 'NOT NULL', 'option_b': 'UNIQUE', 'option_c': 'CHECK', 'option_d': 'VERIFY', 'correct_answer': 'D'},
    {'category': 'dbms', 'question_text': 'TRUNCATE command:', 'option_a': 'Deletes all rows', 'option_b': 'Deletes table structure', 'option_c': 'Updates rows', 'option_d': 'Creates table', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Which isolation level is highest?', 'option_a': 'READ UNCOMMITTED', 'option_b': 'READ COMMITTED', 'option_c': 'REPEATABLE READ', 'option_d': 'SERIALIZABLE', 'correct_answer': 'D'},
    {'category': 'dbms', 'question_text': 'Deadlock occurs when:', 'option_a': 'Two transactions wait for each other', 'option_b': 'Transaction commits', 'option_c': 'Transaction rolls back', 'option_d': 'Database starts', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Which is not a database model?', 'option_a': 'Relational', 'option_b': 'Hierarchical', 'option_c': 'Network', 'option_d': 'Sequential', 'correct_answer': 'D'},
    {'category': 'dbms', 'question_text': 'ER diagram stands for:', 'option_a': 'Entity Relationship', 'option_b': 'Entity Record', 'option_c': 'Entry Relationship', 'option_d': 'Entry Record', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Cardinality refers to:', 'option_a': 'Number of rows', 'option_b': 'Number of columns', 'option_c': 'Number of tables', 'option_d': 'Number of databases', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Which command saves changes?', 'option_a': 'SAVE', 'option_b': 'COMMIT', 'option_c': 'STORE', 'option_d': 'PERSIST', 'correct_answer': 'B'},
    {'category': 'dbms', 'question_text': 'Stored procedure is:', 'option_a': 'Precompiled SQL code', 'option_b': 'Table', 'option_c': 'Index', 'option_d': 'View', 'correct_answer': 'A'},
    {'category': 'dbms', 'question_text': 'Which is fastest to retrieve data?', 'option_a': 'Full table scan', 'option_b': 'Index scan', 'option_c': 'Sequential scan', 'option_d': 'Random scan', 'correct_answer': 'B'}
]

# Computer Networks - 30 Questions
cn_questions = [
    {'category': 'cn', 'question_text': 'OSI model has how many layers?', 'option_a': '5', 'option_b': '6', 'option_c': '7', 'option_d': '8', 'correct_answer': 'C'},
    {'category': 'cn', 'question_text': 'Which layer is responsible for routing?', 'option_a': 'Physical', 'option_b': 'Data Link', 'option_c': 'Network', 'option_d': 'Transport', 'correct_answer': 'C'},
    {'category': 'cn', 'question_text': 'TCP is a:', 'option_a': 'Connection-oriented protocol', 'option_b': 'Connectionless protocol', 'option_c': 'Physical layer protocol', 'option_d': 'Application protocol', 'correct_answer': 'A'},
    {'category': 'cn', 'question_text': 'IP address version 4 is:', 'option_a': '16-bit', 'option_b': '32-bit', 'option_c': '64-bit', 'option_d': '128-bit', 'correct_answer': 'B'},
    {'category': 'cn', 'question_text': 'Which protocol is used for email?', 'option_a': 'HTTP', 'option_b': 'FTP', 'option_c': 'SMTP', 'option_d': 'DNS', 'correct_answer': 'C'},
    {'category': 'cn', 'question_text': 'Default port for HTTP is:', 'option_a': '21', 'option_b': '22', 'option_c': '80', 'option_d': '443', 'correct_answer': 'C'},
    {'category': 'cn', 'question_text': 'MAC address is:', 'option_a': '32-bit', 'option_b': '48-bit', 'option_c': '64-bit', 'option_d': '128-bit', 'correct_answer': 'B'},
    {'category': 'cn', 'question_text': 'Which device works at Network layer?', 'option_a': 'Hub', 'option_b': 'Switch', 'option_c': 'Router', 'option_d': 'Repeater', 'correct_answer': 'C'},
    {'category': 'cn', 'question_text': 'DNS stands for:', 'option_a': 'Domain Name System', 'option_b': 'Domain Network System', 'option_c': 'Data Name System', 'option_d': 'Data Network System', 'correct_answer': 'A'},
    {'category': 'cn', 'question_text': 'Which is not a network topology?', 'option_a': 'Star', 'option_b': 'Ring', 'option_c': 'Bus', 'option_d': 'Square', 'correct_answer': 'D'},
    {'category': 'cn', 'question_text': 'FTP uses which port?', 'option_a': '20', 'option_b': '21', 'option_c': '22', 'option_d': '23', 'correct_answer': 'B'},
    {'category': 'cn', 'question_text': 'Which protocol is connectionless?', 'option_a': 'TCP', 'option_b': 'UDP', 'option_c': 'HTTP', 'option_d': 'FTP', 'correct_answer': 'B'},
    {'category': 'cn', 'question_text': 'Subnet mask is used for:', 'option_a': 'Network identification', 'option_b': 'Host identification', 'option_c': 'Both A and B', 'option_d': 'None', 'correct_answer': 'C'},
    {'category': 'cn', 'question_text': 'Which layer handles encryption?', 'option_a': 'Physical', 'option_b': 'Data Link', 'option_c': 'Presentation', 'option_d': 'Application', 'correct_answer': 'C'},
    {'category': 'cn', 'question_text': 'HTTPS uses port:', 'option_a': '80', 'option_b': '443', 'option_c': '8080', 'option_d': '8443', 'correct_answer': 'B'},
    {'category': 'cn', 'question_text': 'Which is a private IP range?', 'option_a': '192.168.x.x', 'option_b': '8.8.8.8', 'option_c': '1.1.1.1', 'option_d': '4.4.4.4', 'correct_answer': 'A'},
    {'category': 'cn', 'question_text': 'ARP stands for:', 'option_a': 'Address Resolution Protocol', 'option_b': 'Address Routing Protocol', 'option_c': 'Application Resolution Protocol', 'option_d': 'Application Routing Protocol', 'correct_answer': 'A'},
    {'category': 'cn', 'question_text': 'Which device works at Data Link layer?', 'option_a': 'Hub', 'option_b': 'Switch', 'option_c': 'Router', 'option_d': 'Gateway', 'correct_answer': 'B'},
    {'category': 'cn', 'question_text': 'Ping uses which protocol?', 'option_a': 'TCP', 'option_b': 'UDP', 'option_c': 'ICMP', 'option_d': 'HTTP', 'correct_answer': 'C'},
    {'category': 'cn', 'question_text': 'Which is not a routing protocol?', 'option_a': 'RIP', 'option_b': 'OSPF', 'option_c': 'BGP', 'option_d': 'HTTP', 'correct_answer': 'D'},
    {'category': 'cn', 'question_text': 'Bandwidth is measured in:', 'option_a': 'Bytes', 'option_b': 'Bits per second', 'option_c': 'Packets', 'option_d': 'Frames', 'correct_answer': 'B'},
    {'category': 'cn', 'question_text': 'Which is a connection-oriented protocol?', 'option_a': 'UDP', 'option_b': 'IP', 'option_c': 'TCP', 'option_d': 'ICMP', 'correct_answer': 'C'},
    {'category': 'cn', 'question_text': 'NAT stands for:', 'option_a': 'Network Address Translation', 'option_b': 'Network Application Translation', 'option_c': 'Node Address Translation', 'option_d': 'Node Application Translation', 'correct_answer': 'A'},
    {'category': 'cn', 'question_text': 'Which layer is closest to user?', 'option_a': 'Physical', 'option_b': 'Network', 'option_c': 'Transport', 'option_d': 'Application', 'correct_answer': 'D'},
    {'category': 'cn', 'question_text': 'Firewall works at which layer?', 'option_a': 'Physical', 'option_b': 'Network', 'option_c': 'Transport', 'option_d': 'All layers', 'correct_answer': 'D'},
    {'category': 'cn', 'question_text': 'Which protocol is used for file transfer?', 'option_a': 'HTTP', 'option_b': 'FTP', 'option_c': 'SMTP', 'option_d': 'DNS', 'correct_answer': 'B'},
    {'category': 'cn', 'question_text': 'Loopback address is:', 'option_a': '192.168.1.1', 'option_b': '127.0.0.1', 'option_c': '10.0.0.1', 'option_d': '172.16.0.1', 'correct_answer': 'B'},
    {'category': 'cn', 'question_text': 'Which is not a network device?', 'option_a': 'Router', 'option_b': 'Switch', 'option_c': 'Hub', 'option_d': 'Compiler', 'correct_answer': 'D'},
    {'category': 'cn', 'question_text': 'DHCP is used for:', 'option_a': 'Dynamic IP allocation', 'option_b': 'Static IP allocation', 'option_c': 'DNS resolution', 'option_d': 'Routing', 'correct_answer': 'A'},
    {'category': 'cn', 'question_text': 'Which protocol is secure?', 'option_a': 'HTTP', 'option_b': 'FTP', 'option_c': 'HTTPS', 'option_d': 'Telnet', 'correct_answer': 'C'}
]



# Operating Systems - 30 Questions
os_questions = [
    {'category': 'os', 'question_text': 'Which is not an OS?', 'option_a': 'Windows', 'option_b': 'Linux', 'option_c': 'Oracle', 'option_d': 'macOS', 'correct_answer': 'C'},
    {'category': 'os', 'question_text': 'Process is:', 'option_a': 'Program in execution', 'option_b': 'Program on disk', 'option_c': 'Compiled code', 'option_d': 'Source code', 'correct_answer': 'A'},
    {'category': 'os', 'question_text': 'Which scheduling algorithm is non-preemptive?', 'option_a': 'Round Robin', 'option_b': 'FCFS', 'option_c': 'Priority', 'option_d': 'Multilevel', 'correct_answer': 'B'},
    {'category': 'os', 'question_text': 'Deadlock occurs when:', 'option_a': 'Mutual exclusion', 'option_b': 'Hold and wait', 'option_c': 'No preemption', 'option_d': 'All of the above', 'correct_answer': 'D'},
    {'category': 'os', 'question_text': 'Virtual memory uses:', 'option_a': 'RAM only', 'option_b': 'Disk only', 'option_c': 'RAM and Disk', 'option_d': 'Cache only', 'correct_answer': 'C'},
    {'category': 'os', 'question_text': 'Page fault occurs when:', 'option_a': 'Page is in memory', 'option_b': 'Page is not in memory', 'option_c': 'Page is deleted', 'option_d': 'Page is created', 'correct_answer': 'B'},
    {'category': 'os', 'question_text': 'Semaphore is used for:', 'option_a': 'Synchronization', 'option_b': 'Scheduling', 'option_c': 'Memory management', 'option_d': 'File management', 'correct_answer': 'A'},
    {'category': 'os', 'question_text': 'Which is not a process state?', 'option_a': 'Ready', 'option_b': 'Running', 'option_c': 'Waiting', 'option_d': 'Sleeping', 'correct_answer': 'D'},
    {'category': 'os', 'question_text': 'Context switching is:', 'option_a': 'Switching between processes', 'option_b': 'Switching between threads', 'option_c': 'Switching between users', 'option_d': 'Both A and B', 'correct_answer': 'D'},
    {'category': 'os', 'question_text': 'Which is a memory allocation technique?', 'option_a': 'First Fit', 'option_b': 'Best Fit', 'option_c': 'Worst Fit', 'option_d': 'All of the above', 'correct_answer': 'D'},
    {'category': 'os', 'question_text': 'Thrashing occurs when:', 'option_a': 'Too many page faults', 'option_b': 'Too few page faults', 'option_c': 'No page faults', 'option_d': 'Page is loaded', 'correct_answer': 'A'},
    {'category': 'os', 'question_text': 'Which is not a file access method?', 'option_a': 'Sequential', 'option_b': 'Direct', 'option_c': 'Indexed', 'option_d': 'Parallel', 'correct_answer': 'D'},
    {'category': 'os', 'question_text': 'Kernel is:', 'option_a': 'Core of OS', 'option_b': 'Application', 'option_c': 'User interface', 'option_d': 'File system', 'correct_answer': 'A'},
    {'category': 'os', 'question_text': 'Which is a real-time OS?', 'option_a': 'Windows', 'option_b': 'VxWorks', 'option_c': 'Ubuntu', 'option_d': 'macOS', 'correct_answer': 'B'},
    {'category': 'os', 'question_text': 'Spooling is used for:', 'option_a': 'CPU scheduling', 'option_b': 'I/O operations', 'option_c': 'Memory management', 'option_d': 'Process creation', 'correct_answer': 'B'},
    {'category': 'os', 'question_text': 'Which is not a deadlock prevention method?', 'option_a': 'Mutual exclusion', 'option_b': 'Hold and wait', 'option_c': 'Circular wait', 'option_d': 'Aging', 'correct_answer': 'D'},
    {'category': 'os', 'question_text': 'PCB stands for:', 'option_a': 'Process Control Block', 'option_b': 'Program Control Block', 'option_c': 'Process Code Block', 'option_d': 'Program Code Block', 'correct_answer': 'A'},
    {'category': 'os', 'question_text': 'Which scheduling gives minimum average waiting time?', 'option_a': 'FCFS', 'option_b': 'SJF', 'option_c': 'Round Robin', 'option_d': 'Priority', 'correct_answer': 'B'},
    {'category': 'os', 'question_text': 'Paging is a:', 'option_a': 'Memory management technique', 'option_b': 'Scheduling technique', 'option_c': 'File management technique', 'option_d': 'I/O technique', 'correct_answer': 'A'},
    {'category': 'os', 'question_text': 'Which is not an IPC mechanism?', 'option_a': 'Pipe', 'option_b': 'Message Queue', 'option_c': 'Shared Memory', 'option_d': 'Cache', 'correct_answer': 'D'},
    {'category': 'os', 'question_text': 'Critical section is:', 'option_a': 'Code accessing shared resource', 'option_b': 'Code with errors', 'option_c': 'Code with loops', 'option_d': 'Code with functions', 'correct_answer': 'A'},
    {'category': 'os', 'question_text': 'Which is a disk scheduling algorithm?', 'option_a': 'FCFS', 'option_b': 'SCAN', 'option_c': 'C-SCAN', 'option_d': 'All of the above', 'correct_answer': 'D'},
    {'category': 'os', 'question_text': 'Fragmentation is of how many types?', 'option_a': '1', 'option_b': '2', 'option_c': '3', 'option_d': '4', 'correct_answer': 'B'},
    {'category': 'os', 'question_text': 'Which is not a thread type?', 'option_a': 'User thread', 'option_b': 'Kernel thread', 'option_c': 'Hybrid thread', 'option_d': 'Virtual thread', 'correct_answer': 'D'},
    {'category': 'os', 'question_text': 'Mutex is used for:', 'option_a': 'Mutual exclusion', 'option_b': 'Scheduling', 'option_c': 'Memory allocation', 'option_d': 'File access', 'correct_answer': 'A'},
    {'category': 'os', 'question_text': 'Which is not a file attribute?', 'option_a': 'Name', 'option_b': 'Type', 'option_c': 'Size', 'option_d': 'Speed', 'correct_answer': 'D'},
    {'category': 'os', 'question_text': 'Interrupt is:', 'option_a': 'Signal to CPU', 'option_b': 'Error', 'option_c': 'Process', 'option_d': 'Thread', 'correct_answer': 'A'},
    {'category': 'os', 'question_text': 'Which is a page replacement algorithm?', 'option_a': 'FIFO', 'option_b': 'LRU', 'option_c': 'Optimal', 'option_d': 'All of the above', 'correct_answer': 'D'},
    {'category': 'os', 'question_text': 'Belady anomaly occurs in:', 'option_a': 'FIFO', 'option_b': 'LRU', 'option_c': 'Optimal', 'option_d': 'All', 'correct_answer': 'A'},
    {'category': 'os', 'question_text': 'Which is not a system call?', 'option_a': 'fork()', 'option_b': 'exec()', 'option_c': 'wait()', 'option_d': 'print()', 'correct_answer': 'D'}
]

# Coding - 30 Questions
coding_questions = [
    {'category': 'coding', 'question_text': 'What is the output of: print(2 ** 3)?', 'option_a': '6', 'option_b': '8', 'option_c': '9', 'option_d': '5', 'correct_answer': 'B'},
    {'category': 'coding', 'question_text': 'Which loop is entry-controlled?', 'option_a': 'for', 'option_b': 'while', 'option_c': 'do-while', 'option_d': 'Both A and B', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Array index starts from:', 'option_a': '0', 'option_b': '1', 'option_c': '-1', 'option_d': 'Depends on language', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Which is not a data type?', 'option_a': 'int', 'option_b': 'float', 'option_c': 'char', 'option_d': 'loop', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Function returns:', 'option_a': 'Value', 'option_b': 'Nothing', 'option_c': 'Both A and B', 'option_d': 'Error', 'correct_answer': 'C'},
    {'category': 'coding', 'question_text': 'Which is a comparison operator?', 'option_a': '=', 'option_b': '==', 'option_c': '===', 'option_d': 'Both B and C', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Recursion uses:', 'option_a': 'Stack', 'option_b': 'Queue', 'option_c': 'Array', 'option_d': 'List', 'correct_answer': 'A'},
    {'category': 'coding', 'question_text': 'Which is not a loop?', 'option_a': 'for', 'option_b': 'while', 'option_c': 'if', 'option_d': 'do-while', 'correct_answer': 'C'},
    {'category': 'coding', 'question_text': 'String is:', 'option_a': 'Mutable', 'option_b': 'Immutable', 'option_c': 'Both', 'option_d': 'Depends on language', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Which is a logical operator?', 'option_a': 'AND', 'option_b': 'OR', 'option_c': 'NOT', 'option_d': 'All of the above', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Exception handling uses:', 'option_a': 'try-catch', 'option_b': 'if-else', 'option_c': 'switch', 'option_d': 'loop', 'correct_answer': 'A'},
    {'category': 'coding', 'question_text': 'Which is not a programming paradigm?', 'option_a': 'OOP', 'option_b': 'Functional', 'option_c': 'Procedural', 'option_d': 'Sequential', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Variable scope can be:', 'option_a': 'Local', 'option_b': 'Global', 'option_c': 'Both A and B', 'option_d': 'None', 'correct_answer': 'C'},
    {'category': 'coding', 'question_text': 'Which is a conditional statement?', 'option_a': 'if', 'option_b': 'switch', 'option_c': 'Both A and B', 'option_d': 'for', 'correct_answer': 'C'},
    {'category': 'coding', 'question_text': 'Pointer stores:', 'option_a': 'Value', 'option_b': 'Address', 'option_c': 'Both', 'option_d': 'None', 'correct_answer': 'B'},
    {'category': 'coding', 'question_text': 'Which is not an OOP concept?', 'option_a': 'Encapsulation', 'option_b': 'Inheritance', 'option_c': 'Polymorphism', 'option_d': 'Compilation', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Constructor is called when:', 'option_a': 'Object is created', 'option_b': 'Object is destroyed', 'option_c': 'Method is called', 'option_d': 'Class is defined', 'correct_answer': 'A'},
    {'category': 'coding', 'question_text': 'Which is a bitwise operator?', 'option_a': '&', 'option_b': '|', 'option_c': '^', 'option_d': 'All of the above', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Static variable is:', 'option_a': 'Shared by all instances', 'option_b': 'Unique to each instance', 'option_c': 'Local to function', 'option_d': 'None', 'correct_answer': 'A'},
    {'category': 'coding', 'question_text': 'Which is not a sorting algorithm?', 'option_a': 'Bubble Sort', 'option_b': 'Quick Sort', 'option_c': 'Merge Sort', 'option_d': 'Linear Sort', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Time complexity of linear search is:', 'option_a': 'O(1)', 'option_b': 'O(n)', 'option_c': 'O(log n)', 'option_d': 'O(n²)', 'correct_answer': 'B'},
    {'category': 'coding', 'question_text': 'Which is a searching algorithm?', 'option_a': 'Binary Search', 'option_b': 'Linear Search', 'option_c': 'Both A and B', 'option_d': 'None', 'correct_answer': 'C'},
    {'category': 'coding', 'question_text': 'Abstract class can have:', 'option_a': 'Abstract methods', 'option_b': 'Concrete methods', 'option_c': 'Both A and B', 'option_d': 'None', 'correct_answer': 'C'},
    {'category': 'coding', 'question_text': 'Interface can have:', 'option_a': 'Only abstract methods', 'option_b': 'Only concrete methods', 'option_c': 'Both', 'option_d': 'Depends on language', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Which is not a collection?', 'option_a': 'List', 'option_b': 'Set', 'option_c': 'Map', 'option_d': 'Loop', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Garbage collection is:', 'option_a': 'Automatic memory management', 'option_b': 'Manual memory management', 'option_c': 'Error handling', 'option_d': 'None', 'correct_answer': 'A'},
    {'category': 'coding', 'question_text': 'Which is a wrapper class?', 'option_a': 'Integer', 'option_b': 'Float', 'option_c': 'Boolean', 'option_d': 'All of the above', 'correct_answer': 'D'},
    {'category': 'coding', 'question_text': 'Method overloading is:', 'option_a': 'Same name, different parameters', 'option_b': 'Different name, same parameters', 'option_c': 'Same name, same parameters', 'option_d': 'None', 'correct_answer': 'A'},
    {'category': 'coding', 'question_text': 'Method overriding is:', 'option_a': 'In same class', 'option_b': 'In parent-child class', 'option_c': 'In interface', 'option_d': 'None', 'correct_answer': 'B'},
    {'category': 'coding', 'question_text': 'Which is not a access modifier?', 'option_a': 'public', 'option_b': 'private', 'option_c': 'protected', 'option_d': 'hidden', 'correct_answer': 'D'}
]



dsa_questions = [
    {'category': 'dsa', 'question_text': 'Time complexity of binary search is:', 'option_a': 'O(n)', 'option_b': 'O(log n)', 'option_c': 'O(n²)', 'option_d': 'O(1)', 'correct_answer': 'B'},
    {'category': 'dsa', 'question_text': 'Which data structure uses LIFO?', 'option_a': 'Queue', 'option_b': 'Stack', 'option_c': 'Tree', 'option_d': 'Graph', 'correct_answer': 'B'},
    {'category': 'dsa', 'question_text': 'Which data structure uses FIFO?', 'option_a': 'Stack', 'option_b': 'Queue', 'option_c': 'Tree', 'option_d': 'Graph', 'correct_answer': 'B'},
    {'category': 'dsa', 'question_text': 'Array elements are stored in:', 'option_a': 'Contiguous memory', 'option_b': 'Random memory', 'option_c': 'Heap', 'option_d': 'Stack', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'Linked list node contains:', 'option_a': 'Data only', 'option_b': 'Pointer only', 'option_c': 'Data and pointer', 'option_d': 'None', 'correct_answer': 'C'},
    {'category': 'dsa', 'question_text': 'Time complexity of insertion in array at end is:', 'option_a': 'O(1)', 'option_b': 'O(n)', 'option_c': 'O(log n)', 'option_d': 'O(n²)', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'Which is not a tree traversal?', 'option_a': 'Inorder', 'option_b': 'Preorder', 'option_c': 'Postorder', 'option_d': 'Sideorder', 'correct_answer': 'D'},
    {'category': 'dsa', 'question_text': 'Binary tree has maximum how many children?', 'option_a': '1', 'option_b': '2', 'option_c': '3', 'option_d': 'Unlimited', 'correct_answer': 'B'},
    {'category': 'dsa', 'question_text': 'BST stands for:', 'option_a': 'Binary Search Tree', 'option_b': 'Best Search Tree', 'option_c': 'Binary Sort Tree', 'option_d': 'Basic Search Tree', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'Hash table uses:', 'option_a': 'Hash function', 'option_b': 'Sort function', 'option_c': 'Search function', 'option_d': 'None', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'Time complexity of bubble sort is:', 'option_a': 'O(n)', 'option_b': 'O(n log n)', 'option_c': 'O(n²)', 'option_d': 'O(log n)', 'correct_answer': 'C'},
    {'category': 'dsa', 'question_text': 'Quick sort uses:', 'option_a': 'Divide and conquer', 'option_b': 'Greedy', 'option_c': 'Dynamic programming', 'option_d': 'Backtracking', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'Merge sort time complexity is:', 'option_a': 'O(n)', 'option_b': 'O(n log n)', 'option_c': 'O(n²)', 'option_d': 'O(log n)', 'correct_answer': 'B'},
    {'category': 'dsa', 'question_text': 'Heap is a:', 'option_a': 'Complete binary tree', 'option_b': 'Incomplete binary tree', 'option_c': 'Graph', 'option_d': 'List', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'DFS uses:', 'option_a': 'Stack', 'option_b': 'Queue', 'option_c': 'Array', 'option_d': 'Tree', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'BFS uses:', 'option_a': 'Stack', 'option_b': 'Queue', 'option_c': 'Array', 'option_d': 'Tree', 'correct_answer': 'B'},
    {'category': 'dsa', 'question_text': 'Graph can be represented using:', 'option_a': 'Adjacency matrix', 'option_b': 'Adjacency list', 'option_c': 'Both A and B', 'option_d': 'None', 'correct_answer': 'C'},
    {'category': 'dsa', 'question_text': 'Dijkstra algorithm is used for:', 'option_a': 'Shortest path', 'option_b': 'Longest path', 'option_c': 'Sorting', 'option_d': 'Searching', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'AVL tree is:', 'option_a': 'Balanced BST', 'option_b': 'Unbalanced BST', 'option_c': 'Binary tree', 'option_d': 'Graph', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'Trie is used for:', 'option_a': 'String operations', 'option_b': 'Number operations', 'option_c': 'Sorting', 'option_d': 'Searching', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'Priority queue can be implemented using:', 'option_a': 'Heap', 'option_b': 'Array', 'option_c': 'Linked list', 'option_d': 'All of the above', 'correct_answer': 'D'},
    {'category': 'dsa', 'question_text': 'Circular queue overcomes:', 'option_a': 'Memory wastage', 'option_b': 'Time complexity', 'option_c': 'Space complexity', 'option_d': 'None', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'Doubly linked list has:', 'option_a': 'One pointer', 'option_b': 'Two pointers', 'option_c': 'Three pointers', 'option_d': 'No pointer', 'correct_answer': 'B'},
    {'category': 'dsa', 'question_text': 'Recursion uses which data structure internally?', 'option_a': 'Queue', 'option_b': 'Stack', 'option_c': 'Array', 'option_d': 'Tree', 'correct_answer': 'B'},
    {'category': 'dsa', 'question_text': 'Dynamic programming uses:', 'option_a': 'Memoization', 'option_b': 'Tabulation', 'option_c': 'Both A and B', 'option_d': 'None', 'correct_answer': 'C'},
    {'category': 'dsa', 'question_text': 'Greedy algorithm always gives:', 'option_a': 'Optimal solution', 'option_b': 'Local optimal solution', 'option_c': 'No solution', 'option_d': 'Wrong solution', 'correct_answer': 'B'},
    {'category': 'dsa', 'question_text': 'Space complexity of recursive fibonacci is:', 'option_a': 'O(1)', 'option_b': 'O(n)', 'option_c': 'O(log n)', 'option_d': 'O(n²)', 'correct_answer': 'B'},
    {'category': 'dsa', 'question_text': 'Which is not a graph algorithm?', 'option_a': 'Dijkstra', 'option_b': 'Bellman-Ford', 'option_c': 'Floyd-Warshall', 'option_d': 'Bubble Sort', 'correct_answer': 'D'},
    {'category': 'dsa', 'question_text': 'Topological sort is used in:', 'option_a': 'DAG', 'option_b': 'Cyclic graph', 'option_c': 'Tree', 'option_d': 'Array', 'correct_answer': 'A'},
    {'category': 'dsa', 'question_text': 'Kruskal algorithm is used for:', 'option_a': 'Minimum spanning tree', 'option_b': 'Maximum spanning tree', 'option_c': 'Shortest path', 'option_d': 'Sorting', 'correct_answer': 'A'}
]

# Python Programming - 30 Questions
python_questions = [
    {'category': 'python', 'question_text': 'Python is:', 'option_a': 'Compiled', 'option_b': 'Interpreted', 'option_c': 'Both', 'option_d': 'None', 'correct_answer': 'B'},
    {'category': 'python', 'question_text': 'Which is not a Python data type?', 'option_a': 'list', 'option_b': 'tuple', 'option_c': 'array', 'option_d': 'dict', 'correct_answer': 'C'},
    {'category': 'python', 'question_text': 'List is:', 'option_a': 'Mutable', 'option_b': 'Immutable', 'option_c': 'Both', 'option_d': 'None', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Tuple is:', 'option_a': 'Mutable', 'option_b': 'Immutable', 'option_c': 'Both', 'option_d': 'None', 'correct_answer': 'B'},
    {'category': 'python', 'question_text': 'Dictionary stores data as:', 'option_a': 'Key-value pairs', 'option_b': 'Only values', 'option_c': 'Only keys', 'option_d': 'Array', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Which keyword is used to define a function?', 'option_a': 'function', 'option_b': 'def', 'option_c': 'func', 'option_d': 'define', 'correct_answer': 'B'},
    {'category': 'python', 'question_text': 'Python file extension is:', 'option_a': '.py', 'option_b': '.python', 'option_c': '.pt', 'option_d': '.p', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Which is used for comments?', 'option_a': '//', 'option_b': '/* */', 'option_c': '#', 'option_d': '--', 'correct_answer': 'C'},
    {'category': 'python', 'question_text': 'Range(5) generates:', 'option_a': '1,2,3,4,5', 'option_b': '0,1,2,3,4', 'option_c': '0,1,2,3,4,5', 'option_d': '1,2,3,4', 'correct_answer': 'B'},
    {'category': 'python', 'question_text': 'Which is not a loop in Python?', 'option_a': 'for', 'option_b': 'while', 'option_c': 'do-while', 'option_d': 'None', 'correct_answer': 'C'},
    {'category': 'python', 'question_text': 'Lambda function is:', 'option_a': 'Anonymous function', 'option_b': 'Named function', 'option_c': 'Class', 'option_d': 'Module', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Which is used to handle exceptions?', 'option_a': 'try-except', 'option_b': 'if-else', 'option_c': 'switch', 'option_d': 'loop', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Self keyword is used in:', 'option_a': 'Functions', 'option_b': 'Classes', 'option_c': 'Loops', 'option_d': 'Conditions', 'correct_answer': 'B'},
    {'category': 'python', 'question_text': '__init__ is:', 'option_a': 'Constructor', 'option_b': 'Destructor', 'option_c': 'Method', 'option_d': 'Variable', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Which is not a Python framework?', 'option_a': 'Django', 'option_b': 'Flask', 'option_c': 'FastAPI', 'option_d': 'React', 'correct_answer': 'D'},
    {'category': 'python', 'question_text': 'Pip is used for:', 'option_a': 'Package management', 'option_b': 'Compilation', 'option_c': 'Debugging', 'option_d': 'Testing', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Which is used to import modules?', 'option_a': 'include', 'option_b': 'import', 'option_c': 'require', 'option_d': 'use', 'correct_answer': 'B'},
    {'category': 'python', 'question_text': 'List comprehension syntax is:', 'option_a': '[x for x in range(5)]', 'option_b': '{x for x in range(5)}', 'option_c': '(x for x in range(5))', 'option_d': 'All', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Which is not a string method?', 'option_a': 'upper()', 'option_b': 'lower()', 'option_c': 'split()', 'option_d': 'push()', 'correct_answer': 'D'},
    {'category': 'python', 'question_text': 'Len() function returns:', 'option_a': 'Length', 'option_b': 'Size', 'option_c': 'Count', 'option_d': 'All', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Which is used for type conversion?', 'option_a': 'int()', 'option_b': 'str()', 'option_c': 'float()', 'option_d': 'All of the above', 'correct_answer': 'D'},
    {'category': 'python', 'question_text': 'None is:', 'option_a': 'Null value', 'option_b': 'Zero', 'option_c': 'Empty string', 'option_d': 'False', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Which is not a comparison operator?', 'option_a': '==', 'option_b': '!=', 'option_c': '=', 'option_d': '>=', 'correct_answer': 'C'},
    {'category': 'python', 'question_text': 'Global keyword is used to:', 'option_a': 'Access global variable', 'option_b': 'Create global variable', 'option_c': 'Modify global variable', 'option_d': 'All', 'correct_answer': 'D'},
    {'category': 'python', 'question_text': 'Which is used for file handling?', 'option_a': 'open()', 'option_b': 'read()', 'option_c': 'write()', 'option_d': 'All of the above', 'correct_answer': 'D'},
    {'category': 'python', 'question_text': 'Inheritance is implemented using:', 'option_a': 'class Child(Parent):', 'option_b': 'class Child extends Parent:', 'option_c': 'class Child inherits Parent:', 'option_d': 'None', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Which is not a Python keyword?', 'option_a': 'pass', 'option_b': 'break', 'option_c': 'continue', 'option_d': 'exit', 'correct_answer': 'D'},
    {'category': 'python', 'question_text': 'Decorator is denoted by:', 'option_a': '@', 'option_b': '#', 'option_c': '$', 'option_d': '%', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Which is used for multiple inheritance?', 'option_a': 'class Child(Parent1, Parent2):', 'option_b': 'class Child extends Parent1, Parent2:', 'option_c': 'class Child inherits Parent1, Parent2:', 'option_d': 'None', 'correct_answer': 'A'},
    {'category': 'python', 'question_text': 'Yield keyword is used in:', 'option_a': 'Generators', 'option_b': 'Functions', 'option_c': 'Classes', 'option_d': 'Loops', 'correct_answer': 'A'}
]

questions_collection.insert_many(quantitative_questions)
questions_collection.insert_many(reasoning_questions)
questions_collection.insert_many(verbal_questions)
questions_collection.insert_many(dbms_questions)
questions_collection.insert_many(cn_questions)
questions_collection.insert_many(os_questions)
questions_collection.insert_many(coding_questions)
questions_collection.insert_many(dsa_questions)
questions_collection.insert_many(python_questions)



# Sample Roadmaps
roadmaps = [
    {'category': 'quantitative', 'title': 'Master Quantitative Aptitude', 'description': 'Build strong foundation in mathematics and problem-solving', 'resources': 'Khan Academy, Indiabix Aptitude', 'duration': '3 weeks'},
    {'category': 'reasoning', 'title': 'Logical Reasoning Mastery', 'description': 'Improve analytical and logical thinking skills', 'resources': 'RS Aggarwal, Puzzles and riddles', 'duration': '2 weeks'},
    {'category': 'verbal', 'title': 'English Proficiency', 'description': 'Enhance vocabulary and grammar skills', 'resources': 'Wren & Martin, Word Power Made Easy', 'duration': '4 weeks'},
    {'category': 'dbms', 'title': 'Database Fundamentals', 'description': 'Learn SQL, normalization, and database design', 'resources': 'GeeksforGeeks DBMS, W3Schools SQL', 'duration': '3 weeks'},
    {'category': 'cn', 'title': 'Computer Networks Basics', 'description': 'Understand networking concepts and protocols', 'resources': 'Kurose & Ross, Cisco Networking', 'duration': '4 weeks'},
    {'category': 'os', 'title': 'Operating Systems Concepts', 'description': 'Master process management and memory concepts', 'resources': 'Galvin OS book, Tutorialspoint', 'duration': '3 weeks'},
    {'category': 'coding', 'title': 'Data Structures & Algorithms', 'description': 'Practice coding problems and algorithms', 'resources': 'LeetCode, HackerRank, Striver SDE Sheet', 'duration': '8 weeks'},
    {'category': 'dsa', 'title': 'Master Data Structures & Algorithms', 'description': 'Learn arrays, linked lists, trees, graphs and algorithms', 'resources': 'GeeksforGeeks DSA, Striver SDE Sheet, LeetCode', 'duration': '8 weeks'},
    {'category': 'python', 'title': 'Python Programming Mastery', 'description': 'Learn Python from basics to advanced including OOP and libraries', 'resources': 'Python.org docs, Automate the Boring Stuff, LeetCode Python', 'duration': '6 weeks'},

]

# Sample Companies
companies = [
    {'name': 'TCS', 'min_score': 60, 'roles': ['Software Engineer', 'System Engineer'], 'package': '3.5-7 LPA'},
    {'name': 'Infosys', 'min_score': 65, 'roles': ['Software Developer', 'System Engineer'], 'package': '4-8 LPA'},
    {'name': 'Wipro', 'min_score': 60, 'roles': ['Project Engineer', 'Developer'], 'package': '3.5-7 LPA'},
    {'name': 'Cognizant', 'min_score': 70, 'roles': ['Programmer Analyst', 'Developer'], 'package': '4-8 LPA'},
    {'name': 'Accenture', 'min_score': 70, 'roles': ['Application Developer', 'Analyst'], 'package': '4.5-9 LPA'},
    {'name': 'Amazon', 'min_score': 80, 'roles': ['SDE-1', 'Software Engineer'], 'package': '15-30 LPA'},
    {'name': 'Google', 'min_score': 85, 'roles': ['Software Engineer', 'SDE'], 'package': '20-40 LPA'},
]

# Insert data

roadmaps_collection.insert_many(roadmaps)
company_eligibility_collection.insert_many(companies)


print(f"✅ Added {len(roadmaps)} roadmaps to Module 2 database")
print(f"✅ Added {len(companies)} companies to Module 2 database")
print("\n🎉 Database seeded successfully!")
print("\nNow you can:")
print("1. Take tests as student")
print("2. View career guidance")
print("3. Check analytics")
print("4. See company eligibility")
