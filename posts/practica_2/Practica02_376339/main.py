from biblioteca import *

def main():
    biblioteca = Library()
    biblioteca.cargar_datos()

    while True:
        print("\n===== SISTEMA DE BIBLIOTECA =====")
        print("1. Agregar libro")
        print("2. Agregar revista")
        print("3. Mostrar ítems")
        print("4. Agregar miembro")
        print("5. Mostrar miembros")
        print("6. Prestar ítem")
        print("7. Devolver ítem")
        print("8. Buscar ítem")
        print("9. Buscar miembro")
        print("10. Guardar y salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_ = int(input("ID: "))
            title = input("Título: ")
            author = input("Autor: ")
            year = int(input("Año: "))
            genre = Genre[input("Género (FICTION, NON_FICTION, SCIENCE, etc.): ").upper()]
            qty = int(input("Cantidad: "))
            biblioteca.agregar_item(Book(id_, title, author, year, genre, qty))

        elif opcion == "2":
            id_ = int(input("ID: "))
            title = input("Título: ")
            edition = input("Edición: ")
            year = int(input("Año: "))
            genre = Genre[input("Género (FICTION, NON_FICTION, SCIENCE, etc.): ").upper()]
            qty = int(input("Cantidad: "))
            biblioteca.agregar_item(Magazine(id_, title, edition, year, genre, qty))

        elif opcion == "3":
            biblioteca.mostrar_items()
            input()

        elif opcion == "4":
            id_ = int(input("ID miembro: "))
            name = input("Nombre: ")
            biblioteca.agregar_miembro(Member(id_, name))

        elif opcion == "5":
            biblioteca.mostrar_miembros()
            input()

        elif opcion == "6":
            m = int(input("ID miembro: "))
            i = int(input("ID ítem: "))
            biblioteca.prestar_item(m, i)

        elif opcion == "7":
            m = int(input("ID miembro: "))
            i = int(input("ID ítem: "))
            biblioteca.devolver_item(m, i)

        elif opcion == "8":
            t = input("Título a buscar: ")
            biblioteca.buscar_item(t)

        elif opcion == "9":
            n = input("Nombre a buscar: ")
            biblioteca.buscar_miembro(n)

        elif opcion == "10":
            biblioteca.guardar_datos()
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
