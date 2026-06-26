from pydantic import BaseModel, ConfigDict


class BrandBase(BaseModel):
    name: str
    slug: str


class BrandCreate(BrandBase):
    pass


class BrandUpdate(BaseModel):
    name: str | None = None
    slug: str | None = None


class BrandResponse(BrandBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )