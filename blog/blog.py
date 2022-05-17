from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from . import service
from .schemas import PostCreate, PostList

router = APIRouter()


# @router.get("/{author_id}", response_model=List[PostList], name='Все публикации автора без автора')
# def get_post_list(author_id: int, db: Session = Depends(get_db)):
#     return service.get_post_list(db, author_id)


@router.post("/", name='Добавить публикацию автору')
def create_post(item: PostCreate, db: Session = Depends(get_db)):
    return service.create_post(db, item)


# @router.get("/", response_model=List[PostList], name='Количество публикаций авторов')
# def get_post_count(db: Session = Depends(get_db)):
#     return service.get_post_count(db)
