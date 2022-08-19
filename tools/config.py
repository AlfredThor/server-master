from fastapi import Header, HTTPException, Request
from configs.config import SessionLocal


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

async def get_token_header(request: Request, token: str = Header(None)):
    print(token,1)
    print(request.url)