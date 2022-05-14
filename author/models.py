from sqlalchemy import Column, String, Integer, DateTime
from core.db import Base

class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    created_at = Column(DateTime)