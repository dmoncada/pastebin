from sqlmodel import Session, select
from datetime import datetime, timedelta
from app.models import Paste, PasteCreate


def create_paste(session: Session, data: PasteCreate) -> Paste:
    expires_at = datetime.utcnow() + timedelta(seconds=data.expires_in_seconds)
    paste = Paste(content=data.content, expires_at=expires_at)
    session.add(paste)
    session.commit()
    session.refresh(paste)
    return paste


def get_paste(session: Session, paste_id: str) -> Paste | None:
    statement = select(Paste).where(Paste.id == paste_id)
    result = session.exec(statement)
    return result.first()
