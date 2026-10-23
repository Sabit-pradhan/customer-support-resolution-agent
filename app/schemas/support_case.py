
from datetime import datetime
from typing import Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    field_validator,
)


class SupportCaseCreate(BaseModel):
    """Validate incoming customer support case data."""

    customer_name: str = Field(min_length=2, max_length=150)
    customer_email: EmailStr
    subject: str = Field(min_length=3, max_length=255)
    description: str = Field(min_length=10)
    priority: Literal["low", "medium", "high"] = "medium"

    @field_validator("customer_name", "subject", "description")
    @classmethod
    def trim_text(cls, value: str) -> str:
        """Remove surrounding whitespace and reject empty text."""
        value = value.strip()

        if not value:
            raise ValueError("This field cannot be empty.")

        return value


class SupportCaseResponse(BaseModel):
    """Define the data returned by the API."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    customer_name: str
    customer_email: str
    subject: str
    description: str
    status: str
    priority: str
    created_at: datetime
    updated_at: datetime


class SupportCaseUpdate(BaseModel):
    """Validate fields that can be updated on a support case."""

    status: Literal[
        "open",
        "in_progress",
        "resolved",
        "closed",
    ] | None = None

    priority: Literal[
        "low",
        "medium",
        "high",
    ] | None = None
