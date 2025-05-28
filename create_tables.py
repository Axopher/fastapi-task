# create_tables.py
from app.core.db import Base, engine
from app.models import user, post  # import all models here

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done.")
