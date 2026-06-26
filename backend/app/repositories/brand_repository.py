from sqlalchemy.orm import Session

from app.models.brand import Brand
from app.schemas.brand import BrandCreate


class BrandRepository:

    @staticmethod
    def get_by_slug(
    db: Session,
    slug: str
):
     return (
        db.query(Brand)
        .filter(Brand.slug == slug)
        .first()
    )