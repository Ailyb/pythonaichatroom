from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class User(UserCreate):
    id: int
    created_at: datetime

class UserLogin(BaseModel):
    email: EmailStr
    password: str