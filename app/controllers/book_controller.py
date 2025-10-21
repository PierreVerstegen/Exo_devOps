from app.forms.book_form import BookForm
from app.services.book_service import add_book as add_book_service, update_book as update_book_service, delete_book as delete_book_service
from app.services.book_service import get_all, get_book_by_id
from flask import jsonify, request
from app.framework.decorators.inject import inject

def get_books():
	"""EndPoint : GET /api/books"""
	books = get_all()
	payload = [book.to_dict() for book in books]
	return jsonify(payload), 200

def get_book(id : int):
	"""EndPoint : GET /api/book/<id>"""
	book = get_book_by_id(id)
	if (book):
		return jsonify(book.to_dict()), 200
	return jsonify({"error" : "Livre non trouvé"}), 404

def add_book():
    form = BookForm(data=request.get_json())
    if form.validate():
        book = add_book_service(form)  # call the service function directly
        return jsonify(book.serialize()), 201
    return jsonify(form.errors), 400


def update_book(id: int):
    form = BookForm(data=request.get_json())
    if form.validate():
        book = update_book_service(id, form)
        if book is not None:
            return jsonify(book.serialize()), 201
        else:
            return jsonify({"error": "Book not found"}), 404
    return jsonify(form.errors), 400

def delete_book(id:int):
    books = delete_book_service(id)
    payload = [book.to_dict() for book in books]
    return jsonify(payload), 200