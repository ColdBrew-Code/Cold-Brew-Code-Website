# Cold Brew Code Website

## Run locally

1. Activate the virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Create `.env` from `.env.example` and set `DB_PASSWORD=postgres` for local Docker PostgreSQL.
4. Start the development server with `python manage.py runserver`.

The Django project lives in the `config` package.

## Run PostgreSQL and Redis with Docker

1. Start the containers with `docker compose up -d`.
2. Make sure your local `.env` has `DB_PASSWORD=postgres`.
3. Stop the containers with `docker compose down` when you are done.