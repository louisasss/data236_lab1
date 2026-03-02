from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserOut, UserUpdate
from app.schemas.preference import PreferenceOut, PreferenceUpdate

router = APIRouter()


@router.get("/me", response_model=UserOut)
def get_profile(db: Session = Depends(get_db)):
    # TODO: inject current_user via Depends(get_current_user)
    # TODO: return current_user
    raise NotImplementedError


@router.put("/me", response_model=UserOut)
def update_profile(payload: UserUpdate, db: Session = Depends(get_db)):
    # TODO: inject current_user
    # TODO: apply updates and commit
    raise NotImplementedError


@router.post("/me/photo")
def upload_profile_picture(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # TODO: save file to storage (local disk or S3), update user.profile_pic_url
    raise NotImplementedError


@router.get("/me/preferences", response_model=PreferenceOut)
def get_preferences(db: Session = Depends(get_db)):
    # TODO: inject current_user, fetch or create UserPreference record
    raise NotImplementedError


@router.put("/me/preferences", response_model=PreferenceOut)
def update_preferences(payload: PreferenceUpdate, db: Session = Depends(get_db)):
    # TODO: inject current_user, upsert UserPreference record
    raise NotImplementedError


@router.get("/me/favorites")
def get_favorites(db: Session = Depends(get_db)):
    # TODO: return list of restaurants favorited by current_user
    raise NotImplementedError


@router.post("/me/favorites/{restaurant_id}")
def add_favorite(restaurant_id: int, db: Session = Depends(get_db)):
    # TODO: inject current_user, create Favorite record (ignore if already exists)
    raise NotImplementedError


@router.delete("/me/favorites/{restaurant_id}")
def remove_favorite(restaurant_id: int, db: Session = Depends(get_db)):
    # TODO: inject current_user, delete Favorite record if exists
    raise NotImplementedError


@router.get("/me/history")
def get_history(db: Session = Depends(get_db)):
    # TODO: inject current_user
    # TODO: return dict with "reviews" (user's reviews) and "restaurants_added" (added by user)
    raise NotImplementedError
