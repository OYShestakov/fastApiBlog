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
    id: int
    name: str
    email: str
    created_at: datetime

    class Config:
        orm_mode = True


class AuthorList(AuthorBase):
    pass


class AuthorCreate(AuthorBase):
    pass