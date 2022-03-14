import hashlib
from os import name
from typing import AsyncContextManager, Optional, List
from fastapi import FastAPI
from fastapi import Depends, HTTPException
from fastapi import responses
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import query, session
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
import models, schemas, crud, database
from models import User
from database import SessionLocal, engine
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from utilities import hash_password, get_user, get_user_by_id

app=FastAPI()
oauth2_scheme =OAuth2PasswordBearer(tokenUrl="token")
models.Base.metadata.create_all(bind=engine)
get_db= database.get_db

sans = FastAPI(
    title=       "Sans API",
    description= "Softalya Inc. 2021",
    version=     "pre release - v0.4"
)

tags_metadata = [
    {
        "name"          : "users",
        "description"   : "User operations"
    },
    {
        "name"          : "Exercise",
        "description"   : "Exercise Manipulation"
    }
]

def returnIndex():
    content= """
    <html>
        <head>
            <title>Sans</title>
        </head>
        <body>
            <img src="https://antalyabalikevi.com.tr/wp-content/uploads/2020/10/bayat-balik-nasil-anlasilir-min-1536x1017.jpg" alt="paluk" style="width:300px;height:300px;  display: block;
                margin-left: auto;
                margin-right: auto;
                width: 50%;">
            <p style="text-align: center;">Uyyy pu api değildur bu paluktur</p>
            <a href="/docs"><p style="text-align: center;">Docs</p></a>
        </body>
    </html>
    """
    return HTMLResponse(content=content, status_code=200)

@sans.get("/", tags=["TEST"], response_class= HTMLResponse)
# INDEX
async def root():
    return returnIndex()


# @sans.post("/token",tags=['Aycan'])
# async def login(form_data : OAuth2PasswordRequestForm=Depends()): #burdan çekiyor şifreleri
#     user_dict = fake_users_db.get(form_data.username)
#     # print(user_dict)
#     if not user_dict:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     user = schemas.UserInDB(**user_dict)
#     hashed_password = fake_hash_password(form_data.password)
#     if not hashed_password == user.hashed_password:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     return{"access_token " : user.username, "token_type : " :"bearer"}


@sans.post("/alpha/login")
async def login(form_data: OAuth2PasswordRequestForm= Depends(), db: Session= Depends(get_db)):
    identifier= form_data.username
    password= hash_password(form_data.password)
    user= db.query(models.User).filter(models.User.identifier_number== identifier, 
    models.User.password== password).first()
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"login status": "success",
    "access_token " : user.identifier_number, "token_type : " :"bearer"}

@sans.post("/alpha/register")
async def register(user: schemas.RegisterUser, db: Session= Depends(get_db)):
    db_user= get_user_by_id(db, user_id= user.identifier_number)
    if db_user:
        raise HTTPException(status_code=400, detail="User with such identifier is already registered.")
    return crud.register_user(db=db, user=user)