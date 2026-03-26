# 系統入口
from fastapi import FastAPI
from app.routers import user
from app.database import engine, Base

app = FastAPI(
    openapi_tags=[
        {"name": "User", "description": "使用者相關API"}
    ]
)

# 如果table不存在 -> 自動資料表
Base.metadata.create_all(bind=engine)

app.include_router(user.router)

@app.get("/")
def home():
    return{"message": "Auth System Running"}