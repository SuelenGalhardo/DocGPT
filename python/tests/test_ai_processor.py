# tests/test_ai_processor.py
import pytest
from app.ai_processor import AIProcessor

def testTranslateConTextoValido():
    processor = AIProcessor()
    translation = processor.translate("Hello", "es")
    assert translation == "Hola"

def testTranslateConTextoVacio():
    processor = AIProcessor()
    with pytest.raises(ValueError, match="El texto no puede estar vacío"):
        processor.translate("", "es")



def test_interact_with_llama():
    processor = AIProcessor()
    input_text = "¿Cómo estás?"
    
    # Llamamos al método interact_with_llama
    response = processor.interact_with_llama(input_text)
    
    # Verificamos que la respuesta no esté vacía
    assert response != "", "La respuesta del modelo está vacía"
    
    # Imprimir la respuesta para verificar visualmente
    print("Respuesta del modelo:", response)

# Ejecutar la prueba
if __name__ == "__main__":
    test_interact_with_llama()
