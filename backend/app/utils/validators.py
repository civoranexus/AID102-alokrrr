# backend/app/utils/validators.py

def normalize_level(value: str) -> str:
    """
    Normalizes nutrient level strings.
    """
    return value.strip().lower()
