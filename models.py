from typing import Optional, Text
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.type_api import Variant
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, TEXT, Enum, BLOB, String, DATETIME, Date, DateTime, Float, INT, JSON, TEXT

class User(Base):
    __tablename__ = "User"
    id=                 Column(Integer, primary_key= True, index=True, autoincrement= True)
    first_name=         Column(String(100))
    middle_name=        Column(String(100), default= null)
    last_name=          Column(String(100))
    password=           Column(String(100))
    date_of_birth=      Column(Date)
    # gender=             Column(Enum)
    diagnosis=          Column(TEXT)
    phone_1=            Column(String(100), unique= True)
    phone_2=            Column(String(100))
    identifier_number=  Column(String(100), unique= True)
    role=               Column(Integer, default= 0)
    created_at=         Column(Date)

class Exercise(Base):
    __tablename__ = "Exercise"
    id=                      Column(Integer, primary_key= True, index=True, autoincrement= True)
    exercise_id=             Column(Integer)
    exercise_period_time=    Column(Float)
    exercise_completed_time= Column(Float)
    is_completed=            Column(Boolean)
    user_id=                 Column(Integer)
    doctor_id=               Column(Integer)
    created_at=              Column(DateTime)

class Prescription(Base):
    __tablename__= "Prescription"
    id=          Column(Integer, primary_key= True)
    name=        Column(String(100))
    description= Column(String(100))
    animation=   Column(BLOB)
    # type=        Column(Enum)

class Roles(Base):
    __tablename__= "Roles"
    id=        Column(Integer, primary_key= True)
    role_name= Column(String(100))

class Service(Base):
    __tablename__= "Service"
    id=              Column(Integer, primary_key= True, index=True, autoincrement= True)
    plate=           Column(String(100))
    created_at=      Column(DATETIME)
    departure_times= Column(TEXT)