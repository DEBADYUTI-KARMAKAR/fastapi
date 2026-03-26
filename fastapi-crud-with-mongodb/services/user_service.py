from repository.user_repository import UserRepository
from fastapi import HTTPException

class UserService:
    @staticmethod
    async def create_user(user):
        user_dict = user.dict()
        user_id = await UserRepository.create_user(user_dict)
        return user_id
    @staticmethod
    async def get_user(user_id: str):
        user = await UserRepository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        user["_id"] = str(user["_id"])
        return user
    
    @staticmethod
    async def get_all_list():
        all_list = await UserRepository.get_all_list()
        print("eeeee",all_list)
        return all_list
    