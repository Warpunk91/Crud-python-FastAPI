from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import schema
from ..models import models
from ..database import get_db

appRouter = APIRouter()

@appRouter.get("/libros/", response_model=list[schema.Libro])
def getLibros(db: Session = Depends(get_db)):
    return db.query(models.Libro).all()

@appRouter.post("/libros/", response_model=schema.Libro)
def createLibro(libro: schema.LibroCreate, db: Session = Depends(get_db)):
    db_libro = models.Libro(name=libro.name, autor=libro.autor, description=libro.description)
    db.add(db_libro)
    db.commit()
    db.refresh(db_libro)
    return db_libro

@appRouter.get("/libros/{libro_id}", response_model=schema.Libro)
def getLibro(libro_id: int, db: Session = Depends(get_db)):
    return db.query(models.Libro).filter(models.Libro.id == libro_id).first()

@appRouter.delete("/libros/{libro_id}", response_model=schema.Libro)
def deleteLibro(libro_id: int, db: Session = Depends(get_db)):
    db_libro = db.query(models.Libro).filter(models.Libro.id == libro_id).first()
    if db_libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")  
    db.delete(db_libro)
    db.commit()
    return db_libro

@appRouter.put("/libros/{libro_id}", response_model=schema.Libro)
def updateLibro(libro_id: int, libro: schema.LibroUpdate, db: Session = Depends(get_db)):
    db_libro = db.query(models.Libro).filter(models.Libro.id == libro_id).first()
    if db_libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    if libro.name:
        db_libro.name = libro.name
    if libro.autor:
        db_libro.autor = libro.autor
    if libro.description:
        db_libro.description = libro.description
    db.commit()
    db.refresh(db_libro)
    return db_libro
