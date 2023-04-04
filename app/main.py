from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post,user,auth,vote
from pydantic import BaseSettings
from .config import settings


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Settings(BaseSettings):
     DATABASE_HOSTNAME: str 
     DATABASE_PORT: str 
     DATABASE_PASSWORD: str 
     DATABASE_NAME: str 
     DATABASE_USERNAME: str 
     SECRET_KEY:str 
     ALGORITHM:str 
     ACCESS_TOKEN_EXPIRE_MINUTES:int

     class Config:
        env_file = ".env"

settings = Settings()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)



@app.get("/")
async def root():
    return {"message": "Hello World"}







