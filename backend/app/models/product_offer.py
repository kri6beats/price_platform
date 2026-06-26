from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Numeric,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class ProductOffer(Base):
    __tablename__ = "product_offers"

    __table_args__ = (
        UniqueConstraint(
            "product_variant_id",
            "store_id",
            name="uq_variant_store"
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    product_variant_id: Mapped[int] = mapped_column(
        ForeignKey("product_variants.id", ondelete="CASCADE")
    )

    store_id: Mapped[int] = mapped_column(
        ForeignKey("stores.id", ondelete="CASCADE")
    )

    product_url: Mapped[str | None] = mapped_column(String)

    last_price: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2)
    )

    last_scraped_at: Mapped[datetime | None] = mapped_column(
        DateTime
    )

    is_available: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    product_variant = relationship("ProductVariant")
    store = relationship("Store")

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )