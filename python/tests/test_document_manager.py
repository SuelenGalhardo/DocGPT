import pytest
from app.document_manager import DocumentManager
from app.ai_processor import AIProcessor

# Pruebas para el DocumentManager
def testUploadDocumentConArchivoValido():
    manager = DocumentManager()
    document_id = manager.uploadDocument("documento.txt")
    assert document_id != ""

def testUploadDocumentConArchivoInvalido():
    manager = DocumentManager()
    with pytest.raises(ValueError):
        manager.uploadDocument("")  # Debe lanzar ValueError por archivo vacío

def testUploadDocumentConArchivoGrande():
    # Simulamos un archivo grande (más de 1000 caracteres)
    manager = DocumentManager()
    document_id = manager.uploadDocument("archivo_grande.txt")
    assert document_id != ""

def testUploadDocumentConArchivoNoTxt():
    manager = DocumentManager()
    with pytest.raises(ValueError):
        manager.uploadDocument("documento.pdf")  # Solo se permiten archivos .txt

# Pruebas para la API de traducción de documentos
def testTranslateDocumentConDocumentoValido():
    processor = AIProcessor()
    result = processor.translateDocument("123", "es")  # ID válido
    assert result == "Documento 123 traducido al idioma es"

def testTranslateDocumentConDocumentoInvalido():
    processor = AIProcessor()
    with pytest.raises(ValueError, match="Documento no encontrado o inválido"):
        processor.translateDocument("999", "es")  # ID inválido

def testTranslateDocumentConDocumentoVacio():
    processor = AIProcessor()
    with pytest.raises(ValueError, match="Documento no encontrado o inválido"):
        processor.translateDocument("", "es")  # ID vacío

# Pruebas para la API de resumen de documentos
def testSummarizeDocumentConDocumentoValido():
    processor = AIProcessor()
    result = processor.summarizeDocument("123")  # ID válido
    assert result == "Resumen del documento 123"

def testSummarizeDocumentConDocumentoInvalido():
    processor = AIProcessor()
    with pytest.raises(ValueError, match="Documento no encontrado o inválido"):
        processor.summarizeDocument("999")  # ID inválido

def testSummarizeDocumentConDocumentoVacio():
    processor = AIProcessor()
    with pytest.raises(ValueError, match="Documento no encontrado o inválido"):
        processor.summarizeDocument("")  # ID vacío
