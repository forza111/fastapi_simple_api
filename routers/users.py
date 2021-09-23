from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
import schemas
import crud.users
import dependencies

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


@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(db: Session = Depends(get_db),
                                 form_data: dependencies.OAuth2PasswordRequestForm = Depends()):
    user = crud.users.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=dependencies.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud.users.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# ________________GET_______________


@router.get("/me", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(crud.users.get_current_user)):
    return current_user
