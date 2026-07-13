from datetime import datetime
from pydantic import BaseModel


class ChatMessageIn(BaseModel):
    session_id: int | None = None
    message: str


class ChatMessageOut(BaseModel):
    id: int
    role: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True
