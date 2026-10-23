
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.support_case import SupportCase
from app.schemas.support_case import SupportCaseCreate


def create_support_case(
    db: Session,
    case_data: SupportCaseCreate,
) -> SupportCase:
    """Save a new support case in the database."""
    new_case = SupportCase(**case_data.model_dump())

    db.add(new_case)
    db.commit()
    db.refresh(new_case)

    return new_case


def get_support_case_by_id(
    db: Session,
    case_id: int,
) -> SupportCase | None:
    """Retrieve a support case by its ID."""
    statement = select(SupportCase).where(SupportCase.id == case_id)
    return db.scalars(statement).first()


def get_support_cases(
    db: Session,
    limit: int = 100,
    offset: int = 0,
) -> list[SupportCase]:
    """Retrieve support cases with pagination."""
    statement = (
        select(SupportCase)
        .order_by(SupportCase.created_at.desc())
        .limit(limit)
        .offset(offset)
    )
    return list(db.scalars(statement).all())

def update_support_case(
    db: Session,
    case_id: int,
    update_data: dict,
) -> SupportCase | None:
    """Update selected fields on an existing support case."""

    case = get_support_case_by_id(db, case_id)

    if case is None:
        return None

    allowed_fields = {"status", "priority"}

    for field, value in update_data.items():
        if field not in allowed_fields:
            raise ValueError(f"Field cannot be updated: {field}")

        setattr(case, field, value)

    db.commit()
    db.refresh(case)

    return case
