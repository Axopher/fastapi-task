from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.routes.post_routes import router as post_router

app = FastAPI()

# Include routes
app.include_router(user_router, prefix="/api/user", tags=["Users"])
app.include_router(post_router, prefix="/api/post", tags=["Posts"])
