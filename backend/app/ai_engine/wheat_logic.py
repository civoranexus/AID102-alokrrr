# backend/app/ai_engine/wheat_logic.py

def analyze_wheat_soil(pH: float, nitrogen_level: str) -> dict:
    """
    AI logic for wheat soil health analysis.
    Parameters:
        pH (float): Soil pH value
        nitrogen_level (str): 'low', 'medium', or 'high'
    Returns:
        dict: AI-generated soil health analysis
    """

    result = {
        "crop": "Wheat",
        "soil_status": None,
        "risk_level": None,
        "recommendations": [],
        "explanation": ""
    }

    explanation_parts = []

    # STEP 1: pH Evaluation (Highest Priority)
    if pH < 5.5:
        result["soil_status"] = "Acidic"
        result["risk_level"] = "High"
        result["recommendations"].append(
            "Apply lime to correct soil acidity before adding fertilizers"
        )
        explanation_parts.append(
            "Soil pH is too low, making it acidic. Acidic soil reduces nutrient availability "
            "and affects wheat root development."
        )
        soil_acidic = True
    else:
        result["soil_status"] = "Normal"
        soil_acidic = False

    # STEP 2: Nitrogen Evaluation (Only after pH check)
    if nitrogen_level.lower() == "low":
        if not soil_acidic:
            result["recommendations"].append(
                "Apply nitrogen fertilizer (urea) in split doses"
            )
        explanation_parts.append(
            "Nitrogen levels are low. Wheat requires adequate nitrogen for healthy leaf growth "
            "and proper yield formation."
        )

    # STEP 3: Risk Adjustment for Normal Soil
    if not result["recommendations"]:
        result["risk_level"] = "Low"
        result["recommendations"].append(
            "No immediate soil treatment required. Soil conditions are suitable for wheat cultivation."
        )
        explanation_parts.append(
            "Soil pH and nitrogen levels are within acceptable ranges for wheat."
        )

    # STEP 4: Final Explanation Assembly
    result["explanation"] = " ".join(explanation_parts)

    return result
