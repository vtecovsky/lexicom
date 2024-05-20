__all__ = ["router"]

from fastapi import APIRouter

router = APIRouter(tags=["Client"])

import src.api.routes  # noqa: E402, F401
