from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models import chatrooms as models
from app.schemas import chatrooms as schemas

router = APIRouter(
    prefix="/chatrooms",
    tags=["chatrooms"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_chatroom(chatroom: schemas.ChatroomCreate, db: Session = Depends(get_db)):
    return {"message": "Chatroom created"}

@router.get("/")
def get_chatroom(db: Session = Depends(get_db)):
    return {"message": "Chatroom is visible"}