# ui/menu.py

from app import (
    GestionPrestamos,
    GestionAlumnos,
    GestionLibros,
    GestionMaterias,
    GestionCursos
)

class Menu:
    def __init__(self):
        self.gestores = {
            "1": GestionPrestamos(),
            "2": GestionAlumnos(),
            "3": GestionLibros(),
            "4": GestionMaterias(),
            "5": GestionCursos()
        }

        self.nombres = {
            "1": "préstamos",
            "2": "alumnos",
            "3": "libros",
            "4": "materias",
            "5": "cursos"
        }

    def iniciar_sesion(self):
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        if usuario == "administrador" and contraseña == "1234":
            print("Inicio de sesión exitoso.")
            return True
        else:
            print("Usuario o contraseña incorrectos.")
            return False

    def mostrar_menu(self):
        if not self.iniciar_sesion():
            return

        while True:
            print("\nSistema de Gestión")
            print("1. Gestionar préstamos")
            print("2. Gestionar alumnos")
            print("3. Gestionar libros")
            print("4. Gestionar materias")
            print("5. Gestionar cursos")
            print("0. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "0":
                break
            elif opcion in self.gestores:
                self.menu_gestion(opcion)
            else:
                print("Opción no válida.")

    def menu_gestion(self, opcion):
        gestor = self.gestores[opcion]
        nombre = self.nombres[opcion].capitalize()

        while True:
            print(f"\nGestión de {nombre}")
            print("1. Listar")
            print("2. Añadir")
            print("3. Modificar")
            print("4. Eliminar")
            print("0. Volver")
            subop = input("Elige una opción: ")

            if subop == "1":
                gestor.listar()
            elif subop == "2":
                gestor.añadir()
            elif subop == "3":
                gestor.modificar()
            elif subop == "4":
                gestor.eliminar()
            elif subop == "0":
                break
            else:
                print("Opción no válida.")
