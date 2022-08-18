from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware
from app.test.auth import auth
# from configs.config import app

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=['*'],
#     allow_methods=['*'],
#     allow_headers=['*'],
#     allow_credentials=True,
# )

# app.include_router(auth.router, prefix='/test/auth', tags=['auth'])


from fastapi import FastAPI

app=FastAPI()

# @router.get('get', summary='主页', dependencies=[Depends(get_token_header)])
# async def index(db: Session = Depends(get_db)):
@app.get('/')
async def index():
    return {'code':90}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8003)