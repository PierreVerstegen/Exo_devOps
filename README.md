Exercice pratique — CI/CD Flask & GitHub Actions

Énoncé

Faire évoluer l’API Flask et d’adapter la CI pour que le workflow valide tous les
nouveaux endpoints que vous allez créer.

Partie 1 — Implémentation de l’API
Méthode Route Fonction attendue Détails
GET /api/books/<int:id> Retourne le livre
correspondant à
l’ID
404 si non trouvé
POST /api/books Ajoute un nouveau
livre
JSON { 'title': '...',
'author': '...' }
PUT /api/books/<int:id> Met à jour
complètement un
livre
Titre et auteur
remplacés
PATCH /api/books/<int:id> Met à jour
partiellement un
livre
Un seul champ
peut changer
DELETE /api/books/<int:id> Supprime un livre Retourne code
204 si ok
Données simulées : Vous pouvez continuer à travailler avec la liste books = [...] déjà
présente dans le projet.

Partie 2 — Tests unitaires
Dans test_app.py, ajoutez au moins :
- 1 test par endpoint (nommage test_get_book_by_id, test_post_book, etc.)
- Vérifiez :
- Le code HTTP (200, 201, 404, 204)
- Le type de la réponse JSON
- Que la longueur de la liste change après POST ou DELETE.
Bonus (pour les plus rapides)
1. Ajoutez une route /api/books/search?author=... filtrant les livres par auteur.
2. Ajoutez un badge GitHub Actions dans le README.md :
![CI
Status](https://github.com/<user>/<repo>/actions/workflows/ci.yml/badge.svg)