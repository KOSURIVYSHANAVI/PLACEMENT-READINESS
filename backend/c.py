from pymongo import MongoClient
import os

# Use your actual MONGO_URI here
uri = os.environ.get("mongodb+srv://kosurivyshnavi2006_db_user:kFUrh0fPGrgGwEhi@cluster0.dx2e3xi.mongodb.net/?appName=Cluster0")  # or paste the full URI directly for testing

try:
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)  # 5 seconds timeout
    dbs = client.list_database_names()
    print("Connected successfully! Databases:", dbs)
except Exception as e:
    print("Connection failed:", e)