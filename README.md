# rdbms_group4

## TODO

-   [ ] Import drug data (CSV ➜ MySQL)
-   [ ] Set up a frontend (consume the API)

## What’s inside

-   FastAPI service (`main.py`) with modular routers under `handlers/`
-   SQLAlchemy models (`models.py`) and Pydantic schemas (`schemas.py`)
-   MySQL database via `DATABASE_URL` in `.env`
-   Helper scripts in `scripts/` for importing, seeding, and resetting data
-   SQL reference schema (`project_schema.sql`)
-   Sample CSV (`drug_data_korean.csv`)

## Quick start

1. Create a `.env` with your MySQL connection string

    Example:

    ```env
    DATABASE_URL=mysql+pymysql://username:password@localhost:3306/rdbms_group4
    ```

2. Install dependencies

    ```cmd
    pip install -r requirements.txt
    ```

3. Run the API

    ```cmd
    python main.py
    ```

4. Open the interactive API docs

    - Swagger UI: http://localhost:8000/docs
    - ReDoc: http://localhost:8000/redoc

The root endpoint is available at `/`.

## Data import (CSV ➜ DB)

-   Import drug data (adjust the mapping in the script to your CSV headers if needed):

    ```cmd
    python -m scripts.import_data
    ```

-   Optional helpers:

    ```cmd
    # Seed reference data (languages, companies)
    python -m scripts.seed_data

    # Reset database (drop and recreate tables)
    python -m scripts.reset_database

    # Or clear data without dropping tables
    python -m scripts.reset_database --clear-only
    ```

## Project structure (summary)

```
rdbms_group4/
├─ handlers/            # API endpoint routers (languages, companies, drugs, users, feedback)
├─ scripts/             # Import/seed/reset utilities
├─ models.py            # SQLAlchemy models
├─ schemas.py           # Pydantic schemas
├─ database.py          # DB engine/session and init
├─ main.py              # FastAPI app wiring routers
├─ project_schema.sql   # SQL reference schema
└─ README.md
```

## Notes

-   Ensure your MySQL server is running and the target database exists (e.g., `CREATE DATABASE rdbms_group4;`).
-   If you see connection errors, re-check `.env` (driver, user, password, host, port 3306).
