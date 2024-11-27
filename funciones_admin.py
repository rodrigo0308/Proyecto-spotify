from db import conectar_db

# Funcion para añadir un artista
def añadir_artista():
    conexion = conectar_db()
    cursor = conexion.cursor()

    nombre_artista = input("Introduce el nombre del artista: ")
    
    # Insertar el nuevo artista en la base de datos
    cursor.execute("INSERT INTO Artistas (nombre) VALUES (%s)", (nombre_artista,))
    conexion.commit()

    print(f"¡Artista '{nombre_artista}' añadido exitosamente!")

    cursor.close()
    conexion.close()


# Funcion para añadir una cancion
def añadir_cancion():
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Solicitar el título y la duración de la canción
    titulo = input("Introduce el título de la canción: ")
    duracion = input("Introduce la duración de la canción (en formato mm:ss): ")

    # Verificar que la duración tenga el formato correcto
    if not duracion or len(duracion.split(":")) != 2:
        print("Formato de duración incorrecto. Debe ser en formato mm:ss.")
        return

    # Mostrar los artistas disponibles
    cursor.execute("SELECT id, nombre FROM Artistas")
    artistas = cursor.fetchall()

    if artistas:
        print("Artistas disponibles:")
        for artista in artistas:
            print(f"ID: {artista[0]}, Nombre: {artista[1]}")

        # Pedir al usuario que seleccione el artista
        artista_id = input("Introduce el ID del artista correspondiente: ")

        try:
            artista_id = int(artista_id)
        except ValueError:
            print("El ID del artista debe ser un número.")
            return

        # Verificar que el artista existe
        cursor.execute("SELECT id FROM Artistas WHERE id = %s", (artista_id,))
        if not cursor.fetchone():
            print("El ID del artista no es válido.")
            return

        # Mostrar los álbumes disponibles
        cursor.execute("SELECT id, titulo FROM Albumes")
        albumes = cursor.fetchall()

        if albumes:
            print("Álbumes disponibles:")
            for album in albumes:
                print(f"ID: {album[0]}, Título: {album[1]}")

            album_id = input("Introduce el ID del álbum correspondiente: ")

            try:
                album_id = int(album_id)
            except ValueError:
                print("El ID del álbum debe ser un número.")
                return
        else:
            album_id = None  # Si no hay álbumes disponibles, asignar None

        # Solicitar el género de la canción
        cursor.execute("SELECT id, nombre FROM Generos")
        generos = cursor.fetchall()

        if generos:
            print("Géneros disponibles:")
            for genero in generos:
                print(f"ID: {genero[0]}, Nombre: {genero[1]}")

            genero_id = input("Introduce el ID del género correspondiente: ")

            try:
                genero_id = int(genero_id)
            except ValueError:
                print("El ID del género debe ser un número.")
                return
        else:
            print("No hay géneros disponibles.")
            return

        # Validar que el género existe
        cursor.execute("SELECT id FROM Generos WHERE id = %s", (genero_id,))
        if not cursor.fetchone():
            print("El ID del género no es válido.")
            return

        # Insertar la canción en la base de datos
        cursor.execute("""
            INSERT INTO Canciones (titulo, duracion, artista_id, album_id, genero_id)
            VALUES (%s, %s, %s, %s, %s)
        """, (titulo, duracion, artista_id, album_id, genero_id))

        conexion.commit()
        print("¡Canción añadida exitosamente!")

    else:
        print("No hay artistas disponibles.")

    cursor.close()
    conexion.close()

# Funcion para añadir un album
def añadir_album():
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Solicitar el nombre del álbum
    titulo_album = input("Introduce el nombre del álbum: ")

    # Mostrar los artistas disponibles
    cursor.execute("SELECT id, nombre FROM Artistas")
    artistas = cursor.fetchall()

    if artistas:
        print("Artistas disponibles:")
        for artista in artistas:
            print(f"ID: {artista[0]}, Nombre: {artista[1]}")

        # Pedir al usuario que seleccione el artista
        artista_id = input("Selecciona el ID del artista al que pertenece este álbum: ")

        try:
            artista_id = int(artista_id)
        except ValueError:
            print("El ID del artista debe ser un número.")
            return

        # Verificar que el artista existe
        cursor.execute("SELECT id FROM Artistas WHERE id = %s", (artista_id,))
        if not cursor.fetchone():
            print("El ID del artista no es válido.")
            return

        # Solicitar la fecha de lanzamiento del álbum
        fecha_lanzamiento = input("Introduce la fecha de lanzamiento del álbum (formato AAAA-MM-DD): ")

        # Insertar el álbum en la base de datos
        try:
            cursor.execute("""
                INSERT INTO Albumes (titulo, fecha_lanzamiento, artista_id)
                VALUES (%s, %s, %s)
            """, (titulo_album, fecha_lanzamiento, artista_id))

            conexion.commit()
            print("¡Álbum añadido exitosamente!")
        except Exception as e:
            print(f"Error al añadir el álbum: {e}")

    else:
        print("No hay artistas disponibles.")

    cursor.close()
    conexion.close()


# Función para añadir un nuevo género musical
def añadir_genero():
    conexion = conectar_db()
    cursor = conexion.cursor()

    nombre_genero = input("Introduce el nombre del género musical (por ejemplo, 'Pop', 'Rock', etc.): ")

    # Comprobamos si el género ya existe
    cursor.execute("SELECT * FROM Generos WHERE nombre = %s", (nombre_genero,))
    genero_existente = cursor.fetchone()

    if genero_existente:
        print(f"El género '{nombre_genero}' ya existe en la base de datos.")
    else:
        # Insertamos el nuevo género
        cursor.execute("INSERT INTO Generos (nombre) VALUES (%s)", (nombre_genero,))
        conexion.commit()
        print(f"¡Género '{nombre_genero}' añadido exitosamente!")

    cursor.close()
    conexion.close()

