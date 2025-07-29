from fastapi import APIRouter,Query
from fastapi.responses import JSONResponse
from src.client.chromaClient import initClient
from src.db.queries.bookQuery import countBooks

collection = initClient()

bookSearchRouter = APIRouter()

@bookSearchRouter.get('/books')
async def searchBookForQuery(query:str = Query(...)):
     
     numberOfBooks = await countBooks()

     result = collection.query(
        query_texts=[query],
        n_results=numberOfBooks,
     )
     
     return JSONResponse(content={'ids':result['ids'][0]},status_code=200)