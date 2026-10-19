
from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class SupportCase(Base):
    __tablename__ = "support_cases"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )
    customer_name: Mapped[str] = mapped_column(String(150))
    customer_email: Mapped[str] = mapped_column(String(255), index=True)
    subject: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(
        String(30), default="open", index=True
    )
    priority: Mapped[str] = mapped_column(
        String(20), default="medium"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
