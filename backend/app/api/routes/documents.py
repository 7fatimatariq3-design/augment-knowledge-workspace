"""
Milestone 1: CRUD scaffolding for documents.
Milestone 2: Wire up to frontend upload UI.
Milestone 3: Feed extracted_text into RAG indexing pipeline.
"""
from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.document import DocumentOut

router = APIRouter()


@router.post("/upload", response_model=DocumentOut)
def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # TODO: save file to disk/storage, extract text, persist Document row
    raise NotImplementedError("Implement in Milestone 1/2")


@router.get("/", response_model=List[DocumentOut])
def list_documents(db: Session = Depends(get_db)):
    # TODO: return documents for current authenticated user
    raise NotImplementedError("Implement in Milestone 1/2")


@router.delete("/{document_id}")
def delete_document(document_id: int, db: Session = Depends(get_db)):
    # TODO: delete document + file
    raise NotImplementedError("Implement in Milestone 1/2")
