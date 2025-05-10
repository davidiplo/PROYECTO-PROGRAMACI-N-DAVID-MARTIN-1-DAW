import unittest
from unittest.mock import patch, MagicMock
from PROYECTO.app import (
    validar_nie, validar_isbn,
    GestionAlumnos, GestionLibros, GestionMaterias,
    GestionCursos, GestionPrestamos
)
from PROYECTO.ui.menu import Menu


# ----------------- VALIDACIONES -----------------

class TestValidaciones(unittest.TestCase):
    def test_validar_nie_valido(self):
        self.assertTrue(validar_nie("X1234567A"))

    def test_validar_nie_invalido(self):
        self.assertFalse(validar_nie("12345678Z"))

    def test_validar_isbn_valido(self):
        self.assertTrue(validar_isbn("123456789X"))

    def test_validar_isbn_invalido(self):
        self.assertFalse(validar_isbn("ABC"))


# ----------------- GESTIÓN ALUMNOS -----------------

class TestGestionAlumnos(unittest.TestCase):

    @patch("app.cargar_csv", return_value=[])
    @patch("app.guardar_csv")
    @patch("builtins.input", side_effect=["X1234567A", "Juan", "Pérez", "ESO", "sí"])
    def test_añadir_alumno(self, mock_input, mock_guardar, mock_cargar):
        gestor = GestionAlumnos()
        with patch("PROYECTO.lib.alumnos.Alumno.to_dict", return_value={
            "nie": "X1234567A", "nombre": "Juan", "apellidos": "Pérez", "tramo": "ESO", "bilingue": "sí"
        }):
            gestor.añadir()
            mock_guardar.assert_called_once()


# ----------------- GESTIÓN LIBROS -----------------

class TestGestionLibros(unittest.TestCase):

    @patch("app.cargar_csv", return_value=[])
    @patch("app.guardar_csv")
    @patch("builtins.input", side_effect=["123456789X", "1984", "Orwell", "Minotauro"])
    def test_añadir_libro(self, mock_input, mock_guardar, mock_cargar):
        gestor = GestionLibros()
        with patch("PROYECTO.lib.libros.Libro.to_dict", return_value={
            "isbn": "123456789X", "titulo": "1984", "autor": "Orwell", "editorial": "Minotauro"
        }):
            gestor.añadir()
            mock_guardar.assert_called_once()


# ----------------- GESTIÓN MATERIAS -----------------

class TestGestionMaterias(unittest.TestCase):

    @patch("app.cargar_csv", return_value=[])
    @patch("app.guardar_csv")
    @patch("builtins.input", side_effect=["MAT01", "Matemáticas", "CUR01"])
    def test_añadir_materia(self, mock_input, mock_guardar, mock_cargar):
        gestor = GestionMaterias()
        with patch("PROYECTO.lib.materias.Materia.to_dict", return_value={
            "id_materia": "MAT01", "nombre": "Matemáticas", "id_curso": "CUR01"
        }):
            gestor.añadir()
            mock_guardar.assert_called_once()


# ----------------- GESTIÓN CURSOS -----------------

class TestGestionCursos(unittest.TestCase):

    @patch("app.cargar_csv", return_value=[])
    @patch("app.guardar_csv")
    @patch("builtins.input", side_effect=["CUR01", "1º ESO"])
    def test_añadir_curso(self, mock_input, mock_guardar, mock_cargar):
        gestor = GestionCursos()
        with patch("PROYECTO.lib.cursos.Curso.to_dict", return_value={
            "id_curso": "CUR01", "nivel": "1º ESO"
        }):
            gestor.añadir()
            mock_guardar.assert_called_once()


# ----------------- GESTIÓN PRÉSTAMOS -----------------

class TestGestionPrestamos(unittest.TestCase):

    @patch("app.cargar_csv")
    @patch("app.guardar_csv")
    @patch("builtins.input", side_effect=["X1234567A", "123456789X", "pendiente"])
    def test_añadir_prestamo(self, mock_input, mock_guardar, mock_cargar):
        mock_cargar.side_effect = [
            [{"nie": "X1234567A"}],     # alumnos
            [{"isbn": "123456789X"}],  # libros
            []                         # préstamos
        ]
        gestor = GestionPrestamos()
        with patch("PROYECTO.lib.prestamos.Prestamo.to_dict", return_value={
            "nie": "X1234567A", "isbn": "123456789X", "estado": "pendiente"
        }):
            gestor.añadir()
            mock_guardar.assert_called_once()


# ----------------- MENÚ PRINCIPAL -----------------

class TestMenu(unittest.TestCase):

    @patch("builtins.input", side_effect=["administrador", "1234"])
    def test_iniciar_sesion_valida(self, mock_input):
        menu = Menu()
        self.assertTrue(menu.iniciar_sesion())

    @patch("builtins.input", side_effect=["user", "wrong"])
    def test_iniciar_sesion_invalida(self, mock_input):
        menu = Menu()
        self.assertFalse(menu.iniciar_sesion())

    @patch("builtins.input", side_effect=[
        "administrador", "1234",  # login
        "2",  # alumnos
        "1",  # listar
        "0",  # volver
        "0"   # salir
    ])
    def test_menu_listar_alumnos(self, mock_input):
        menu = Menu()
        with patch.object(menu.gestores["2"], "listar") as mock_listar:
            menu.mostrar_menu()
            mock_listar.assert_called_once()

    @patch("builtins.input", side_effect=[
        "administrador", "1234", "0"
    ])
    def test_menu_salir_directamente(self, mock_input):
        menu = Menu()
        menu.mostrar_menu()  # Solo inicia y sale sin errores


if __name__ == "__main__":
    unittest.main()
