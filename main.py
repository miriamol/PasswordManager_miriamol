# Password Manager - main.py

# Importar librerías necesarias
import os
import hashlib

# Función para guardar contraseñas
def save_password():
    pass  # Implementar más adelante

# Función para recuperar contraseñas
def get_password():
    pass  # Implementar más adelante

# Menú principal
def main_menu():
    print("Bienvenido al Gestor de Contraseñas")
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
    while True:
        main_menu()
