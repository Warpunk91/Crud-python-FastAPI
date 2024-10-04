from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import engine, get_db

# Crear las tablas
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Ruta para obtener todos los items
@app.get("/libros/", response_model=list[schemas.Libro])
def getLibros(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    libros = crud.get_Libros(db, skip=skip, limit=limit)
    return libros

# Ruta para crear un nuevo item
@app.post("/libros/", response_model=schemas.Libro)
def createLibro(libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    return crud.create_libro(db=db, libro=libro)

# Ruta para obtener un item por ID
@app.get("/libros/{libro_id}", response_model=schemas.Libro)
def getLibro(libro_id: int, db: Session = Depends(get_db)):
    db_libro = crud.libro(db, libro_id=libro_id)
    if db_libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return db_libro

# Ruta para eliminar un item
@app.delete("/libros/{id}")
def deleteLibro(id: int, db: Session = Depends(get_db)):
    dbLibro = crud.delete_libro(db, id)
    if dbLibro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return {"message": "Libro Eliminado"}


# Ruta para actualizar un item
@app.put("/libros/{libro_id}", response_model=schemas.Libro)
def updateLibro(libro_id: int, libro: schemas.LibroUpdate, db: Session = Depends(get_db)):
    db_libro = crud.update_libro(db, libro_id, libro=libro)
    if db_libro is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_libro
