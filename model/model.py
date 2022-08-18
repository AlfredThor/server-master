from datetime import datetime
from configs.config import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, TEXT
from sqlalchemy.orm import relationship


class BaseModel(object):
    create_time = Column(DateTime, default=datetime.now())
    update_time = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    def to_dict(self, exclude=[], revers=True, time_=True):
        '''
        reverse=True: not in exclude：输出去除该列表里面的字段
        reverse=False: in exclude：输出只有该列表里面的字段
        '''
        if revers:
            data = {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name not in exclude}
        else:
            if time_:
                exclude = exclude + ['create_time', 'update_time']
            data = {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name not in exclude}
        if time_:
            data['create_time'] = data['create_time'].strftime('%Y-%m-%d %H:%M:%S') if data['create_time'] else ''
            data['update_time'] = data['update_time'].strftime('%Y-%m-%d %H:%M:%S') if data['update_time'] else ''
        return data


class Auth(BaseModel, Base):
    __tablename__ = 'auth'
    id = Column(Integer, primary_key=True, index=True) # 自增ID
    username = Column(String(20), nullable=False) # 用户名
    password = Column(String(80), nullable=False) # 密码
    email = Column(String(50), unique=True, index=True) # 邮箱
    phone = Column(String(50), nullable=True, index=True) # 手机号


class Role(BaseModel, Base):
    __tablename__ = 'role'


class Authority(BaseModel,Base):
    __tablename__ = 'authority'