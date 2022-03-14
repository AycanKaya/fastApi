from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


JAWS_ARGS = {
    "database":     "ylomw9fm93njcm1q",
    "drivername":   "mysql",
    "username":     "j5eizmmbp0ybc6gz",
    "password":     "yj4ojoomqipe2teq",
    "host":         "c8u4r7fp8i8qaniw.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
    "query": {
                    "charset": "utf8",
                    # "reconnect": "true"
    }
}


engine= create_engine(URL(**JAWS_ARGS), encoding="utf8")

SessionLocal = sessionmaker(autocommit= False, autoflush= False, bind= engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()