from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
import schemas
from crud.authentication import get_current_user
import crud.users

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


# ________________POST________________


@router.post("/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.users.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.users.create_user(db=db, user=user)


@router.post("/{user_id}/create_user_detail", response_model=schemas.UserDetail)
async def create_user_detail(user_id: int, user_detail: schemas.UserDetailCreate, db: Session = Depends(get_db)):
    db_user_detail = crud.users.get_user_detail(db, user_id=user_id)
    if db_user_detail:
        raise HTTPException(status_code=400, detail="You can create user information only once")
    return crud.users.create_user_detail(db=db, user_detail=user_detail, user_id=user_id)


# ________________GET_______________


@router.get("/me", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(get_current_user)):
    return current_user
