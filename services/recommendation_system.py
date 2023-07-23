import joblib
from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from config import models

nbrs = joblib.load('files\\job_recommender.joblib')
vectorizer = joblib.load('files\\vectorizer.joblib')


def get_recommendation(query, n_neighbors, db: Session):
    queryTFIDF = vectorizer.transform(query)
    distances, indices = nbrs.kneighbors(queryTFIDF, n_neighbors=n_neighbors)
    q = select(models.Job).where(models.Job.job_id.in_(indices[0]))
    res = db.execute(q).fetchall()
    # recommended = []
    # for i in range(len(indices[0])):
    #
    #     recommended.append(db.query(models.Job).filter(models.Job.job_id == indices[0][i]).first())

    # if not recommended:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail="Sorry, something went wrong")
    return res

