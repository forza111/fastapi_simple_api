from typing import List, Optional

from pydantic import BaseModel


# ________TOKEN_________

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


# ________USER_________

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


# ________USER_DETAIL_________

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