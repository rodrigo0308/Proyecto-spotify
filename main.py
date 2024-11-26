from usuarios import crear_cuenta, iniciar_sesion
from menu import menu_administrador, menu_usuario

def menu_principal():
    while True:
        print("\n===== SPOTIFY =====")
        print("1. Crear cuenta")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_cuenta()
        elif opcion == "2":
            iniciar_sesion(menu_administrador, menu_usuario)
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()
