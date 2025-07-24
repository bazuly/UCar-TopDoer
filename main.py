from fastapi import FastAPI

from review_app.handlers import router as review_router


app = FastAPI()

app.include_router(review_router)
