import joblib
from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from config import models

# nbrs = joblib.load('files\\job_recommender.joblib')
# vectorizer = joblib.load('files\\vectorizer.joblib')

job_id, vectorizer, model = joblib.load("models\\rec_model.joblib")


def get_recommendation(query, n_neighbors, db: Session):
    queryTFIDF = vectorizer.transform(query)
    distances, indices = model.kneighbors(queryTFIDF, n_neighbors=n_neighbors)
    rec_index = [job_id[i] for i in indices[0]]
    res = db.query(models.Job).filter(models.Job.job_id.in_(indices[0])).all()
    # q = select(models.Job).where(models.Job.job_id.in_(rec_index))
    # res = db.execute(q).all()
    # recommended = []
    # for i in range(len(indices[0])):
    #
    #     recommended.append(db.query(models.Job).filter(models.Job.job_id == indices[0][i]).first())

    # if not recommended:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail="Sorry, something went wrong")
    return res

