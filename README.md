# Portfolio Site

A personal portfolio website built with **Django** and **FastAPI**.

## Tech Stack

- **Backend**: Django 6.0 — main site, admin panel, data models
- **API**: FastAPI — contact form microservice (receives messages via REST)
- **Database**: PostgreSQL (Django ORM + SQLAlchemy)
- **Frontend**: Vanilla HTML/CSS/JS with Tabler Icons
- **Design**: Dark theme, responsive layout, matrix grid background
- **Hosting**: Railway

## Features

- 🧑‍💻 Profile section with avatar, bio, and availability badge
- 🛠️ Skills / Technologies display
- 📂 Projects showcase with GitHub links
- 🎓 Experience timeline
- 📬 Contact form powered by FastAPI
- 📱 Fully responsive (desktop, tablet, mobile)

## Project Structure

```
portfolio_site/
├── portfolio/                  # Django project root
│   ├── manage.py
│   ├── portfolio/              # Django settings & config
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── main/                   # Main Django app
│   │   ├── models.py           # Profile, Skill, Project, Experience
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── templates/main/
│   │       └── index.html
│   └── fastapi_service/        # FastAPI contact microservice
│       ├── main.py
│       ├── models.py
│       └── database.py
├── railway.toml                # Railway config (Django service)
├── railway-fastapi.toml        # Railway config (FastAPI service)
├── Dockerfile                  # Multi-target Docker image
├── docker-compose.yml          # Local container orchestration
├── docker-entrypoint.sh        # Django startup script
├── .env.docker                 # Docker environment variables
├── .dockerignore
├── requirements.txt
├── .env.example
└── .gitignore
```

## Getting Started

### Option 1: Deploy to Railway (Production)

Deploy the portfolio to [Railway](https://railway.com) — no cold starts, free tier with $5/month credits.

#### Step 1: Create a Railway project

1. Go to [railway.com](https://railway.com) and sign in with GitHub
2. Click **"New Project"** → **"Deploy from GitHub repo"**
3. Select your `portfolio-site` repository

#### Step 2: Add PostgreSQL database

1. In your Railway project, click **"+ New"** → **"Database"** → **"Add PostgreSQL"**
2. Railway will automatically create a `DATABASE_URL` variable

#### Step 3: Configure the Django service

1. The first service created from your repo will use `railway.toml` by default (Django)
2. Go to the service **Settings** → **Variables** and add:
   - `DJANGO_SECRET_KEY` — generate a secure random string
   - `DJANGO_DEBUG` — set to `False`
   - `DATABASE_URL` — reference the PostgreSQL plugin variable (`${{Postgres.DATABASE_URL}}`)
   - `FASTAPI_URL` — the public URL of your FastAPI service (set after Step 4)

#### Step 4: Add the FastAPI service

1. In the same project, click **"+ New"** → **"GitHub Repo"** → select the same repo
2. Go to the new service's **Settings** → **Config as Code Path** → set to `railway-fastapi.toml`
3. Add environment variables:
   - `DATABASE_URL` — reference the PostgreSQL plugin variable (`${{Postgres.DATABASE_URL}}`)
   - `CORS_ORIGINS` — set to the Django service's public URL (e.g., `https://your-django-service.up.railway.app`)

#### Step 5: Generate domains

1. For each service, go to **Settings** → **Networking** → **"Generate Domain"**
2. Update `FASTAPI_URL` on the Django service with the FastAPI domain
3. Update `CORS_ORIGINS` on the FastAPI service with the Django domain

That's it! Both services will auto-deploy on every push to your GitHub repo.

---

### Option 2: Docker (Local Development)

The easiest way to run the project locally — no need to install Python or PostgreSQL.

**Prerequisites:** [Docker](https://www.docker.com/products/docker-desktop/) installed and running.

```bash
# Clone the repository
git clone https://github.com/Dmytro-Oleksiienko/portfolio-site.git
cd portfolio-site

# Start all services
docker compose up --build
```

That's it! The app will be available at:

- 🌐 **Site**: http://localhost:8000
- 🔧 **Admin panel**: http://localhost:8000/admin
- 📬 **Contact API**: http://localhost:8001

```bash
# Run in background
docker compose up -d --build

# View logs
docker compose logs -f

# Stop all services
docker compose down

# Stop and remove all data
docker compose down -v
```

> **Note:** Docker uses `.env.docker` for configuration. Edit it to change default credentials.

---

### Option 3: Local Setup

### Prerequisites

- Python 3.10+
- PostgreSQL

### Installation

```bash
# Clone the repository
git clone https://github.com/Dmytro-Oleksiienko/portfolio-site.git
cd portfolio-site

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your secret key and database settings
```

### Setting Up PostgreSQL

```bash
# Start PostgreSQL service
brew services start postgresql@17

# Create the database
createdb portfolio
```

### Running the Django Server

```bash
cd portfolio
python manage.py migrate
python manage.py createsuperuser  # Create admin user
python manage.py runserver
```

Visit `http://127.0.0.1:8000` for the site and `http://127.0.0.1:8000/admin` for the admin panel.

### Running the FastAPI Service

```bash
cd portfolio
uvicorn fastapi_service.main:app --port 8001 --reload
```

The contact API will be available at `http://127.0.0.1:8001`.

### Adding Content

1. Go to Django Admin at `/admin`
2. Add your **Profile** (name, bio, photo, links)
3. Add **Skills**, **Projects**, and **Experience** entries
4. Refresh the main page to see your portfolio

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DJANGO_SECRET_KEY` | Django secret key | *required* |
| `DJANGO_DEBUG` | Enable debug mode | `True` |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated hosts | Empty |
| `RAILWAY_PUBLIC_DOMAIN` | Railway public domain (auto-set by Railway) | — |
| `DB_NAME` | PostgreSQL database name | `portfolio` |
| `DB_USER` | PostgreSQL user | `postgres` |
| `DB_PASSWORD` | PostgreSQL password | Empty |
| `DB_HOST` | PostgreSQL host | `localhost` (`db` in Docker) |
| `DB_PORT` | PostgreSQL port | `5432` |
| `DATABASE_URL` | Full database URL (Railway/FastAPI) | `postgresql://postgres@localhost:5432/portfolio` |
| `CORS_ORIGINS` | Comma-separated CORS origins | `*` |
| `FASTAPI_URL` | URL of the FastAPI contact service | `http://localhost:8001` |
