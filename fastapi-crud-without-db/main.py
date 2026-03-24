from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

class User(BaseModel):
    id: int 
    name: str
    phone: str
    email: str
    password: str
    confirm_password: str
users: List[User] = []

@app.get("/")
def root():
    return {
        "message":"Hello Fast api"
    }
@app.post("/user")
def addData(user: User):
    users.append(user)
    return {
        "message":"User add successfully!",
        "status": "201",
        "data": user
    }
@app.get("/alllist")
def all_list():
    return{
        "message": "User fetch successfully!",
        "status": "200",
        "data":users
    }
@app.get("/user/get/{user_id}")
def get_by_id(user_id: int):
    for us in users:
        if us.id == user_id:
            return {
                "message" : "User data fetch successfully!",
                "status" : "200",
                "data" : us
            }
@app.put("/user/{user_id}")
def update_by_id(user_id: int,user: User):
    for us in users:
        if us.id == user_id:
            users.remove(us)
            users.append(user)
            return {
                "message" : "User data updated successfully!",
                "status" : "200",
                "data" : user
            }


@app.delete("/user/{user_id}")
def delete_by_id(user_id: int):
    for us in users:
        if us.id == user_id:
            users.remove(us)
            return {
                "message" : "User data deleted successfully!",
                "status" : "200",
            }
