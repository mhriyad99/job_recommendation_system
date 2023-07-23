from fastapi import FastAPI
from config import models
from config.database import engine
from routers import recommender, user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(recommender.router)
app.include_router(user.router)