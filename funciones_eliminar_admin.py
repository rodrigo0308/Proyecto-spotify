from db import conectar_db

# FUNCIONES PARA ELIMINAR 
# Funcion para eliminar artista
def eliminar_artista():
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Mostrar lista de artistas
    cursor.execute("SELECT id, nombre FROM artistas")
    artistas = cursor.fetchall()

    if artistas:
        print("Artistas disponibles:")
        for artista in artistas:
            print(f"ID: {artista[0]}, Nombre: {artista[1]}")

        # Pedir al usuario que seleccione el artista a eliminar
        artista_id = input("Introduce el ID del artista que deseas eliminar: ")

        # Confirmar eliminación
        confirmacion = input(f"¿Estás seguro de que deseas eliminar al artista con ID {artista_id}? (s/n): ").lower()

        if confirmacion == 's':
            # Eliminar el artista
            cursor.execute("DELETE FROM artistas WHERE id = %s", (artista_id,))
            conexion.commit()

            print("¡Artista eliminado exitosamente!")
        else:
            print("Eliminación cancelada.")
    else:
        print("No hay artistas disponibles para eliminar.")

    cursor.close()
    conexion.close()

# Funcion para eliminar una cancion
def eliminar_cancion():
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Mostrar lista de canciones
    cursor.execute("SELECT id, titulo FROM canciones")
    canciones = cursor.fetchall()

    if canciones:
        print("Canciones disponibles:")
        for cancion in canciones:
            print(f"ID: {cancion[0]}, Título: {cancion[1]}")

        # Pedir al usuario que seleccione la canción a eliminar
        cancion_id = input("Introduce el ID de la canción que deseas eliminar: ")

        # Confirmar eliminación
        confirmacion = input(f"¿Estás seguro de que deseas eliminar la canción con ID {cancion_id}? (s/n): ").lower()

        if confirmacion == 's':
            # Eliminar la canción
            cursor.execute("DELETE FROM canciones WHERE id = %s", (cancion_id,))
            conexion.commit()

            print("¡Canción eliminada exitosamente!")
        else:
            print("Eliminación cancelada.")
    else:
        print("No hay canciones disponibles para eliminar.")

    cursor.close()
    conexion.close()

# Funcion para eliminar un album
def eliminar_album():
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Mostrar lista de álbumes
    cursor.execute("SELECT id, titulo FROM albumes")
    albumes = cursor.fetchall()

    if albumes:
        print("Álbumes disponibles:")
        for album in albumes:
            print(f"ID: {album[0]}, Título: {album[1]}")

        # Pedir al usuario que seleccione el álbum a eliminar
        album_id = input("Introduce el ID del álbum que deseas eliminar: ")

        # Confirmar eliminación
        confirmacion = input(f"¿Estás seguro de que deseas eliminar el álbum con ID {album_id}? (s/n): ").lower()

        if confirmacion == 's':
            # Eliminar el álbum
            cursor.execute("DELETE FROM albumes WHERE id = %s", (album_id,))
            conexion.commit()

            print("¡Álbum eliminado exitosamente!")
        else:
            print("Eliminación cancelada.")
    else:
        print("No hay álbumes disponibles para eliminar.")

    cursor.close()
    conexion.close()

# Funcion para eliminar genero
def eliminar_genero():
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Mostrar lista de géneros
    cursor.execute("SELECT id, nombre FROM generos")
    generos = cursor.fetchall()

    if generos:
        print("Géneros disponibles:")
        for genero in generos:
            print(f"ID: {genero[0]}, Nombre: {genero[1]}")

        # Pedir al usuario que seleccione el género a eliminar
        genero_id = input("Introduce el ID del género que deseas eliminar: ")

        # Confirmar eliminación
        confirmacion = input(f"¿Estás seguro de que deseas eliminar el género con ID {genero_id}? (s/n): ").lower()

        if confirmacion == 's':
            # Eliminar el género
            cursor.execute("DELETE FROM generos WHERE id = %s", (genero_id,))
            conexion.commit()

            print("¡Género eliminado exitosamente!")
        else:
            print("Eliminación cancelada.")
    else:
        print("No hay géneros disponibles para eliminar.")

    cursor.close()
    conexion.close()
