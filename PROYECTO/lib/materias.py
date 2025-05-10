class Materia:
    def __init__(self, id_materia, nombre, id_curso):
        self.id_materia = id_materia
        self.nombre = nombre
        self.id_curso = id_curso

    def to_dict(self):
        return {
            "id_materia": self.id_materia,
            "nombre": self.nombre,
            "id_curso": self.id_curso
        }
