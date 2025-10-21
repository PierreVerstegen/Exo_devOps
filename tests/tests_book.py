import pytest
from app import create_app
from app.models.book_model import Book

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

def test_add_book(client):
	response = client.post("/api/books", json={
    "title": "Test Book",
    "author": "Tester"})

	response2 = client.get("/api/books")
	assert response.status_code == 201
	assert response2.status_code == 200
	data = response.get_json()
	data2 = response2.get_json()
	assert set(data.keys()) == {"id", "title", "author"}
	assert isinstance(data2, list)
	assert len(data2) != 3

def test_update_book(client):
	response1 = client.get("/api/books/1")
	response2 = client.put("/api/books/1", json={
		"title": "Coucou",
		"author":"Moi"
	})

	assert response2.status_code == 201
	data1 = response1.get_json()
	data2 = response2.get_json()

	assert data1["title"] != data2["title"] or data1["author"] != data2["author"]

def test_delete_book(client):
	
	response2 = client.delete("/api/books/3")
	response3 = client.delete("/api/books/2")
	response1 = client.get("/api/books")

	assert response2.status_code == 200
	assert response3.status_code == 200
	data = response1.get_json()
	assert len(data) !=3

