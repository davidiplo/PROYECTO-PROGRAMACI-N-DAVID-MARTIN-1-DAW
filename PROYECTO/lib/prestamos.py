class Prestamo:
    def __init__(self, nie, isbn, estado="pendiente"):
        self.nie = nie
        self.isbn = isbn
        self.estado = estado

    def to_dict(self):
        return {
            "nie": self.nie,
            "isbn": self.isbn,
            "estado": self.estado
        }
