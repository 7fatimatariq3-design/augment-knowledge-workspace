"""
Augment Knowledge Workspace - Backend Entry Point
Milestone 1: Project Foundation
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import auth, documents, chat

app = FastAPI(
    title="Augment Knowledge Workspace API",
    description="Backend API for document upload, management, and AI-powered chat",
    version="0.1.0",
)

# CORS - adjust allowed origins for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(documents.router, prefix="/api/documents", tags=["Documents"])
app.include_router(chat.router, prefix="/api/chat", tags=["Chat"])


@app.get("/")
def read_root():
    return {"status": "ok", "service": "Augment Knowledge Workspace API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
