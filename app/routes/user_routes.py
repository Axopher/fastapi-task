from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserOut, UserLogin, Token
from app.services.user_service import signup_user, login_user
from app.core.db import get_db

router = APIRouter()


@router.post("/signup", response_model=UserOut)
def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    Signup a new user.
    - Validates input
    - Hashes password
    - Saves to DB
    """
    return signup_user(db, user_data)


@router.post("/login", response_model=Token)
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    """
    Login user and return JWT.
    """
    token = login_user(db, credentials)
    return {"access_token": token, "token_type": "bearer"}
