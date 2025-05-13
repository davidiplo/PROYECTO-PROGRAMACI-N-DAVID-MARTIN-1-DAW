import unittest
import os
import tempfile
from PROYECTO.app import GestionCsv

class TestGestionCsv(unittest.TestCase):
    def setUp(self):
        # Crear un archivo temporal para pruebas
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+', newline='', encoding='utf-8')
        self.campos = ["nie", "nombre", "apellidos", "tramo", "bilingue"]
        self.gestor = GestionCsv(self.temp_file.name, self.campos)

    def tearDown(self):
        # Eliminar el archivo temporal después de cada prueba
        self.temp_file.close()
        os.unlink(self.temp_file.name)

    def test_listar_vacio(self):
        # Verificar que listar devuelve una lista vacía inicialmente
        self.assertEqual(self.gestor.listar(), [])

    def test_añadir_registro_valido(self):
        # Añadir un registro válido y verificar que se añade correctamente
        alumno = {
            "nie": "X1234567L",
            "nombre": "Juan",
            "apellidos": "Pérez",
            "tramo": "I",
            "bilingue": "S"
        }
        self.assertTrue(self.gestor.añadir(alumno))
        registros = self.gestor.listar()
        self.assertEqual(len(registros), 1)
        self.assertEqual(registros[0]["nombre"], "Juan")

    def test_añadir_nie_invalido(self):
        # Intentar añadir un registro con NIE inválido
        alumno = {
            "nie": "X123",
            "nombre": "Juan",
            "apellidos": "Pérez",
            "tramo": "I",
            "bilingue": "S"
        }
        with self.assertRaises(ValueError):
            self.gestor.añadir(alumno)

    def test_modificar_registro(self):
        # Añadir y luego modificar un registro
        alumno = {
            "nie": "X1234567L",
            "nombre": "Juan",
            "apellidos": "Pérez",
            "tramo": "I",
            "bilingue": "S"
        }
        self.gestor.añadir(alumno)
        nuevos_datos = {"nombre": "Juan Carlos"}
        self.assertTrue(self.gestor.modificar("nie", "X1234567L", nuevos_datos))
        registros = self.gestor.listar()
        self.assertEqual(registros[0]["nombre"], "Juan Carlos")

    def test_eliminar_registro(self):
        # Añadir y luego eliminar un registro
        alumno = {
            "nie": "X1234567L",
            "nombre": "Juan",
            "apellidos": "Pérez",
            "tramo": "I",
            "bilingue": "S"
        }
        self.gestor.añadir(alumno)
        self.assertTrue(self.gestor.eliminar("nie", "X1234567L"))
        self.assertEqual(self.gestor.listar(), [])

    def test_añadir_nie_duplicado(self):
        # Intentar añadir dos registros con el mismo NIE
        alumno1 = {
            "nie": "X1234567L",
            "nombre": "Juan",
            "apellidos": "Pérez",
            "tramo": "I",
            "bilingue": "S"
        }
        alumno2 = {
            "nie": "X1234567L",
            "nombre": "Ana",
            "apellidos": "López",
            "tramo": "II",
            "bilingue": "N"
        }
        self.gestor.añadir(alumno1)
        with self.assertRaises(ValueError):
            self.gestor.añadir(alumno2)

    def test_validar_isbn10_valido(self):
        # Verificar que un ISBN-10 válido se añade correctamente
        campos_libro = ["isbn", "titulo", "autor", "numero_ejemplares", "Id_materia", "Id_curso"]
        gestor_libros = GestionCsv(self.temp_file.name, campos_libro)
        libro = {
            "isbn": "0306406152",
            "titulo": "Libro de Prueba",
            "autor": "Autor",
            "numero_ejemplares": "3",
            "Id_materia": "MAT1",
            "Id_curso": "CUR1"
        }
        self.assertTrue(gestor_libros.añadir(libro))

    def test_validar_isbn10_invalido(self):
        # Verificar que un ISBN-10 inválido lanza una excepción
        campos_libro = ["isbn", "titulo", "autor", "numero_ejemplares", "Id_materia", "Id_curso"]
        gestor_libros = GestionCsv(self.temp_file.name, campos_libro)
        libro = {
            "isbn": "123",
            "titulo": "Libro de Prueba",
            "autor": "Autor",
            "numero_ejemplares": "3",
            "Id_materia": "MAT1",
            "Id_curso": "CUR1"
        }
        with self.assertRaises(ValueError):
            gestor_libros.añadir(libro)

if __name__ == '__main__':
    unittest.main()