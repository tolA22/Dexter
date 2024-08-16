from typing import Union

from fastapi import FastAPI

from controllers import register_jobs

app = FastAPI()



# register routes
register_jobs(app)

