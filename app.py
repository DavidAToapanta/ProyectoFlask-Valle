from flask import jsonify
import os
from flask import Flask, render_template
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from base_datos import _init_db, db

load_dotenv()

app = Flask(__name__)

# Capturar los datos del .env
DB_USER = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# Construcción de la URI
DB_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Vincular SQLAlchemy a la app con manejo de errores
try:
    _init_db(app, DB_URI)
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
    raise

# Crear la ruta de prueba inicial
@app.route('/')
def test_conecciton():
    return jsonify({
        "user_connected": DB_USER,
        "status": "conectado",
        "Data_base": DB_NAME
    })

# @app.route('/')
# def hello():
#     return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)