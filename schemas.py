from typing import List, Optional
from pydantic import BaseModel
from sqlalchemy.sql.selectable import FromClause
import hashlib

from sqlalchemy.sql.sqltypes import String


class User(BaseModel):
    id: int
    first_name: str
    middle_name: Optional[str]
    last_name: str
    password: str
    date_of_birth: str
    diagnosis: str
    phone_1: str
    phone_2: str
    identifier_number: str
    role: int

class RegisterUser(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    password: str
    date_of_birth: str
    diagnosis: str
    phone_1: str
    phone_2: str
    identifier_number: str

class UserInDB(User):
    crypted_password: str
