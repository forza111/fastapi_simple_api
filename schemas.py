from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True



class UserDetail(BaseModel):
    user_id: int
    username: str
    full_name: str
    age: int
    groups_id: int = None

    class Config:
        orm_mode = True