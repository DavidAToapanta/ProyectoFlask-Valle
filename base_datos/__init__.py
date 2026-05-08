# pyrefly: ignore [missing-import]
from flask_sqlalchemy import SQLAlchemy


#Creacmos la intancia de la base de datos
db = SQLAlchemy()

def _init_db(app, db_uri):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #Unir la base de datos con los modelos de flask
    db.init_app(app)

    #Crear las tablas en la base de datos
    with app.app_context():
        print("Iniciando BD")
        from .models import Usuario, Categoria, Libro, Cliente, Prestamo
    
        db.create_all()
        print("Tablas creadas")





