# Función para eliminar un usuario
def eliminar_usuario():
    conexion = conectar_db()
    cursor = conexion.cursor()

    email_usuario = input("Introduce el email del usuario que deseas eliminar: ")

    # Verificar si el usuario existe
    cursor.execute("SELECT id, nombre, es_admin FROM Usuarios WHERE Email = %s", (email_usuario,))
    usuario = cursor.fetchone()

    if usuario:
        usuario_id, nombre, es_admin = usuario
        if es_admin:
            print(f"El usuario {nombre} es administrador.")
        else:
            print(f"El usuario {nombre} no es administrador.")

        confirmar = input(f"¿Estás seguro de que deseas eliminar al usuario {nombre}? (sí/no): ").lower()
        if confirmar == "sí":
            # Eliminar al usuario de la base de datos
            cursor.execute("DELETE FROM Usuarios WHERE id = %s", (usuario_id,))
            conexion.commit()
            print(f"¡El usuario {nombre} ha sido eliminado exitosamente!")
        else:
            print("Operación cancelada.")
    else:
        print("No se encontró un usuario con ese email.")

    cursor.close()
    conexion.close()
