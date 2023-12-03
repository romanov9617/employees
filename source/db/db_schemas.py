from db.db_base import Base

from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class EmployeeORM(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    middle_name: Mapped[str]
    last_name: Mapped[str]
    position: Mapped[str]
    hired_at: Mapped[datetime]
    salary: Mapped[float]
    age: Mapped[int]
