from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy import inspect
from sqlalchemy.orm import Session

from config import schemas, models
from config.database import get_db
from services.recommendation_system import get_recommendation

router = APIRouter()


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


#@router.get("/recommended-job")
@router.get("/recommended-job", response_model=List[schemas.Recommendation])
def recommendation(payload: schemas.Search, db: Session = Depends(get_db)):
    recommended = get_recommendation([payload.search], 10, db)
    jobs = []
    for i in recommended:
        job = i['Job']
        jobs.append(object_as_dict(job))
    return jobs
