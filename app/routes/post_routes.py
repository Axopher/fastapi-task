from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.post import PostCreate, PostOut
from app.services import post_service
from app.core.db import get_db
from app.core.security import get_current_user

router = APIRouter()

@router.post("/", summary="Add a post", response_model=PostOut)
def add_post(post: PostCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return post_service.create_post(db, current_user.id, post)

@router.get("/", summary="Get user's posts", response_model=List[PostOut])
def get_posts(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return post_service.get_posts(db, current_user.id)

@router.delete("/{post_id}", summary="Delete a post")
def delete_post(post_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    if not post_service.delete_post(db, current_user.id, post_id):
        raise HTTPException(status_code=404, detail="Post not found")
    return {"detail": "Post deleted"}
