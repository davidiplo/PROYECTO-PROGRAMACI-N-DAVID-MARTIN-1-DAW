class Curso:
    def __init__(self, id_curso, nivel):
        self.id_curso = id_curso
        self.nivel = nivel

    def to_dict(self):
        return {
            "id_curso": self.id_curso,
            "nivel": self.nivel
        }
