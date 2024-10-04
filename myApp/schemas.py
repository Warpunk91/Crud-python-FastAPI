from pydantic import BaseModel

class LibroBase(BaseModel):
    name: str
    autor: str
    description: str

class LibroCreate(LibroBase):
    pass

class Libro(LibroBase):
    id: int

    class Config:
        orm_mode = True
