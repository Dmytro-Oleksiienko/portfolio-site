#!/bin/bash
set -e

DB_HOST_VAL="${DB_HOST:-db}"
DB_PORT_VAL="${DB_PORT:-5432}"

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL at ${DB_HOST_VAL}:${DB_PORT_VAL}..."
while ! python -c "
import socket, sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(('${DB_HOST_VAL}', ${DB_PORT_VAL}))
    s.close()
    sys.exit(0)
except Exception:
    sys.exit(1)
" 2>/dev/null; do
    echo "PostgreSQL is unavailable - sleeping..."
    sleep 1
done
echo "PostgreSQL is up!"

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Execute the main command
exec "$@"
