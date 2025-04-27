from fastapi import FastAPI
from .routers import users_router, chatrooms_router

app = FastAPI()

# Add the routers to the app
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(chatrooms_router, prefix="/chatrooms", tags=["chatrooms"])


@app.get("/")
def index():
    return {"message": "Hello, world!"}