# tests/test_chat.py
import pytest
from app.chat_interface import ChatInterface

def testSendMessageConTextoValido():
    chat = ChatInterface()
    response = chat.sendMessage("Hola, IA")
    assert response != ""

def testSendMessageConTextoVacio():
    chat = ChatInterface()
    with pytest.raises(ValueError):
        chat.sendMessage("")
