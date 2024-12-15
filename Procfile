web: cd backend && uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-5000} --workers 4
release: cd backend && alembic upgrade head 