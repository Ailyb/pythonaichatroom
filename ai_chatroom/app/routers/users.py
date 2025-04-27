from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models import User as user_models
from app.schemas import users as user_schemas
from app.security import get_password_hash, verify_password

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user.password)
    db_user = db.query(user_models).filter((user_models.username == user.username) | (user_models.email == user.email)).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username or email already registered")
    try:
        db_user = user_models(username=user.username, email=user.email, hashed_password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/login", response_model=user_schemas.User)
def login_user(user: user_schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(user_models).filter(user_models.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")
    try:
        return db_user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("/me")
def get_current_user(db: Session = Depends(get_db)):
    return {"message": "User is logged in"}