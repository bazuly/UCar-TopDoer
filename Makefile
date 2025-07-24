
run locally:
	uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload

migrate-create:
	alembic revision --autogenerate -m "$(MIGRATION)"

migrate-apply:
	alembic upgrade head

make install:
	uv venv .venv
	uv init