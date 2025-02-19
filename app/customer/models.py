
from datetime import datetime
from typing import Optional
from sqlalchemy import Column, DateTime, func
from sqlmodel import Field, SQLModel

class Customer(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    city: str | None = Field(default=None)
    age: int = 0
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