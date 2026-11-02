from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import os


db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()


def create_app():

    app_dir = os.path.abspath(os.path.dirname(__file__))

    app = Flask(__name__,
        template_folder=os.path.join(app_dir, "templates"),
        static_folder=os.path.join(app_dir, "static")
    )

    app.config.from_object("config.Config")

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    from app import models # faz com que as classes de app/models/__init__.py sejam carregadas e reconhecidas pelo SQLAlchemy.

    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        # Temporário: Retorna None já que não temos o banco de dados de usuários ainda
        return None

    from .routes.main import main
    app.register_blueprint(main)

    from .routes.produtos import produtos
    app.register_blueprint(produtos)

    

    return app


