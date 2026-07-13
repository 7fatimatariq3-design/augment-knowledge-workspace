from datetime import datetime
from pydantic import BaseModel


class DocumentOut(BaseModel):
    id: int
    filename: str
    content_type: str | None = None
    uploaded_at: datetime

    class Config:
        from_attributes = True
