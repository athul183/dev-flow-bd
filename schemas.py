from pydantic import BaseModel, EmailStr

class UserSignUp(BaseModel):
    email: EmailStr
    password: str
    name: str

class UserInDB(BaseModel):
    email: str
    hashed_password: str
    name: str

class Token(BaseModel):
    access_token: str
    token_type: str
    user: dict
