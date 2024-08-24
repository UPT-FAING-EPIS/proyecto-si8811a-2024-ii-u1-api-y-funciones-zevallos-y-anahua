from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Crear la instancia de SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Inicializar la base de datos
    db.init_app(app)

    # Registrar Blueprints
    from app.routes import event_routes_blueprint
    app.register_blueprint(event_routes_blueprint, url_prefix='/events')

    with app.app_context():
        db.create_all()  # Crear las tablas de la base de datos

    return app
