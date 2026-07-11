# Cold Brew Code Website

## Run locally

1. Create a virtual environment if you do not already have one:
   - Windows: `python -m venv .venv`
   - macOS / Linux: `python3 -m venv .venv`
2. Activate it:
   - Windows PowerShell: `& .venv\Scripts\Activate.ps1`
   - macOS / Linux: `source .venv/bin/activate`
3. Install dependencies with `pip install -r requirements.txt`.
4. Create `.env` from `.env.example` and set `DB_PASSWORD=postgres` for local Docker PostgreSQL.
5. Start the development server with `python manage.py runserver`.

## Run PostgreSQL and Redis with Docker

1. Start the containers with `docker compose up -d`.
2. Make sure your local `.env` has `DB_PASSWORD=postgres`.
3. Stop the containers with `docker compose down` when you are done.