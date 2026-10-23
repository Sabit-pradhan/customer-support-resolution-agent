
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.investigation import Investigation
from app.db.models.support_case import SupportCase
from app.schemas.investigation import InvestigationCreate


def create_investigation(
    db: Session,
    investigation_data: InvestigationCreate,
) -> Investigation:
    """Create an investigation linked to an existing support case."""

    case = db.get(SupportCase, investigation_data.case_id)

    if case is None:
        raise ValueError(
            f"Support case {investigation_data.case_id} was not found."
        )

    investigation = Investigation(
        **investigation_data.model_dump()
    )

    db.add(investigation)
    db.commit()
    db.refresh(investigation)

    return investigation


def get_investigation_by_id(
    db: Session,
    investigation_id: int,
) -> Investigation | None:
    """Retrieve an investigation by its ID."""

    statement = select(Investigation).where(
        Investigation.id == investigation_id
    )

    return db.scalars(statement).first()


def get_investigations(
    db: Session,
    limit: int = 100,
    offset: int = 0,
) -> list[Investigation]:
    """Retrieve investigations with pagination."""

    statement = (
        select(Investigation)
        .order_by(Investigation.created_at.desc())
        .limit(limit)
        .offset(offset)
    )

    return list(db.scalars(statement).all())


def get_investigations_by_case_id(
    db: Session,
    case_id: int,
) -> list[Investigation]:
    """Retrieve all investigations for one support case."""

    statement = (
        select(Investigation)
        .where(Investigation.case_id == case_id)
        .order_by(Investigation.created_at.desc())
    )

    return list(db.scalars(statement).all())
