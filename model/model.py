from datetime import datetime
from configs.config import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, TEXT, JSON
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
    status = Column(Integer, nullable=False, default=1) # 1:正常， 0：封禁， -1：注销
    is_manager = Column(Integer, nullable=False, default=0)# 是否为管理员
    role = Column(String(20),nullable=True)

class Role(BaseModel, Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True, index=True)  # 自增ID
    name = Column(String(30), nullable=False) # 角色名称
    brief = Column(String(256), nullable=False) # 角色简介
    author = Column(JSON, nullable=True) # 角色所拥有的权限

class Authority(BaseModel,Base):
    __tablename__ = 'authority'
    id = Column(Integer, primary_key=True, index=True)  # 自增ID
    name = Column(String(30), nullable=False) #权限名称
    brief = Column(String(256), nullable=False)  # 权限简介
    url = Column(String(50), nullable=False) # 路由