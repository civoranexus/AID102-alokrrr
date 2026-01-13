# backend/app/main.py

from fastapi import FastAPI
from app.api.routes_soil import router as soil_router

app = FastAPI(
    title="SoilSense – Intelligent Soil Health Analyzer",
    description="AI-powered soil health analysis and advisory system",
    version="1.0.0"
)

# Register routes
app.include_router(soil_router)
