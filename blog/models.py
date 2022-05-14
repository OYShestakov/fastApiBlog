from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base


class Post(Base):
    __tablename__ = 'blog_posts'
    id = Column(Integer, primary_key=True, unique=True, index=True)
    author = Column(Integer, ForeignKey("author.id"))
    author_id = relationship("Author")
    title = Column(String)
    created_at = Column(DateTime)

