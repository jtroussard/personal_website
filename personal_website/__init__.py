from flask import Flask
from personal_website.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.__static_folder = "./static/"

    from personal_website.main.routes import main
    from personal_website.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
