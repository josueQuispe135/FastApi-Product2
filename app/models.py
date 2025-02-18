# models.py
from datetime import datetime

from typing import Optional
from pydantic import BaseModel

from sqlalchemy import Column, DateTime, func
from sqlmodel import Field, Relationship, Session, SQLModel, select


