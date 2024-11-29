import pytest
from app.api_controller import APIController

def testHandleRequestConDatosValidos():
    controller = APIController()
    request_data = {"action": "translate", "text": "Hello", "target_language": "es"}
    response = controller.handleRequest(request_data)
    assert response == {"translation": "Hola"}

# tests/test_api_controller.py

def testHandleRequestConDatosInvalidos():
    controller = APIController()
    request_data = {"action": "translate", "text": ""}
    with pytest.raises(ValueError, match="El texto no puede estar vacío"):
        controller.handleRequest(request_data)


        