import pytest
from app import create_app

@pytest.fixture
def client():
	"""Client de test Flask isolé pour chaque test"""
	app = create_app()
	app.testing = True
	return app.test_client()

def test_get_all_books(client):
	# Quand / When
	response = client.get("/api/books")

	# Alors / Then
	assert response.status_code == 200
	data = response.get_json()
	assert isinstance(data, list)
	assert len(data) == 3 # Correpond aux fake data
	# Vérification basique de notre schéma
	assert set(data[0].keys()) == {"id", "title", "author"}

def test_book_not_found(client):
	response = client.get("/api/books/999")

	assert response.status_code == 404
	assert response.get_json()['error'] == "Livre non trouvé"

def test_get_single_book(client):
	response = client.get("/api/books/1")

	assert response.status_code == 200
	data = response.get_json()
	assert data["title"] == "Harry Potter"
	assert data["author"] == "JK Rowling"