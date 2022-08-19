from typing import List
from configs.config import conf
from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
from app.test.auth import router
from tools.config import get_token_header, get_db
from model.schemas import AuthCreate
from model.curd.auth import AuthCurd

DefaultReturn = conf['DefaultReturn']

# @router.get('get', summary='主页', dependencies=[Depends(get_token_header)])
# async def index(db: Session = Depends(get_db)):
@router.get('/auth', summary='主页', dependencies=[Depends(get_token_header)])
async def index(db: Session = Depends(get_db)):
    return {'code': 90}


@router.post('/auth/enroll', summary='主页', dependencies=[Depends(get_token_header)])
async def index(auth: AuthCreate, db: Session = Depends(get_db)):
    userCurd = AuthCurd(db)
    email = AuthCurd.get_(data={'curd': {'email': auth.email}})
    phone = AuthCurd.get_(data={'curd': {'phone': auth.phone}})
    print(email)
    print(phone)

    return DefaultReturn