from flask import Flask
from .db import init_db
from flask_cors import CORS

def create_app():

    app = Flask(__name__)
    CORS(app)

    init_db(app)


    from . import usuario_bp

    app.register_blueprint(usuario_bp.usuario_bp)


    @app.route('/')
    def inicio():
        return 'Hola Mundo'

    return app



