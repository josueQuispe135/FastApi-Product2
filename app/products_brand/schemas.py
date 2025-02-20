
from typing import Optional
from sqlmodel import Field, SQLModel

class ProductBrandBase(SQLModel):
    name: str = Field(default=None)
    description: str | None = Field(default=None)

# Modelo para crear una nueva tarea (hereda de TaskBase)
class ProductBrandCreate(ProductBrandBase):
    pass

class ProductBrandUpdate(ProductBrandBase):
    pass

class ProductBrandRead(SQLModel):
    id: int
    name: str
    description: Optional[str] = None