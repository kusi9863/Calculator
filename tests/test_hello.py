import pytest
from src.api import app

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

def test_hello_route(client):
	response = client.get('/hello')
	assert response.status_code == 200
	assert response.get_json() == {"message": "Hello World!"}
