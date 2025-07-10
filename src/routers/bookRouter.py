from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from src.validations.bookValidation import BookValidation

bookRouter = APIRouter()


@bookRouter.post('/books/upload')
def upload_book(book:BookValidation):
    try:
        print(book)
        return JSONResponse(content=book.model_dump(), status_code=200)
    except Exception as e:
        print(f"Error: {e}")
        return JSONResponse(content={"msg":"error inesperado en el servidor por favor intente de nuevo"}, status_code=422)