class Alumno:
    def __init__(self, nie, nombre, apellidos, tramo, bilingue):
        self.nie = nie
        self.nombre = nombre
        self.apellidos = apellidos
        self.tramo = tramo
        self.bilingue = bilingue

    def to_dict(self):
        return {
            "nie": self.nie,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "tramo": self.tramo,
            "bilingue": self.bilingue
        }
