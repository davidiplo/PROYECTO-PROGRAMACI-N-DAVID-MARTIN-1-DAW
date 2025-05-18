import csv
from config.config import configuraciones

def exportar_alumnos_formato_delphos():
    archivo_origen = configuraciones["alumnos"]["archivo"]
    archivo_destino = "alumnos_delphos.csv"

    campos = [
        "Alumno", "NumeroEscolar", "NumeroSolicitud", "FechaSolicitud",
        "CampoNoNecesario", "CampoNoNecesario", "CampoNoNecesario", "CampoNoNecesario",
        "CampoNoNecesario", "CampoNoNecesario", "CampoNoNecesario", "CampoNoNecesario",
        "ResultadoLibros", "ResultadoComedor", "Matriculado", "TipoBecaLibros", "TipoBecaComedor"
    ]

    with open(archivo_origen, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        alumnos = list(reader)

    with open(archivo_destino, mode="w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos, quoting=csv.QUOTE_ALL)
        writer.writeheader()

        for a in alumnos:
            fila = {
                "Alumno": f"{a['apellidos']}, {a['nombre']}",
                "NumeroEscolar": a["nie"],
                "NumeroSolicitud": "2024001",
                "FechaSolicitud": "26/06/2024",
                "ResultadoLibros": "Sí",
                "ResultadoComedor": "No",
                "Matriculado": "Sí",
                "TipoBecaLibros": f"Renta {a.get('tramo', '0')}",
                "TipoBecaComedor": f"Tramo {a.get('tramo', '0')}",
            }
            # Rellenar los 8 campos no necesarios
            for i in range(8):
                fila[f"CampoNoNecesario"] = ""
            writer.writerow(fila)

    print("Exportación completada: alumnos_delphos.csv")