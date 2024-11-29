from flask import Flask

def create_app():
    app = Flask(__name__)

    # Aquí puedes importar las rutas
    from . import routes

    # Registra las rutas en la app
    app.register_blueprint(routes.bp)

    return app
