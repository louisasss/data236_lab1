from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.review import ReviewOut, ReviewUpdate

router = APIRouter()


@router.put("/{review_id}", response_model=ReviewOut)
def update_review(review_id: int, payload: ReviewUpdate, db: Session = Depends(get_db)):
    # TODO: inject current_user
    # TODO: verify review belongs to current_user (403 otherwise)
    # TODO: apply updates, recalculate restaurant avg_rating
    raise NotImplementedError


@router.delete("/{review_id}", status_code=204)
def delete_review(review_id: int, db: Session = Depends(get_db)):
    # TODO: inject current_user
    # TODO: verify review belongs to current_user (403 otherwise)
    # TODO: delete review, recalculate restaurant avg_rating
    raise NotImplementedError
