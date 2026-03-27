from fastapi import APIRouter

from schemas.login_schema import LoginRequest
from services.auth_service import AuthService
from services.user_service import UserService

router = APIRouter(prefix="/auth")

@router.post("/login")
async def login(data: LoginRequest):
    return await AuthService.login(data)
@router.post("/refresh")
async def refresh(data: dict):
    return await AuthService.refresh_token(data["refresh_token"])