from app.ai_engine.risk_scoring import calculate_risk_score


def analyze_cotton_soil(pH: float, nitrogen_level: str, potassium_level: str) -> dict:
    result = {
        "crop": "Cotton",
        "soil_status": None,
        "risk_level": None,
        "recommendations": [],
        "explanation": ""
    }

    explanation_parts = []
    nutrient_deficiencies = []
    nutrient_excesses = []

    # STEP 1: pH Evaluation
    if pH < 6.0:
        pH_status = "moderate"
        result["soil_status"] = "Acidic"
        explanation_parts.append(
            "Soil pH is low. Cotton prefers neutral to slightly alkaline soil."
        )
        result["recommendations"].append(
            "Apply lime to increase soil pH slightly"
        )
    elif pH > 8.5:
        pH_status = "severe"
        result["soil_status"] = "Highly Alkaline"
        explanation_parts.append(
            "Soil pH is very high. Excess alkalinity reduces nutrient uptake in cotton."
        )
    else:
        pH_status = "normal"
        result["soil_status"] = "Normal"

    # STEP 2: Potassium Evaluation
    if potassium_level.lower() == "low":
        nutrient_deficiencies.append("potassium")
        explanation_parts.append(
            "Potassium level is low. It is critical for boll quality in cotton."
        )
        if pH_status == "normal":
            result["recommendations"].append(
                "Apply potash-based fertilizer"
            )

    # STEP 3: Nitrogen Evaluation
    if nitrogen_level.lower() == "high":
        nutrient_excesses.append("nitrogen")
        explanation_parts.append(
            "Nitrogen level is high. Excess nitrogen reduces boll formation in cotton."
        )
        result["recommendations"].append(
            "Avoid additional nitrogen application"
        )

    elif nitrogen_level.lower() == "low":
        nutrient_deficiencies.append("nitrogen")
        explanation_parts.append(
            "Nitrogen level is low. Cotton requires balanced nitrogen."
        )
        if pH_status == "normal":
            result["recommendations"].append(
                "Apply nitrogen fertilizer carefully in controlled amounts"
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
            "Soil conditions are suitable for cotton cultivation."
        )

    return result
