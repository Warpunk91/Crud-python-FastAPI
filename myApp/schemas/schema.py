from pydantic import BaseModel

class LibroBase(BaseModel):
    name: str
    autor: str
    description: str
    
class Libro(LibroBase):
    id: int

class LibroCreate(LibroBase):
    pass
    
class LibroUpdate(BaseModel):
    name: str
    autor: str
    description: str

    class Config:
        orm_mode = True

