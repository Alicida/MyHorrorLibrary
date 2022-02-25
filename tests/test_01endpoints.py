import pytest
from app import create_app
from api.project.models import db, Autor, Editorial, Libro
from api.project.schemas import AutorSchema, EditorialSchema, LibroSchema
from flask import Request

app = create_app()

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.init_app(app)
        yield client


def test_get_autores(client):
    r = client.get('/api/autor')
    print(r)
    assert r.status == '200 OK'
    data = r.get_json()
    assert type(data) is list
    for autor in data:
        AutorSchema().load(data=autor)

def test_get_editoriales(client):
    r = client.get('/api/editorial')
    assert r.status == '200 OK'
    data = r.get_json()
    assert type(data) is list
    for editorial in data:
        EditorialSchema().load(data=editorial)

def test_get_libros(client):
    r = client.get('/api/libro')
    assert r.status == '200 OK'
    data = r.get_json()
    assert type(data) is list
    for libro in data:
        LibroSchema().load(data=libro)