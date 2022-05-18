from pydantic import BaseModel
from datetime import datetime


class PostBase(BaseModel):
    title: str
    created_at: datetime

    class Config:
        orm_mode = True


class PostList(PostBase):
    id: int
    author_id: int = None


class PostCreate(PostBase):

    author_id: int


class AuthorBase(BaseModel):
    name: str
    email: str
    created_at: datetime

    class Config:
        orm_mode = True


class AuthorList(AuthorBase):
    id: int
    posts: list = []


class AuthorListCount(AuthorBase):
    id: int
    count_posts: int = 0


class AuthorCreate(AuthorBase):
    pass