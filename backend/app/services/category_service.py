from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.category_repository import CategoryRepository
from app.schemas.category import CategoryCreate


class CategoryService:

    @staticmethod
    def get_all(db: Session):
        return CategoryRepository.get_all(db)

    @staticmethod
    def create(
        db: Session,
        category: CategoryCreate
    ):
        existing = CategoryRepository.get_by_slug(
            db,
            category.slug
        )

        if existing:
            raise HTTPException(
                status_code=400,
                detail="Category already exists"
            )

        return CategoryRepository.create(
            db,
            category
        )