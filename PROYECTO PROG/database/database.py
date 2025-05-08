import mysql.connector

class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""  # Si tienes contraseña en MySQL, cámbiala aquí
        self.database = "proyectobd"

        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor()
        self._crear_tablas_si_no_existen()

    def _crear_tablas_si_no_existen(self):
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS alumnos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100),
                correo VARCHAR(100)
            )
            """)

            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS libros (
                id INT AUTO_INCREMENT PRIMARY KEY,
                titulo VARCHAR(200),
                autor VARCHAR(100)
            )
            """)

            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS materias (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100)
            )
            """)

            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS prestamos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                id_alumno INT,
                id_libro INT,
                fecha DATE,
                FOREIGN KEY (id_alumno) REFERENCES alumnos(id) ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (id_libro) REFERENCES libros(id) ON DELETE CASCADE ON UPDATE CASCADE
            )
            """)
            self.conn.commit()

    def get_cursor(self):
        return self.cursor

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()