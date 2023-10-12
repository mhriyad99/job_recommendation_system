from fastapi import FastAPI
from config import models
from config.database import engine
from routers import recommender, user, auth
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origin = ['http://localhost:5173']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(recommender.router)
app.include_router(user.router)
app.include_router(auth.router)