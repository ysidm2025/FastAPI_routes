from fastapi import APIRouter, Depends , HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
import schemas, crud
import logging

import json
from config import redis_client, USE_REDIS

# Initialize logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

router = APIRouter()

@router.post("/log-student", status_code=status.HTTP_200_OK)
def log_student_data(student: schemas.StudentResponse):
    """
    Logs student name and number. Raises an error if validation fails or some other issue occurs.
    """
    try:
        # Log student data
        logger.info(f"Student Name: {student.name}, Student Number: {student.number}")
        return {"message": "Student data logged successfully."}
    
    except Exception as e:
        # If something goes wrong, raise a custom error with status code 500
        logger.error(f"Error while logging student data: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error: Custom 500 error"
        )

# without redis below
@router.post("/students", response_model=schemas.StudentResponse)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    """
    Adds a new student to the database.
    """
    return crud.create_student(db, student)

# redis updated code below
# @router.post("/students", response_model=schemas.StudentResponse)
# def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
#     # Create the student in the database
#     new_student = crud.create_student(db, student)
    
#     # If Redis is enabled, cache the new student data
#     if USE_REDIS == "true" and redis_client:
#         redis_client.set(f"student:{new_student.id}", json.dumps(new_student.dict()))
    
#     return new_student

# without redis below
@router.get("/students", response_model=list[schemas.StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return crud.get_students(db)

# redis updated code below
# @router.get("/students", response_model=list[schemas.StudentResponse])
# def get_students(db: Session = Depends(get_db)):
#     if USE_REDIS == "true" and redis_client:
#         # Check if students are already cached in Redis
#         cached_students = redis_client.get("students")
#         if cached_students:
#             # Return cached data
#             return json.loads(cached_students)
    
#     # Fetch from the database if not in cache or Redis is disabled
#     students = crud.get_students(db)
    
#     if USE_REDIS == "true" and redis_client:
#         # Cache the result for future requests
#         redis_client.set("students", json.dumps([student.dict() for student in students]))
    
#     return students

# Create a new student and log to both DB and Redis
# @router.post("/students", response_model=schemas.StudentResponse)
# def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
#     logger.info(f"Creating student: {student.name}")
    
#     # Check if Redis is enabled and use Redis caching logic
#     if redis_client.get("students"):
#         logger.info("Redis cache found, clearing it before adding new student.")
#         redis_client.delete("students")  # Clear students cache before updating

#     db_student = crud.create_student(db, student)
    
#     # After creating student in DB, cache it in Redis
#     logger.info(f"Saving student {db_student.name} to Redis cache.")
#     cached_students = redis_client.get("students")
    
#     # Fetch and cache all students after adding a new one
#     if cached_students:
#         students = json.loads(cached_students)
#     else:
#         students = []
    
#     students.append(db_student.dict())  # Append new student
#     redis_client.set("students", json.dumps(students))
    
#     logger.info(f"Saved student {db_student.name} to Redis cache.")
#     return db_student

# Get all students, with logging for Redis and DB
# @router.get("/students", response_model=list[schemas.StudentResponse])
# def get_students(db: Session = Depends(get_db)):
#     logger.info("Checking Redis cache for students...")
    
#     # Check Redis first
#     cached_students = redis_client.get("students")
#     if cached_students:
#         logger.info("Found students in Redis cache.")
#         return json.loads(cached_students)
    
#     logger.info("No students found in Redis cache. Fetching from DB...")
#     students = crud.get_students(db)
    
#     # Save to Redis for future requests
#     redis_client.set("students", json.dumps([student.dict() for student in students]))
#     logger.info("Saved students to Redis cache.")
    
#     return students

@router.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return {"deleted": crud.delete_student(db, student_id)}
