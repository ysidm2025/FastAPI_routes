from sqlalchemy.orm import Session
import models, schemas

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(name=student.name, number=student.number)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db: Session):
    return db.query(models.Student).all()

def delete_student(db: Session, student_id: int):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
        return True
    return False

def create_topic(db: Session, topic: schemas.TopicCreate):
    db_topic = models.Topic(name=topic.name)
    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)
    return db_topic

def get_topics(db: Session):
    return db.query(models.Topic).all()

def assign_topic(db: Session, student_id: int, topic_id: int):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    topic = db.query(models.Topic).filter(models.Topic.id == topic_id).first()
    if student and topic:
        student.topics.append(topic)
        db.commit()
        return student
    return None