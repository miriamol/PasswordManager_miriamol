# Password Manager - main.py

# Importar librerías necesarias
import os
import hashlib
from cryptography.fernet import Fernet
from tkinter import messagebox

# Función para guardar contraseñas
# librería de cifrado para proteger las contraseñas antes de guardarlas cryptography
# Función para generar y guardar la clave de cifrado (se debe ejecutar una sola vez)
def generate_key():
    # Genera una clave secreta
    key = Fernet.generate_key()
    # Guardar la clave en un archivo
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Clave generada y guardada en 'secret.key'.")

# Función para cargar la clave de cifrado desde el archivo
def load_key():
    return open("secret.key", "rb").read()

# Función para guardar contraseñas
def save_password():
    # Pedimos la contraseña y el nombre de usuario al usuario
    password = input("Introduce la contraseña que quieras guardar: ")
    username = input("Introduce tu nombre de usuario: ")

    # Cargar la clave de cifrado
    key = load_key()

    # Crear un objeto Fernet para cifrar
    f = Fernet(key)

    # Cifrar la contraseña
    encrypted_password = f.encrypt(password.encode())

    # Guardar la contraseña cifrada en un archivo
    with open("passwords.txt", "ab") as f:
        f.write(f"{username}: {encrypted_password.decode()}\n".encode())

    print("Contraseña guardada de manera segura.")

# Función para recuperar contraseñas
def get_password():
    username = input("Introduce tu nombre de usuario para recuperar la contraseña: ")
    try:
        with open("passwords.txt", "r") as f:
            for line in f:
                stored_user, encrypted_password = line.strip().split(": ")
                if stored_user == username:
                    with open("secret.key", "rb") as key_file:
                        key = key_file.read()
                    fernet = Fernet(key)
                    decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
                    print(f"Contraseña recuperada: {decrypted_password}")
                    return
            print("Usuario no encontrado.")
    except ValueError:
        print("Error al procesar el archivo. Asegúrate de que el formato sea correcto.")
    except FileNotFoundError:
        print("Archivo de contraseñas no encontrado. Guarda una contraseña primero.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def recuperar_contraseña():
    username = username_entry.get() # type: ignore
    try:
        with open("passwords.txt", "r") as f:
            for line in f:
                stored_user, encrypted_password = line.strip().split(": ")
                if stored_user == username:
                    with open("secret.key", "rb") as key_file:
                        key = key_file.read()
                    fernet = Fernet(key)
                    decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
                    messagebox.showinfo("Contraseña Recuperada", f"Tu contraseña es: {decrypted_password}")
                    return
            messagebox.showwarning("Usuario no encontrado", "No se encontró este usuario.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")
# Menú principal
def main_menu():
    print("¡Bienvenido/a a este Gestor de Contraseñas!")
    print("1. Guardar una contraseña")
    print("2. Recuperar una contraseña")
    print("3. Salir")

    option = input("¿Qué quieres hacer?: ")
    if option == "1":
        save_password()
    elif option == "2":
        get_password()
    elif option == "3":
        print("¡Hasta la próxima!")
        exit()
    else:
        print("Esta no es una opción válida, inténtalo de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
    # Solo ejecuta esta parte una vez, si no tienes la clave
    # Descomenta esta línea la primera vez que corras el código
    # generate_key()

    while True:
        main_menu()