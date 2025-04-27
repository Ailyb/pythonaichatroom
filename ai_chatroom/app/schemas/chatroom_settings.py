from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ChatroomSettingsCreate(BaseModel):
    chatroom_id: int
    theme: Optional[str] = None
    max_users: Optional[int] = None
    is_public: bool = True


class ChatroomSettings(ChatroomSettingsCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True