from flask import Flask
from app.controllers import book_controller

def init_routes(app : Flask) -> None:
	app.add_url_rule(
		"/api/books",
		endpoint="get_books",
		view_func=book_controller.get_books,
		methods=["GET"],
	)
	
	app.add_url_rule(
		"/api/books/<int:id>",
		endpoint="get_book_by_id",
		view_func=lambda id : book_controller.get_book(id),
		methods=["GET"],
	)
	
	app.add_url_rule(
		"/api/books",
		endpoint="add_book",
		view_func=book_controller.add_book,
		methods=["POST"]
	)

	app.add_url_rule(
		"/api/books/<int:id>",
		endpoint="update_book",
		view_func=book_controller.update_book,
		methods=["PUT"],
	)
	app.add_url_rule(
		"/api/books/<int:id>",
		endpoint="delete_book",
		view_func=book_controller.delete_book,
		methods=["DELETE"]
	)