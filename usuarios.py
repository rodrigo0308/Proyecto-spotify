import bcrypt
from db import conectar_db
import mysql.connector


# Función para crear cuenta
def crear_cuenta():
    conexion = conectar_db()
    if conexion is None:
        return
    cursor = conexion.cursor()

    # Pedimos los datos al usuario
    nombre = input("Introduce tu nombre: ")
    apellido = input("Introduce tu apellido: ")
    email = input("Introduce tu email: ")
    contraseña = input("Introduce tu contraseña: ")

    # Verificamos si el email ya está registrado
    cursor.execute("SELECT * FROM Usuarios WHERE Email = %s", (email,))
    usuario_existente = cursor.fetchone()

    if usuario_existente:
        print("El email ya está registrado. Intenta con otro.")
    else:
        # Hasheamos la contraseña
        contraseña_hash = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt())

        # Verificamos si el email es de dominio @example.com para ser admin
        es_admin = True if email.endswith("@example.com") else False

        # Insertamos el nuevo usuario en la base de datos
        try:
            cursor.execute(
                "INSERT INTO Usuarios (Nombre, Apellido, Email, Contraseña, es_admin) VALUES (%s, %s, %s, %s, %s)",
                (nombre, apellido, email, contraseña_hash.decode('utf-8'), es_admin)
            )
            conexion.commit()
            print("¡Cuenta creada exitosamente!")
        except mysql.connector.Error as err:
            print(f"Error al crear la cuenta: {err}")

    cursor.close()
    conexion.close()

# Función para iniciar sesión
def iniciar_sesion(menu_administrador, menu_usuario):
    conexion = conectar_db()
    if conexion is None:
        return
    cursor = conexion.cursor()

    correo = input("Introduce tu correo: ")
    contraseña = input("Introduce tu contraseña: ")

    try:
        cursor.execute("SELECT id, nombre, Contraseña, es_admin FROM Usuarios WHERE Email = %s", (correo,))
        resultado = cursor.fetchone()

        if resultado:
            usuario_id = resultado[0]
            nombre = resultado[1]
            contraseña_hash = resultado[2]
            es_admin = resultado[3]

            # Verificamos la contraseña usando bcrypt
            if bcrypt.checkpw(contraseña.encode('utf-8'), contraseña_hash.encode('utf-8')):
                print("Inicio de sesión exitoso.")
                
                # Si es administrador, mostramos el menú de administrador
                if es_admin:
                    print(f"Bienvenido Administrador {nombre}")
                    menu_administrador()
                else:
                    print(f"Bienvenido Usuario {nombre}")
                    menu_usuario(usuario_id, nombre)
            else:
                print("Contraseña incorrecta.")
        else:
            print("Correo no encontrado.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conexion.close()
