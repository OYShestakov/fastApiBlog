from pydantic import BaseModel
from datetime import datetime

class AuthorList(BaseModel):
    id: int
    date: datetime

    class Config:
        orm_mode = True