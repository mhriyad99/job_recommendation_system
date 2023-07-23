from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

from config.database import get_db
from config import models, schemas, utils

router = APIRouter(tags=["authentication"])

@router.post("/login")
def login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid credentials")

    #create token
    #send token

    return {"token": "example token"}


