from fastapi import FastAPI
from routes import student_routes , topic_routes
from database import init_db
app = FastAPI()

# from routes import image_routes , student_routes , topic_routes

# Call init_db during the startup of the application
@app.on_event("startup")
def on_startup():
    init_db()  # This will create the tables in the newdb if they don't exist.

# app.include_router(image_routes.router, prefix="/api")
app.include_router(student_routes.router, prefix="/api")  
app.include_router(topic_routes.router, prefix="/api")
