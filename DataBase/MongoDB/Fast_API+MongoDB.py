from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()
client = MongoClient("mongodb://localhost:27017/")
db = client["fastapi_db"]

@app.post("/mongo/items")
def create_item(item: dict):
    res = db["items"].insert_one(item)
    return {"id": str(res.inserted_id)}

@app.get("/mongo/items/{name}")
def get_item(name: str):
    item = db["items"].find_one({"name": name})
    if item:
        item["_id"] = str(item["_id"])
        return item
    return {"msg": "不存在"}