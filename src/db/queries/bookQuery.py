from src.db.connection import db
from bson import ObjectId

collections = db['books']

def convert_objectid(doc):
    """Convierte todos los ObjectId en un documento a str, incluso los anidados."""
    if isinstance(doc, list):
        return [convert_objectid(item) for item in doc]
    elif isinstance(doc, dict):
        return {
            key: convert_objectid(value)
            for key, value in doc.items()
        }
    elif isinstance(doc, ObjectId):
        return str(doc)
    else:
        return doc

async def getAllBook():
    books = []
    async for book in collections.find():
        books.append(convert_objectid(book))
    return books

async def countBooks():
    total = await collections.count_documents({})
    return  total