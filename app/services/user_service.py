# service 處理商業邏輯
users_db = []

def create_user(email: str, password: str):
    user = {
        "email": email,
        "password": password
    }
    users_db.append(user)
    return user

def get_all_users():
    return users_db