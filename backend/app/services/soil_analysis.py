# backend/app/services/soil_analysis.py

from app.ai_engine.wheat_logic import analyze_wheat_soil
from app.ai_engine.rice_logic import analyze_rice_soil
from app.ai_engine.cotton_logic import analyze_cotton_soil


def analyze_soil(crop: str, soil_data: dict) -> dict:
    """
    Master soil analysis service.
    Routes soil data to the appropriate crop AI engine.

    Parameters:
        crop (str): Crop type (wheat, rice, cotton)
        soil_data (dict): Soil parameters

    Returns:
        dict: AI-generated soil health analysis
    """

    crop = crop.lower()

    if crop == "wheat":
        return analyze_wheat_soil(
            pH=soil_data.get("pH"),
            nitrogen_level=soil_data.get("nitrogen")
        )

    elif crop == "rice":
        return analyze_rice_soil(
            pH=soil_data.get("pH"),
            nitrogen_level=soil_data.get("nitrogen"),
            potassium_level=soil_data.get("potassium")
        )

    elif crop == "cotton":
        return analyze_cotton_soil(
            pH=soil_data.get("pH"),
            nitrogen_level=soil_data.get("nitrogen"),
            potassium_level=soil_data.get("potassium")
        )

    else:
        return {
            "error": f"Crop '{crop}' is not supported yet."
        }
