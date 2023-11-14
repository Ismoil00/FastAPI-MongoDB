from fastapi import APIRouter
from config import collection_name
from models import ToDo
from schemas import list_serial
from bson import ObjectId

router = APIRouter()


# GET Request Method:
@router.get("/read")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos


# POST Request Method:
@router.post("/create")
async def create_todo(todo: ToDo):
    collection_name.insert_one(dict(todo))
    return "Success!"


# PUT Request Method:
@router.put("/update/{id}")
async def update_todo(id: str, todo: ToDo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
    return "Success!"


# DELETE Request Method:
@router.delete("/delete/{id}")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return "Success!"
