from utils.jwt import create_access_token, create_refresh_token, verify_token
from utils.hash import verify_password
from fastapi import HTTPException
from repository.user_repository import UserRepository
from jose import JWTError

class AuthService:

    @staticmethod
    async def login(data):
        user = await UserRepository.get_user_by_email(data.email)

        if not user:
            raise HTTPException(status_code=400, detail="User not found")

        if not verify_password(data.password, user["password"]):
            raise HTTPException(status_code=400, detail="Invalid credentials")

        payload = {"sub": str(user["_id"])}

        return {
            "access_token": create_access_token(payload),
            "refresh_token": create_refresh_token(payload),
            "token_type": "bearer"
        }
   
   
    @staticmethod
    async def refresh_token(refresh_token: str):
        try:
            payload = verify_token(refresh_token)

            if payload.get("type") != "refresh":
                raise Exception("Invalid token type")

            user_id = payload.get("sub")

            user = await UserRepository.get_user_by_id(user_id)

            if user["refresh_token"] != refresh_token:
                raise Exception("Token mismatch")

            new_access_token = create_access_token({"sub": user_id})

            return {"access_token": new_access_token}

        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid token")