from . import db
from datetime import datetime


class Usuario(db.Model):
    __tablename__ = "Usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    prestamos = db.relationship('Prestamo', backref='usuario', lazy=True)

    def to_dict(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "correo": self.correo,
            "fecha_registro": self.fecha_registro,
        }


class Categoria(db.Model):
    __tablename__ = "Categorias"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255), nullable=True)

    libros = db.relationship('Libro', backref='categoria', lazy=True)

    def to_dict(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
        }

class Libro(db.Model):
    __tablename__ = "Libros"
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    autor = db.Column(db.String(150), nullable=False)
    fecha_publicacion = db.Column(db.Date, nullable=True)
    isbn = db.Column(db.String(20), unique=True, nullable=True)
    stock = db.Column(db.Integer, default=1)
    categoria_id = db.Column(db.Integer, db.ForeignKey('Categorias.id'), nullable=True)

    prestamos = db.relationship('Prestamo', backref='libro', lazy=True)

    def to_dict(self):
        return{
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "fecha_publicacion": self.fecha_publicacion,
            "isbn": self.isbn,
            "stock": self.stock,
            "categoria_id": self.categoria_id,
        }

class Cliente(db.Model):
    __tablename__ = "Clientes"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.String(20), nullable=True)
    direccion = db.Column(db.String(255), nullable=True)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    prestamos = db.relationship('Prestamo', backref='cliente', lazy=True)

    
    def to_dict(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "correo": self.correo,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "fecha_registro": self.fecha_registro,
        }

class Prestamo(db.Model):
    __tablename__ = "Prestamos"
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('Clientes.id'), nullable=False)
    libro_id = db.Column(db.Integer, db.ForeignKey('Libros.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('Usuarios.id'), nullable=False)
    fecha_prestamo = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_limite = db.Column(db.DateTime, nullable=False)
    fecha_devolucion = db.Column(db.DateTime, nullable=True)
    estado = db.Column(db.String(20), default='activo')

    def to_dict(self):
        return{
            "id": self.id,
            "cliente_id": self.cliente_id,
            "libro_id": self.libro_id,
            "usuario_id": self.usuario_id,
            "fecha_prestamo": self.fecha_prestamo,
            "fecha_limite": self.fecha_limite,
            "fecha_devolucion": self.fecha_devolucion,
            "estado": self.estado,
        }


