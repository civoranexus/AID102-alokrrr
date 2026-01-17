# backend/app/main.py

from fastapi import FastAPI
from app.api.routes_soil import router as soil_router
from app.api.routes_admin import router as admin_router
from app.api.routes_user import router as user_router

app = FastAPI(
    title="SoilSense – Intelligent Soil Health Analyzer",
    version="1.0.0"
)

app.include_router(soil_router)
app.include_router(admin_router)
app.include_router(user_router)

@app.get("/")
def root():
    return {
        "message": "SoilSense API is running",
        "docs": "/docs"
    }
