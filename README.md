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

## Railway deployment

1. Set these environment variables in Railway:
	- `DEBUG=False`
	- `SECRET_KEY=<strong-random-secret>`
	- `ALLOWED_HOSTS=<your-app-domain>`
	- `CSRF_TRUSTED_ORIGINS=https://<your-app-domain>`
	- `DATABASE_URL=<from Railway PostgreSQL service>`
	- `REDIS_URL=<from Railway Redis service>`
2. Use the web start command from `Procfile`:
	- `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`
3. Railway will run the `release` command from `Procfile` to collect static files and run migrations automatically.
4. You can copy the values from [.env.railway.example](.env.railway.example) as a starting point.
