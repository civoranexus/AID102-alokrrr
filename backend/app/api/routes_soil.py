# backend/app/api/routes_soil.py

from fastapi import APIRouter, HTTPException
from app.services.soil_analysis import analyze_soil

router = APIRouter()


@router.post("/analyze-soil")
def analyze_soil_endpoint(payload: dict):
    """
    API endpoint to analyze soil health using AI logic.
    """

    crop = payload.get("crop")
    soil_data = payload.get("soil_data")

    if not crop or not soil_data:
        raise HTTPException(
            status_code=400,
            detail="Payload must contain 'crop' and 'soil_data'"
        )

    result = analyze_soil(crop, soil_data)

    if "error" in result:
        raise HTTPException(
            status_code=400,
            detail=result["error"]
        )

    return {
        "status": "success",
        "analysis": result
    }
