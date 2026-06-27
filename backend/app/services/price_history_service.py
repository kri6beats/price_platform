from sqlalchemy.orm import Session

from app.repositories.price_history_repository import (
    PriceHistoryRepository
)
from app.schemas.price_history import (
    PriceHistoryCreate
)


class PriceHistoryService:

    @staticmethod
    def get_all(db: Session):
        return PriceHistoryRepository.get_all(db)

    @staticmethod
    def create(
        db: Session,
        price_history: PriceHistoryCreate
    ):
        return PriceHistoryRepository.create(
            db,
            price_history
        )