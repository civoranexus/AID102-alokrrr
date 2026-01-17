# backend/app/api/routes_admin.py

from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/health")
def system_health():
    """
    Basic admin health check endpoint.
    """
    return {
        "status": "ok",
        "message": "SoilSense system is running"
    }
