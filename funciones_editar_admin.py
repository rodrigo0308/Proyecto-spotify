from db import conectar_db

# FUNCIONES DE EDITAR 

# Funcion editar artista
def editar_artista():
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Mostrar lista de artistas
    cursor.execute("SELECT id, nombre FROM artistas")
    artistas = cursor.fetchall()

    if artistas:
        print("Artistas disponibles:")
        for artista in artistas:
            print(f"ID: {artista[0]}, Nombre: {artista[1]}")

        # Pedir al usuario que seleccione el artista a editar
        artista_id = input("Introduce el ID del artista que deseas editar: ")

        # Obtener el nombre actual del artista
        cursor.execute("SELECT nombre FROM artistas WHERE id = %s", (artista_id,))
        artista_actual = cursor.fetchone()

        if artista_actual:
            print(f"Nombre actual: {artista_actual[0]}")
            nuevo_nombre = input("Introduce el nuevo nombre del artista (deja en blanco para mantener el actual): ")

            # Si el campo está vacío, mantener el valor actual
            if not nuevo_nombre:
                nuevo_nombre = artista_actual[0]

            # Actualizar el nombre del artista
            cursor.execute("UPDATE artistas SET nombre = %s WHERE id = %s", (nuevo_nombre, artista_id))
            conexion.commit()

            print("¡Artista actualizado exitosamente!")
        else:
            print("Artista no encontrado.")
    else:
        print("No hay artistas disponibles para editar.")

    cursor.close()
    conexion.close()


# Funcion para editar las cancioes
def editar_cancion():
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Mostrar lista de canciones
    cursor.execute("SELECT id, titulo, duracion FROM canciones")
    canciones = cursor.fetchall()

    if canciones:
        print("Canciones disponibles:")
        for cancion in canciones:
            print(f"ID: {cancion[0]}, Título: {cancion[1]}")

        # Pedir al usuario que seleccione la canción a editar
        cancion_id = input("Introduce el ID de la canción que deseas editar: ")

        # Obtener los valores actuales de la canción
        cursor.execute("SELECT titulo, duracion FROM canciones WHERE id = %s", (cancion_id,))
        cancion_actual = cursor.fetchone()

        if cancion_actual:
            print(f"Título actual: {cancion_actual[0]}")
            nuevo_titulo = input("Introduce el nuevo título de la canción (deja en blanco para mantener el actual): ")

            print(f"Duración actual: {cancion_actual[1]}")
            nueva_duracion = input("Introduce la nueva duración de la canción (deja en blanco para mantener la actual): ")

            # Si los campos están vacíos, mantener los valores actuales
            if not nuevo_titulo:
                nuevo_titulo = cancion_actual[0]
            if not nueva_duracion:
                nueva_duracion = cancion_actual[1]

            # Actualizar la canción
            cursor.execute("UPDATE canciones SET titulo = %s, duracion = %s WHERE id = %s", 
                           (nuevo_titulo, nueva_duracion, cancion_id))
            conexion.commit()

            print("¡Canción actualizada exitosamente!")
        else:
            print("Canción no encontrada.")
    else:
        print("No hay canciones disponibles para editar.")

    cursor.close()
    conexion.close()


