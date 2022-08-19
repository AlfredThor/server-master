from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware
from app.test.auth import auth
from app.test.order import order
from configs.config import app

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True,
)

app.include_router(auth.router, prefix='/test/1.0', tags=['auth'])
app.include_router(order.router, prefix='/test/1.0', tags=['order'])

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8003, debug=True)
