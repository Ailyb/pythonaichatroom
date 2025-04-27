from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base

class ChatroomBots(Base):
    __tablename__ = "chatroom_bots"
    chatroom_id = Column(Integer, ForeignKey("chatrooms.id"), primary_key=True)
    bot_id = Column(Integer, ForeignKey("bots.id"), primary_key=True)