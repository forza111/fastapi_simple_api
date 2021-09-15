from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import schemas
import crud


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


# ________________POST________________


@router.post("/",response_model=schemas.User)
async def create_user(user: schemas.User, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


# ________________GET________________


