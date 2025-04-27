from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .base import Base


class Chatroom(Base):
    __tablename__ = "chatrooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="owned_chatrooms")
    messages = relationship("Message", back_populates="chatroom")
    settings = relationship("ChatroomSetting", back_populates="chatroom", uselist=False)
    bots = relationship("ChatroomBot", back_populates="chatroom")
    users = relationship("ChatroomUser", back_populates="chatroom")