from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    TURSO_AUTH_TOKEN = os.getenv("TURSO_AUTH_TOKEN")
    TURSO_DATABASE_URL = os.getenv("TURSO_DATABASE_URL")

    SQLALCHEMY_DATABASE_URI = f"sqlite+{TURSO_DATABASE_URL}?secure=true"
    CONNECT_ARGS = {"auth_token": TURSO_AUTH_TOKEN}

# # instance 폴더 경로
# INSTANCE_DIR = os.path.join(os.path.dirname(__file__), "..", "instance")

# # 폴더가 없으면 생성
# os.makedirs(INSTANCE_DIR, exist_ok=True)

# class Config:
#     """환경 설정 (로컬 SQLite 기본값)"""
#     SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///instance/reviews.db")