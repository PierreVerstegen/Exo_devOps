class Book:
	def __init__(self, id : int, title: str, author : str) -> None :
		self.id = id
		self.title = title
		self.author = author

	def to_dict(self) -> dict:
		"""Conversion utilitaire pour la sérialisation en JSON"""
		return {
			"id" : self.id,
			"title" : self.title,
			"author" : self.author
		}
	def serialize(self):
        	return {
            "id": self.id,
            "title": self.title,
            "author": self.author
        }