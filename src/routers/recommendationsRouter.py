from fastapi.responses import JSONResponse
from fastapi import APIRouter
from src.db.queries.bookQuery import getAllBook
from fastapi.encoders import jsonable_encoder

recommendationsRouter = APIRouter()

@recommendationsRouter.get('/recommendations')
async def recommendations_book():
    try:
        books = await getAllBook()
        return JSONResponse(content=jsonable_encoder(books))
    except Exception as erro:
        print(erro)
        return JSONResponse(
            content={'msg': "error interno en el servidor por favor intente de nuevo"},
            status_code=500
        )