
from datetime import datetime
from typing import Optional,TYPE_CHECKING
from sqlalchemy import DateTime, func, Column
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.products_category.models import ProductCategory
    from app.products_brand.models import ProductBrand
class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(default=None)
    price: int = 0
    description: str | None = Field(default=None)
    category: str | None = Field(default=None)
    image: str = Field(default=None)

    category_id: Optional[int] = Field(default=None, foreign_key="product_category.id")
    category: Optional["ProductCategory"] = Relationship(back_populates="products")

    brand_id: Optional[int] = Field(default=None, foreign_key="product_brand.id")
    brand: Optional["ProductBrand"] = Relationship(back_populates="products")

    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), nullable=True
        ),
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), onupdate=func.now(), nullable=True),
    )