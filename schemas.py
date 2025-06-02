from pydantic import BaseModel, EmailStr
from typing import List, Optional

# --------------------
# User Schemas
# --------------------

# What we need from user during signup
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# What we return when user data is fetched
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        model_config = {"from_attributes": True}




class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True  # For Pydantic v2

class JobOut(BaseModel):
    id: int
    title: str
    description: str
    company: str
    location: str
    salary: Optional[str] = None

    class Config:
        from_attributes = True




# --------------------
# Job Schemas
# --------------------

# What we expect when someone creates a job
class JobCreate(BaseModel):
    title: str
    description: str
    company: str
    location: str
    salary: Optional[str] = None


# What we return when a job is retrieved
class JobResponse(BaseModel):
    id: int
    title: str
    description: str
    company: str
    location: str
    salary: Optional[str]
    owner: UserResponse

    class Config:
        model_config = {"from_attributes": True}



# --------------------
# Token Schemas
# --------------------

# Response schema for access token
class Token(BaseModel):
    access_token: str
    token_type: str


# Request schema for login
class TokenData(BaseModel):
    username: Optional[str] = None

