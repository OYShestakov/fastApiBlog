from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from blog import service
from blog.schemas import AuthorCreate, AuthorList, AuthorListCount

router = APIRouter()


@router.get("/{author_id}", response_model=List[AuthorList], name='Все публикации автора')
def get_author_list(author_id: int, db: Session = Depends(get_db)):
    return service.get_author_list(db, author_id)


@router.post("/", name='Добавить автора')
def create_author(item: AuthorCreate, db: Session = Depends(get_db)):
    return service.create_author(db, item)


@router.get("/", response_model=List[AuthorListCount], name='Получить всех авторов и количество публикаций')
def get_author_post_count(db: Session = Depends(get_db)):
    return service.get_author_post_count(db)




