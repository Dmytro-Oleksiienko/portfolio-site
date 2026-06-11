from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    message = Column(String)
    created_at = Column(DateTime, default=datetime.now)