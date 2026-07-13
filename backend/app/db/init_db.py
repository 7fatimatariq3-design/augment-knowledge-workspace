"""
Helper to create all tables in the database.
Useful for quick local development (instead of Alembic migrations).

Usage (from backend/ folder):
    python -m app.db.init_db
"""
from app.db.database import Base, engine
from app.models import user, document, chat  # noqa: F401  (import so models register with Base)


def init_db():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")


if __name__ == "__main__":
    init_db()
