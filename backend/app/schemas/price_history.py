from datetime import datetime
from pydantic import BaseModel, ConfigDict


class PriceHistoryBase(BaseModel):
    offer_id: int
    price: float
    original_price: float | None = None
    discount_percentage: float | None = None
    currency: str


class PriceHistoryCreate(PriceHistoryBase):
    pass


class PriceHistoryUpdate(BaseModel):
    price: float | None = None
    original_price: float | None = None
    discount_percentage: float | None = None
    currency: str | None = None


class PriceHistoryResponse(PriceHistoryBase):
    id: int
    scraped_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )