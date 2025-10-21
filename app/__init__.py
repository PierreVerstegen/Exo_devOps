from flask import Flask
from .routes import init_routes

def create_app() -> Flask:
	"""Crée et configurer l'application Flask"""
	app = Flask(__name__)
	init_routes(app)
	for rule in app.url_map.iter_rules():
		print(rule)
	return app