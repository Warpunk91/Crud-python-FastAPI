from sqlalchemy import Column, Integer, String
from ..database import Base

class Libro(Base):
    __tablename__ = "Libro"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    autor = Column(String, index=True)
    description = Column(String, index=True)