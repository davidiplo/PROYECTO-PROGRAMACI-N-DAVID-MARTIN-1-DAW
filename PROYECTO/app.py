import csv
import re
import os

from lib.alumnos import Alumno
from lib.libros import Libro
from lib.materias import Materia
from lib.cursos import Curso
from lib.prestamos import Prestamo


def cargar_csv(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return []
    with open(nombre_archivo, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def guardar_csv(nombre_archivo, lista_diccionarios, campos):
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(lista_diccionarios)

def validar_existencia(lista, clave, valor):
    return any(item[clave] == valor for item in lista)

def validar_nie(nie):
    return bool(re.match(r'^[XYZ]\d{7}[A-Z]$', nie))

def validar_isbn(isbn):
    return bool(re.match(r'^\d{9}[\dX]$', isbn))


class GestionAlumnos:
    ARCHIVO = "alumnos.csv"
    CAMPOS = ["nie", "nombre", "apellidos", "tramo", "bilingue"]

    def listar(self):
        datos = cargar_csv(self.ARCHIVO)
        for d in datos:
            print(d)

    def añadir(self):
        valores = [input(f"{campo}: ") for campo in self.CAMPOS]
        alumno = Alumno(*valores)
        datos = cargar_csv(self.ARCHIVO)
        datos.append(alumno.to_dict())
        guardar_csv(self.ARCHIVO, datos, self.CAMPOS)
        print("Alumno añadido correctamente.")

    def modificar(self):
        datos = cargar_csv(self.ARCHIVO)
        id_buscar = input("NIE del alumno a modificar: ")
        for i, d in enumerate(datos):
            if d["nie"] == id_buscar:
                print("Introduce los nuevos datos:")
                nuevos_valores = [input(f"{campo} ({d[campo]}): ") or d[campo] for campo in self.CAMPOS]
                datos[i] = dict(zip(self.CAMPOS, nuevos_valores))
                guardar_csv(self.ARCHIVO, datos, self.CAMPOS)
                print("Alumno modificado.")
                return
        print("Alumno no encontrado.")

    def eliminar(self):
        datos = cargar_csv(self.ARCHIVO)
        id_borrar = input("NIE del alumno a eliminar: ")
        datos = [d for d in datos if d["nie"] != id_borrar]
        guardar_csv(self.ARCHIVO, datos, self.CAMPOS)
        print("Alumno eliminado si existía.")


class GestionLibros:
    ARCHIVO = "libros.csv"
    CAMPOS = ["isbn", "titulo", "autor", "editorial"]

    def listar(self):
        datos = cargar_csv(self.ARCHIVO)
        for d in datos:
            print(d)

    def añadir(self):
        valores = [input(f"{campo}: ") for campo in self.CAMPOS]
        libro = Libro(*valores)
        datos = cargar_csv(self.ARCHIVO)
        datos.append(libro.to_dict())
        guardar_csv(self.ARCHIVO, datos, self.CAMPOS)
        print("Libro añadido correctamente.")

    def modificar(self):
        datos = cargar_csv(self.ARCHIVO)
        id_buscar = input("ISBN del libro a modificar: ")
        for i, d in enumerate(datos):
            if d["isbn"] == id_buscar:
                print("Introduce los nuevos datos:")
                nuevos_valores = [input(f"{campo} ({d[campo]}): ") or d[campo] for campo in self.CAMPOS]
                datos[i] = dict(zip(self.CAMPOS, nuevos_valores))
                guardar_csv(self.ARCHIVO, datos, self.CAMPOS)
                print("Libro modificado.")
                return
        print("Libro no encontrado.")

    def eliminar(self):
        datos = cargar_csv(self.ARCHIVO)
        id_borrar = input("ISBN del libro a eliminar: ")
        datos = [d for d in datos if d["isbn"] != id_borrar]
        guardar_csv(self.ARCHIVO, datos, self.CAMPOS)
        print("Libro eliminado si existía.")


class GestionMaterias:
    ARCHIVO = "materias.csv"
    CAMPOS = ["id_materia", "nombre", "id_curso"]

    def listar(self):
        datos = cargar_csv(self.ARCHIVO)
        for d in datos:
            print(d)

    def añadir(self):
        valores = [input(f"{campo}: ") for campo in self.CAMPOS]
        materia = Materia(*valores)
        datos = cargar_csv(self.ARCHIVO)
        datos.append(materia.to_dict())
        guardar_csv(self.ARCHIVO, datos, self.CAMPOS)
        print("Materia añadida correctamente.")

    def modificar(self):
        datos = cargar_csv(self.ARCHIVO)
        id_buscar = input("ID de la materia a modificar: ")
        for i, d in enumerate(datos):
            if d["id_materia"] == id_buscar:
                print("Introduce los nuevos datos:")
                nuevos_valores = [input(f"{campo} ({d[campo]}): ") or d[campo] for campo in self.CAMPOS]
                datos[i] = dict(zip(self.CAMPOS, nuevos_valores))
                guardar_csv(self.ARCHIVO, datos, self.CAMPOS)
                print("Materia modificada.")
                return
        print("Materia no encontrada.")

    def eliminar(self):
        datos = cargar_csv(self.ARCHIVO)
        id_borrar = input("ID de la materia a eliminar: ")
        datos = [d for d in datos if d["id_materia"] != id_borrar]
        guardar_csv(self.ARCHIVO, datos, self.CAMPOS)
        print("Materia eliminada si existía.")


class GestionCursos:
    ARCHIVO = "cursos.csv"
    CAMPOS = ["id_curso", "nivel"]

    def listar(self):
        datos = cargar_csv(self.ARCHIVO)
        for d in datos:
            print(d)

    def añadir(self):
        valores = [input(f"{campo}: ") for campo in self.CAMPOS]
        curso = Curso(*valores)
        datos = cargar_csv(self.ARCHIVO)
        datos.append(curso.to_dict())
        guardar_csv(self.ARCHIVO, datos, self.CAMPOS)
        print("Curso añadido correctamente.")

    def modificar(self):
        datos = cargar_csv(self.ARCHIVO)
        id_buscar = input("ID del curso a modificar: ")
        for i, d in enumerate(datos):
            if d["id_curso"] == id_buscar:
                print("Introduce los nuevos datos:")
                nuevos_valores = [input(f"{campo} ({d[campo]}): ") or d[campo] for campo in self.CAMPOS]
                datos[i] = dict(zip(self.CAMPOS, nuevos_valores))
                guardar_csv(self.ARCHIVO, datos, self.CAMPOS)
                print("Curso modificado.")
                return
        print("Curso no encontrado.")

    def eliminar(self):
        datos = cargar_csv(self.ARCHIVO)
        id_borrar = input("ID del curso a eliminar: ")
        datos = [d for d in datos if d["id_curso"] != id_borrar]
        guardar_csv(self.ARCHIVO, datos, self.CAMPOS)
        print("Curso eliminado si existía.")


class GestionPrestamos:
    ARCHIVO = "prestamos.csv"
    CAMPOS = ["nie", "isbn", "estado"]

    def listar(self):
        datos = cargar_csv(self.ARCHIVO)
        for d in datos:
            print(d)

    def añadir(self):
        alumnos = cargar_csv("alumnos.csv")
        libros = cargar_csv("libros.csv")
        prestamos = cargar_csv(self.ARCHIVO)

        nie = input("Introduce el NIE del alumno: ")
        isbn = input("Introduce el ISBN del libro: ")

        if not validar_nie(nie):
            print("NIE inválido.")
            return
        if not validar_isbn(isbn):
            print("ISBN inválido.")
            return
        if not validar_existencia(alumnos, "nie", nie):
            print("Alumno no encontrado.")
            return
        if not validar_existencia(libros, "isbn", isbn):
            print("Libro no encontrado.")
            return

        estado = input("Introduce el estado del préstamo (pendiente/devuelto): ").strip() or "pendiente"
        prestamo = Prestamo(nie, isbn, estado)
        prestamos.append(prestamo.to_dict())
        guardar_csv(self.ARCHIVO, prestamos, self.CAMPOS)
        print("Préstamo añadido correctamente.")

    def modificar(self):
        alumnos = cargar_csv("alumnos.csv")
        libros = cargar_csv("libros.csv")
        prestamos = cargar_csv(self.ARCHIVO)

        nie = input("Introduce el NIE: ")
        isbn = input("Introduce el ISBN: ")

        if not validar_existencia(alumnos, "nie", nie):
            print("Alumno no encontrado.")
            return
        if not validar_existencia(libros, "isbn", isbn):
            print("Libro no encontrado.")
            return

        for prestamo in prestamos:
            if prestamo["nie"] == nie and prestamo["isbn"] == isbn:
                print(f"Estado actual: {prestamo['estado']}")
                nuevo_estado = input("Nuevo estado: ").strip()
                if nuevo_estado:
                    prestamo["estado"] = nuevo_estado
                    guardar_csv(self.ARCHIVO, prestamos, self.CAMPOS)
                    print("Estado actualizado.")
                else:
                    print("No se modificó el estado.")
                return
        print("Préstamo no encontrado.")

    def eliminar(self):
        prestamos = cargar_csv(self.ARCHIVO)
        nie = input("Introduce el NIE: ")
        isbn = input("Introduce el ISBN: ")
        nuevos = [p for p in prestamos if not (p["nie"] == nie and p["isbn"] == isbn)]
        guardar_csv(self.ARCHIVO, nuevos, self.CAMPOS)
        print("Préstamo eliminado si existía.")


# ------------------ AUTENTICACIÓN ------------------ #

def iniciar_sesion():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    if usuario == "administrador" and contraseña == "1234":
        print("Inicio de sesión exitoso.")
        return True
    else:
        print("Usuario o contraseña incorrectos.")
        return False


# ------------------ MENÚ PRINCIPAL ------------------ #

def menu():
    if not iniciar_sesion():
        return

    gestores = {
        "1": GestionPrestamos(),
        "2": GestionAlumnos(),
        "3": GestionLibros(),
        "4": GestionMaterias(),
        "5": GestionCursos()
    }

    nombres = {
        "1": "préstamos",
        "2": "alumnos",
        "3": "libros",
        "4": "materias",
        "5": "cursos"
    }

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
        elif opcion in gestores:
            gestor = gestores[opcion]
            while True:
                print(f"\nGestión de {nombres[opcion].capitalize()}")
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
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    from ui.menu import Menu
    Menu().mostrar_menu()

