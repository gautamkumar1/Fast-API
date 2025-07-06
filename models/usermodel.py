from pydantic import BaseModel,EmailStr

class RegisterModel(BaseModel):
    username: str
    email: EmailStr
    password: str
class LoginModel(BaseModel):
    email: EmailStr
    password: str

class UserData(BaseModel):
    id: int
    username: str
    email: EmailStr
class UserResponse(BaseModel):
    user: UserData
    access_token: str

