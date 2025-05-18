from PROYECTO.app import GestionCsv
from PROYECTO.exportacion import exportar_alumnos_formato_delphos
from PROYECTO.config.config import configuraciones, credenciales

class Menu:
    def __init__(self):
        self.gestores = {
            "1": ("alumnos", GestionCsv(**configuraciones["alumnos"])),
            "2": ("libros", GestionCsv(**configuraciones["libros"])),
            "3": ("materias", GestionCsv(**configuraciones["materias"])),
            "4": ("cursos", GestionCsv(**configuraciones["cursos"])),
            "5": ("prestamos", GestionCsv(**configuraciones["prestamos"])),
        }

    def login(self):
        print("=== LOGIN ===")
        for _ in range(3):
            usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")
            if usuario == credenciales["usuario"] and contraseña == credenciales["contraseña"]:
                print("Acceso concedido.\n")
                return True
            else:
                print("Usuario o contraseña incorrectos.\n")
        print("Demasiados intentos fallidos. Saliendo...")
        return False

    def iniciar(self):
        if not self.login():
            return
        while True:
            self.mostrar_menu_principal()
            opcion = input("Elige una opción: ")
            if opcion in self.gestores:
                nombre, gestor = self.gestores[opcion]
                self.menu_gestion(nombre, gestor)
            elif opcion == "0":
                print("¡Hasta luego!")
                break
            elif opcion == "6":
                exportar_alumnos_formato_delphos()
            else:
                print("Opción no válida.")

    def mostrar_menu_principal(self):
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Gestionar alumnos")
        print("2. Gestionar libros")
        print("3. Gestionar materias")
        print("4. Gestionar cursos")
        print("5. Gestionar préstamos")
        print("6. Exportar alumnos a formato Delphos")
        print("0. Salir")

    def menu_gestion(self, nombre, gestor):
        while True:
            print(f"\n--- Gestión de {nombre} ---")
            print("1. Listar")
            print("2. Añadir")
            print("3. Modificar")
            print("4. Eliminar")
            print("0. Volver")
            opcion = input("Elige una opción: ")
            if opcion == "1":
                registros = gestor.listar()
                if registros:
                    for fila in registros:
                        print(fila)
                else:
                    print("No hay registros.")
            elif opcion == "2":
                self._añadir_registro(gestor)
            elif opcion == "3":
                self._modificar_registro(gestor)
            elif opcion == "4":
                self._eliminar_registro(gestor)
            elif opcion == "0":
                break
            else:
                print("Opción no válida.")

    def _añadir_registro(self, gestor):
        try:
            datos = {}
            for campo in gestor.campos:
                datos[campo] = input(f"{campo}: ").strip()
            if gestor.añadir(datos):
                print("Añadido correctamente")
            else:
                print("Error al añadir")
        except ValueError as e:
            print(f"Error de validación: {str(e)}")

    def _modificar_registro(self, gestor):
        try:
            clave = input("Campo clave para buscar: ").strip()
            valor = input(f"Valor de {clave}: ").strip()
            nuevos_datos = {}
            for campo in gestor.campos:
                nuevo = input(f"Nuevo {campo} (vacío=no cambiar): ").strip()
                if nuevo:
                    nuevos_datos[campo] = nuevo
            if gestor.modificar(clave, valor, nuevos_datos):
                print("Modificado correctamente")
            else:
                print("No se encontró el registro")
        except ValueError as e:
            print(f"Error de validación: {str(e)}")

    def _eliminar_registro(self, gestor):
        clave = input("Campo clave para buscar (ej. 'nie' o 'isbn'): ").strip()
        valor = input(f"Valor de {clave}: ").strip()
        if gestor.eliminar(clave, valor):
            print("Eliminado correctamente.")
        else:
            print("No se encontró el registro.")


