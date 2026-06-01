from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class InsertRequest(BaseModel):
    vector: List[float]
    payload: Dict[str, Any]

class SearchRequest(BaseModel):
    vector: List[float]
    metric: Optional[str] = "cosine"

class SearchResponse(BaseModel):
    payload: Dict[str, Any]
    distance: float
