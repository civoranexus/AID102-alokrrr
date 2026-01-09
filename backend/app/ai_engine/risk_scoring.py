# backend/app/ai_engine/risk_scoring.py

def calculate_risk_score(
    pH_status: str,
    nutrient_deficiencies: list,
    nutrient_excesses: list
) -> dict:
    """
    Shared risk scoring model for soil health analysis.

    Parameters:
        pH_status (str): 'normal', 'moderate', or 'severe'
        nutrient_deficiencies (list): list of deficient nutrients
        nutrient_excesses (list): list of excess nutrients

    Returns:
        dict: risk_score and risk_level
    """

    score = 0

    # pH risk scoring (highest priority)
    if pH_status == "severe":
        score += 50
    elif pH_status == "moderate":
        score += 30

    # Nutrient deficiency scoring
    score += len(nutrient_deficiencies) * 20

    # Nutrient excess scoring
    score += len(nutrient_excesses) * 15

    # Risk level mapping
    if score > 50:
        risk_level = "High"
    elif score >= 21:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return {
        "risk_score": score,
        "risk_level": risk_level
    }
