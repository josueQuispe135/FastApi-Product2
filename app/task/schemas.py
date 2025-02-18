
from sqlmodel import Field, Relationship, Session, SQLModel, select
from typing import Optional

class TaskBase(SQLModel):
    title: str = Field(default=None)
    description: str | None = Field(default=None)
    completed: bool = False

# Modelo para crear una nueva tarea (hereda de TaskBase)
class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass
