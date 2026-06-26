from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.brand_repository import BrandRepository
from app.schemas.brand import BrandCreate


class BrandService:

    @staticmethod
    def get_all(db: Session):
        return BrandRepository.get_all(db)

    @staticmethod
    def create(
        db: Session,
        brand: BrandCreate
    ):
        return BrandRepository.create(
            db,
            brand
        )