from db import conectar_db

# Funcion para crear una lista de reproduccion
def crear_lista_reproduccion(usuario_id):
    conexion = conectar_db()
    cursor = conexion.cursor()

    nombre_lista = input("Introduce el nombre de la lista de reproducción: ")
    tipo_lista = input("¿La lista será pública o privada? (publica/privada): ").lower()

    # Asigna el valor de privacidad basado en la opción del usuario
    privacidad = 'publica' if tipo_lista == 'publica' else 'privada'

    # Asegúrate de incluir 'privacidad' en la inserción
    cursor.execute("""
        INSERT INTO Listas_Reproducciones (nombre, usuario_id, fecha_creacion, privacidad) 
        VALUES (%s, %s, NOW(), %s)
    """, (nombre_lista, usuario_id, privacidad))
    conexion.commit()

    lista_id = cursor.lastrowid
    print(f"¡Lista de reproducción '{nombre_lista}' creada exitosamente!")

    añadir_a_biblioteca = input("¿Deseas añadir esta lista a tu biblioteca? (si/no): ").lower()
    if añadir_a_biblioteca == "si":
        cursor.execute("INSERT INTO Bibliotecas (usuario_id, lista_id) VALUES (%s, %s)", (usuario_id, lista_id))
        conexion.commit()
        print(f"La lista '{nombre_lista}' ha sido añadida a tu biblioteca.")
    else:
        print(f"La lista '{nombre_lista}' ha sido creada, pero no añadida a la biblioteca.")

    cursor.close()
    conexion.close()

# Funcion para agregar una cancion a una lista de reproduccion
def agregar_cancion_a_lista(usuario_id):
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Mostrar las listas de reproducción del usuario
    cursor.execute("SELECT id, nombre FROM Listas_Reproducciones WHERE usuario_id = %s", (usuario_id,))
    listas = cursor.fetchall()

    if listas:
        print("Listas de reproducción disponibles:")
        for lista in listas:
            print(f"ID: {lista[0]}, Nombre: {lista[1]}")

        # Pedir al usuario que seleccione la lista
        lista_id = input("Introduce el ID de la lista de reproducción: ")

        # Verificar si la lista de reproducción existe
        cursor.execute("SELECT id FROM Listas_Reproducciones WHERE id = %s AND usuario_id = %s", (lista_id, usuario_id))
        lista_valida = cursor.fetchone()

        if not lista_valida:
            print("ID de lista no válido. Por favor, intenta de nuevo.")
        else:
            # Mostrar canciones disponibles
            cursor.execute("SELECT id, titulo FROM Canciones")
            canciones = cursor.fetchall()

            if canciones:
                print("Canciones disponibles:")
                for cancion in canciones:
                    print(f"ID: {cancion[0]}, Título: {cancion[1]}")

                # Pedir al usuario que seleccione una canción
                cancion_id = input("Introduce el ID de la canción que deseas añadir a la lista: ")

                # Verificar si la canción existe
                cursor.execute("SELECT id FROM Canciones WHERE id = %s", (cancion_id,))
                cancion_valida = cursor.fetchone()

                if not cancion_valida:
                    print("ID de canción no válido.")
                else:
                    # Insertar la canción en la lista de reproducción
                    cursor.execute("INSERT INTO Lista_Canciones (lista_id, cancion_id) VALUES (%s, %s)", (lista_id, cancion_id))
                    conexion.commit()
                    print("¡Canción añadida exitosamente a la lista de reproducción!")
            else:
                print("No hay canciones disponibles para añadir.")
    else:
        print("No tienes listas de reproducción disponibles para añadir canciones.")

    cursor.close()
    conexion.close()


# Funcion par agregar una cancion a la biblioteca
def agregar_cancion_a_biblioteca(usuario_id):
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Mostrar canciones disponibles
    cursor.execute("SELECT id, titulo FROM Canciones")
    canciones = cursor.fetchall()

    if canciones:
        print("Canciones disponibles para añadir a tu biblioteca:")
        for cancion in canciones:
            print(f"ID: {cancion[0]}, Título: {cancion[1]}")

        # Pedir al usuario que seleccione una canción
        cancion_id = input("Introduce el ID de la canción que deseas agregar a tu biblioteca: ")

        # Verificar si la canción existe
        cursor.execute("SELECT id FROM Canciones WHERE id = %s", (cancion_id,))
        cancion_valida = cursor.fetchone()

        if not cancion_valida:
            print("ID de canción no válido. Por favor, intenta de nuevo.")
        else:
            # Añadir la canción a la biblioteca del usuario
            cursor.execute("INSERT INTO Bibliotecas (usuario_id, cancion_id) VALUES (%s, %s)", (usuario_id, cancion_id))
            conexion.commit()
            print("¡Canción añadida exitosamente a tu biblioteca!")
    else:
        print("No hay canciones disponibles para añadir.")

    cursor.close()
    conexion.close()


