from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ChatroomCreate(BaseModel):
    name: str
    description: Optional[str] = None
    owner_id: int


class Chatroom(ChatroomCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True