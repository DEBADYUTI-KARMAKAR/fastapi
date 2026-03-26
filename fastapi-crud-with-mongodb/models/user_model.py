from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None
    name: str
    phone: str
    email: str
    password: str
    