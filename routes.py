from fastapi import APIRouter

from author import author_post
from blog import blog

routes = APIRouter()

routes.include_router(blog.router, prefix="/post")
routes.include_router(author_post.router, prefix="/author")

