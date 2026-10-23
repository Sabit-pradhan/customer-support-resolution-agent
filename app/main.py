
from fastapi import FastAPI

from app.api.routes.investigations import router as investigations_router
from app.api.routes.support_cases import router as support_cases_router

app = FastAPI(
    title="Agentic AI Customer Support Resolution System",
    description=(
        "An AI-powered system for investigating customer complaints "
        "and recommending policy-based resolutions."
    ),
    version="0.1.0",
)

# Register API endpoints.
app.include_router(support_cases_router)
app.include_router(investigations_router)


@app.get("/")
def root():
    return {
        "message": "Customer Support Resolution System API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "customer-support-resolution-agent",
    }
