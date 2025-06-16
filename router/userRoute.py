from fastapi import APIRouter
from controller.userController import register_user
from models.usermodel import RegisterModel

router = APIRouter()
@router.post("/register")
async def register(user: RegisterModel):
    return await register_user(user)