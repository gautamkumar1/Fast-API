from pydantic import BaseModel,EmailStr

class RegisterModel(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserData(BaseModel):
    id: int
    username: str
    email: EmailStr
