from fastapi import FastAPI

from app.api.brand import router as brand_router

app = FastAPI(
    title="Platform Price API"
)

app.include_router(brand_router)


@app.get("/")
def root():
    return {
        "message": "Platform Price API"
    }