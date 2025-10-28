from app.services.sentiment_service import predict_sentiment



def test_sentiment_position():
    input_text = "I love programming!"
    result = predict_sentiment(input_text)
    assert 'label' in result, "Result should contain 'label' key"
    assert result['label'] == 'POSITIVE', f"Expected 'POSITIVE', got {result['label']}"
    assert 0.5 < result['score'] <= 1.0, f"Score should be between 0.5 and 1.0, got {result['score']}"


def test_predict_sentiment():
    input_text = ""
    try:
        predict_sentiment(input_text)
        assert False, "Should raise value error for empty input text"
    except ValueError as e:
        assert True, f"value error raised as excepted : {e}"
    