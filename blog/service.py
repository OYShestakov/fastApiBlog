from sqlalchemy.orm import Session
from blog.models import Post
from author.models import Author
from .schemas import PostCreate, AuthorCreate


def get_author_list(db: Session, author_id: int):
    """Получаем информацию об авторе и списке его публикаций по ID"""
    return db.query(Author).filter(Author.id == author_id).all()

# def get_author(db: Session, author_id: int):
#     return db.query(Post).where(Post.author_id == author_id)
#     return db.query(Post).all()

def get_post_count(db: Session):
    """Получаем информацию о количестве публикаций авторов"""
    return db.query(Post).count()


def create_author(db: Session, item: AuthorCreate):
    """Добавляем автора"""
    author = Author(**item.dict())
    db.add(author)
    db.commit()
    db.refresh(author)
    return author


def create_post(db: Session, item: PostCreate):
    """Добавляем публикацию автору"""
    post = Post(**item.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def get_author_post_count(db: Session):
    """Получаем всех авторов и количество публикаций"""
    author = db.query(Author).all()
    post = db.query(Author.posts).count()
    # author['posts'] = post
    print(post)
    return author


def get_post_list(db: Session, author_id: int):
    """Получаем все публикации авторов"""
    return db.query(Post).filter(Post.author_id == author_id).all()


