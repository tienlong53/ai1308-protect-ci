from predict import predict
def test_confident():
    assert predict({"cat": 0.9, "dog": 0.1}) == "cat"
def test_low_confidence():
    assert predict({"cat": 0.4, "dog": 0.35}) == "unknown"
