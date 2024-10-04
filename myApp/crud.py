from sqlalchemy.orm import Session
from . import models, schemas

def libro(db: Session, libro_id: int):
    return db.query(models.Libro).filter(models.Libro.id == libro_id).first()

def get_Libros(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Libro).offset(skip).limit(limit).all()

def create_libro(db: Session, libro: schemas.LibroCreate):
    db_libro = models.Libro(name=libro.name, autor=libro.autor, description=libro.description)
    db.add(db_libro)
    db.commit()
    db.refresh(db_libro)
    return db_libro

def delete_libro(db: Session, libro_id: int):
    db_libro = db.query(models.Libro).filter(models.Libro.id == libro_id).first()
    if db_libro:
        db.delete(db_libro)
        db.commit()
    return db_libro
