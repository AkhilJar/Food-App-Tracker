from fastapi import FastAPI

from app.routers import inventory

app = FastAPI(title="Food Tracker API")


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(inventory.router)