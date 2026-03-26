# routers 定義API接口(req)
from fastapi import APIRouter
from app.schemas.user import UserRegister
from app.services import user_service

router = APIRouter(prefix="/users", tags=["User"])

@router.get("")
def get_users():
    return {"users": user_service.get_all_users()}

@router.post("/register")
def register(user: UserRegister): # 接收到 request body 透過自訂義的 UserRegister 自動驗證
    new_user = user_service.create_user(user.email, user.password)
    return{
        "message": "User registered",
        "user": new_user
    }