
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.repositories import support_case_repository
from app.schemas.support_case import (
    SupportCaseCreate,
    SupportCaseResponse,
    SupportCaseUpdate,
)

router = APIRouter(prefix="/support-cases", tags=["Support Cases"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "",
    response_model=SupportCaseResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_case(
    case_data: SupportCaseCreate,
    db: Session = Depends(get_db),
):
    return support_case_repository.create_support_case(db, case_data)


@router.get("", response_model=list[SupportCaseResponse])
def list_cases(
    limit: int = Query(default=100, ge=1, le=500),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
):
    return support_case_repository.get_support_cases(db, limit, offset)


@router.get("/{case_id}", response_model=SupportCaseResponse)
def get_case(
    case_id: int,
    db: Session = Depends(get_db),
):
    case = support_case_repository.get_support_case_by_id(db, case_id)

    if case is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Support case {case_id} was not found.",
        )

    return case


@router.patch("/{case_id}", response_model=SupportCaseResponse)
def update_case(
    case_id: int,
    update_data: SupportCaseUpdate,
    db: Session = Depends(get_db),
):
    case = support_case_repository.update_support_case(
        db=db,
        case_id=case_id,
        update_data=update_data.model_dump(exclude_unset=True),
    )

    if case is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Support case {case_id} was not found.",
        )

    return case
