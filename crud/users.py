from sqlalchemy.orm import Session

import models, schemas
import dependencies


def get_password_hash(password):
    return dependencies.pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return dependencies.pwd_context.verify(plain_password, hashed_password)


# ________________GET________________



def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()



def get_user_detail(db: Session, user_id: int):
    return db.query(models.UserDetail).filter(models.UserDetail.user_id == user_id).first()


# ________________POST________________


def create_user(db: Session, user: schemas.User):
    db_user = models.User(email=user.email, password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_detail(db: Session, user_detail: schemas.UserDetailCreate, user_id: int):
    db_user_detail = models.UserDetail(**user_detail.dict(), user_id=user_id)
    db.add(db_user_detail)
    db.commit()
    db.refresh(db_user_detail)
    return db_user_detail



