from flask import Flask
from flask_migrate import Migrate
from .src.models.product import configuration as config
from .src.serializer import configuration as serializer_config
from .src.routes import create_api as api


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/products.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    config(app)
    # Responsavel por Serializar os dados do banco
    serializer_config(app)
    # Cria as Rotas
    api(app)

    Migrate(app, app.db)

    return app
