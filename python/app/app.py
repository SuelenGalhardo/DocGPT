from flask import Flask
from flask_cors import CORS
from config import DevelopmentConfig
from api_routes import api_routes  # Importa el Blueprint directamente si ya está configurado

def create_app():
    """Crea y configura la aplicación Flask."""
    app = Flask(__name__)

    # Configuración del proyecto
    app.config.from_object(DevelopmentConfig)

    # Habilitar CORS para permitir solicitudes desde cualquier origen
    CORS(app)

    # Registrar el Blueprint con todas las rutas
    app.register_blueprint(api_routes, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
