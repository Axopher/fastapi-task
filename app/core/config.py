import os

class Settings:
    DB_URL: str = os.getenv("DATABASE_URL", "mysql+mysqlconnector://root:root@localhost:3306/fastapi_db")
    JWT_SECRET: str = os.getenv("JWT_SECRET", "abcdefghijk")
    JWT_ALGORITHM: str = "HS256"

settings = Settings()
