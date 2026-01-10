from app.ai_engine.risk_scoring import calculate_risk_score


def analyze_wheat_soil(pH: float, nitrogen_level: str) -> dict:
    result = {
        "crop": "Wheat",
        "soil_status": None,
        "risk_level": None,
        "recommendations": [],
        "explanation": ""
    }

    explanation_parts = []
    nutrient_deficiencies = []
    nutrient_excesses = []

    # STEP 1: pH Evaluation
    if pH < 5.5:
        pH_status = "severe"
        result["soil_status"] = "Acidic"
        explanation_parts.append(
            "Soil pH is too low. Acidic soil reduces nutrient availability for wheat."
        )
        result["recommendations"].append(
            "Apply lime to correct soil acidity before adding fertilizers"
        )
    else:
        pH_status = "normal"
        result["soil_status"] = "Normal"

    # STEP 2: Nitrogen Evaluation
    if nitrogen_level.lower() == "low":
        nutrient_deficiencies.append("nitrogen")
        explanation_parts.append(
            "Nitrogen level is low. Wheat requires nitrogen for healthy leaf growth."
        )
        if pH_status == "normal":
            result["recommendations"].append(
                "Apply nitrogen fertilizer (urea) in split doses"
            )

    # STEP 3: Risk Scoring
    risk = calculate_risk_score(
        pH_status=pH_status,
        nutrient_deficiencies=nutrient_deficiencies,
        nutrient_excesses=nutrient_excesses
    )

    result["risk_level"] = risk["risk_level"]
    result["explanation"] = " ".join(explanation_parts)

    if not result["recommendations"]:
        result["recommendations"].append(
            "Soil conditions are suitable for wheat cultivation."
        )

    return result
