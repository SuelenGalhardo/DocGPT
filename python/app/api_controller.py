# src/api_controller.py

from app.ai_processor import AIProcessor

class APIController:
    def __init__(self):
        self.processor = AIProcessor()

    def handleRequest(self, request):
        action = request.get("action")
        text = request.get("text")
        if not text:
            raise ValueError("El texto no puede estar vacío")

        if action == "translate":
            target_language = request.get("target_language")
            return {"translation": self.processor.translate(text, target_language)}
        elif action == "summarize":
            return {"summary": self.processor.summarize(text)}
        elif action == "modify":
            modifications = request.get("modifications")
            return {"modified_text": self.processor.modify(text, modifications)}
        else:
            raise ValueError("Acción no válida")
