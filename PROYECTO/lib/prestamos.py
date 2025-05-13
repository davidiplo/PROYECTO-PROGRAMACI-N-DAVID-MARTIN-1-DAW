class Prestamo:
    def __init__(self, nie, curso, isbn, fecha_entrega, fecha_devolucion, estado="pendiente"):
        self.nie = nie
        self.curso = curso
        self.isbn = isbn
        self.fecha_entrega = fecha_entrega
        self.fecha_devolucion = fecha_devolucion
        self.estado = estado

    def to_dict(self):
        return {
            "nie": self.nie,
            "curso": self.curso,
            "isbn": self.isbn,
            "fecha_entrega": self.fecha_entrega,
            "fecha_devolucion": self.fecha_devolucion,
            "estado": self.estado
        }
