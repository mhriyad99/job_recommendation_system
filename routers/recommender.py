from typing import List

from fastapi import Depends, APIRouter, status
from sqlalchemy import inspect
from sqlalchemy.orm import Session
from config import oauth2
from config import schemas, models
from config.database import get_db
from services.recommendation_system import get_recommendation
from services.train import TrainJobRecommendationModel

router = APIRouter(tags=['Recommendation'])


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


# @router.get("/recommended-job")
@router.get("/recommended-job", response_model=List[schemas.Recommendation], )
def recommendation(payload: schemas.Search, db: Session = Depends(get_db),
                   get_current_user: int = Depends(oauth2.get_current_user)):
    recommended = get_recommendation([payload.search], 10, db)
    # jobs = []
    # for i in recommended:
    #     job = i['Job']
    #     jobs.append(object_as_dict(job))
    # return jobs
    return recommended

@router.post("/train",  status_code=status.HTTP_201_CREATED)
def train_model(payload:schemas.TrainModel, get_current_user: int = Depends(oauth2.get_current_user)):

    if payload.train == "run":
        rec_model = TrainJobRecommendationModel()
        rec_model.begin()
        return {"response": "Model trained!"}

    return {"response": "Something went wrong!"}

