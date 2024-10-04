from pydantic import BaseModel
from typing import Optional

class LibroBase(BaseModel):
    name: str
    autor: str
    description: str

class LibroCreate(LibroBase):
    pass

class Libro(LibroBase):
    id: int
    
class LibroUpdate(BaseModel):
    name: Optional[str] = None
    autor: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True

