from sqlalchemy import Column, Integer, ForeignKey, Table
from .base import Base

class ChatroomUsers(Base):
     __tablename__ = "chatroom_users"
 
     chatroom_id = Column(Integer, ForeignKey("chatrooms.id"), primary_key=True)
     user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)