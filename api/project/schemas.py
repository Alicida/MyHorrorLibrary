from api.project.models import Autor, Editorial, Libro
from apiflask.validators import Length, Range
from apiflask.fields import String, Integer
from apiflask import Schema, fields

class AutorSchema(Schema):
    id = Integer(required=True, validate=Range(min=1000000, max=9999999))
    nombre = String(required=True, validate=Length(min=2, max=50))
    apellido = String(required=True, validate=Length(min=2, max=50))
    libros = fields.Pluck("LibroSchema", "nombre", many=True)

class AutorInSchema(Schema):
    nombre = String(required=True, validate=Length(min=2, max=50))
    apellido = String(required=True, validate=Length(min=2, max=50))
    libros = fields.Pluck("LibroSchema", "nombre", many=True)

class EditorialSchema(Schema):
    id = Integer(required=True, validate=Range(min=1000000, max=9999999))
    nombre = String(required=True, validate=Length(min=2, max=50))
    libros = fields.Pluck("LibroSchema", "nombre", many=True)

class EditorialInSchema(Schema):
    class Meta:
        model = Editorial
        include_relationships = True
        load_instance = True
    nombre = String(required=True, validate=Length(min=2, max=50))
    libros = fields.Pluck("LibroSchema", "nombre", many=True)

class LibroSchema(Schema):
    id = Integer(required=True, validate=Range(min=1000000, max=9999999))
    nombre = String(required=True, validate=Length(min=2, max=250))
    comentario = String(required=False, validate=Length(min=2, max=500), load_default=None)
    autor = fields.Nested(AutorSchema(exclude=("libros",)))
    autor_id = Integer(required=True, validate=Range(min=1000000, max=9999999))
    editorial = fields.Nested(EditorialSchema(exclude=("libros",)))
    editorial_id = Integer(required=True, validate=Range(min=1000000, max=9999999))

class LibroInSchema(Schema):
    nombre = String(required=True, validate=Length(min=2, max=250))
    comentario = String(required=False, validate=Length(min=2, max=500), load_default=None)
    autor = fields.Nested(AutorSchema(exclude=("libros",)))
    autor_id = Integer(required=True, validate=Range(min=1000000, max=9999999))
    editorial = fields.Nested(EditorialSchema(exclude=("libros",)))
    editorial_id = Integer(required=True, validate=Range(min=1000000, max=9999999))