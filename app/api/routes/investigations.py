
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.repositories import investigation_repository
from app.schemas.investigation import (
    InvestigationCreate,
    InvestigationResponse,
)

router = APIRouter(
    prefix="/investigations",
    tags=["Investigations"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "",
    response_model=InvestigationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_investigation(
    investigation_data: InvestigationCreate,
    db: Session = Depends(get_db),
):
    try:
        return investigation_repository.create_investigation(
            db,
            investigation_data,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


@router.get(
    "",
    response_model=list[InvestigationResponse],
)
def list_investigations(
    limit: int = Query(default=100, ge=1, le=500),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
):
    return investigation_repository.get_investigations(
        db,
        limit=limit,
        offset=offset,
    )


@router.get(
    "/{investigation_id}",
    response_model=InvestigationResponse,
)
def get_investigation(
    investigation_id: int,
    db: Session = Depends(get_db),
):
    investigation = investigation_repository.get_investigation_by_id(
        db,
        investigation_id,
    )

    if investigation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Investigation {investigation_id} was not found.",
        )

    return investigation


@router.get(
    "/case/{case_id}",
    response_model=list[InvestigationResponse],
)
def list_case_investigations(
    case_id: int,
    db: Session = Depends(get_db),
):
    return investigation_repository.get_investigations_by_case_id(
        db,
        case_id,
    )
