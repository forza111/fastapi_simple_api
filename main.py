from typing import List

import uvicorn

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

# from testing_sql import models
# from testing_sql import schemas, crud
from database import SessionLocal, engine, Base
from routers import users


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



app.include_router(users.router)



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)