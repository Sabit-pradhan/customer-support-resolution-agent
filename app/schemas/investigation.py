
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class InvestigationCreate(BaseModel):
    """Validate incoming investigation data."""

    case_id: int = Field(gt=0)
    summary: str = Field(min_length=5, max_length=500)
    findings: str = Field(min_length=5)

    model_config = ConfigDict(str_strip_whitespace=True)


class InvestigationResponse(BaseModel):
    """Define the investigation response returned by the API."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    case_id: int
    summary: str
    findings: str
    created_at: datetime
