from .schemas import AnalyzeRequest

def predict(req: AnalyzeRequest):
    reasons = []
    score = 0.0

    if req.network_mb > 50:
        score += 0.4
        reasons.append("High outbound network usage")

    if req.background_activity:
        score += 0.3
        reasons.append("Background activity detected")

    if req.suspicious_domains_count > 0:
        score += min(0.3, 0.1 * req.suspicious_domains_count)
        reasons.append("Connection to suspicious domains")

    confidence = min(0.99, 0.5 + score)
    prediction = "Suspicious" if confidence >= 0.75 else "Safe"

    return prediction, confidence, reasons