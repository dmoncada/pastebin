from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime, timedelta
import uuid


def generate_id():
    return uuid.uuid4().hex[:8]


class Paste(SQLModel, table=True):
    id: str = Field(default_factory=generate_id, primary_key=True, index=True)
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    expires_at: datetime = Field(
        default_factory=lambda: datetime.utcnow() + timedelta(days=7)
    )


class PasteCreate(SQLModel):
    content: str
    expires_in_seconds: Optional[int] = 604800  # 7 days


class PasteOut(SQLModel):
    id: str
    content: str
    created_at: datetime
    expires_at: datetime
