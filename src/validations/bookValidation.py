from pydantic import BaseModel, Field, HttpUrl,ConfigDict
from typing import List
from datetime import datetime
from bson import ObjectId
from pydantic import GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value,info):
        if not ObjectId.is_valid(value):
            raise ValueError("ID inválido de MongoDB")
        return ObjectId(value)

    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        schema = handler(core_schema)
        schema.update({"type": "string"})
        return schema

# Submodelo para contenido del libro
class ContentBook(BaseModel):
    idContentBook: str
    url_secura: HttpUrl
    id: PyObjectId = Field(..., alias="_id")

    model_config = ConfigDict(
        validate_by_alias=True,
        validate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId:str}
    )

# Submodelo para imagen de portada
class BookCoverImage(BaseModel):
    idBookCoverImage: str
    url_secura: HttpUrl
    id: PyObjectId = Field(..., alias="_id")

    model_config = ConfigDict(
        validate_by_alias=True,
        validate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId:str}
    )



# Modelo principal del libro
class BookValidation(BaseModel):
    id: PyObjectId = Field(..., alias="_id")
    title: str
    author: List[str]
    summary: str
    subgenre: List[str]
    language: str
    available: bool
    yearBook: datetime
    synopsis: str
    contentBook: ContentBook
    bookCoverImage: BookCoverImage
    theme: List[str]
    genre: str
    level: str
    format: str

    model_config = ConfigDict(
        validate_by_alias=True,
        validate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId:str}
    )
