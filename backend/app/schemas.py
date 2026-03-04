from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    network_mb: float
    background_activity: bool
    suspicious_domains_count: int = 0

class AnalyzeResponse(BaseModel):
    prediction: str
    confidence: float
    reasons: list[str]