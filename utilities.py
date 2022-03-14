import hashlib
from os import name
from typing import AsyncContextManager, Optional, List
from fastapi import FastAPI, Depends, HTTPException
from fastapi import responses
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import query, session
from sqlalchemy.orm.session import Session
import models, schemas, database
from database import SessionLocal, engine
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

def get_user(db, identifier: str):
    if identifier in db:
        user_dict= db[identifier]
        return schemas.UserInDB(**user_dict)

def hash_password(password:str):
    return hashlib.sha256(password.encode()).hexdigest()

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.identifier_number == user_id).first()