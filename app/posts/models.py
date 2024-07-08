from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Date
from datetime import datetime


class Posts(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    content: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(Date)
    updated_at: Mapped[datetime] = mapped_column(Date)
