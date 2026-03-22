# schemas 定義req資料格式
from pydantic import BaseModel, EmailStr 
# pydantic = 驗證資料工具ㄝ
# EmailStr = 驗證 email 格式工具(需先安裝套件pip install pydantic[email])

class UserRegister(BaseModel): # 定義驗證資料
    email: EmailStr            # 驗證 email 格式
    password: str              # 驗證必須是字串(str)