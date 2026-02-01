class Libro:
    def __init__(self, titulo, autor, isbn, copias=1):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.copias_disponibles = copias
        print(f"[CONSTRUCTOR] Libro creado: {self.titulo} - {self.autor}")

    def __del__(self):
        print(f"[DESTRUCTOR] Libro eliminado del sistema: {self.titulo}")
