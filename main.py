import uvicorn
from fastapi import Depends, FastAPI, HTTPException

from database import engine, Base
from routers import users


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)