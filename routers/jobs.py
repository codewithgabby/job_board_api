from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from routers.auth import get_current_user
import models, schemas
from services import job_service

router = APIRouter()

# --- CREATE A JOB ---
@router.post("/", response_model=schemas.JobOut)
def create_job(
    job: schemas.JobCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return job_service.create_job(job, current_user, db)


# --- GET ALL JOBS ---
@router.get("/", response_model=list[schemas.JobOut])
def get_jobs(db: Session = Depends(get_db)):
    return job_service.get_all_jobs(db)


# --- GET A SPECIFIC JOB ---
@router.get("/{job_id}", response_model=schemas.JobOut)
def get_job(job_id: int, db: Session = Depends(get_db)):
    return job_service.get_job_by_id(job_id, db)


# --- UPDATE A JOB ---
@router.put("/{job_id}", response_model=schemas.JobOut)
def update_job(
    job_id: int,
    job: schemas.JobCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return job_service.update_job(job_id, job, current_user, db)


# --- DELETE A JOB ---
@router.delete("/{job_id}")
def delete_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return job_service.delete_job(job_id, current_user, db)
