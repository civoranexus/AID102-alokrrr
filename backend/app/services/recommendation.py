# backend/app/services/recommendation.py

def format_recommendations(recommendations: list) -> list:
    """
    Standardizes recommendation output.
    """
    return [rec.strip().capitalize() for rec in recommendations]
