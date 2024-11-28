import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import os

# Configura la clave
if not os.path.exists('secret.key'):
    with open('secret.key', 'wb') as key_file:
        key_file.write(Fernet.generate_key())

with open('secret.key', 'rb') as key_file:
    key = key_file.read()

f = Fernet(key)

# Funciones
def save_password():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:
        encrypted_password = f.encrypt(password.encode())
        with open('passwords.txt', 'a') as file:
            file.write(f"{username}: {encrypted_password.decode()}\n")
        messagebox.showinfo("Éxito", "Contraseña guardada.")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Introduce todos los campos.")

def retrieve_password():
    username = username_entry.get()
    if username:
        with open('passwords.txt', 'r') as file:
            for line in file:
                stored_user, encrypted_password = line.strip().split(': ')
                if stored_user == username:
                    decrypted_password = f.decrypt(encrypted_password.encode()).decode()
                    messagebox.showinfo("Contraseña Recuperada", f"Contraseña: {decrypted_password}")
                    return
        messagebox.showerror("Error", "Usuario no encontrado.")
    else:
        messagebox.showerror("Error", "Introduce el usuario.")

# Interfaz gráfica
root = tk.Tk()
root.title("Gestor de Contraseñas")

# Diseño
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Usuario:").grid(row=0, column=0, sticky="e")
username_entry = tk.Entry(frame, width=30)
username_entry.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Contraseña:").grid(row=1, column=0, sticky="e")
password_entry = tk.Entry(frame, show="*", width=30)
password_entry.grid(row=1, column=1, pady=5)

tk.Button(frame, text="Guardar Contraseña", command=save_password).grid(row=2, column=0, columnspan=2, pady=10)
tk.Button(frame, text="Recuperar Contraseña", command=retrieve_password).grid(row=3, column=0, columnspan=2)

# Ejecución
root.mainloop()
