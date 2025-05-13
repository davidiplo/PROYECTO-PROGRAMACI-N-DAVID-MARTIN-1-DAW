import sys
sys.path.append('path_to_config_directory')

configuraciones = {
    "alumnos": {
        "archivo": "alumnos.csv",
        "campos": ["nie", "nombre", "apellidos", "tramo", "bilingue"]
    },
    "libros": {
        "archivo": "libros.csv",
        "campos": ["isbn", "titulo", "autor", "numero_ejemplares", "Id_materia", "Id_curso"]
    },
    "materias": {
        "archivo": "materias.csv",
        "campos": ["id_materia", "nombre", "id_curso"]
    },
    "cursos": {
        "archivo": "cursos.csv",
        "campos": ["id_curso", "nivel"]
    },
    "prestamos": {
    "archivo": "prestamos.csv",
    "campos": ["nie", "curso", "isbn", "fecha_entrega", "fecha_devolucion", "estado"]
    }

}

credenciales = {
    "usuario": "administrador",
    "contraseña": "1234"
}
