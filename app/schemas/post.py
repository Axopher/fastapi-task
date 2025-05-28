from pydantic import BaseModel, constr
from typing import List

class PostCreate(BaseModel):
    text: constr(max_length=1024 * 1024)  # Validate max 1MB

class PostOut(BaseModel):
    id: int
    text: str

    class Config:
        orm_mode = True
