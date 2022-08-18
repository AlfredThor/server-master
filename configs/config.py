from fastapi import FastAPI
from redis import StrictRedis, ConnectionPool, Redis
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:root@120.79.138.248/erp?charset=utf8md4'
Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_recycle=1800)
DBSession = scoped_session(sessionmaker())
DBSession.configure(bind=engine, autoflush=False, expire_on_commit=False)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

app = FastAPI(redoc_url=None)