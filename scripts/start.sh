#!/bin/sh
set -e

echo "Waiting for database to be ready..."
sleep 15
echo "Database should be ready!"

echo "Running Alembic migrations..."
alembic upgrade head || { echo "Alembic migration failed!"; exit 1; }
echo "Migrations completed successfully!"

echo "Starting FastAPI application..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000

