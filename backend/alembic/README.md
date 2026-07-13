# Alembic Migrations

Run `alembic init alembic` from the `backend/` directory if not already initialized,
then point `sqlalchemy.url` in `alembic.ini` to `DATABASE_URL`, and set `target_metadata`
in `env.py` to `app.db.database.Base.metadata`.

Generate a migration:
```bash
alembic revision --autogenerate -m "create initial tables"
alembic upgrade head
```
