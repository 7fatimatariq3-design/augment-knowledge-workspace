"""
Milestone 3: AI-powered chat routes (RAG pipeline).
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.chat import ChatMessageIn, ChatMessageOut

router = APIRouter()


@router.post("/message", response_model=ChatMessageOut)
def send_message(payload: ChatMessageIn, db: Session = Depends(get_db)):
    # TODO: retrieve relevant document chunks (RAG), call LLM service, store + return response
    raise NotImplementedError("Implement in Milestone 3")


@router.get("/history/{session_id}")
def get_chat_history(session_id: int, db: Session = Depends(get_db)):
    # TODO: return chat message history for a session
    raise NotImplementedError("Implement in Milestone 3")
