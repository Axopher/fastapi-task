from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories import user_repository
from app.core.security import hash_password, verify_password
from app.schemas.user import UserCreate, UserLogin
from app.models.user import User
from app.core.jwt import create_access_token

def signup_user(db: Session, user_data: UserCreate) -> User:
    """
    Handles the signup process:
    - Checks if user already exists
    - Hashes password
    - Stores in database
    """
    existing_user = user_repository.get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

    hashed_pw = hash_password(user_data.password)
    new_user = user_repository.create_user(db, user_data.email, hashed_pw)
    return new_user


def login_user(db: Session, credentials: UserLogin) -> str:
    user = db.query(User).filter(User.email == credentials.email).first()
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return create_access_token({"sub": str(user.id)})