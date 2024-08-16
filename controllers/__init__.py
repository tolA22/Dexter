

from fastapi import FastAPI

from controllers.user import router as user_router


def register_jobs(app: FastAPI):
    """Registers all jobs with the FastAPI app.

    When you add a new job:
    1. Import the job router above
    2. Include the job router below
    """
    app.include_router(user_router, prefix="", tags=["user"])

    ...