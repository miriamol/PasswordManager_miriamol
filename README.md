# PasswordManager_miriamol

# Gestor de Contraseñas

Este es un proyecto de gestión de contraseñas, donde puedes guardar y recuperar contraseñas de forma segura utilizando cifrado simétrico. El propósito del proyecto es proporcionar una solución simple y segura para almacenar contraseñas de manera cifrada.

## Características

- Guardar contraseñas de manera segura.
- Recuperar contraseñas de manera segura.
- Cifrado utilizando una clave secreta.

## Requisitos

- Python 3.x
- Pip

## Instalación

Para instalar y ejecutar este proyecto en tu máquina local, sigue estos pasos:

1. Clona este repositorio:
   git clone https://github.com/tu_usuario/PasswordManager.git
Navega al directorio del proyecto:

cd PasswordManager
Crea un entorno virtual (opcional pero recomendado):

python -m venv .venv
Activa el entorno virtual:

En Windows:

.venv\Scripts\activate
En macOS/Linux:

source .venv/bin/activate
Instala las dependencias necesarias:

pip install -r requirements.txt
Ejecuta el proyecto:

python main.py
Esto iniciará el Gestor de Contraseñas, donde podrás elegir entre guardar o recuperar contraseñas.

Uso
Cuando ejecutes el proyecto, verás un menú de opciones:

Guardar una contraseña
Recuperar una contraseña
Salir
Guardar una Contraseña
Ingresa la contraseña que quieras guardar.
Ingresa el nombre de usuario asociado.
La contraseña se cifrará y se almacenará de forma segura.
Recuperar una Contraseña
Ingresa el nombre de usuario para recuperar la contraseña guardada previamente.
La contraseña se descifrará y se mostrará en la terminal.
Contribuciones
Si deseas contribuir a este proyecto, sigue estos pasos:

Haz un fork de este repositorio.
Crea una nueva rama para tu característica (git checkout -b nueva-caracteristica).
Realiza tus cambios y haz commit (git commit -am 'Añadir nueva característica').
Haz un push a la rama (git push origin nueva-caracteristica).
Abre un Pull Request describiendo tus cambios.

Licencia
Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.