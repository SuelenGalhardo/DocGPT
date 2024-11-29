import os

class DocumentManager:
    def __init__(self, upload_folder: str):
        self.upload_folder = upload_folder

        # Crear la carpeta si no existe
        if not os.path.exists(self.upload_folder):
            os.makedirs(self.upload_folder)

    def uploadDocument(self, file) -> str:
        """Valida y guarda un archivo subido."""
        if not file:
            raise ValueError("El archivo no puede estar vacío.")

        # Validar la extensión del archivo
        if not file.filename.endswith('.txt'):
            raise ValueError("El archivo debe ser un archivo .txt")

        # Leer contenido del archivo
        file_content = file.read().decode('utf-8')
        if len(file_content) > 1000:
            raise ValueError("El archivo es demasiado grande")

        # Generar una ruta para guardar el archivo
        file_path = os.path.join(self.upload_folder, file.filename)
        file.seek(0)  # Restablecer el puntero del archivo
        file.save(file_path)

        return file.filename  # Devolver el nombre del archivo
