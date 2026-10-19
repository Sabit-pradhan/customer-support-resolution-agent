
from datetime import datetime

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Resolution(Base):
    __tablename__ = "resolutions"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )
    case_id: Mapped[int] = mapped_column(
        ForeignKey("support_cases.id"), index=True
    )
    resolution_type: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(
        String(30), default="pending", index=True
    )
    requires_approval: Mapped[bool] = mapped_column(
        Boolean, default=True
    )
    approved_by: Mapped[str | None] = mapped_column(
        String(150), nullable=True
    )
    executed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
