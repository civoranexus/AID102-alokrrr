# backend/app/ai_engine/cotton_logic.py

def analyze_cotton_soil(pH: float, nitrogen_level: str, potassium_level: str) -> dict:
    """
    AI logic for cotton soil health analysis.
    Parameters:
        pH (float): Soil pH value
        nitrogen_level (str): 'low', 'medium', or 'high'
        potassium_level (str): 'low', 'medium', or 'high'
    Returns:
        dict: AI-generated soil health analysis for cotton
    """

    result = {
        "crop": "Cotton",
        "soil_status": None,
        "risk_level": None,
        "recommendations": [],
        "explanation": ""
    }

    explanation_parts = []
    soil_problem = False

    # STEP 1: pH Evaluation (Cotton tolerant but not extreme)
    if pH < 6.0:
        result["soil_status"] = "Acidic"
        result["risk_level"] = "Medium"
        result["recommendations"].append(
            "Apply lime to slightly increase soil pH for cotton"
        )
        explanation_parts.append(
            "Soil pH is low. Cotton performs better in neutral to slightly alkaline soil."
        )
        soil_problem = True

    elif pH > 8.5:
        result["soil_status"] = "Highly Alkaline"
        result["risk_level"] = "High"
        result["recommendations"].append(
            "Add organic matter to reduce soil alkalinity"
        )
        explanation_parts.append(
            "Soil pH is very high. Excess alkalinity reduces nutrient uptake in cotton."
        )
        soil_problem = True

    else:
        result["soil_status"] = "Normal"

    # STEP 2: Potassium Evaluation (CRITICAL for cotton)
    if potassium_level.lower() == "low":
        explanation_parts.append(
            "Potassium level is low. Potassium is essential for boll development and disease resistance in cotton."
        )
        if not soil_problem:
            result["recommendations"].append(
                "Apply potash-based fertilizer to improve potassium levels"
            )

    # STEP 3: Nitrogen Evaluation (EXCESS is harmful)
    if nitrogen_level.lower() == "high":
        explanation_parts.append(
            "Nitrogen level is high. Excess nitrogen causes excessive vegetative growth and reduces cotton boll quality."
        )
        result["recommendations"].append(
            "Avoid additional nitrogen application and monitor crop growth"
        )

    elif nitrogen_level.lower() == "low":
        explanation_parts.append(
            "Nitrogen level is low. Cotton requires balanced nitrogen for healthy growth."
        )
        if not soil_problem:
            result["recommendations"].append(
                "Apply nitrogen fertilizer carefully in controlled amounts"
            )

    # STEP 4: Risk Adjustment
    if result["recommendations"]:
        if not result["risk_level"]:
            result["risk_level"] = "Medium"
    else:
        result["risk_level"] = "Low"
        result["recommendations"].append(
            "Soil conditions are suitable for cotton cultivation. No immediate action required."
        )
        explanation_parts.append(
            "Soil pH and nutrient levels are within acceptable ranges for cotton."
        )

    # STEP 5: Final Explanation
    result["explanation"] = " ".join(explanation_parts)

    return result
