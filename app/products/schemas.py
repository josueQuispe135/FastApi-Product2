from typing import Optional
from sqlmodel import Field, SQLModel,Session,select
from pydantic import field_validator
from datetime import datetime
from app.db import engine
from app.products_category.schemas import ProductCategoryRead
from app.products_brand.schemas import ProductBrandRead
from app.products_brand.models import ProductBrand

class ProductBase(SQLModel):
    title: str = Field(default=None)
    price: int = 0
    description: Optional[str] = None
    image: Optional[str] = None

# Modelo para crear una nueva tarea (hereda de TaskBase)
class ProductCreate(ProductBase):
    category_id: Optional[int] = None
    brand_id: Optional[int] = None
    @field_validator("brand_id")
    @classmethod
    def validate_brand(cls, value):
        session = Session(engine)
        query = select(ProductBrand).where(ProductBrand.id == value)
        result = session.exec(query).first()
        if not result:
            raise ValueError(f"Brand Id:{value} doesn't exist")
        return value
  
class ProductUpdate(SQLModel):
    title: Optional[str] = None
    price: Optional[int] = None
    description: Optional[str] = None
    image: Optional[str] = None
    category_id: Optional[int] = None
    brand_id: Optional[int] = None

class ProductRead(ProductBase):
    id: int
    created_at: Optional[datetime]
    category: Optional[ProductCategoryRead] = None  # Relación con la categoría
    brand: Optional[ProductBrandRead] = None  # Relación con la categoría