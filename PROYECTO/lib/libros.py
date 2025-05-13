class Libro:
    def __init__(self, isbn, titulo, autor, numero_ejemplares, Id_materia, Id_curso):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.numero_ejemplares = numero_ejemplares
        self.Id_materia = Id_materia
        self.Id_curso = Id_curso

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "numero_ejemplares": self.numero_ejemplares,
            "Id_materia": self.Id_materia,
            "Id_curso": self.Id_curso
        }
