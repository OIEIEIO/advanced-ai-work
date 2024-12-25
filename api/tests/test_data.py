import pytest
from api.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_data_info(client):
    response = client.get('/data/info')
    assert response.status_code == 200
    assert response.json == {'data': 'Sample Data'}

