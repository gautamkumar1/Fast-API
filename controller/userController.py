from models.usermodel import UserData, RegisterModel
from utils.db import get_db  # Make sure this returns an async DB client
from fastapi import HTTPException
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def register_user(user: RegisterModel):
    db = get_db()  # Ensure get_db() is async and returns AsyncIOMotorClient
    existing_user = await db.users.find_one({"email": user.email})
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = pwd_context.hash(user.password)
    
    new_user = {
        "username": user.username,
        "email": user.email,
        "password": hashed_password
    }

    result = await db.users.insert_one(new_user)
    
    return {
        "message": "User registered successfully",
        "id": str(result.inserted_id)
    }
