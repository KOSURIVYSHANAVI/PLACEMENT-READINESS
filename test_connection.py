from pymongo import MongoClient

uri = "mongodb+srv://kosurivyshnavi2006_db_user:kFUrh0fPGrgGwEhi@cluster0.dx2e3xi.mongodb.net/placement_readiness_module1?retryWrites=true&w=majority"
client = MongoClient(uri, serverSelectionTimeoutMS=5000)

try:
    dbs = client.list_database_names()
    print("Connected successfully! Databases:", dbs)
except Exception as e:
    print("Connection failed:", e)