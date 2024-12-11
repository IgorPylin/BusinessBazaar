web: cd backend && uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-5000}
release: cd backend && alembic upgrade head 