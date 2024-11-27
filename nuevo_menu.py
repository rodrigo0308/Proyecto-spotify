# Función para mostrar menú del administrador
def menu_administrador():
    while True:
        print("\n=== Menú Administrador ===")
        print("1. Crear usuario")
        print("2. Ver usuarios")
        print("3. Eliminar lista de reproducción")
        print("4. Eliminar usuario")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_cuenta()
        elif opcion == "2":
            visualizar_usuarios()
        elif opcion == "3":
            usuario_id = input("Introduce tu ID de usuario para eliminar una lista: ")
            eliminar_lista_reproduccion(usuario_id)
        elif opcion == "4":
            eliminar_usuario()  # Aquí añadimos la opción para eliminar un usuario
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")
