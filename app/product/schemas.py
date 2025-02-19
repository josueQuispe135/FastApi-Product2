
from sqlmodel import Field, Relationship, Session, SQLModel, select
from typing import Optional

class ProductBase(SQLModel):
    name: str = Field(default=None)
    description: str | None = Field(default=None)
    price: int = 0

# Modelo para crear una nueva tarea (hereda de ProductBase)
class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass
