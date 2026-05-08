# AGENTS — ProyectoFlask-Valle

## Quick start

```bash
pip install flask flask-sqlalchemy psycopg2-binary python-dotenv
python app.py
```

Requires a running PostgreSQL server. No `requirements.txt` exists — create one if adding deps.

## Environment

- `.env` is loaded via `python-dotenv` in `app.py`.
- Required vars: `DB_USERNAME`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `DB_NAME`
- ⚠️ **Gotcha**: `base_datos/__init__.py:_init_db()` overwrites the DB URI with `os.getenv('DATABASE_URL')`. If `DATABASE_URL` is not set, the URI becomes `None` and the app crashes. Either set `DATABASE_URL` in `.env` or fix `_init_db` to use the `DB_*` vars.
- No `.env.example` template exists.

## Architecture

```
app.py                  ← Flask entry point (run with `python app.py`)
base_datos/
  __init__.py           ← SQLAlchemy instance + _init_db(app); calls db.create_all() at import time
  models.py             ← SQLAlchemy models: Usuario, Libros
modelos/
  libros.py             ← Plain Python class Libro (not used by Flask/SQLAlchemy)
  usuario.py            ← Empty file
```

- **Real models** live in `base_datos/models.py` (SQLAlchemy), not in `modelos/`.
- `modelos/` contains legacy/unused plain-Python classes. Do not add new SQLAlchemy models here.
- Tables are auto-created on import of `base_datos` via `db.create_all()`. No migration tool (Alembic) is configured.

## Conventions

- Spanish comments/codebase. Match existing language in new code.
- PEP 8 style, 4-space indentation.

## Testing / Linting

- No tests, no pytest config, no linter config currently exist.
- If adding tests: use `pytest` with Flask test client (`app.config['TESTING'] = True`).
- If adding linting: `flake8 .` or `ruff check .` (not yet installed).

## Commands

| Action | Command |
|---|---|
| Run dev server | `python app.py` |
| Run with Flask CLI | `flask run` |
| Install deps | `pip install flask flask-sqlalchemy psycopg2-binary python-dotenv` |
