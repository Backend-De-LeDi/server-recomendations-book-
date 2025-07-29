from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.bookRouter import bookRouter
from src.routers.recommendationsRouter import recommendationsRouter
from src.routers.bookSearchRoute import bookSearchRouter
app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:3402",  # por ejemplo, si usás React
    "https://tu-dominio.com"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # orígenes permitidos
    allow_credentials=True,           # permite cookies/autenticación
    allow_methods=["*"],              # permite todos los métodos HTTP
    allow_headers=["*"]               # permite todos los headers
)


app.include_router(router=bookRouter)
app.include_router(router=recommendationsRouter)
app.include_router(router=bookSearchRouter)
