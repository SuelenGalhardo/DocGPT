from flask import Blueprint, request, jsonify
from document_manager import DocumentManager
from ai_processor import AIProcessor
import os

# Crear el Blueprint global
api_routes = Blueprint('api_routes', __name__)

# Instancia global de AIProcessor
ai_processor = AIProcessor()

# Rutas generales
@api_routes.route('/chat', methods=['POST'])
def chat():
    """Ruta para interactuar con el modelo de chat."""
    try:
        text = request.json.get('text', '')
        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Procesar la solicitud con AIProcessor
        response = ai_processor.interact_with_llama(text)
        return jsonify({"response": response}), 200

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500


@api_routes.route('/translate', methods=['POST'])
def translate():
    """Ruta para traducir un texto."""
    try:
        text = request.json.get('text', '')
        target_language = request.json.get('target_language', 'es')

        if not text:
            return jsonify({"error": "No text provided"}), 400

        translation = ai_processor.interact_with_llama(
            f"Translate the following text to {target_language}: {text}"
        )
        return jsonify({"translation": translation}), 200

    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500


@api_routes.route('/summarize', methods=['POST'])
def summarize():
    """Ruta para resumir un texto."""
    try:
        text = request.json.get('text', '')

        if not text:
            return jsonify({"error": "No text provided"}), 400

        summary = ai_processor.summarize(text)
        return jsonify({"summary": summary}), 200

    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500


@api_routes.route('/modify', methods=['POST'])
def modify():
    """Ruta para modificar un texto."""
    try:
        text = request.json.get('text', '')
        modifications = request.json.get('modifications', {})

        if not text:
            return jsonify({"error": "No text provided"}), 400

        modified_text = ai_processor.modify(text, modifications)
        return jsonify({"modified_text": modified_text}), 200

    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500


# Ruta específica para subir y traducir archivos
@api_routes.route('/upload_and_translate', methods=['POST'])
def upload_and_translate():
    """Sube un archivo, valida su contenido y tradúcelo."""
    try:
        # Directorio donde se guardan los archivos
        upload_folder = os.path.join(os.getcwd(), 'uploads')
        document_manager = DocumentManager(upload_folder)

        if 'file' not in request.files:
            return jsonify({"error": "No file found in request"}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400

        # Guardar el archivo usando DocumentManager
        document_id = document_manager.uploadDocument(file)

        # Leer contenido del archivo
        file_path = os.path.join(document_manager.upload_folder, document_id)
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()

        # Obtener el idioma de destino
        target_language = request.form.get('target_language', 'es')

        # Traducir el contenido usando AIProcessor
        translation = ai_processor.interact_with_llama(
            f"Translate the following text to {target_language}: {file_content}"
        )

        return jsonify({
            "message": "Archivo traducido correctamente.",
            "translation": translation,
            "file_path": file_path
        }), 200

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500
