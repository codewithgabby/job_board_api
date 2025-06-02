from fastapi import FastAPI
from routers import users, jobs, auth

app = FastAPI(
    title="Job Board API",
    description="A FastAPI-based backend for posting and applying to jobs.",
    version="1.0.0"
)

# Registering all the routers with tags and prefixes
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])

