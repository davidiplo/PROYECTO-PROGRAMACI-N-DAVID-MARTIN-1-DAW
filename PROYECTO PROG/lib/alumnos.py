from database.database import Database

class Alumno:
    def __init__(self, nombre, id=None):
        self.id = id
        self.nombre = nombre

    @staticmethod
    def agregar_alumno(nombre, correo):
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("INSERT INTO alumnos (nombre, correo) VALUES (%s, %s)", (nombre, correo))
        db.commit()
        db.close()
        print("✅ Alumno agregado correctamente.")

    @staticmethod
    def listar_alumnos():
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("SELECT id, nombre, correo FROM alumnos")
        alumnos = cursor.fetchall()
        db.close()
        if not alumnos:
            print("⚠️ No hay alumnos registrados.")
        else:
            for alumno in alumnos:
                print(f"[{alumno[0]}] {alumno[1]} - {alumno[2]}")

    @staticmethod
    def eliminar_alumno(id_alumno):
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("DELETE FROM alumnos WHERE id = %s", (id_alumno,))
        db.commit()
        db.close()
        print("🗑️ Alumno eliminado.")