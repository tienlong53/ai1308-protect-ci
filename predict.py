THRESHOLD = 0.95


def predict(scores):
    """Nhãn có điểm cao nhất; "unknown" khi độ tin cậy < THRESHOLD."""
    label = max(scores, key=scores.get)
    if scores[label] < THRESHOLD:
        return "unknown"
    return label
