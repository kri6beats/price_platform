from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class ProductVariant(Base):
    __tablename__ = "product_variants"

    __table_args__ = (
        UniqueConstraint(
            "product_id",
            "color",
            "storage",
            "ram",
            name="uq_product_variant"
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE")
    )

    sku: Mapped[str | None] = mapped_column(
        String,
        unique=True
    )

    ean: Mapped[str | None] = mapped_column(
        String,
        unique=True
    )

    color: Mapped[str | None] = mapped_column(String)
    storage: Mapped[str | None] = mapped_column(String)
    ram: Mapped[str | None] = mapped_column(String)
    model_number: Mapped[str | None] = mapped_column(String)

    product = relationship("Product")

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )