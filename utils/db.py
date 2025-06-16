import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
from motor.motor_asyncio import AsyncIOMotorClient

# Read values from .env
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DATABASE_NAME")
if not MONGO_URI or not DB_NAME:
    raise ValueError("MONGO_URI and DATABASE_NAME must be set in .env file")
# Initialize MongoDB client and database
client = None
db = None

async def connect_db():
    global client, db
    try:
        client = AsyncIOMotorClient(MONGO_URI)
        db = client[DB_NAME]
        print("✅ Connected to MongoDB")
    except Exception as e:
        print("❌ Error connecting to MongoDB:", e)
        raise
async def disconnect_db():
    global client
    if client:
        client.close()
        print("🔌 MongoDB disconnected")
# Optional: expose `db` so other modules can import
def get_db():
    return db
