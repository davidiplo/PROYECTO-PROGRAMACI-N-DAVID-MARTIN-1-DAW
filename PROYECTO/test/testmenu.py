import unittest
from unittest.mock import patch, MagicMock
from PROYECTO.ui.menu import Menu
from PROYECTO.app import GestionCsv

class TestMenu(unittest.TestCase):

    @patch("builtins.input", side_effect=["administrador", "1234"])
    @patch("builtins.print")
    def test_login_success(self, mock_print, mock_input):
        menu = Menu()
        self.assertTrue(menu.login())
        mock_print.assert_any_call("Acceso concedido.\n")

    @patch("builtins.input", side_effect=["wrong_user", "wrong_pass", "administrador", "1234"])
    @patch("builtins.print")
    def test_login_failure_then_success(self, mock_print, mock_input):
        menu = Menu()
        self.assertTrue(menu.login())
        self.assertEqual(mock_print.call_count, 4)  # 3 failed attempts + success message

    @patch("builtins.input", side_effect=["wrong_user", "wrong_pass", "wrong_user", "wrong_pass", "wrong_user", "wrong_pass"])
    @patch("builtins.print")
    def test_login_failure(self, mock_print, mock_input):
        menu = Menu()
        self.assertFalse(menu.login())
        mock_print.assert_any_call("Demasiados intentos fallidos. Saliendo...")

    @patch("builtins.input", side_effect=["0"])
    @patch("builtins.print")
    def test_iniciar_exit(self, mock_print, mock_input):
        menu = Menu()
        menu.login = MagicMock(return_value=True)
        menu.iniciar()
        mock_print.assert_any_call("¡Hasta luego!")

    @patch("builtins.input", side_effect=["1", "0"])
    @patch("builtins.print")
    def test_menu_principal_listar(self, mock_print, mock_input):
        menu = Menu()
        menu.login = MagicMock(return_value=True)
        mock_gestor = MagicMock(spec=GestionCsv)
        mock_gestor.listar.return_value = [{"nie": "X1234567A", "nombre": "Juan"}]
        menu.gestores["1"] = ("alumnos", mock_gestor)
        menu.iniciar()
        mock_gestor.listar.assert_called_once()
        mock_print.assert_any_call({"nie": "X1234567A", "nombre": "Juan"})

    @patch("builtins.input", side_effect=["X1234567A", "Juan", ""])
    @patch("builtins.print")
    def test_añadir_registro(self, mock_print, mock_input):
        menu = Menu()
        mock_gestor = MagicMock(spec=GestionCsv)
        mock_gestor.campos = ["nie", "nombre"]
        mock_gestor.añadir.return_value = True
        menu._añadir_registro(mock_gestor)
        mock_gestor.añadir.assert_called_once_with({"nie": "X1234567A", "nombre": "Juan"})
        mock_print.assert_any_call("Añadido correctamente")

    @patch("builtins.input", side_effect=["nie", "X1234567A", "nombre", "Juan"])
    @patch("builtins.print")
    def test_modificar_registro(self, mock_print, mock_input):
        menu = Menu()
        mock_gestor = MagicMock(spec=GestionCsv)
        mock_gestor.campos = ["nie", "nombre"]
        mock_gestor.modificar.return_value = True
        menu._modificar_registro(mock_gestor)
        mock_gestor.modificar.assert_called_once_with("nie", "X1234567A", {"nombre": "Juan"})
        mock_print.assert_any_call("Modificado correctamente")

    @patch("builtins.input", side_effect=["nie", "X1234567A"])
    @patch("builtins.print")
    def test_eliminar_registro(self, mock_print, mock_input):
        menu = Menu()
        mock_gestor = MagicMock(spec=GestionCsv)
        mock_gestor.eliminar.return_value = True
        menu._eliminar_registro(mock_gestor)
        mock_gestor.eliminar.assert_called_once_with("nie", "X1234567A")
        mock_print.assert_any_call("Eliminado correctamente.")

if __name__ == "__main__":
    unittest.main()