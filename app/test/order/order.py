from . import router
from sqlalchemy.orm import Session
from tools.config import get_token_header, get_db
from fastapi import Depends, HTTPException, Header

@router.get('/irder/list', summary='订单', dependencies=[Depends(get_token_header)])
async def list(db: Session = Depends(get_db)):
    return {'code': 200, 'message':'订单！'}