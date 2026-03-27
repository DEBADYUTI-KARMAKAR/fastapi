from core.database import get_user_collection
from bson import ObjectId


class UserRepository:
    @staticmethod
    async def create_user(user_data: str):
        collection = get_user_collection()
        result = await collection.insert_one(user_data)
        return str(result.inserted_id)
    
    @staticmethod
    async def get_user_by_id(user_id: str):
        collection = get_user_collection()
        user = await collection.find_one({"_id": ObjectId(user_id)})
        return user
    @staticmethod
    async def get_all_list():
        collection = get_user_collection()
        users = await collection.find().to_list(length=100)
        for user in users:
            user["_id"] = str(user["_id"])
        return users
    @staticmethod
    async def get_user_by_email(email: str):
        collection = get_user_collection()
        return await collection.find_one({"email": email})

    @staticmethod
    async def save_refresh_token(user_id: str, refresh_token: str):
        collection = get_user_collection()
        await collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"refresh_token": refresh_token}}
        )