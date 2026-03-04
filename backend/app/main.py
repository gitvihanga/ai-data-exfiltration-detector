from fastapi import FastAPI  # type: ignore[reportMissingImports]
from .schemas import AnalyzeRequest, AnalyzeResponse
from .detector import predict

app = FastAPI(title="AI Data Exfiltration Malware Detector")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(payload: AnalyzeRequest):
    prediction, confidence, reasons = predict(payload)
    return AnalyzeResponse(
        prediction=prediction,
        confidence=confidence,
        reasons=reasons
    )