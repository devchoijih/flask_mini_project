from .models import SessionLocal, Review
from flask import request, jsonify, Blueprint, redirect, url_for

review_bp = Blueprint("review", __name__)

# Read: 전체 목록 조회
@review_bp.route("/reviews", methods=["GET"])
def get_reviews():
    db = SessionLocal()
    reviews = db.query(Review).all()
    db.close()
    return jsonify([{"id": r.id, "title": r.title, "contents" : r.contents, "score" : r.score} for r in reviews])

# Read: 특정 목록 조회
@review_bp.route("/reviews/<int:review_id>", methods=["GET"])
def get_review(review_id):
    db = SessionLocal()
    review = db.query(Review).get(review_id)
    db.close()
    if not review:
        return jsonify({"error": "그런건 없어요"}), 404
    return jsonify({"id": review.id, "title": review.title, "contents" : review.contents, "score" : review.score})

# Create: 새로운 todo 추가
@review_bp.route("/reviews", methods=["POST"])
def create_review():
    data = request.get_json() # body 값 받기

    db = SessionLocal()
    r = Review(title=data["title"], contents=data["contents"], score=data["score"])
    db.add(r)
    db.commit()
    db.refresh(r) # commit 이후로 자동 생성된 id 불러오기
    db.close()

    return ''

# Update: todo 수정
@review_bp.route("/review/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    data = request.get_json()

    db = SessionLocal()
    review = db.query(Review).get(todo_id)
    # 데이터 없을 때
    if not review:
        db.close()
        return jsonify({"error": "못찾았어요"}), 404

    # 데이터 있을 때
    review.title = data["title"]
    review.contents = data["contents"]
    review.score = data["score"]
    db.commit()
    updated = {"id": review.id, "title": review.title, "contents" : review.contents, "score" : review.score}
    db.close()
    return jsonify(updated)

# Delete: todo 삭제
@review_bp.route("/review/<int:review_id>", methods=["DELETE"])
def delete_todo(review_id):
    db = SessionLocal()
    review = db.query(Review).get(review_id)
    if not review:
        db.close()
        return jsonify({"error": "없어요"}), 404
    db.delete(review)
    db.commit()
    db.close()
    return jsonify({"deleted": review_id})