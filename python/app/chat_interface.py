# app/chat.py
class ChatInterface:
    def sendMessage(self, text: str) -> str:
        if not text:
            raise ValueError("El texto no puede estar vacío.")
        # Aquí agregamos la lógica para enviar el mensaje a la IA
        return "Respuesta de IA"
