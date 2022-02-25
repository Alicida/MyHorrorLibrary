from apiflask import APIFlask
from api.project.models import db, Autor, Editorial, Libro, User
from api.project.blueprints import abc_autores, abc_editoriales, abc_libros
from api.project.auth.blueprints import auth_bp
from sqlalchemy import engine, inspect

def create_app():
    '''Función principal de la aplicación'''
    # Crear el objeto app
    app = APIFlask(__name__)
    
    # Obtener la configuración de la aplicación a partir de settings.py
    app.config.from_pyfile("settings.py")
    
    # Se incializa la conexión entre SQLALchemy y la base de datos
    db.init_app(app) 
    
    @app.before_first_request
    def crea_bases():
        '''Función encargada de verificar que exista una base de datos  con
           las tablas de autores, de editoriales, de libros y de usuarios pobladas correctamente. 
            En caso de no existir, es creada'''

        # Verifica que exista la tabla autor en la base de datos
        inspector = inspect(db.engine)
        if not inspector.has_table('autor'):
            # Crea y llena la base de autor.
            db.create_all()
            with open(app.config['PATH'] + "/../data/autores.txt", "rt") as f:
                autores = eval(f.read())
                for autor in autores:
                    if Autor.query.filter_by(id=autor["id"]).first():
                        continue
                    else:
                        db.session.add(Autor(**autor))
                db.session.commit()
        
            # Llena la base de editorial.
            with open(app.config['PATH'] + "/../data/editoriales.txt", "rt") as f:
                editoriales = eval(f.read())
                for editorial in editoriales:
                    if Editorial.query.filter_by(id=editorial["id"]).first():
                        continue
                    else:
                        db.session.add(Editorial(**editorial))
                db.session.commit()

            # Llena la base de libro.
            with open(app.config['PATH'] + "/../data/libros.txt", "rt") as f:
                libros = eval(f.read())
                for libro in libros:
                    if Libro.query.filter_by(id=libro["id"]).first():
                        continue
                    else:
                        db.session.add(Libro(**libro))
                db.session.commit()
                
        # Verifica que exista el usuario admin y lo crea si no es así 
        if not User.query.filter_by(username="admin").first():
            user = User(username='admin',
                        email='example@example.com',
                        password='admin', 
                        active=True)
            db.session.add(user)
            db.session.commit()
                
    # Registra los blueprints con los endpoints
    app.register_blueprint(abc_autores, url_prefix='/api/autor')
    app.register_blueprint(abc_editoriales, url_prefix='/api/editorial')
    app.register_blueprint(abc_libros, url_prefix='/api/libro')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    #Regresa la aplicación
    return app