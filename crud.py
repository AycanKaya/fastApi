import hashlib
from fastapi import responses
from fastapi.param_functions import Query
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import desc, true
import models, schemas
from utilities import hash_password, get_user, get_user_by_id

def register_user(db: Session, user: schemas.RegisterUser):
    db_user= models.User(identifier_number= user.identifier_number, 
                         password= hash_password(user.password),
                         first_name= user.first_name,
                         middle_name= user.middle_name,
                         last_name= user.last_name,
                         date_of_birth= user.date_of_birth,
                         diagnosis= user.diagnosis,
                         phone_1= user.phone_1,
                         phone_2= user.phone_2)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user