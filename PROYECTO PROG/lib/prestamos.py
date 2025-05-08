from database.database import Database
from datetime import date

class Prestamo:
    def __init__(self, id_alumno, id_libro, fecha=None, id=None):
        self.id = id
        self.id_alumno = id_alumno
        self.id_libro = id_libro
        self.fecha = fecha or date.today()

    @staticmethod
    def registrar_prestamo(id_alumno, id_libro):
        db = Database()
        cursor = db.get_cursor()
        cursor.execute(
            "INSERT INTO prestamos (id_alumno, id_libro, fecha) VALUES (%s, %s, %s)",
            (id_alumno, id_libro, date.today())
        )
        db.commit()
        db.close()
        print("📖 Préstamo registrado correctamente.")

    @staticmethod
    def listar_prestamos():
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("""
            SELECT p.id, a.nombre, l.titulo, p.fecha
            FROM prestamos p
            JOIN alumnos a ON p.id_alumno = a.id
            JOIN libros l ON p.id_libro = l.id
        """)
        prestamos = cursor.fetchall()
        db.close()
        if not prestamos:
            print("⚠️ No hay préstamos registrados.")
        else:
            for prestamo in prestamos:
                print(f"[{prestamo[0]}] {prestamo[1]} prestó '{prestamo[2]}' el {prestamo[3]}")

    @staticmethod
    def eliminar_prestamo(id_prestamo):
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("DELETE FROM prestamos WHERE id = %s", (id_prestamo,))
        db.commit()
        db.close()
        print("🗑️ Préstamo eliminado.")
