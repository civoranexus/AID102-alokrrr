from app.ai_engine.risk_scoring import calculate_risk_score


def analyze_rice_soil(pH: float, nitrogen_level: str, potassium_level: str) -> dict:
    result = {
        "crop": "Rice",
        "soil_status": None,
        "risk_level": None,
        "recommendations": [],
        "explanation": ""
    }

    explanation_parts = []
    nutrient_deficiencies = []
    nutrient_excesses = []

    # STEP 1: pH Evaluation
    if pH < 5.0:
        pH_status = "severe"
        result["soil_status"] = "Highly Acidic"
        result["recommendations"].append(
            "Apply lime to slightly raise soil pH before nutrient application"
        )
        explanation_parts.append(
            "Soil pH is very low, which affects nutrient uptake in rice."
        )
    elif pH > 7.5:
        pH_status = "moderate"
        result["soil_status"] = "Alkaline"
        explanation_parts.append(
            "Soil pH is high. Alkaline soil reduces micronutrient availability in rice."
        )
    else:
        pH_status = "normal"
        result["soil_status"] = "Normal"

    # STEP 2: Nitrogen Evaluation
    if nitrogen_level.lower() == "low":
        nutrient_deficiencies.append("nitrogen")
        explanation_parts.append(
            "Nitrogen level is low. Rice requires high nitrogen for vegetative growth."
        )
        if pH_status == "normal":
            result["recommendations"].append(
                "Apply nitrogen fertilizer (urea) in split doses"
            )

    # STEP 3: Potassium Evaluation
    if potassium_level.lower() == "low":
        nutrient_deficiencies.append("potassium")
        explanation_parts.append(
            "Potassium level is low. It increases disease resistance and grain quality in rice."
        )
        if pH_status == "normal":
            result["recommendations"].append(
                "Apply potash-based fertilizer"
            )

    # STEP 4: Risk Scoring
    risk = calculate_risk_score(
        pH_status=pH_status,
        nutrient_deficiencies=nutrient_deficiencies,
        nutrient_excesses=nutrient_excesses
    )

    result["risk_level"] = risk["risk_level"]
    result["explanation"] = " ".join(explanation_parts)

    if not result["recommendations"]:
        result["recommendations"].append(
            "Soil conditions are suitable for rice cultivation."
        )

    return result
