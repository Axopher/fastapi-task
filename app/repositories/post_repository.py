from sqlalchemy.orm import Session
from app.models.post import Post

def create_post(db: Session, user_id: int, text: str) -> Post:
    post = Post(user_id=user_id, text=text)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_user_posts(db: Session, user_id: int) -> list[Post]:
    return db.query(Post).filter(Post.user_id == user_id).all()

def delete_post(db: Session, post_id: int, user_id: int) -> bool:
    post = db.query(Post).filter(Post.id == post_id, Post.user_id == user_id).first()
    if post:
        db.delete(post)
        db.commit()
        return True
    return False
