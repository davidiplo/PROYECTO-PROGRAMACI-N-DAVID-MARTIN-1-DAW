import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="biblioteca"
    )

# === archivo: base_datos/alumnos.py ===
from base_datos.conexion import obtener_conexion

def listar_alumnos():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM alumnos")
    alumnos = cursor.fetchall()
    conexion.close()
    return alumnos

def insertar_alumno(nie, nombre, apellidos, tramo, bilingue):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "INSERT INTO alumnos (nie, nombre, apellidos, tramo, bilingue) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (nie, nombre, apellidos, tramo, bilingue))
    conexion.commit()
    conexion.close()

# === archivo: base_datos/libros.py ===
from base_datos.conexion import obtener_conexion

def listar_libros():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()
    conexion.close()
    return libros

def insertar_libro(isbn, titulo, autor, ejemplares, id_materia, id_curso):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "INSERT INTO libros (isbn, titulo, autor, numero_ejemplares, id_materia, id_curso) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (isbn, titulo, autor, ejemplares, id_materia, id_curso))
    conexion.commit()
    conexion.close()

# === archivo: base_datos/prestamos.py ===
from base_datos.conexion import obtener_conexion

def listar_prestamos():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM prestamos")
    prestamos = cursor.fetchall()
    conexion.close()
    return prestamos

def insertar_prestamo(nie, curso, isbn, fecha_entrega, fecha_devolucion, estado):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "INSERT INTO prestamos (nie, curso, isbn, fecha_entrega, fecha_devolucion, estado) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (nie, curso, isbn, fecha_entrega, fecha_devolucion, estado))
    conexion.commit()
    conexion.close()

# === archivo: main.py ===
from base_datos.alumnos import listar_alumnos, insertar_alumno
from base_datos.libros import listar_libros, insertar_libro
from base_datos.prestamos import listar_prestamos, insertar_prestamo

def menu_alumnos():
    while True:
        print("\n--- GESTIÓN DE ALUMNOS ---")
        print("1. Ver alumnos")
        print("2. Añadir alumno")
        print("0. Volver")
        opcion = input("Opcion: ")
        if opcion == "1":
            for a in listar_alumnos():
                print(f"{a['nie']} - {a['nombre']} {a['apellidos']} - {a['tramo']} - Bilingüe: {a['bilingue']}")
        elif opcion == "2":
            nie = input("NIE: ")
            nombre = input("Nombre: ")
            apellidos = input("Apellidos: ")
            tramo = input("Tramo: ")
            bilingue = input("Bilingüe (s/n): ").lower() == "s"
            insertar_alumno(nie, nombre, apellidos, tramo, bilingue)
        elif opcion == "0":
            break


def menu_libros():
    while True:
        print("\n--- GESTIÓN DE LIBROS ---")
        print("1. Ver libros")
        print("2. Añadir libro")
        print("0. Volver")
        opcion = input("Opcion: ")
        if opcion == "1":
            for l in listar_libros():
                print(f"{l['isbn']} - {l['titulo']} ({l['autor']}) - Ejemplares: {l['numero_ejemplares']}")
        elif opcion == "2":
            isbn = input("ISBN: ")
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            ejemplares = int(input("N. Ejemplares: "))
            id_materia = input("ID Materia: ")
            id_curso = input("ID Curso: ")
            insertar_libro(isbn, titulo, autor, ejemplares, id_materia, id_curso)
        elif opcion == "0":
            break


def menu_prestamos():
    while True:
        print("\n--- GESTIÓN DE PRÉSTAMOS ---")
        print("1. Ver préstamos")
        print("2. Añadir préstamo")
        print("0. Volver")
        opcion = input("Opcion: ")
        if opcion == "1":
            for p in listar_prestamos():
                print(f"{p['nie']} - {p['isbn']} ({p['estado']}) - Entregado: {p['fecha_entrega']}, Devuelto: {p['fecha_devolucion']}")
        elif opcion == "2":
            nie = input("NIE del alumno: ")
            curso = input("Curso: ")
            isbn = input("ISBN del libro: ")
            fecha_entrega = input("Fecha entrega (AAAA-MM-DD): ")
            fecha_devolucion = input("Fecha devolución (AAAA-MM-DD): ")
            estado = input("Estado (prestado/devuelto): ")
            insertar_prestamo(nie, curso, isbn, fecha_entrega, fecha_devolucion, estado)
        elif opcion == "0":
            break


def main():
    while True:
        print("\n====== MENÚ PRINCIPAL ======")
        print("1. Gestionar alumnos")
        print("2. Gestionar libros")
        print("3. Gestionar préstamos")
        print("0. Salir")
        opcion = input("Opcion: ")
        if opcion == "1":
            menu_alumnos()
        elif opcion == "2":
            menu_libros()
        elif opcion == "3":
            menu_prestamos()
        elif opcion == "0":
            print("Hasta luego!")
            break

if __name__ == "__main__":
    main()
