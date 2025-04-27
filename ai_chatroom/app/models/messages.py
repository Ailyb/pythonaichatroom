from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from .base import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    chatroom_id = Column(Integer, ForeignKey("chatrooms.id"), nullable=False)
    sender_id = Column(Integer, nullable=False)
    message = Column(Text, nullable=False)
    timestamp = Column(DateTime, server_default=func.now())