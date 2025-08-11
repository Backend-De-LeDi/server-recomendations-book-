from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.validations.bookValidation import BookValidation
from rich import print
from src.client.chromaClient import initClient

bookRouter = APIRouter()

collection = initClient()

@bookRouter.post('/books/upload')
def upload_book(book:BookValidation):
    try:

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
            

        collection.add(
            documents=[textToEmbed],
            ids=[str(book.id)],
            metadatas=bookData
        )

        print(f"Libro {book.title} subido correctamente")
        
        return JSONResponse(content={'msg':'libro recibido'},status_code=200)
    except Exception as e:
        print(f"Error: {e}")
        return JSONResponse(content={"msg":"error inesperado en el servidor por favor intente de nuevo"}, status_code=500)