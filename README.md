# Portfolio Site

A personal portfolio website built with **Django** and **FastAPI**.

## Tech Stack

- **Backend**: Django 6.0 — main site, admin panel, data models
- **API**: FastAPI — contact form microservice (receives messages via REST)
- **Database**: PostgreSQL (Django ORM + SQLAlchemy)
- **Frontend**: Vanilla HTML/CSS/JS with Tabler Icons
- **Design**: Dark theme, responsive layout, matrix grid background

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
├── Dockerfile                  # Multi-target Docker image
├── docker-compose.yml          # Container orchestration
├── docker-entrypoint.sh        # Django startup script
├── .env.docker                 # Docker environment variables
├── .dockerignore
├── requirements.txt
├── .env.example
└── .gitignore
```

## Getting Started

### Option 1: Docker (Recommended)

The easiest way to run the project — no need to install Python or PostgreSQL locally.

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

### Option 2: Local Setup

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
| `DJANGO_SECRET_KEY` | Django secret key | Dev fallback (insecure) |
| `DJANGO_DEBUG` | Enable debug mode | `True` |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated hosts | Empty |
| `DB_NAME` | PostgreSQL database name | `portfolio` |
| `DB_USER` | PostgreSQL user | `postgres` |
| `DB_PASSWORD` | PostgreSQL password | Empty |
| `DB_HOST` | PostgreSQL host | `localhost` (`db` in Docker) |
| `DB_PORT` | PostgreSQL port | `5432` |
| `DATABASE_URL` | FastAPI database URL | `postgresql://postgres@localhost:5432/portfolio` |
| `CORS_ORIGINS` | Comma-separated CORS origins | `*` |
