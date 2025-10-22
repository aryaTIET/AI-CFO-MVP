def analyze_finances(data):
    """Analyzes financial health based on invoice total."""
    total = data.get("total", 0)

    # Example scoring logic
    score = 100 - (total / 1000) * 10
    if score < 0:
        score = 0

    insight = ""
    if total < 5000:
        insight = "Low expenditure — good cash management."
    elif total < 20000:
        insight = "Moderate spending — review recurring costs."
    else:
        insight = "High expense detected — possible cash flow risk."

    return {
        "vendor": data["vendor"],
        "date": data["date"],
        "total": total,
        "score": round(score, 2),
        "insight": insight
    }

