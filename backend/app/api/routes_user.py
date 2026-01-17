# backend/app/api/routes_user.py

from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/info")
def user_info():
    """
    Placeholder for user-related endpoints.
    """
    return {
        "message": "User module will be extended later"
    }
