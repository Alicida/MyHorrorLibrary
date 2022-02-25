from apiflask import APIBlueprint, abort, output, input
from api.project.auth import login_required
from api.project.models import db, Autor, Editorial, Libro
from api.project.schemas import AutorSchema, AutorInSchema, EditorialSchema, EditorialInSchema, LibroSchema, LibroInSchema
from marshmallow.exceptions import ValidationError

abc_autores = APIBlueprint('abc_autor', __name__)

@abc_autores.get("/")
@output(AutorSchema(many=True))
def vuelca_base():
    return Autor.query.all()

@abc_autores.get("/<int:id>")
@output(AutorSchema)
def despliega_autor(id):
    return Autor.query.get_or_404(id)

@abc_autores.delete("/<int:id>")
@output(AutorSchema)
@login_required
def elimina_autor(id):
    autor = Autor.query.get_or_404(id)
    db.session.delete(autor)
    db.session.commit()
    return autor
    
@abc_autores.post("/<int:id>")
@output(AutorSchema)
@input(AutorInSchema)
@login_required
def crea_autor(id, data):
    if Autor.query.filter_by(id=id).first():
        abort(409)
    else: 
        data["id"] = id
        try:
            autor = Autor(**AutorSchema().load(data))
        except ValidationError:
            return abort(400)
        db.session.add(autor)
        db.session.commit()
        return autor

@abc_autores.put("/<int:id>")
@output(AutorSchema)
@input(AutorInSchema)
@login_required
def sustituye_autor(id, data):
    autor = Autor.query.get_or_404(id)
    db.session.delete(autor)
    data["id"] = id
    nuevo_autor = Autor(**data)
    db.session.add(nuevo_autor)
    db.session.commit()
    return nuevo_autor

abc_editoriales = APIBlueprint('abc_editorial', __name__)

@abc_editoriales.get("/")
@output(EditorialSchema(many=True))
def vuelca_base():
    return Editorial.query.all()

@abc_editoriales.get("/<int:id>")
@output(EditorialSchema)
def despliega_editorial(id):
    return Editorial.query.get_or_404(id)

@abc_editoriales.delete("/<int:id>")
@output(EditorialSchema)
@login_required
def elimina_editorial(id):
    editorial = Editorial.query.get_or_404(id)
    db.session.delete(editorial)
    db.session.commit()
    return editorial
    
@abc_editoriales.post("/<int:id>")
@output(EditorialSchema)
@input(EditorialInSchema)
@login_required
def crea_editorial(id, data):
    if Editorial.query.filter_by(id=id).first():
        abort(409)
    else: 
        data["id"] = id
        try:
            editorial = Editorial(**EditorialSchema().load(data))
        except ValidationError:
            return abort(400)
        db.session.add(editorial)
        db.session.commit()
        return editorial

@abc_editoriales.put("/<int:id>")
@output(EditorialSchema)
@input(EditorialInSchema)
@login_required
def sustituye_editorial(id, data):
    editorial = Editorial.query.get_or_404(id)
    db.session.delete(editorial)
    data["id"] = id
    nueva_editorial = Editorial(**data)
    db.session.add(nueva_editorial)
    db.session.commit()
    return nueva_editorial

abc_libros = APIBlueprint('abc_libro', __name__)

@abc_libros.get("/")
@output(LibroSchema(many=True))
def vuelca_base():
    return Libro.query.all()

@abc_libros.get("/<int:id>")
@output(LibroSchema)
def despliega_libro(id):
    return Libro.query.get_or_404(id)

@abc_libros.delete("/<int:id>")
@output(LibroSchema)
@login_required
def elimina_libro(id):
    libro = Libro.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()
    return libro
    
@abc_libros.post("/<int:id>")
@output(LibroSchema)
@input(LibroInSchema)
@login_required
def crea_libro(id, data):
    if Libro.query.filter_by(id=id).first():
        abort(409)
    else: 
        data["id"] = id
        try:
            libro = Libro(**LibroSchema().load(data))
        except ValidationError:
            return abort(400)
        db.session.add(libro)
        db.session.commit()
        return libro

@abc_libros.put("/<int:id>")
@output(LibroSchema)
@input(LibroInSchema)
@login_required
def sustituye_libro(id, data):
    libro = Libro.query.get_or_404(id)
    db.session.delete(libro)
    data["id"] = id
    nuevo_libro = Libro(**data)
    db.session.add(nuevo_libro)
    db.session.commit()
    return nuevo_libro