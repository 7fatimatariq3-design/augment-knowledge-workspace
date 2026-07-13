# Backend - Augment Knowledge Workspace

FastAPI backend for the Augment Knowledge Workspace project.

## Local Setup

```bash
python -m venv venv
source venv/Scripts/activate    # Windows Git Bash
pip install -r requirements.txt
cp .env.example .env            # fill in DATABASE_URL etc.
uvicorn app.main:app --reload
```

API docs available at `http://localhost:8000/docs`.

## Structure

```
app/
  core/       -> app settings (config.py)
  db/         -> database engine/session (database.py), init_db.py to create tables
  models/     -> SQLAlchemy models
  schemas/    -> Pydantic request/response schemas
  api/routes/ -> route handlers (auth, documents, chat)
  services/   -> business logic (document handling, RAG, LLM calls)
tests/        -> pytest test suite
```

## Create Database Tables (quick dev method)

```bash
python -m app.db.init_db
```

For production-grade schema changes, use Alembic migrations instead (see `alembic/README.md`).

## Milestone Mapping

- **Milestone 1**: project setup, DB models, CRUD scaffolding (this state)
- **Milestone 2**: auth implementation, frontend integration
- **Milestone 3**: RAG pipeline + LLM chat
- **Milestone 4**: Dockerization, tests, docs, final polish
