from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from . import service
from .schemas import PostCreate

router = APIRouter()


@router.post("/", name='Добавить публикацию автору')
def create_post(item: PostCreate, db: Session = Depends(get_db)):
    return service.create_post(db, item)