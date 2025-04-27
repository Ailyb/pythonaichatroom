from pydantic import BaseModel
from datetime import datetime


class MessageCreate(BaseModel):
    chatroom_id: int
    sender_id: int
    message: str


class Message(MessageCreate):
    id: int
    timestamp: datetime