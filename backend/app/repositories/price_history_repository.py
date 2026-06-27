from sqlalchemy.orm import Session

from app.models.price_history import PriceHistory
from app.schemas.price_history import PriceHistoryCreate


class PriceHistoryRepository:

    @staticmethod
    def get_all(db: Session):
        return db.query(PriceHistory).all()

    @staticmethod
    def create(
        db: Session,
        price_history: PriceHistoryCreate
    ):
        db_price_history = PriceHistory(
            offer_id=price_history.offer_id,
            price=price_history.price,
            original_price=price_history.original_price,
            discount_percentage=price_history.discount_percentage,
            currency=price_history.currency,
        )

        db.add(db_price_history)
        db.commit()
        db.refresh(db_price_history)

        return db_price_history