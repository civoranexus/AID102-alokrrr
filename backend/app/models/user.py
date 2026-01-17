# backend/app/models/user.py

from pydantic import BaseModel


class User(BaseModel):
    name: str | None = None
    role: str = "farmer"
