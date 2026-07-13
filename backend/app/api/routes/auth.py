"""
Milestone 1 (foundation) / Milestone 2 (full implementation): Authentication routes.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import UserCreate, UserOut, Token

router = APIRouter()


@router.post("/register", response_model=UserOut)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    # TODO: hash password, save user, handle duplicate email
    raise NotImplementedError("Implement in Milestone 2")


@router.post("/login", response_model=Token)
def login(email: str, password: str, db: Session = Depends(get_db)):
    # TODO: verify credentials, issue JWT
    raise NotImplementedError("Implement in Milestone 2")
