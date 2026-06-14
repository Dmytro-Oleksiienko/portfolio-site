# ============================================
# Base stage: shared Python dependencies
# ============================================
FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies for psycopg2
RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project source code
COPY portfolio/ .

# ============================================
# Django target
# ============================================
FROM base AS django

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# ============================================
# FastAPI target
# ============================================
FROM base AS fastapi

EXPOSE 8001

CMD ["uvicorn", "fastapi_service.main:app", "--host", "0.0.0.0", "--port", "8001"]
