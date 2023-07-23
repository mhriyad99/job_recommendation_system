from sqlalchemy import Column, Integer, Text, String, FLOAT
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base


class Job(Base):
    __tablename__ = 'job_table'

    job_id = Column(Integer, primary_key=True, nullable=False)
    job_title = Column(Text, nullable=False)
    salary_estimate = Column(Text, nullable=False)
    job_description = Column(Text, nullable=False)
    rating = Column(FLOAT)
    company_name = Column(Text, nullable=False)
    location = Column(Text, nullable=False)
    headquarters = Column(Text, nullable=False)
    size = Column(Text, nullable=False)
    founded = Column(Integer)
    type_of_ownership = Column(Text)
    industry = Column(Text, nullable=False)
    sector = Column(Text)
    competitors = Column(Text)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
