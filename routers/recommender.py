from typing import List

from fastapi import Depends, APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from config import oauth2
from config import schemas, models
from config.database import get_db
from services.recommendation_system import get_recommendation
from services.train import TrainJobRecommendationModel

router = APIRouter(
    prefix="/jobs",
    tags=['Recommendation']
)


@router.get("/{id}", response_model=schemas.JobDetails)
def get_job(id: int, db: Session = Depends(get_db)):
    job = db.query(models.Job).filter(models.Job.job_id == id).first()
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Job with ID {id} is missing')
    return job


# @router.get("/recommended-job")
@router.post("/recommended-job", response_model=List[schemas.Recommendation], )
def recommendation(payload: schemas.Search, db: Session = Depends(get_db)):
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

