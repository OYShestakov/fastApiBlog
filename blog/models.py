from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from core.db import Base


class Post(Base):
    __tablename__ = 'blog_posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    created_at = Column(DateTime(), default=datetime.now)
    author_id = Column(Integer, ForeignKey("author.id"))

