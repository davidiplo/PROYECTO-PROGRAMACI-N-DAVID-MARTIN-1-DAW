from database.database import Database

class Libro:
    def __init__(self, titulo, autor, id=None):
        self.id = id
        self.titulo = titulo
        self.autor = autor

    @staticmethod
    def agregar_libro(titulo, autor):
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("INSERT INTO libros (titulo, autor) VALUES (%s, %s)", (titulo, autor))
        db.commit()
        db.close()
        print("📚 Libro agregado correctamente.")

    @staticmethod
    def listar_libros():
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("SELECT id, titulo, autor FROM libros")
        libros = cursor.fetchall()
        db.close()
        if not libros:
            print("⚠️ No hay libros registrados.")
        else:
            for libro in libros:
                print(f"[{libro[0]}] {libro[1]} - {libro[2]}")

    @staticmethod
    def eliminar_libro(id_libro):
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("DELETE FROM libros WHERE id = %s", (id_libro,))
        db.commit()
        db.close()
        print("🗑️ Libro eliminado.")
