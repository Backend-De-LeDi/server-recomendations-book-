from fastapi import FastAPI
from src.routers.bookRouter import bookRouter

app = FastAPI()

app.include_router(router=bookRouter)
