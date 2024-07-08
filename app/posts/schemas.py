from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class SPutPost(BaseModel):
    title: Optional[str] = Field(None, description="Новый заголовок поста")
    content: Optional[str] = Field(None, description="Новое содержимое поста")
    created_at: Optional[datetime] = Field(None, description="Статус публикации поста")
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True


class SPost(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
    