from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import schemas, crud

router = APIRouter()

# without redis below
@router.post("/topics", response_model=schemas.TopicResponse)
def create_topic(topic: schemas.TopicCreate, db: Session = Depends(get_db)):
    return crud.create_topic(db, topic)

# redis updated code below
# @router.post("/topics", response_model=schemas.TopicResponse)
# def create_topic(topic: schemas.TopicCreate, db: Session = Depends(get_db)):
#     # Create the topic in the database
#     new_topic = crud.create_topic(db, topic)
    
#     # If Redis is enabled, cache the new topic data
#     if USE_REDIS == "true" and redis_client:
#         redis_client.set(f"topic:{new_topic.id}", json.dumps(new_topic.dict()))
    
#     return new_topic

# without redis below
@router.get("/topics", response_model=list[schemas.TopicResponse])
def get_topics(db: Session = Depends(get_db)):
    return crud.get_topics(db)

# redis updated code below
# @router.get("/topics", response_model=list[schemas.TopicResponse])
# def get_topics(db: Session = Depends(get_db)):
#     if USE_REDIS == "true" and redis_client:
#         # Check if topics are already cached in Redis
#         cached_topics = redis_client.get("topics")
#         if cached_topics:
#             # Return cached data
#             return json.loads(cached_topics)
    
#     # Fetch from the database if not in cache or Redis is disabled
#     topics = crud.get_topics(db)
    
#     if USE_REDIS == "true" and redis_client:
#         # Cache the result for future requests
#         redis_client.set("topics", json.dumps([topic.dict() for topic in topics]))
    
#     return topics

# Create a new topic and log to both DB and Redis
# @router.post("/topics", response_model=schemas.TopicResponse)
# def create_topic(topic: schemas.TopicCreate, db: Session = Depends(get_db)):
#     logger.info(f"Creating topic: {topic.name}")
    
#     # Check if Redis is enabled and use Redis caching logic
#     if redis_client.get("topics"):
#         logger.info("Redis cache found, clearing it before adding new topic.")
#         redis_client.delete("topics")  # Clear topics cache before updating

#     db_topic = crud.create_topic(db, topic)
    
#     # After creating topic in DB, cache it in Redis
#     logger.info(f"Saving topic {db_topic.name} to Redis cache.")
#     cached_topics = redis_client.get("topics")
    
#     # Fetch and cache all topics after adding a new one
#     if cached_topics:
#         topics = json.loads(cached_topics)
#     else:
#         topics = []
    
#     topics.append(db_topic.dict())  # Append new topic
#     redis_client.set("topics", json.dumps(topics))
    
#     logger.info(f"Saved topic {db_topic.name} to Redis cache.")
#     return db_topic

# Get all topics, with logging for Redis and DB
# @router.get("/topics", response_model=list[schemas.TopicResponse])
# def get_topics(db: Session = Depends(get_db)):
#     logger.info("Checking Redis cache for topics...")
    
#     # Check Redis first
#     cached_topics = redis_client.get("topics")
#     if cached_topics:
#         logger.info("Found topics in Redis cache.")
#         return json.loads(cached_topics)
    
#     logger.info("No topics found in Redis cache. Fetching from DB...")
#     topics = crud.get_topics(db)
    
#     # Save to Redis for future requests
#     redis_client.set("topics", json.dumps([topic.dict() for topic in topics]))
#     logger.info("Saved topics to Redis cache.")
    
#     return topics


@router.post("/assign/{student_id}/{topic_id}")
def assign_topic(student_id: int, topic_id: int, db: Session = Depends(get_db)):
    return {"assigned": bool(crud.assign_topic(db, student_id, topic_id))}
