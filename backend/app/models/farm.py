# backend/app/models/farm.py

from pydantic import BaseModel


class Farm(BaseModel):
    location: str | None = None
    land_size_acres: float | None = None
    irrigation_type: str | None = None
