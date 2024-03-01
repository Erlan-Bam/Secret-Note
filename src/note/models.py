from sqlalchemy import Column, Integer, String
from database import Base

class Note(Base):
    __tablename__ = 'Note'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    text = Column(String, nullable=False)
    hashed_id = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)