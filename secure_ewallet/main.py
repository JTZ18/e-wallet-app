## main.py
from fastapi import FastAPI
from secure_ewallet.routers import router as api_router
from secure_ewallet.middlewares import setup_middlewares

app = FastAPI()

setup_middlewares(app)

app.include_router(api_router)
