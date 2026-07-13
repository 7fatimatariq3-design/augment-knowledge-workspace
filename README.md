# Augment Knowledge Workspace

A full-stack web application where users upload documents, organize knowledge, and interact with an AI-powered assistant that answers questions based on uploaded content.

Built as part of the **Augment Software Engineering Internship** (4-week, project-based).

## Tech Stack

| Layer      | Technology              |
|------------|--------------------------|
| Frontend   | React (Vite)             |
| Backend    | FastAPI                  |
| Database   | PostgreSQL               |
| AI         | OpenAI / OpenRouter API  |
| Deployment | Docker & Docker Compose  |

## Project Structure

```
augment-knowledge-workspace/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── core/          # settings (config.py)
│   │   ├── db/            # database engine/session + init_db.py
│   │   ├── models/        # SQLAlchemy models (user, document, chat)
│   │   ├── schemas/       # Pydantic schemas
│   │   ├── api/routes/    # auth, documents, chat endpoints
│   │   └── services/      # business logic (RAG, LLM, document handling)
│   ├── alembic/           # DB migrations
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   ├── services/
│   │   ├── hooks/
│   │   └── context/
│   ├── package.json
│   └── Dockerfile
├── docs/                  # design docs, diagrams, per-milestone artifacts
├── docker-compose.yml     # full stack orchestration
└── .github/workflows/     # CI placeholders
```

## Milestone Roadmap

| Milestone | Focus                          | Status |
|-----------|--------------------------------|--------|
| 1 | Project Foundation (Git, FastAPI setup, DB design, CRUD APIs) | 🔄 In Progress |
| 2 | Build the Product (React frontend, auth, upload/manage docs)  | ⬜ Planned |
| 3 | AI Integration (LLM API, prompt engineering, basic RAG, chat) | ⬜ Planned |
| 4 | Deployment & Finalization (Docker, testing, docs, demo)       | ⬜ Planned |

Full roadmap: https://internship-roadmap.augmentgroup.ai/

## Getting Started

### Backend
```bash
cd backend
python -m venv venv && source venv/Scripts/activate
pip install -r requirements.txt
cp .env.example .env
python -m app.db.init_db   # creates database tables
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Full stack via Docker
```bash
docker compose up --build
```

## Documentation

Design documents, architecture diagrams, and use case tables for each milestone live under `docs/`.
