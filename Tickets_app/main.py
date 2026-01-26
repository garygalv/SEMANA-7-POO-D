from servicios.gestor_biblioteca import GestorBiblioteca

def main():
    print("=== INICIO DEL PROGRAMA ===\n")
    
    gestor = GestorBiblioteca()
    
    # Crear objetos → se llaman los __init__
    libro1 = gestor.agregar_libro("Cien años de soledad", "García Márquez", "978-3-16-148410-0")
    usuario1 = gestor.registrar_usuario("Juan Pérez", 1001)
    
    # Aquí se pueden hacer más operaciones...
    
    print("\n=== Vamos a forzar la destrucción de algunos objetos ===\n")
    del libro1                  # → debería aparecer el __del__ del libro
    
    print("\nFin del main. Los objetos restantes se destruirán al terminar.\n")

if __name__ == "__main__":
    main()