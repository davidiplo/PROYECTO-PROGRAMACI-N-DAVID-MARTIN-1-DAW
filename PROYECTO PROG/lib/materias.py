from database.database import Database

class Materia:
    def __init__(self, nombre, id=None):
        self.id = id
        self.nombre = nombre

    @staticmethod
    def agregar_materia(nombre):
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("INSERT INTO materias (nombre) VALUES (%s)", (nombre,))
        db.commit()
        db.close()
        print("📘 Materia agregada correctamente.")

    @staticmethod
    def listar_materias():
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("SELECT id, nombre FROM materias")
        materias = cursor.fetchall()
        db.close()
        if not materias:
            print("⚠️ No hay materias registradas.")
        else:
            for materia in materias:
                print(f"[{materia[0]}] {materia[1]}")

    @staticmethod
    def eliminar_materia(id_materia):
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("DELETE FROM materias WHERE id = %s", (id_materia,))
        db.commit()
        db.close()
        print("🗑️ Materia eliminada.")
