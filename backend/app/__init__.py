from flask import Flask
from .db import init_db
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

def create_app():

    app = Flask(__name__)
    CORS(app)

    init_db(app)


    from . import usuario_bp

    app.register_blueprint(usuario_bp.usuario_bp)

    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config = {
            'app_name': 'Sport Club Challenges'
        }
    )

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


    @app.route('/')
    def inicio():
        return 'Hola Mundo'

    return app



