from pydantic import BaseModel

class ChatroomUsers(BaseModel):
    chatroom_id: int
    user_id: int