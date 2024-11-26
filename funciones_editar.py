from db import conectar_db
#FUNCION PARA EDITAR

# Funcion par edita las lista de reproduccion
def editar_lista_reproduccion(usuario_id):
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Mostrar las listas de reproducción del usuario
    cursor.execute("SELECT id, nombre FROM Listas_Reproducciones WHERE usuario_id = %s", (usuario_id,))
    listas = cursor.fetchall()

    if not listas:
        print("No tienes listas de reproducción.")
        return

    print("Tus listas de reproducción:")
    for lista in listas:
        print(f"ID: {lista[0]}, Nombre: {lista[1]}")

    # Seleccionar una lista para editar
    lista_id = input("Introduce el ID de la lista que deseas editar: ")

    # Verificar si la lista existe
    cursor.execute("SELECT nombre, privacidad FROM Listas_Reproducciones WHERE id = %s", (lista_id,))
    lista = cursor.fetchone()

    if not lista:
        print("Lista no encontrada.")
        return

    print(f"Lista seleccionada: {lista[0]}, Privacidad: {lista[1]}")

    # Pedir nuevos datos
    nuevo_nombre = input("Introduce el nuevo nombre para la lista (deja en blanco para mantener el actual): ")
    nueva_privacidad = input("Introduce la nueva privacidad (publica/privada, deja en blanco para mantener el actual): ").lower()

    # Actualizar los datos
    if nuevo_nombre:
        cursor.execute("UPDATE Listas_Reproducciones SET nombre = %s WHERE id = %s", (nuevo_nombre, lista_id))

    if nueva_privacidad:
        cursor.execute("UPDATE Listas_Reproducciones SET privacidad = %s WHERE id = %s", (nueva_privacidad, lista_id))

    conexion.commit()
    print("Lista de reproducción actualizada exitosamente.")

    cursor.close()
    conexion.close()

# Funcion para editar el perfil
def editar_perfil(usuario_id):
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Obtener datos actuales del usuario
    cursor.execute("SELECT Nombre, Apellido, Email FROM Usuarios WHERE id = %s", (usuario_id,))
    usuario = cursor.fetchone()

    if not usuario:
        print("Usuario no encontrado.")
        return

    print(f"Usuario actual: {usuario[0]} {usuario[1]}, Email: {usuario[2]}")

    # Pedir nuevos datos
    nuevo_nombre = input("Introduce tu nuevo nombre (deja en blanco para mantener el actual): ")
    nuevo_apellido = input("Introduce tu nuevo apellido (deja en blanco para mantener el actual): ")
    nuevo_email = input("Introduce tu nuevo email (deja en blanco para mantener el actual): ")

    # Actualizar los datos
    if nuevo_nombre:
        cursor.execute("UPDATE Usuarios SET Nombre = %s WHERE id = %s", (nuevo_nombre, usuario_id))

    if nuevo_apellido:
        cursor.execute("UPDATE Usuarios SET Apellido = %s WHERE id = %s", (nuevo_apellido, usuario_id))

    if nuevo_email:
        cursor.execute("UPDATE Usuarios SET Email = %s WHERE id = %s", (nuevo_email, usuario_id))

    conexion.commit()
    print("Perfil actualizado exitosamente.")

    cursor.close()
    conexion.close()