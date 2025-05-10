class Libro:
    def __init__(self, isbn, titulo, autor, editorial):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "editorial": self.editorial
        }