# Funcion para buscar una cancion por nombre
def buscar_cancion_por_nombre():
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Pedir al usuario que introduzca el nombre de la canción
    nombre_cancion = input("Introduce el nombre de la canción que deseas buscar: ")

    # Buscar la canción en la base de datos, incluyendo la relación con el artista
    cursor.execute("""
        SELECT c.id, c.titulo, c.duracion, a.nombre 
        FROM Canciones c 
        JOIN Artistas a ON c.artista_id = a.id 
        WHERE c.titulo LIKE %s
    """, ('%' + nombre_cancion + '%',))

    canciones = cursor.fetchall()

    if canciones:
        print("Canciones encontradas:")
        for cancion in canciones:
            print(f"ID: {cancion[0]}, Título: {cancion[1]}, Duración: {cancion[2]}, Artista: {cancion[3]}")
    else:
        print("No se encontraron canciones con ese nombre.")

    cursor.close()
    conexion.close()

# FUNCIONES DE READ, ES DECIR LEER
# Funcion para ver las listas de reproducciones del usuario
def ver_listas_usuario(usuario_id):
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Obtener listas de reproducción del usuario
    cursor.execute("SELECT id, nombre FROM listas_reproducciones WHERE usuario_id = %s", (usuario_id,))
    listas = cursor.fetchall()

    if listas:
        print("Listas de reproducción:")
        for lista in listas:
            print(f"ID: {lista[0]}, Nombre: {lista[1]}")
    else:
        print("No tienes listas de reproducción.")

    cursor.close()
    conexion.close()

# Funcion para ver canciones en una lista de reproducción
def ver_canciones_en_lista(usuario_id):
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Mostrar listas de reproducción del usuario
    cursor.execute("SELECT id, nombre FROM listas_reproducciones WHERE usuario_id = %s", (usuario_id,))
    listas = cursor.fetchall()

    if listas:
        print("Listas de reproducción disponibles:")
        for lista in listas:
            print(f"ID: {lista[0]}, Nombre: {lista[1]}")

        lista_id = input("Introduce el ID de la lista para ver sus canciones: ")

        # Mostrar canciones en la lista seleccionada
        cursor.execute("""
            SELECT c.id, c.titulo, c.duracion 
            FROM lista_canciones lc
            JOIN canciones c ON lc.cancion_id = c.id
            WHERE lc.lista_id = %s
        """, (lista_id,))
        canciones = cursor.fetchall()

        if canciones:
            print(f"Canciones en la lista {lista_id}:")
            for cancion in canciones:
                print(f"ID: {cancion[0]}, Título: {cancion[1]}, Duración: {cancion[2]}")
        else:
            print("La lista seleccionada no tiene canciones.")
    else:
        print("No tienes listas de reproducción disponibles.")

    cursor.close()
    conexion.close()

# Funcon par ver biblioteca
def ver_biblioteca(usuario_id):
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Mostrar canciones en la biblioteca del usuario
    print("\n===== Canciones en tu Biblioteca =====")
    cursor.execute("""
        SELECT c.id, c.titulo, c.duracion 
        FROM bibliotecas b
        JOIN canciones c ON b.cancion_id = c.id
        WHERE b.usuario_id = %s
    """, (usuario_id,))
    canciones = cursor.fetchall()

    if canciones:
        for cancion in canciones:
            print(f"ID: {cancion[0]}, Título: {cancion[1]}, Duración: {cancion[2]}")
    else:
        print("No tienes canciones en tu biblioteca.")

    # Mostrar listas de reproducción en la biblioteca del usuario
    print("\n===== Listas de Reproducción en tu Biblioteca =====")
    cursor.execute("""
        SELECT lr.id, lr.nombre, lr.fecha_creacion, lr.privacidad 
        FROM bibliotecas b
        JOIN listas_reproducciones lr ON b.lista_id = lr.id
        WHERE b.usuario_id = %s
    """, (usuario_id,))
    listas_reproduccion = cursor.fetchall()

    if listas_reproduccion:
        for lista in listas_reproduccion:
            print(f"ID: {lista[0]}, Nombre: {lista[1]}, Fecha de creación: {lista[2]}, Privacidad: {lista[3]}")
    else:
        print("No tienes listas de reproducción en tu biblioteca.")

    cursor.close()
    conexion.close()

