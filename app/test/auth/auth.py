from typing import List
from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
from app.test.auth import router
from tools.config import get_token_header, get_db
from fastapi import FastAPI

app=FastAPI()

# @router.get('get', summary='主页', dependencies=[Depends(get_token_header)])
# async def index(db: Session = Depends(get_db)):
@app.get('/')
async def index():
    return {'code':90}
