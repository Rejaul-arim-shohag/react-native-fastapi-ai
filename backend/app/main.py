from fastapi import FastAPI

from app.api.v1.endpoints import health

app = FastAPI(title="AI Chat API")

app.include_router(health.router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "AI Chat API is running"}
