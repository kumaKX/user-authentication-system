# 系統入口
from fastapi import FastAPI
from app.routers import user

app = FastAPI(
    openapi_tags=[
        {"name": "User", "description": "使用者相關API"}
    ]
)

app.include_router(user.router)

@app.get("/")
def home():
    return{"message": "Auth System Running"}