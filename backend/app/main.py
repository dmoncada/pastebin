from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session
from app.models import PasteCreate, PasteOut
from app.db import get_session, init_db
from app import crud, cache

app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()


@app.post("/paste", response_model=PasteOut)
def create_paste(paste: PasteCreate, session: Session = Depends(get_session)):
    return crud.create_paste(session, paste)


@app.get("/paste/{paste_id}", response_model=PasteOut)
def read_paste(paste_id: str, session: Session = Depends(get_session)):
    cached = cache.get_cached_paste(paste_id)
    if cached:
        # Fake timestamps for cached response
        from datetime import datetime

        return PasteOut(
            id=paste_id,
            content=cached.decode(),
            created_at=datetime.utcnow(),
            expires_at=datetime.utcnow(),
        )

    db_paste = crud.get_paste(session, paste_id)
    if not db_paste:
        raise HTTPException(status_code=404, detail="Paste not found")
    cache.cache_paste(paste_id, db_paste.content)
    return db_paste
