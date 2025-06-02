from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models
from schemas import UserCreate
from routers.auth import hash_password


# Create a new user
def create_user(user_data: UserCreate, db: Session):
    # Check if username or email already exists
    existing_user = db.query(models.User).filter(
        (models.User.username == user_data.username) |
        (models.User.email == user_data.email)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already registered"
        )

    new_user = models.User(
        username=user_data.username,
        email=user_data.email,
        password=hash_password(user_data.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# Get a user by username
def get_user_by_username(username: str, db: Session):
    user = db.query(models.User).filter(models.User.username == username).first()
    return user


# Get a user by ID
def get_user_by_id(user_id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

