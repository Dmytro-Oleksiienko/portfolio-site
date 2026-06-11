from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from .models import Message
from fastapi.middleware.cors import CORSMiddleware
import os

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Load allowed origins from environment variable; defaults to all origins in development
cors_origins = os.environ.get("CORS_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)
class ContactMessage(BaseModel):
    name: str
    email: EmailStr
    message: str


@app.post("/contact")
def send_message(data: ContactMessage, db: Session = Depends(get_db)):
    msg = Message(name=data.name, email=data.email, message=data.message)
    db.add(msg)
    db.commit()
    return {"status": "ok"}


@app.get("/")
def root():
    return {"message": "Contact API is running"}