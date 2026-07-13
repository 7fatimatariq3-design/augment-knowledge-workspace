"""
Shared FastAPI dependencies (e.g. get_current_user).
Implemented fully in Milestone 2 once JWT auth is in place.
"""
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.database import get_db


def get_current_user(db: Session = Depends(get_db)):
    # TODO: decode JWT from Authorization header, fetch user
    raise NotImplementedError("Implement in Milestone 2")
