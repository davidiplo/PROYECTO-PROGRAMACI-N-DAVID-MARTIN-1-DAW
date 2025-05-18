import csv
import os
import re
from PROYECTO.config.config import configuraciones

class GestionCsv:
    def __init__(self, archivo, campos):
        self.archivo = archivo
        self.campos = campos
        self._asegurar_archivo()

    def _asegurar_archivo(self):
        if not os.path.exists(self.archivo) or os.path.getsize(self.archivo) == 0:
            with open(self.archivo, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.campos)
                writer.writeheader()

    def listar(self):
        with open(self.archivo, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]

    def añadir(self, datos):
        if not self._validar_datos(datos, es_modificacion=False):
            return False
        with open(self.archivo, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.campos)
            writer.writerow(datos)
        return True

    def modificar(self, clave, valor, nuevos_datos):
        filas = []
        modificado = False
        if clave in nuevos_datos and nuevos_datos[clave] != valor:
            if not self._validar_datos(nuevos_datos, es_modificacion=True, clave=clave, valor=valor):
                return False
        with open(self.archivo, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row[clave] == valor:
                    row.update({k: v for k, v in nuevos_datos.items() if v != ""})
                    modificado = True
                filas.append(row)
        with open(self.archivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.campos)
            writer.writeheader()
            writer.writerows(filas)
        return modificado

    def eliminar(self, clave, valor):
        filas = []
        eliminado = False
        with open(self.archivo, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row[clave] != valor:
                    filas.append(row)
                else:
                    eliminado = True
        with open(self.archivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.campos)
            writer.writeheader()
            writer.writerows(filas)
        return eliminado

    def existe_valor_repetido(self, campo, valor):
        return any(row.get(campo) == valor for row in self.listar())

    def _validar_datos(self, datos, es_modificacion=False, clave=None, valor=None):
        # Validaciones existentes (NIE, ISBN, tramo, etc.)
        if 'nie' in self.campos and 'nie' in datos and datos['nie']:
            if not self.validar_nie(datos['nie']):
                raise ValueError("NIE inválido. Formato: X/Y/Z + 7 dígitos + letra de control")
            if not es_modificacion and self.existe_valor_repetido('nie', datos['nie']):
                raise ValueError("Ya existe un alumno con este NIE")

        if 'isbn' in self.campos and 'isbn' in datos and datos['isbn']:
            if not self.validar_isbn10(datos['isbn']):
                raise ValueError("ISBN-10 inválido. Formato: 10 dígitos o X al final")
            if not es_modificacion and self.existe_valor_repetido('isbn', datos['isbn']):
                raise ValueError("Ya existe un libro con este ISBN")

        # Nueva validación: Ejemplares disponibles (solo para préstamos)
        if self.archivo == configuraciones["prestamos"]["archivo"] and not es_modificacion:
            # 1. Verificar ejemplares del libro
            libros_gestion = GestionCsv(
                configuraciones["libros"]["archivo"],
                configuraciones["libros"]["campos"]
            )
            libro = next((l for l in libros_gestion.listar() if l["isbn"] == datos["isbn"]), None)

            if not libro:
                raise ValueError("El libro no está registrado")
            if int(libro["num_ejemplares"]) <= 0:
                raise ValueError("No hay ejemplares disponibles para prestar")

            # 2. Verificar préstamos pendientes del alumno
            prestamos_alumno = [
                p for p in self.listar()
                if p["nie"] == datos["nie"] and p["estado"].lower() == "pendiente"
            ]
            if prestamos_alumno:
                raise ValueError("El alumno tiene préstamos pendientes de devolución")

        # Resto de validaciones existentes
        if 'tramo' in self.campos and 'tramo' in datos and datos['tramo']:
            if datos['tramo'] not in ['0', 'I', 'II']:
                raise ValueError("Tramo inválido. Valores permitidos: 0, I, II")

        if 'bilingue' in self.campos and 'bilingue' in datos and datos['bilingue']:
            if datos['bilingue'] not in ['S', 'N']:
                raise ValueError("Bilingüe inválido. Valores permitidos: S o N")

        return True

    @staticmethod
    def validar_nie(nie):
        nie = nie.upper().strip()
        if not re.match(r'^[XYZ]\d{7}[A-Z0-9]$', nie):
            return False
        letras = {'X': '0', 'Y': '1', 'Z': '2'}
        nie_num = letras[nie[0]] + nie[1:8]
        letras_control = 'TRWAGMYFPDXBNJZSQVHLCKE'
        return nie[-1] == letras_control[int(nie_num) % 23]

    @staticmethod
    def validar_isbn10(isbn):
        isbn = isbn.replace('-', '').replace(' ', '').upper()
        if len(isbn) != 10 or not isbn[:9].isdigit():
            return False
        if isbn[-1] not in '0123456789X':
            return False
        suma = sum((i + 1) * int(d) for i, d in enumerate(isbn[:9]))
        suma += 10 * (10 if isbn[-1] == 'X' else int(isbn[-1]))
        return suma % 11 == 0


