import requests

def test_read_investors():
    response = requests.get("http://localhost:8000/investors/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
