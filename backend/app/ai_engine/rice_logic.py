# backend/app/ai_engine/rice_logic.py

def analyze_rice_soil(pH: float, nitrogen_level: str, potassium_level: str) -> dict:
    """
    AI logic for rice soil health analysis.
    Parameters:
        pH (float): Soil pH value
        nitrogen_level (str): 'low', 'medium', or 'high'
        potassium_level (str): 'low', 'medium', or 'high'
    Returns:
        dict: AI-generated soil health analysis for rice
    """

    result = {
        "crop": "Rice",
        "soil_status": None,
        "risk_level": None,
        "recommendations": [],
        "explanation": ""
    }

    explanation_parts = []
    soil_problem = False

    # STEP 1: pH Evaluation (Highest Priority)
    if pH < 5.0:
        result["soil_status"] = "Highly Acidic"
        result["risk_level"] = "High"
        result["recommendations"].append(
            "Apply lime to slightly raise soil pH before nutrient application"
        )
        explanation_parts.append(
            "Soil pH is very low. Highly acidic soil affects root function and nutrient uptake in rice."
        )
        soil_problem = True

    elif pH > 7.5:
        result["soil_status"] = "Alkaline"
        result["risk_level"] = "Medium"
        result["recommendations"].append(
            "Apply organic matter to improve soil balance"
        )
        explanation_parts.append(
            "Soil pH is high. Alkaline soil can reduce micronutrient availability for rice."
        )
        soil_problem = True

    else:
        result["soil_status"] = "Normal"

    # STEP 2: Nitrogen Evaluation
    if nitrogen_level.lower() == "low":
        explanation_parts.append(
            "Nitrogen level is low. Rice requires high nitrogen for vegetative growth and yield formation."
        )
        if not soil_problem:
            result["recommendations"].append(
                "Apply nitrogen fertilizer (urea) in split doses"
            )

    # STEP 3: Potassium Evaluation
    if potassium_level.lower() == "low":
        explanation_parts.append(
            "Potassium level is low. Potassium improves disease resistance and grain quality in rice."
        )
        if not soil_problem:
            result["recommendations"].append(
                "Apply potash-based fertilizer to improve potassium levels"
            )

    # STEP 4: Risk Adjustment
    if result["recommendations"]:
        if not result["risk_level"]:
            result["risk_level"] = "Medium"
    else:
        result["risk_level"] = "Low"
        result["recommendations"].append(
            "Soil conditions are suitable for rice cultivation. No immediate action required."
        )
        explanation_parts.append(
            "Soil pH and nutrient levels are within acceptable ranges for rice."
        )

    # STEP 5: Final Explanation
    result["explanation"] = " ".join(explanation_parts)

    return result
