from flask import Flask
from .routes import main
from .models import init_db

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.register_blueprint(main)
    init_db(app)
    return app