# FastAPI Project with Student, Topic, and Image Routes

This is a FastAPI project that includes routes for managing students, topics, and image summary generation using OpenAI. The project also demonstrates how to integrate a PostgreSQL database, use Redis for caching, and process images with the OpenAI API.

## Features

- **Student Routes**: Manage student data, including creation, retrieval, and deletion of students.
- **Topic Routes**: Create and retrieve topics. Students can be assigned to topics.
- **Image Summary Routes**: Upload images and receive a brief description of the image using OpenAI's GPT-4o-mini model.
- **Database Integration**: Uses SQLAlchemy to interact with a PostgreSQL database for persistent storage.
- **Redis Caching (optional)**: Redis caching is supported to optimize API performance by caching student and topic data.
- **OpenAI Integration**: Summarizes images via OpenAI's API.

## Requirements

- Python 3.8+
- PostgreSQL Database
- Redis (optional, for caching)
- OpenAI API Key (for image summary generation)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fastapi-project.git
   cd fastapi-project
   
2. Create and activate a virtual environment :
   * python3 -m venv venv
   * source venv/bin/activate  # On Windows use: venv\Scripts\activate
   
3. Install the required dependencies :
   * pip install -r requirements.txt

4. Create a .env file in the project root directory and add your environment variables :
   * DATABASE_URL= postgresql://user:password@localhost:5432/Database_name
   * USE_REDIS=true  # or false if Redis is not being used
   * REDIS_HOST=localhost
   * REDIS_PORT=6379
   * OPENAI_API_KEY=your-openai-api-key

5. Initialize the PostgreSQL database :
   * uvicorn main:app --reload

6. Optionally, start Redis :
   * redis-server

## API Screenshots

**All routes**

![image](https://github.com/user-attachments/assets/0ac47dab-2686-4757-862e-1443e6db9b3f)

**Image-summary**

![image](https://github.com/user-attachments/assets/da729e46-6580-4d4e-9827-23b0fa6f8457)

**Get-students**

![image](https://github.com/user-attachments/assets/d8a09326-4666-49f2-ac5b-dc0e1adf4ddc)

**Log student data**

Logs student name and number. Raises an error if validation fails or some other issue occurs.

![image](https://github.com/user-attachments/assets/c4a738f5-dcd6-4331-97ab-df075fafd922)

