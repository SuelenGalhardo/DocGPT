import os

class Config:
    """Configuración base para el proyecto."""
    BASE_DIR = os.path.abspath(os.getcwd())  # Directorio base del proyecto
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'app', 'uploads')  # Carpeta para guardar archivos subidos
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Tamaño máximo de archivo permitido (16 MB)

class DevelopmentConfig(Config):
    """Configuración para el entorno de desarrollo."""
    DEBUG = True

class ProductionConfig(Config):
    """Configuración para el entorno de producción."""
    DEBUG = False
