from pydantic import BaseModel, Field, field_validator

class BookValidation(BaseModel):
    id: str = Field(..., description="ID requerido")
    title: str = Field(..., description="Título requerido")
    summary: str = Field(..., description="Resumen requerido")

    @field_validator('id', 'title', 'summary')
    def no_empty(cls, v, info):
        print(cls)
        print(v)
        print(info)
        if not v or not v.strip():
            print(v)
            raise ValueError(f'El campo "{info.field_name}" no puede estar vacío.')
        return v