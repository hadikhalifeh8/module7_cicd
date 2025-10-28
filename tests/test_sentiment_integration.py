def test_sentement_api_positive(test_client):
    input_data = {"text": "I love programming!"}
    response = test_client.post("/sentiment/predict", json=input_data)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    result = response.json()
    # assert 'label' in result, "Response should contain 'label' key"
    assert result['sentiment'] == 'POSITIVE', f"Expected 'POSITIVE', got {result['label']}"
    # result['sentiment'] from schema



def test_sentement_api_negative(test_client):
    input_data = {"text": "I hate programming!"}
    response = test_client.post("/sentiment/predict", json=input_data)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    result = response.json()
    # assert 'label' in result, "Response should contain 'label' key"
    assert result['sentiment'] == 'NEGATIVE', f"Expected 'NEGATIVE', got {result['label']}"
    # result['sentiment'] from schema    
    