from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.brand import (
    BrandCreate,
    BrandResponse,
)
from app.services.brand_service import BrandService

router = APIRouter(
    prefix="/brands",
    tags=["Brands"]
)


@router.get(
    "/",
    response_model=list[BrandResponse]
)
def get_brands(
    db: Session = Depends(get_db)
):
    return BrandService.get_all(db)


@router.post(
    "/",
    response_model=BrandResponse
)
def create_brand(
    brand: BrandCreate,
    db: Session = Depends(get_db)
):
    return BrandService.create(
        db,
        brand
    )