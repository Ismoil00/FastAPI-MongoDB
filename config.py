from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://ismoil:ismoil@myfirstcluster.11mqx2p.mongodb.net/?retryWrites=true&w=majority"
)

db = client.todo_db

collection_name = db["todo_collection"]
