from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_URL)
db = client["myuserdbfastapi"]
def get_user_collection():
    return db["users"]