# Funcion para editar los albumes 
def editar_album():
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Mostrar lista de álbumes
    cursor.execute("SELECT id, titulo, fecha_lanzamiento FROM albumes")
    albumes = cursor.fetchall()

    if albumes:
        print("Álbumes disponibles:")
        for album in albumes:
            print(f"ID: {album[0]}, Título: {album[1]}")

        # Pedir al usuario que seleccione el álbum a editar
        album_id = input("Introduce el ID del álbum que deseas editar: ")

        # Obtener los valores actuales del álbum
        cursor.execute("SELECT titulo, fecha_lanzamiento FROM albumes WHERE id = %s", (album_id,))
        album_actual = cursor.fetchone()

        if album_actual:
            print(f"Título actual: {album_actual[0]}")
            nuevo_titulo = input("Introduce el nuevo título del álbum (deja en blanco para mantener el actual): ")

            print(f"Fecha de lanzamiento actual: {album_actual[1]}")
            nueva_fecha = input("Introduce la nueva fecha de lanzamiento (deja en blanco para mantener la actual): ")

            # Si los campos están vacíos, mantener los valores actuales
            if not nuevo_titulo:
                nuevo_titulo = album_actual[0]
            if not nueva_fecha:
                nueva_fecha = album_actual[1]

            # Actualizar el álbum
            cursor.execute("UPDATE albumes SET titulo = %s, fecha_lanzamiento = %s WHERE id = %s", 
                           (nuevo_titulo, nueva_fecha, album_id))
            conexion.commit()

            print("¡Álbum actualizado exitosamente!")
        else:
            print("Álbum no encontrado.")
    else:
        print("No hay álbumes disponibles para editar.")

    cursor.close()
    conexion.close()


# Funcion editar los generos 
def editar_genero():
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Mostrar lista de géneros
    cursor.execute("SELECT id, nombre FROM generos")
    generos = cursor.fetchall()

    if generos:
        print("Géneros disponibles:")
        for genero in generos:
            print(f"ID: {genero[0]}, Nombre: {genero[1]}")

        # Pedir al usuario que seleccione el género a editar
        genero_id = input("Introduce el ID del género que deseas editar: ")

        # Obtener el nombre actual del género
        cursor.execute("SELECT nombre FROM generos WHERE id = %s", (genero_id,))
        genero_actual = cursor.fetchone()

        if genero_actual:
            print(f"Nombre actual: {genero_actual[0]}")
            nuevo_nombre = input("Introduce el nuevo nombre del género (deja en blanco para mantener el actual): ")

            # Si el campo está vacío, mantener el valor actual
            if not nuevo_nombre:
                nuevo_nombre = genero_actual[0]

            # Actualizar el género
            cursor.execute("UPDATE generos SET nombre = %s WHERE id = %s", (nuevo_nombre, genero_id))
            conexion.commit()

            print("¡Género actualizado exitosamente!")
        else:
            print("Género no encontrado.")
    else:
        print("No hay géneros disponibles para editar.")

    cursor.close()
    conexion.close()

# FUNCONES PARA READ, ES DECIR LEER
# funcion par ver artistas
def ver_artistas():
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("SELECT id, nombre FROM Artistas")
    artistas = cursor.fetchall()

    if artistas:
        print("\n===== Lista de Artistas =====")
        for artista in artistas:
            print(f"ID: {artista[0]}, Nombre: {artista[1]}")
    else:
        print("No hay artistas registrados.")

    cursor.close()
    conexion.close()

# Funcion para ver canciones
def ver_canciones():
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("SELECT id, titulo, duracion FROM Canciones")
    canciones = cursor.fetchall()

    if canciones:
        print("\n===== Lista de Canciones =====")
        for cancion in canciones:
            print(f"ID: {cancion[0]}, Título: {cancion[1]}, Duración: {cancion[2]}")
    else:
        print("No hay canciones registradas.")

    cursor.close()
    conexion.close()

# Funcion para ver albumes
def ver_albumes():
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Seleccionar los álbumes de la base de datos
    cursor.execute("SELECT id, titulo, fecha_lanzamiento FROM Albumes")  # Usamos 'titulo' en lugar de 'nombre'
    albumes = cursor.fetchall()

    if albumes:
        print("\n===== Álbumes =====")
        for album in albumes:
            print(f"ID: {album[0]}, Título: {album[1]}, Fecha de lanzamiento: {album[2]}")
    else:
        print("No hay álbumes disponibles.")

    cursor.close()
    conexion.close()


# Funcion para ver géneros
def ver_generos():
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("SELECT id, nombre FROM Generos")
    generos = cursor.fetchall()

    if generos:
        print("\n===== Lista de Géneros =====")
        for genero in generos:
            print(f"ID: {genero[0]}, Nombre: {genero[1]}")
    else:
        print("No hay géneros registrados.")

    cursor.close()
    conexion.close()
