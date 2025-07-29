import asyncio
from src.db.connection import db
from src.db.queries.bookQuery import convert_objectid

collections = db['books']

async def getAllBook():
    books = []
    async for book in collections.find():
        books.append(convert_objectid(book))
    print(books)

if __name__ == "__main__":
    asyncio.run(getAllBook())