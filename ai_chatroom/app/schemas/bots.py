from pydantic import BaseModel
from datetime import datetime

class BotCreate(BaseModel):
    name: str
    description: str | None = None
    personality: str | None = None

class Bot(BotCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True