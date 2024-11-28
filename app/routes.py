from flask import Flask, render_template, request, redirect, url_for
from cryptography.fernet import Fernet
import os

app = Flask(__name__)

# Carga la clave secreta
if not os.path.exists('secret.key'):
    with open('secret.key', 'wb') as key_file:
        key_file.write(Fernet.generate_key())

with open('secret.key', 'rb') as key_file:
    key = key_file.read()

f = Fernet(key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['GET', 'POST'])
def save_password():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        encrypted_password = f.encrypt(password.encode())
        with open('passwords.txt', 'a') as file:
            file.write(f"{username}: {encrypted_password.decode()}\n")
        return redirect(url_for('index'))
    return render_template('save_password.html')

@app.route('/retrieve', methods=['GET', 'POST'])
def retrieve_password():
    if request.method == 'POST':
        username = request.form['username']
        with open('passwords.txt', 'r') as file:
            for line in file:
                stored_user, encrypted_password = line.strip().split(': ')
                if stored_user == username:
                    decrypted_password = f.decrypt(encrypted_password.encode()).decode()
                    return f"Contraseña recuperada: {decrypted_password}"
        return "Usuario no encontrado"
    return render_template('retrieve_password.html')

if __name__ == '__main__':
    app.run(debug=True)
