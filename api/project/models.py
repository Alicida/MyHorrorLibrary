from flask_sqlalchemy import SQLAlchemy
import virtualenv
from flask_user import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    username= db.Column(db.String(25), nullable=False, unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    authenticated = db.Column(db.Boolean())

class Autor(UserMixin, db.Model):
    __tablename__ = 'autor'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    libros = db.relationship('Libro', backref='autor.id', lazy=True)

class Editorial(UserMixin, db.Model):
    __tablename__ = 'editorial'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    libros = db.relationship('Libro', backref='editorial.id', lazy=True)

class Libro(UserMixin, db.Model):
    __tablename__ = 'libro'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    autor_id = db.Column(db.Integer, db.ForeignKey('autor.id'),nullable=False)
    autor = db.relationship('Autor',backref=db.backref('autor', lazy=True),viewonly=True)
    editorial_id = db.Column(db.Integer, db.ForeignKey('editorial.id'),nullable=False)
    editorial = db.relationship('Editorial',backref=db.backref('libro.id', lazy=True),viewonly=True)
    comentario = db.Column(db.String(500))
