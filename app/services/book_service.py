from app.models.book_model import Book
from app.forms.book_form import BookForm

BOOKS = [
	Book(1, "Harry Potter", "JK Rowling"),
	Book(2, "ça", "Stephen King"),
	Book(3, "La Bible", "Dieu")
]

def get_all() -> list[Book]:
	"""Retourne une liste complète des livres"""
	return BOOKS

def get_book_by_id(book_id : int) -> Book | None:
	"""Retourne un livre par son identifiant, sinon None."""
	return next((b for b in BOOKS if b.id == book_id), None)

def add_book(form: BookForm) -> list[Book]:
	new_id = len(BOOKS) + 1
	book = Book(
            id=new_id,
			title=form.title.data,
            author=form.author.data)
	BOOKS.append(book)
	return book

def update_book(book_id : int, form: BookForm) -> Book | None:
	book_to_update = next((b for b in BOOKS if b.id == book_id), None)
	if book_to_update == None:
		return None
	
	updated_book = Book(
		id=book_to_update.id,
		title=form.title.data,
		author=form.author.data
	)
	return updated_book

def delete_book(book_id : int) -> None:
	book_to_delete = next((b for b in BOOKS if b.id == book_id), None)
	if book_to_delete == None:
		return None
	BOOKS.remove(book_to_delete)
	return BOOKS