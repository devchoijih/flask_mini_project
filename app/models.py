from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, declarative_base
import os

load_dotenv()

class Config:
    TURSO_AUTH_TOKEN = os.getenv("TURSO_AUTH_TOKEN")
    TURSO_DATABASE_URL = os.getenv("TURSO_DATABASE_URL")

    SQLALCHEMY_DATABASE_URI = f"sqlite+{TURSO_DATABASE_URL}?secure=true"
    CONNECT_ARGS = {"auth_token": TURSO_AUTH_TOKEN}

engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,
    connect_args=Config.CONNECT_ARGS
)

##########
# 모델 정의
##########
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    contents = Column(Text, nullable=False)
    score = Column(Integer)


    def __repr__(self):
        return f"<Todo id={self.id} task='{self.task}'>"

Base.metadata.create_all(bind=engine)