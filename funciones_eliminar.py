from db import conectar_db

# Funcion para eliminar la lista de reproduccion
def eliminar_lista_reproduccion(usuario_id):
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Mostrar listas de reproducción del usuario
    cursor.execute("SELECT id, nombre FROM Listas_Reproducciones WHERE usuario_id = %s", (usuario_id,))
    listas = cursor.fetchall()

    if listas:
        print("Listas de reproducción disponibles:")
        for lista in listas:
            print(f"ID: {lista[0]}, Nombre: {lista[1]}")

        # Pedir al usuario que seleccione la lista a eliminar
        lista_id = input("Introduce el ID de la lista que deseas eliminar: ")

        # Eliminar la lista de reproducción y también eliminarla de la tabla Bibliotecas
        cursor.execute("DELETE FROM Listas_Reproducciones WHERE id = %s AND usuario_id = %s", (lista_id, usuario_id))
        cursor.execute("DELETE FROM Bibliotecas WHERE lista_id = %s", (lista_id,))
        conexion.commit()

        print("¡Lista de reproducción eliminada exitosamente!")
    else:
        print("No tienes listas de reproducción disponibles para eliminar.")

    cursor.close()
    conexion.close()


# Funcion para eliminar cancion de la biblioteca
def eliminar_cancion_de_biblioteca(usuario_id):
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Mostrar canciones en la biblioteca del usuario
    cursor.execute("""
        SELECT b.id, c.titulo 
        FROM Bibliotecas b 
        JOIN Canciones c ON b.cancion_id = c.id 
        WHERE b.usuario_id = %s
    """, (usuario_id,))
    canciones = cursor.fetchall()

    if canciones:
        print("Canciones en tu biblioteca:")
        for cancion in canciones:
            print(f"ID: {cancion[0]}, Título: {cancion[1]}")

        # Pedir al usuario que seleccione la canción a eliminar
        cancion_id = input("Introduce el ID de la canción que deseas eliminar de tu biblioteca: ")

        # Eliminar la canción de la biblioteca del usuario
        cursor.execute("DELETE FROM Bibliotecas WHERE id = %s AND usuario_id = %s", (cancion_id, usuario_id))
        conexion.commit()

        print("¡Canción eliminada de tu biblioteca exitosamente!")
    else:
        print("No tienes canciones en tu biblioteca para eliminar.")

    cursor.close()
    conexion.close()


# Función para eliminar canción de una lista de reproducción
def eliminar_cancion_de_lista(usuario_id):
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Mostrar listas de reproducción del usuario
    cursor.execute("SELECT id, nombre FROM listas_reproducciones WHERE usuario_id = %s", (usuario_id,))
    listas = cursor.fetchall()

    if listas:
        print("Listas de reproducción disponibles:")
        for lista in listas:
            print(f"ID: {lista[0]}, Nombre: {lista[1]}")

        # Pedir al usuario que seleccione la lista de reproducción
        lista_id = input("Introduce el ID de la lista de la que deseas eliminar una canción: ")

        # Mostrar las canciones en la lista seleccionada
        cursor.execute("""
            SELECT c.id, c.titulo 
            FROM lista_canciones lc 
            JOIN canciones c ON lc.cancion_id = c.id 
            WHERE lc.lista_id = %s
        """, (lista_id,))
        canciones = cursor.fetchall()

        if canciones:
            print("Canciones en la lista seleccionada:")
            for cancion in canciones:
                print(f"ID: {cancion[0]}, Título: {cancion[1]}")

            # Pedir al usuario que seleccione la canción a eliminar
            cancion_id = input("Introduce el ID de la canción que deseas eliminar de la lista: ")

            # Eliminar la canción de la lista de reproducción
            cursor.execute("DELETE FROM lista_canciones WHERE cancion_id = %s AND lista_id = %s", (cancion_id, lista_id))
            conexion.commit()

            print("¡Canción eliminada de la lista de reproducción exitosamente!")
        else:
            print("La lista seleccionada no contiene canciones.")

    else:
        print("No tienes listas de reproducción disponibles.")

    cursor.close()
    conexion.close()
