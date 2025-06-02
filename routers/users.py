from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import schemas
import models
from services import user_service

router = APIRouter()

# --- REGISTER A NEW USER ---
@router.post("/register", response_model=schemas.UserOut)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(user, db)


# --- GET USER BY ID ---
@router.get("/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_user_by_id(user_id, db)

