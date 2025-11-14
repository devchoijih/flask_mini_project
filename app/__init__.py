from flask import Flask, render_template
from .routes import review_bp

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/edit")
    def edit():
        return render_template("edit.html")

    @app.route("/edit/<int:review_id>")
    def edit_update(review_id):
        return render_template("edit.html", review_id=review_id)

    app.register_blueprint(review_bp)
    return app
