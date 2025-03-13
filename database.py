# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from config import DATABASE_URL
# import redis
# import os

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# Base = declarative_base()


# # # Redis setup
# # REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
# # REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# # # Initialize Redis connection
# # redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

# def get_db():
#     dbname = SessionLocal()
#     try:
#         yield dbname
#     finally:
#         dbname.close()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from config import DATABASE_URL  # Importing DATABASE_URL from config

# Create an engine for the PostgreSQL database
engine = create_engine(DATABASE_URL)

# SessionLocal is the factory for creating new database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models
Base = declarative_base()

# Function to initialize the database, creating tables if they don't exist
def init_db():
    # Create all tables in the database (if not already created)
    Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

