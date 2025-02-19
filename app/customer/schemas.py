
from sqlmodel import Field, Relationship, Session, SQLModel, select
from typing import Optional

class CustomerBase(SQLModel):
    name: str = Field(default=None)
    city: str | None = Field(default=None)
    age: int = 0

# Modelo para crear una nueva tarea (hereda de CustomerBase)
class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass
