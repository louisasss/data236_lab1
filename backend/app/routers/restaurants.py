from fastapi import APIRouter, Depends, Query
from typing import Optional, List
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.restaurant import RestaurantCreate, RestaurantOut, RestaurantUpdate
from app.schemas.review import ReviewCreate, ReviewOut

router = APIRouter()


@router.get("", response_model=List[RestaurantOut])
def search_restaurants(
    name: Optional[str] = Query(None),
    cuisine: Optional[str] = Query(None),
    keywords: Optional[str] = Query(None),
    city: Optional[str] = Query(None),
    zip_code: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    # TODO: build filtered query against Restaurant model
    # TODO: support partial-match on name, cuisine, keywords (amenities/description), city, zip
    raise NotImplementedError


@router.post("", response_model=RestaurantOut, status_code=201)
def create_restaurant(payload: RestaurantCreate, db: Session = Depends(get_db)):
    # TODO: inject current_user (requires auth)
    # TODO: create Restaurant record with added_by_user_id = current_user.id
    raise NotImplementedError


@router.get("/{restaurant_id}", response_model=RestaurantOut)
def get_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    # TODO: fetch restaurant by id, 404 if not found
    raise NotImplementedError


@router.put("/{restaurant_id}", response_model=RestaurantOut)
def update_restaurant(restaurant_id: int, payload: RestaurantUpdate, db: Session = Depends(get_db)):
    # TODO: inject current_user, verify ownership
    # TODO: apply updates and commit
    raise NotImplementedError


@router.get("/{restaurant_id}/reviews", response_model=List[ReviewOut])
def get_reviews(restaurant_id: int, db: Session = Depends(get_db)):
    # TODO: return all reviews for the given restaurant
    raise NotImplementedError


@router.post("/{restaurant_id}/reviews", response_model=ReviewOut, status_code=201)
def create_review(restaurant_id: int, payload: ReviewCreate, db: Session = Depends(get_db)):
    # TODO: inject current_user
    # TODO: create Review record, update restaurant avg_rating and review_count
    raise NotImplementedError
