from flask import render_template, Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
from .config import Config

# TODO: DB 연결 엔진을 생성하세요 (create_engine)
engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,
    echo=True,
    connect_args=Config.CONNECT_ARGS
)

# TODO: 세션(SessionLocal) 객체를 만드세요 (scoped_session)
SessionLocal = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False))

# TODO: Base 클래스를 만드세요 (declarative_base)
Base = declarative_base()

def create_app():
    """Flask 앱 생성 및 초기화"""
    app = Flask(__name__)

    # TODO: 모델을 import 하세요 (예: from . import models.py)
    from . import models

    # TODO: DB 테이블을 생성하세요 (Base.metadata.create_all)
    Base.metadata.create_all(bind=engine)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/edit")
    def edit():
        return render_template("edit.html")

    @app.route("/edit/<int:review_id>")
    def edit_update(review_id):
        return render_template("edit.html", review_id=review_id)

    # TODO: 라우트 블루프린트를 등록하세요 (review_routes 불러와서 app.register_blueprint)
    from routes import review_bp
    app.register_blueprint(review_bp)

    # 요청이 끝날 때마다 세션 닫기
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        SessionLocal.remove()

    return app