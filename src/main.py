from fastapi import FastAPI
from src.routers.bookRouter import bookRouter
from src.routers.recommendationsRouter import recommendationsRouter

app = FastAPI()

app.include_router(router=bookRouter)
app.include_router(router=recommendationsRouter)
