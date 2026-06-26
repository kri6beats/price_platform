from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Numeric, CHAR, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class PriceHistory(Base):
    __tablename__ = "price_history"

    id: Mapped[int] = mapped_column(primary_key=True)

    offer_id: Mapped[int] = mapped_column(
        ForeignKey("product_offers.id", ondelete="CASCADE")
    )

    price: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2)
    )

    original_price: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2)
    )

    discount_percentage: Mapped[Decimal | None] = mapped_column(
        Numeric(5, 2)
    )

    currency: Mapped[str] = mapped_column(
        CHAR(3),
        nullable=False
    )

    scraped_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    offer = relationship("ProductOffer")