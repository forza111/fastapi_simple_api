from typing import List, Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True



class UserDetailBase(BaseModel):
    username: str
    full_name: str
    age: int


class UserDetailCreate(UserDetailBase):
    pass


class UserDetail(UserDetailBase):
    user_id: int

    class Config:
        orm_mode = True