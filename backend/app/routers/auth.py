from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserCreate, UserOut
from app.schemas.auth import Token, LoginRequest

router = APIRouter()


@router.post("/signup", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def signup(payload: UserCreate, db: Session = Depends(get_db)):
    # TODO: check if email already exists
    # TODO: hash password with bcrypt (see app.utils.auth.hash_password)
    # TODO: create and persist User record
    # TODO: return created user
    raise NotImplementedError


@router.post("/login", response_model=Token)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    # TODO: look up user by email
    # TODO: verify password (see app.utils.auth.verify_password)
    # TODO: create JWT (see app.utils.auth.create_access_token)
    # TODO: return Token
    raise NotImplementedError


@router.get("/me", response_model=UserOut)
def get_me(db: Session = Depends(get_db)):
    # TODO: inject current user via Depends(get_current_user) from app.utils.auth
    # TODO: return current user
    raise NotImplementedError
