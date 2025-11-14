# Flask 설정 파일
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    TURSO_AUTH_TOKEN = os.getenv("TURSO_AUTH_TOKEN")
    TURSO_DATABASE_URL = os.getenv("TURSO_DATABASE_URL")

    SQLALCHEMY_DATABASE_URI = f"sqlite+{TURSO_DATABASE_URL}?secure=true"
    CONNECT_ARGS = {"auth_token": TURSO_AUTH_TOKEN}