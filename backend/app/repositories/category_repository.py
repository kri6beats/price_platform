from sqlalchemy.orm import Session

from app.models.category import Category
from app.schemas.category import CategoryCreate


class CategoryRepository:

    @staticmethod
    def get_all(db: Session):
        return db.query(Category).all()

    @staticmethod
    def get_by_slug(
        db: Session,
        slug: str
    ):
        return (
            db.query(Category)
            .filter(Category.slug == slug)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        category: CategoryCreate
    ):
        db_category = Category(
            name=category.name,
            slug=category.slug,
            parent_id=category.parent_id
        )

        db.add(db_category)
        db.commit()
        db.refresh(db_category)

        return db_category