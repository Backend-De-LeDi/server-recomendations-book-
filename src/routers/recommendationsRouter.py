from fastapi.responses import JSONResponse
from fastapi import APIRouter,Body
from src.db.queries.bookQuery import getAllBook
from fastapi.encoders import jsonable_encoder
from src.validations.bookValidation import BookValidation
from typing import List
from rich import print
from src.utils.generateText import generateText
from src.client.chromaClient import initClient
from src.db.queries.bookQuery import countBooks


collection = initClient()

recommendationsRouter = APIRouter()

@recommendationsRouter.post('/recommendations')
async def recommendations_book(books:List[BookValidation] = Body(...)):
    try:

        baseRecommended = list(map(generateText ,books ))

        numberOfBooks = await countBooks()

        result = collection.query(
            query_texts=baseRecommended,
            n_results=numberOfBooks
        )

        return JSONResponse(content={'ids':result['ids'][0]},status_code=200)
    except Exception as erro:
        print(erro)
        return JSONResponse(
            content={'msg': "error interno en el servidor por favor intente de nuevo"},
            status_code=500
        )