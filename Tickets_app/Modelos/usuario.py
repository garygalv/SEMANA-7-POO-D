class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []
        print(f"[CONSTRUCTOR] Usuario registrado: {self.nombre} (ID: {self.id_usuario})")

    def __del__(self):
        print(f"[DESTRUCTOR] Usuario {self.nombre} eliminado del registro")
