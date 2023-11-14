from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from routes import router

app = FastAPI()

app.include_router(router)