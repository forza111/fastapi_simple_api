from typing import List, Optional

from pydantic import BaseModel, EmailStr, validator

# ________TOKEN_________

class Token(BaseModel):
    access_token: str
    token_type: str


# ________USER_________

class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str

    @validator('password')
    def password_validator(cls, v):
        if len(v) < 6:
            raise ValueError("Password length must be at least 6 characters")
        return v


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