from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base


class ChatroomSettings(Base):
    __tablename__ = "chatroom_settings"

    id = Column(Integer, primary_key=True, index=True)
    chatroom_id = Column(Integer, ForeignKey("chatrooms.id"), unique=True, nullable=False)
    theme = Column(String, nullable=True)
    max_users = Column(Integer, nullable=True)
    is_public = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    chatroom = relationship("Chatroom", back_populates="settings")