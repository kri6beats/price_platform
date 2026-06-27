from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.price_history import (
    PriceHistoryCreate,
    PriceHistoryResponse
)
from app.services.price_history_service import (
    PriceHistoryService
)

router = APIRouter(
    prefix="/price-history",
    tags=["Price History"]
)


@router.get(
    "/",
    response_model=list[PriceHistoryResponse]
)
def get_price_history(
    db: Session = Depends(get_db)
):
    return PriceHistoryService.get_all(db)


@router.post(
    "/",
    response_model=PriceHistoryResponse
)
def create_price_history(
    price_history: PriceHistoryCreate,
    db: Session = Depends(get_db)
):
    return PriceHistoryService.create(
        db,
        price_history
    )