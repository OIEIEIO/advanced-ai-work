import pytest
from api.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_login(client):
    response = client.post('/auth/login')
    assert response.status_code == 200
    assert response.json == {'message': 'Login successful'}

