import csv
import os

# ------------------ CLASES ------------------ #

class Alumno:
    def __init__(self, nie, nombre, apellidos, tramo, bilingue):
        self.nie = nie
        self.nombre = nombre
        self.apellidos = apellidos
        self.tramo = tramo
        self.bilingue = bilingue

    def to_dict(self):
        return {
            "nie": self.nie,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "tramo": self.tramo,
            "bilingue": self.bilingue
        }

class Libro:
    def __init__(self, isbn, titulo, autor, editorial):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "editorial": self.editorial
        }

class Prestamo:
    def __init__(self, nie, isbn):
        self.nie = nie
        self.isbn = isbn

    def to_dict(self):
        return {
            "nie": self.nie,
            "isbn": self.isbn
        }

class Materia:
    def __init__(self, id_materia, nombre, id_curso):
        self.id_materia = id_materia
        self.nombre = nombre
        self.id_curso = id_curso

    def to_dict(self):
        return {
            "id_materia": self.id_materia,
            "nombre": self.nombre,
            "id_curso": self.id_curso
        }

class Curso:
    def __init__(self, id_curso, nivel):
        self.id_curso = id_curso
        self.nivel = nivel

    def to_dict(self):
        return {
            "id_curso": self.id_curso,
            "nivel": self.nivel
        }

# ------------------ FUNCIONES GENERALES ------------------ #

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

# ------------------ FUNCIONES DE GESTIÓN ------------------ #

def validar_existencia(lista, clave, valor):
    return any(item[clave] == valor for item in lista)

def agregar_prestamo():
    alumnos = cargar_csv('alumnos.csv')
    libros = cargar_csv('libros.csv')
    prestamos = cargar_csv('prestamos.csv')

    nie = input("Introduce el NIE del alumno: ")
    isbn = input("Introduce el ISBN del libro: ")

    if not validar_existencia(alumnos, 'nie', nie):
        print("Error: El NIE no existe.")
        return
    if not validar_existencia(libros, 'isbn', isbn):
        print("Error: El ISBN no existe.")
        return

    prestamo = Prestamo(nie, isbn)
    prestamos.append(prestamo.to_dict())
    guardar_csv('prestamos.csv', prestamos, ['nie', 'isbn'])
    print("Préstamo añadido correctamente.")

def gestionar_entidad(nombre, clase, campos):
    archivo = f"{nombre}.csv"
    datos = cargar_csv(archivo)

    while True:
        print(f"\nGestión de {nombre.capitalize()}:")
        print("1. Listar")
        print("2. Añadir")
        print("3. Modificar")
        print("4. Eliminar")
        print("0. Volver")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            for d in datos:
                print(d)
        elif opcion == '2':
            valores = [input(f"{campo}: ") for campo in campos]
            obj = clase(*valores)
            datos.append(obj.to_dict())
            guardar_csv(archivo, datos, campos)
            print(f"{nombre.capitalize()} añadido correctamente.")
        elif opcion == '3':
            id_buscar = input(f"ID de {nombre} a modificar: ")
            for i, d in enumerate(datos):
                if d[campos[0]] == id_buscar:
                    print("Introduce los nuevos datos:")
                    nuevos_valores = [input(f"{campo} ({d[campo]}): ") or d[campo] for campo in campos]
                    datos[i] = dict(zip(campos, nuevos_valores))
                    guardar_csv(archivo, datos, campos)
                    print(f"{nombre.capitalize()} modificado.")
                    break
            else:
                print(f"{nombre.capitalize()} no encontrado.")
        elif opcion == '4':
            id_borrar = input(f"ID de {nombre} a eliminar: ")
            datos = [d for d in datos if d[campos[0]] != id_borrar]
            guardar_csv(archivo, datos, campos)
            print(f"{nombre.capitalize()} eliminado si existía.")
        elif opcion == '0':
            break
        else:
            print("Opción no válida.")

# ------------------ MENÚ PRINCIPAL ------------------ #

def menu():
    while True:
        print("\nSistema de Gestión de Préstamos")
        print("1. Añadir préstamo")
        print("2. Gestionar alumnos")
        print("3. Gestionar libros")
        print("4. Gestionar materias")
        print("5. Gestionar cursos")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_prestamo()
        elif opcion == '2':
            gestionar_entidad("alumnos", Alumno, ["nie", "nombre", "apellidos", "tramo", "bilingue"])
        elif opcion == '3':
            gestionar_entidad("libros", Libro, ["isbn", "titulo", "autor", "editorial"])
        elif opcion == '4':
            gestionar_entidad("materias", Materia, ["id_materia", "nombre", "id_curso"])
        elif opcion == '5':
            gestionar_entidad("cursos", Curso, ["id_curso", "nivel"])
        elif opcion == '0':
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    menu()
