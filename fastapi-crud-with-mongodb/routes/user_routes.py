from fastapi import APIRouter
from models.user_model import User
from services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
async def create_user(user: User):
    await UserService.create_user(user)
    return {
        "message": "User is created successfully!",
        "status": "200"
    }
@router.get("/alllist")
async def all_list():
    all_list_data = await UserService.get_all_list()
    return {
        "message": "All data fetch successfully!!",
        "status": "200",
        "data": all_list_data
    }

@router.get("/{user_id}")
async def get_user(user_id: str):
    user_data = await UserService.get_user(user_id)
    return {
        "message": "User data fetch successfully!!",
        "status": "200",
        "data": user_data
    }