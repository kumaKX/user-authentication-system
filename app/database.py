from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://user:password@localhost:5432/auth_db"

# 建立與資料庫的連線
engine = create_engine(DATABASE_URL)
# Session工廠(對db操作工具)
SessionLocal = sessionmaker(bind=engine)
# table實體物件
Base = declarative_base()