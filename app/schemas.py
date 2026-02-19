from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class TodoCreate(BaseModel):
    title: str


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    is_done: Optional[bool] = None


class TodoRead(BaseModel):
    id: int
    title: str
    is_done: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

