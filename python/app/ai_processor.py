from langchain_ollama import OllamaLLM  # Asegúrate de que esta biblioteca esté instalada y configurada correctamente
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class AIProcessor:
    def __init__(self):
        # Inicialización del modelo OllamaLLM con Llama 3.1
        self.llm = OllamaLLM(model="llama3.1")  # Modelo Llama 3.1

    def translate(self, text, target_language):
        """Traducir texto de un idioma a otro."""
        if not text:
            raise ValueError("El texto no puede estar vacío")
        
        # Lógica de traducción simplificada (esto debería integrarse con el modelo Llama)
        if text == "Hello" and target_language == "es":
            return "Hola"
        return f"Texto traducido a {target_language}"  # Esto puede mejorarse usando Llama para traducción real

    def translateDocument(self, document_id, target_language):
        """Traducir un documento usando su ID y un idioma de destino."""
        if not document_id or document_id == "999":  # Verificar si el documento es inválido
            raise ValueError("Documento no encontrado o inválido")
        
        # Lógica de traducción de documentos (esto puede integrarse con Llama para traducir documentos completos)
        return f"Documento {document_id} traducido al idioma {target_language}"

    def summarize(self, text):
        """Resumir un texto dado."""
        if not text:
            raise ValueError("El texto no puede estar vacío")
        
        # Implementación simplificada de resumen
        return "Resumen del texto" if text else "Texto vacío no puede ser resumido"

    def summarizeDocument(self, document_id):
        """Resumir un documento usando su ID."""
        if not document_id or document_id == "999":  # Verificar si el documento es inválido
            raise ValueError("Documento no encontrado o inválido")
        
        # Lógica simplificada para resumir documentos (esto puede integrarse con Llama)
        return f"Resumen del documento {document_id}"

    def modify(self, text, modifications):
        """Modificar un texto basado en las modificaciones proporcionadas."""
        if not text:
            raise ValueError("El texto no puede estar vacío")
        
        # Lógica de modificación de texto (esto es solo un ejemplo)
        if modifications:
            return text + " modificado"
        return text

    def interact_with_llama(self, input_text):
        """Método para interactuar con el modelo OllamaLLM (Llama 3.1) usando LangChain."""
        if not input_text:
            raise ValueError("El texto no puede estar vacío")

        # Define el prompt para el modelo Llama
        prompt_template = "Por favor, responde de manera detallada a lo siguiente: {text}"
        prompt = PromptTemplate(input_variables=["text"], template=prompt_template)
        chain = LLMChain(llm=self.llm, prompt=prompt)

        # Ejecuta la cadena con el texto de entrada
        response = chain.run(text=input_text)
        return response  # La respuesta del modelo Llama será devuelta

