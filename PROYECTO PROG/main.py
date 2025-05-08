from lib.alumnos import Alumno
from lib.libros import Libro
from lib.materias import Materia
from lib.prestamos import Prestamo

def menu_alumnos():
    while True:
        print("\n--- Gestión de Alumnos ---")
        print("1. Agregar alumno")
        print("2. Listar alumnos")
        print("3. Eliminar alumno")
        print("0. Volver al menú principal")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
        elif opcion == "2":
            Alumno.listar_alumnos()
        elif opcion == "3":
            id_alumno = input("ID del alumno a eliminar: ")
            Alumno.eliminar_alumno(id_alumno)
        elif opcion == "0":
            break
        else:
            print("❌ Opción inválida.")

def menu_libros():
    while True:
        print("\n--- Gestión de Libros ---")
        print("1. Agregar libro")
        print("2. Listar libros")
        print("3. Eliminar libro")
        print("0. Volver al menú principal")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            Libro.agregar_libro(titulo, autor)
        elif opcion == "2":
            Libro.listar_libros()
        elif opcion == "3":
            id_libro = input("ID del libro a eliminar: ")
            Libro.eliminar_libro(id_libro)
        elif opcion == "0":
            break
        else:
            print("❌ Opción inválida.")

def menu_materias():
    while True:
        print("\n--- Gestión de Materias ---")
        print("1. Agregar materia")
        print("2. Listar materias")
        print("3. Eliminar materia")
        print("0. Volver al menú principal")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la materia: ")
            Materia.agregar_materia(nombre)
        elif opcion == "2":
            Materia.listar_materias()
        elif opcion == "3":
            id_materia = input("ID de la materia a eliminar: ")
            Materia.eliminar_materia(id_materia)
        elif opcion == "0":
            break
        else:
            print("❌ Opción inválida.")

def menu_prestamos():
    while True:
        print("\n--- Gestión de Préstamos ---")
        print("1. Registrar préstamo")
        print("2. Listar préstamos")
        print("3. Eliminar préstamo")
        print("0. Volver al menú principal")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            id_alumno = input("ID del alumno: ")
            id_libro = input("ID del libro: ")
            Prestamo.registrar_prestamo(id_alumno, id_libro)
        elif opcion == "2":
            Prestamo.listar_prestamos()
        elif opcion == "3":
            id_prestamo = input("ID del préstamo a eliminar: ")
            Prestamo.eliminar_prestamo(id_prestamo)
        elif opcion == "0":
            break
        else:
            print("❌ Opción inválida.")

def main():
    while True:
        print("\n==== MENÚ PRINCIPAL ====")
        print("1. Gestionar alumnos")
        print("2. Gestionar libros")
        print("3. Gestionar materias")
        print("4. Gestionar préstamos")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            menu_alumnos()
        elif opcion == "2":
            menu_libros()
        elif opcion == "3":
            menu_materias()
        elif opcion == "4":
            menu_prestamos()
        elif opcion == "0":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")

main()
