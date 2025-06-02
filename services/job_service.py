from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models import Job, User
from schemas import JobCreate


def create_job(job_data: JobCreate, current_user: User, db: Session):
    new_job = Job(
        title=job_data.title,
        description=job_data.description,
        company=job_data.company,
        location=job_data.location,
        salary=job_data.salary,
        owner_id=current_user.id
    )
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job


def get_all_jobs(db: Session):
    return db.query(Job).all()


def get_job_by_id(job_id: int, db: Session):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


def update_job(job_id: int, job_data: JobCreate, current_user: User, db: Session):
    job = get_job_by_id(job_id, db)
    if job.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    job.title = job_data.title
    job.description = job_data.description
    job.company = job_data.company
    job.location = job_data.location
    job.salary = job_data.salary

    db.commit()
    db.refresh(job)
    return job


def delete_job(job_id: int, current_user: User, db: Session):
    job = get_job_by_id(job_id, db)
    if job.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    db.delete(job)
    db.commit()
    return {"message": "Job deleted successfully"}
