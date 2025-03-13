from dotenv import load_dotenv
import os
import redis

load_dotenv()  # Load environment variables from .env file
# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://user:password@localhost:5432/newdb")

DATABASE_URL = "postgresql://postgres:password@localhost:5432/dbname"
# DATABASE_URL = "postgresql://postgres:password@localhost:5432/newdb"
USE_REDIS = os.getenv("USE_REDIS", "false")  # Default is 'false'

# Redis setup
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# Initialize Redis connection
if USE_REDIS == "true":
    import redis
    redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
else:
    redis_client = None

# DATABASE_URL = os.getenv("DATABASE_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Added
