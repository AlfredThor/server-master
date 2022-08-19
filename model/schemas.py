from pydantic import BaseModel, ValidationError, validator
from tools.publictool import MakeTool


class AuthBase(BaseModel):
    email: str = None
    phone: str = None

    @validator('email')
    def check_email(cls, v):
        if v is not None and len(v) > 0:
            if len(v) < 5:
                raise ValueError('邮箱必须大于五位！')
            if not MakeTool.check_re(v, 'email'):
                raise ValueError('请输入正确的邮箱')
        return v.title()

    @validator('phone')
    def check_phone(cls, v):
        if v is not None and len(v) > 0:
            if len(v) != 11:
                raise ValueError('手机号码必须是11位！')
        return v.title()

class AuthCreate(AuthBase):
    username: str = None
    status: int = None
    role: str = None
    is_manager: int = 0