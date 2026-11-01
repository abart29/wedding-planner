# Project context

- Wedding-planner app for me and my partner, starting with venues and pricing, then budget and vendors.
- I'm an experienced Java backend developer (Spring Boot, Kafka, Mongo) learning Python, AI and web development as I build this.
- One service for now, structured as a modular monolith (src/wedding_planner/venues/, later budget/, vendors/, etc.).

# How to help

- Help me understand and build the project rather than doing the learning for me.
- Explain using Java comparisons where useful. Don't teach OOP basics.
- Do not write or change application code unless I explicitly ask. Prefer explaining the issue and guiding me.
- When reviewing my code, point out issues and explain why. Don't rewrite it.
- Ask before making significant product or technical decisions; do not invent requirements.
- Keep this file accurate and concise as decisions are made.

# Stack and decisions

- Python, managed with uv. Tests: pytest. Lint/format: ruff. Types: mypy (strict).
- Planned: FastAPI, Pydantic, SQLAlchemy 2.0, Alembic, SQLite. Later: Claude API and MCP.
- Money is always Decimal, created from strings. Never float.
- Tests first for business logic. Plain pytest functions preferred over unittest.
- Frontend: not decided yet.

# Commands

- uv run pytest
- uv run ruff check . && uv run ruff format .
- uv run mypy src tests

# Safety

- Never commit secrets, API keys or .env files. No real guest data in the repo.