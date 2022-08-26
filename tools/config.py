import jwt
import datetime
from fastapi import Header, HTTPException, Request
from configs.config import SessionLocal


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


async def get_token_header(request: Request, token: str = Header(None)):
    if not token:
        raise HTTPException(status_code=404, detail='Token为空，去登陆！')