from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database.database import SessionLocal
from .schemas import users as user_schemas, chatrooms as chatroom_schemas
from .routers import users_router, chatrooms_router

app = FastAPI()

# Add the routers to the app
app.include_router(users_router, tags=["users"], prefix="/users")
app.include_router(chatrooms_router, tags=["chatrooms"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def index():
    return {"message": "Hello, world!"}

@app.post("/create_user")
def create_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    from .routers.users import register_user
    return register_user(user=user, db=db)


@app.post("/create_chatroom")
def create_chatroom(chatroom: chatroom_schemas.ChatroomCreate, db: Session = Depends(get_db)):
    from .routers.chatrooms import create_chatroom
    return create_chatroom(chatroom=chatroom, db=db)
