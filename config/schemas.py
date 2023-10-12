from typing import Optional

from pydantic import BaseModel, EmailStr


class Search(BaseModel):
    search: str


class Recommendation(BaseModel):
    job_id: int
    job_title: str
    company_name: str
    salary_estimate: str
    location: str
    job_description: str

    class Config:
        orm_mode = True


class JobDetails(BaseModel):
    job_id: int
    job_title: str
    company_name: str
    salary_estimate: str
    location: str
    job_description: str

    class Config:
        orm_mode = True


class Recommendations(BaseModel):
    job: list[Recommendation]

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class TrainModel(BaseModel):
    train: str = "run"

