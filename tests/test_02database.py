import pytest
from api import create_app
from api.project.models import Autor, Editorial, Libro, User, db
from api.project.schemas import AutorSchema, EditorialSchema, LibroSchema
from sqlalchemy import inspect

app = create_app()


@pytest.fixture
def base_conectada():
    print("Conectando a base de datos...")
    with app.app_context() as conectada:
        db.init_app(app)
        yield conectada


def test_existe_admin(base_conectada):
    print("Probando si existe el usuario 'admin...'")
    assert User.query.filter_by(username="admin").first()


# def test_existe_tabla_autores(base_conectada):
#     print('Probando que existan autores...')
#     assert Autor.query.all()
    
    
# def test_datos_correctos_autores(base_conectada):
#     print('Probando que los datos de los autores sean correctos..')
    
#     def object_as_dict(obj):
#         return {c.key: getattr(obj, c.key)
#             for c in inspect(obj).mapper.column_attrs}
    
#     for autor in Autor.query.all():
#         AutorSchema().load(data=object_as_dict(autor))


# def test_existe_tabla_editoriales(base_conectada):
#     print('Probando que existan editoriales...')
#     assert Editorial.query.all()
    
    
# def test_datos_correctos_editoriales(base_conectada):
#     print('Probando que los datos de los editoriales sean correctos..')
    
#     def object_as_dict(obj):
#         return {c.key: getattr(obj, c.key)
#             for c in inspect(obj).mapper.column_attrs}
    
#     for editorial in Editorial.query.all():
#         EditorialSchema().load(data=object_as_dict(editorial))


# def test_existe_tabla_libros(base_conectada):
#     print('Probando que existan libros...')
#     assert Editorial.query.all()
    
    
# def test_datos_correctos_libros(base_conectada):
#     print('Probando que los datos de los libros sean correctos..')
    
#     def object_as_dict(obj):
#         return {c.key: getattr(obj, c.key)
#             for c in inspect(obj).mapper.column_attrs}
    
#     for libro in Libro.query.all():
#         LibroSchema().load(data=object_as_dict(libro))