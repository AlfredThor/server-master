from typing import List
from configs.config import conf
from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
from app.test.auth import router
from tools.config import get_token_header, get_db
from model.schemas import AuthCreate
from model.curd.auth import AuthCurd

DefaultReturn = conf['DefaultReturn']


@router.get('/index', summary='主页', dependencies=[Depends(get_token_header)])
async def index(db: Session = Depends(get_db)):
    return {'code': 90}


@router.post('/auth/enroll', summary='注册')
async def enroll(auth: AuthCreate, db: Session = Depends(get_db)):
    email = AuthCurd().get_(data={'curd': {'email': auth.email}})
    print(email)
    return DefaultReturn


@router.put('/auth/update', summary='修改密码', dependencies=[Depends(get_token_header)])
async def update():
    return {'code': 400, 'message': 563541}


@router.delete('/auth/delete', summary='删除', dependencies=[Depends(get_token_header)])
async def delete():
    return {'code': 200, 'message': '删除一个用户!'}
