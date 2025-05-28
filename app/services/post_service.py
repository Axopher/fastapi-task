from sqlalchemy.orm import Session
from app.repositories import post_repository
from app.schemas.post import PostCreate
from app.cache.post_cache import post_cache

def create_post(db: Session, user_id: int, post_data: PostCreate):
    return post_repository.create_post(db, user_id, post_data.text)

def get_posts(db: Session, user_id: int):
    cached = post_cache.get(user_id)
    if cached:
        return cached
    posts = post_repository.get_user_posts(db, user_id)
    post_cache.set(user_id, posts)
    return posts

def delete_post(db: Session, user_id: int, post_id: int):
    success = post_repository.delete_post(db, post_id, user_id)
    if success:
        post_cache.invalidate(user_id)
    return success
