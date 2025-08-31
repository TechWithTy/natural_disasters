import logging
from typing import Dict, Optional

from fastapi import APIRouter, Query

from app.core.third_party_integrations.natural_disasters.client import (
    OpenFEMANaturalDisastersClient,
)

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/openfema/natural-disasters", tags=["natural_disasters-declarations"])


# Utility

def list_declarations_util(*, filter: Optional[str], top: int, skip: int, select: Optional[str], orderby: Optional[str]) -> Dict:
    client = OpenFEMANaturalDisastersClient()
    return client.list_disaster_declarations(filter=filter, top=top, skip=skip, select=select, orderby=orderby)


# Routes
@router.get("/declarations")
async def list_disaster_declarations(filter: Optional[str] = Query(default=None), top: int = 1000, skip: int = 0, select: Optional[str] = None, orderby: Optional[str] = None) -> Dict:
    return list_declarations_util(filter=filter, top=top, skip=skip, select=select, orderby=orderby)
