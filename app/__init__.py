from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../instance/mensagens.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from .routes import mensagens_bp
    app.register_blueprint(mensagens_bp)

    with app.app_context():
        from .models import Mensagem
        db.create_all()

    return app
