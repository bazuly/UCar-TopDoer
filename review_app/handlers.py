from datetime import datetime
from typing import Optional

from fastapi import APIRouter

from review_app.db_connection import get_db_connection
from review_app.exceptions import CreateReviewException
from review_app.service import analyze_sentiment
from review_app.schemas import ReviewRequest, ReviewResponse

router = APIRouter()


@router.post("/reviews", response_model=ReviewResponse)
async def create_review(review: ReviewRequest):
    sentiment = analyze_sentiment(review.text)
    created_at = datetime.utcnow().isoformat()

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO reviews (text, sentiment, created_at) VALUES (?, ?, ?)",
            (review.text, sentiment, created_at)
        )
        conn.commit()

        review_id = cursor.lastrowid
        return {
            "id": review_id,
            "text": review.text,
            "sentiment": sentiment,
            "created_at": created_at
        }
    except CreateReviewException as e:
        conn.rollback()
        raise e.detail


@router.get("/reviews", response_model=list[ReviewResponse])
async def get_reviews(sentiment: Optional[str] = None):
    conn = get_db_connection()
    cursor = conn.cursor()

    if sentiment:
        cursor.execute(
            "SELECT * FROM reviews WHERE sentiment = ? ORDER BY created_at DESC",
            (sentiment,)
        )
    else:
        cursor.execute("SELECT * FROM reviews ORDER BY created_at DESC")

    reviews = cursor.fetchall()
    return [dict(review) for review in reviews]
