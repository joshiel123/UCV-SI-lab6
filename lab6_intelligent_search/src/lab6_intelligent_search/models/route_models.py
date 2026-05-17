from pydantic import BaseModel
from typing import Dict

class RouteRequest(BaseModel):
    start: str
    goal: str

# Añade este nuevo modelo abajo:
class BayesianRequest(BaseModel):
    evidence: Dict[str, int]