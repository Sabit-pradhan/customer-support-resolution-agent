# Agentic AI Customer Support Resolution System

An AI-powered customer support backend designed to investigate customer complaints, retrieve relevant business policies, and recommend appropriate resolutions through a controlled, multi-agent workflow.

## Business Problem

Customer support teams often spend significant time investigating complaints across payment, shipping, and ticketing systems. Manual investigation can delay resolutions, create inconsistent decisions, and make it difficult to track why an action was taken.

This project aims to streamline complaint handling through AI-assisted investigation, policy-based decision-making, controlled API integrations, and auditable resolution workflows.

## Project Objectives

- Automate repetitive customer complaint investigation.
- Retrieve relevant company policies using Retrieval-Augmented Generation (RAG).
- Coordinate specialized AI agents through a workflow orchestrator.
- Recommend policy-compliant resolutions such as refunds, replacements, or shipping investigations.
- Require human approval before sensitive actions such as refunds.
- Maintain case records, approval history, and audit logs.
- Improve reliability through testing, error handling, and idempotent operations.

## Planned Architecture

1. **FastAPI backend:** Receives customer support requests and exposes REST endpoints.
2. **Investigation agent:** Collects and summarizes relevant case, payment, shipping, and ticket information.
3. **Policy agent:** Retrieves relevant policy documents using RAG and identifies applicable rules.
4. **Resolution agent:** Recommends an appropriate action based on investigation findings and policy rules.
5. **LangGraph workflow:** Coordinates agents, workflow state, decision paths, and approval steps.
6. **PostgreSQL database:** Stores support cases, investigation findings, resolution records, and workflow history.
7. **Mock integrations:** Simulate payment, shipping, and ticketing services during development.
8. **Approval and audit controls:** Help ensure sensitive actions are authorized and traceable.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend application logic |
| FastAPI | REST API development |
| PostgreSQL | Persistent data storage |
| SQLAlchemy | Database access and ORM |
| Psycopg | PostgreSQL connectivity |
| Pydantic Settings | Environment-based configuration |
| Alembic | Planned database schema migrations |
| LangGraph | Planned multi-agent workflow orchestration |
| LLM and RAG | Planned language understanding and policy retrieval |
| Pytest and HTTPX | Automated testing |

## Current Development Progress

### Initial backend and database setup

- Created the initial project directory structure.
- Implemented basic FastAPI root and health-check endpoints.
- Installed the initial backend and database dependencies.
- Created the PostgreSQL `support_agent` database.
- Configured environment-based application settings in `.env`.
- Added a SQLAlchemy engine and session factory.
- Created a database connection test using `SELECT 1`.

### Next development milestones

- Define and validate the support case, investigation, and resolution models.
- Create and manage database tables using Alembic migrations.
- Build APIs to create, retrieve, and update support cases.
- Implement mock payment, shipping, and ticketing integrations.
- Develop the investigation, policy, and resolution agents.
- Add RAG-based policy retrieval and LangGraph orchestration.
- Implement approval gates, idempotency, audit logging, and automated evaluation.

## Project Structure

```text
customer-support-resolution-agent/
├── app/
│   ├── api/
│   ├── agents/
│   ├── db/
│   │   ├── models/
│   │   └── repositories/
│   ├── integrations/
│   ├── monitoring/
│   ├── rag/
│   ├── schemas/
│   ├── services/
│   ├── tools/
│   ├── workflows/
│   ├── config.py
│   └── main.py
├── evals/
├── mock_services/
│   ├── payments/
│   └── shipping/
├── policies/
├── scripts/
├── tests/
├── docs/
├── .env.example
├── .gitignore
├── pyproject.toml
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Local Setup

### 1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install fastapi "uvicorn[standard]" sqlalchemy "psycopg[binary]" pydantic-settings alembic pytest httpx python-dotenv
```

### 3. Configure environment variables

Create a local `.env` file based on `.env.example` and configure your PostgreSQL connection.

```dotenv
APP_NAME=Agentic AI Customer Support Resolution System
APP_ENV=development
APP_DEBUG=true
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/support_agent
```

Replace the password placeholder with your actual database password. URL-encode special characters when necessary. Never commit `.env` to version control.

### 4. Start the API

```powershell
python -m uvicorn app.main:app --reload
```

### 5. Explore the API

- Home endpoint: http://127.0.0.1:8000/
- Health endpoint: http://127.0.0.1:8000/health
- Interactive API documentation: http://127.0.0.1:8000/docs

### 6. Test the database connection

```powershell
python -m scripts.test_db_connection
```

The connection test should report success and return `1` from the test query.

## Security and Reliability

- Store credentials in environment variables, not source code.
- Exclude `.env` and `.venv` from Git.
- Require appropriate authorization and approval for sensitive operations.
- Record workflow decisions and action outcomes for auditability.
- Use idempotency controls to help prevent duplicate execution of supported operations.
- Validate inputs and test API behavior before deployment.

## Project Status

**Status:** In development.

The initial backend and PostgreSQL connectivity are the current foundation. The multi-agent workflow, RAG pipeline, mock integrations, and approval-controlled resolution process remain development milestones until implemented and tested.

## License

A license has not yet been selected.