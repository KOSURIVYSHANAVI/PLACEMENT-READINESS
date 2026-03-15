from pymongo import MongoClient
import os

# Set your MongoDB Atlas URI here (or use environment variable)
MONGO_URI = "mongodb+srv://kosurivyshnavi2006_db_user:kFUrh0fPGrgGwEhi@cluster0.dx2e3xi.mongodb.net/?retryWrites=true&w=majority"

# Use environment variable if you want
# MONGO_URI = os.environ.get("MONGO_URI")

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)  # 5 sec timeout
    # List databases to test connection
    dbs = client.list_database_names()
    print("✅ Connected to MongoDB Atlas!")
    print("Databases:", dbs)
except Exception as e:
    print("❌ Connection failed:", e)