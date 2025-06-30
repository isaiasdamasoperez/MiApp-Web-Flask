from flask import Flask, render_template # Importa render_template
import os
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos desde variables de entorno
DB_HOST = os.environ.get('DB_HOST', 'db')
DB_USER = os.environ.get('DB_USER', 'user')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
DB_NAME = os.environ.get('DB_NAME', 'mydatabase')

@app.route('/')
def hello_world():
    db_message = ""
    try:
        # Intentar conectar a la base de datos
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        db_version = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        db_message = f"isaias damaso perez 2015-2659"
    except Exception as e:
        db_message = f"Error al conectar a la base de datos: <span class='error'>{e}</span>"

    # Renderiza el template index.html y le pasa el mensaje de la base de datos
    return render_template('index.html', message=db_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)