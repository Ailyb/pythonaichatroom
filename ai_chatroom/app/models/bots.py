from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .base import Base


class Bot(Base):
    __tablename__ = "bots"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    personality = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())