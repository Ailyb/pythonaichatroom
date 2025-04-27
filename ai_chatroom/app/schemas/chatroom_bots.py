from pydantic import BaseModel

class ChatroomBots(BaseModel):
    chatroom_id: int
    bot_id: int