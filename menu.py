from funciones import crear_lista_reproduccion, agregar_cancion_a_lista, agregar_cancion_a_biblioteca, buscar_cancion_por_nombre, ver_listas_usuario, ver_canciones_en_lista, ver_biblioteca
from funciones_admin import añadir_artista, añadir_cancion, añadir_album, añadir_genero
from funciones_editar_admin import editar_artista, editar_cancion, editar_album, editar_genero, ver_artistas, ver_canciones, ver_albumes, ver_generos
from funciones_eliminar_admin import eliminar_artista, eliminar_cancion, eliminar_album, eliminar_genero
from funciones_editar import editar_lista_reproduccion, editar_lista_reproduccion, editar_perfil
from funciones_eliminar import eliminar_lista_reproduccion, eliminar_cancion_de_biblioteca, eliminar_cancion_de_lista

# Menu del administrador
def menu_administrador():
    while True:
        print("\n===== Menú de Administrador =====")
        print("1. Añadir artista")
        print("2. Añadir canción")
        print("3. Añadir álbum")
        print("4. Añadir género")
        print("5. Ver artistas")  # Nueva opción para ver artistas
        print("6. Ver canciones")  # Nueva opción para ver canciones
        print("7. Ver álbumes")  # Nueva opción para ver álbumes
        print("8. Ver géneros")  # Nueva opción para ver géneros
        print("9. Editar artista")
        print("10. Editar canción")
        print("11. Editar álbum")
        print("12. Editar género")
        print("13. Eliminar artista")
        print("14. Eliminar canción")
        print("15. Eliminar álbum")
        print("16. Eliminar género")
        print("17. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            añadir_artista()
        elif opcion == "2":
            añadir_cancion()
        elif opcion == "3":
            añadir_album()
        elif opcion == "4":
            añadir_genero()
        elif opcion == "5":
            ver_artistas()  # Llamada a la función de ver artistas
        elif opcion == "6":
            ver_canciones()  # Llamada a la función de ver canciones
        elif opcion == "7":
            ver_albumes()  # Llamada a la función de ver álbumes
        elif opcion == "8":
            ver_generos()  # Llamada a la función de ver géneros
        elif opcion == "9":
            editar_artista()  # Llamada a la función de editar artista
        elif opcion == "10":
            editar_cancion()  # Llamada a la función de editar canción
        elif opcion == "11":
            editar_album()  # Llamada a la función de editar álbum
        elif opcion == "12":
            editar_genero()  # Llamada a la función de editar género
        elif opcion == "13":
            eliminar_artista()  # Llamada a la función de eliminar artista
        elif opcion == "14":
            eliminar_cancion()  # Llamada a la función de eliminar canción
        elif opcion == "15":
            eliminar_album()  # Llamada a la función de eliminar álbum
        elif opcion == "16":
            eliminar_genero()  # Llamada a la función de eliminar género
        elif opcion == "17":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Menú del usuario
def menu_usuario(usuario_id, nombre):
    while True:
        print(f"\n===== Menú de Usuario =====")
        print(f"Bienvenido, {nombre}!")
        print("1. Crear lista de reproducción")
        print("2. Añadir canción a lista de reproducción")
        print("3. Añadir canción a biblioteca")
        print("4. Buscar canciones")
        print("5. Ver todas las listas de reproducción")  # Opción para ver todas las listas de reproducción
        print("6. Ver canciones en una lista de reproducción")  # Opción para ver canciones en una lista específica
        print("7. Ver biblioteca (canciones y listas)")  # Opción para ver la biblioteca del usuario
        print("8. Editar perfil")
        print("9. Editar lista de reproducción")
        print("10. Eliminar lista de reproducción")  # Opción para eliminar lista
        print("11. Eliminar canción de lista de reproducción")  # Opción para eliminar canción de una lista
        print("12. Eliminar canción de biblioteca")  # Opción para eliminar canción de la biblioteca
        print("13. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_lista_reproduccion(usuario_id)
        elif opcion == "2":
            agregar_cancion_a_lista(usuario_id)
        elif opcion == "3":
            agregar_cancion_a_biblioteca(usuario_id)
        elif opcion == "4":
            buscar_cancion_por_nombre()
        elif opcion == "5":
            ver_listas_usuario(usuario_id)  # Llamada a la función para ver todas las listas de reproducción
        elif opcion == "6":
            ver_canciones_en_lista(usuario_id)  # Llamada a la función para ver canciones en una lista específica
        elif opcion == "7":
            ver_biblioteca(usuario_id)  # Llamada a la función de ver biblioteca
        elif opcion == "8":
            editar_perfil(usuario_id)
        elif opcion == "9":
            editar_lista_reproduccion(usuario_id)
        elif opcion == "10":
            eliminar_lista_reproduccion(usuario_id)  # Llamada a la función de eliminar lista
        elif opcion == "11":
            eliminar_cancion_de_lista(usuario_id)  # Llamada a la función de eliminar canción de lista
        elif opcion == "12":
            eliminar_cancion_de_biblioteca(usuario_id)  # Llamada a la función de eliminar canción de biblioteca
        elif opcion == "13":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
