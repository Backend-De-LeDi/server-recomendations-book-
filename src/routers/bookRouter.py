from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from src.validations.bookValidation import BookValidation
from fastapi.encoders import jsonable_encoder
from rich import print
from src.client.chromaClient import initClient
from src.utils.generateFlags import generateFlags

bookRouter = APIRouter()

collection = initClient()

@bookRouter.post('/books/upload')
def upload_book(book:BookValidation):
    try:
        # ? especificación de tipo de lenguaje para la IA debe saber que lenguaje es cada uno en base a las siglas 

        if(book.language == 'es'):
            language = 'español'

        if(book.language == 'en'):
            language = "ingles"

        textToEmbed = '\n'.join([
            book.title,
            book.summary,
            ', '.join(book.subgenre),
            language,
            book.synopsis,
            ', '.join(book.theme),
            book.genre,            
        ])

        bookData = {
            "id": str(book.id),
                "title": book.title,
                "author": book.author[0],
                "language": book.language,
                "yearBook": book.yearBook.year,
                "genre": book.genre,
                "format":book.format,
                "available":book.available,
                "level":book.level,
        }

        bookData.update(generateFlags('theme', book.theme))
        bookData.update(generateFlags('subgenre',   book.subgenre))

        print(bookData)

        collection.add(
            documents=[textToEmbed],
            ids=[str(book.id)],
            metadatas=bookData
        )
        return JSONResponse(content={'msg':'libro recibido'},status_code=200)
    except Exception as e:
        print(f"Error: {e}")
        return JSONResponse(content={"msg":"error inesperado en el servidor por favor intente de nuevo"}, status_code=500)