DocGPT Backend - Documentación Inicial
Introducción
El proyecto DocGPT Backend está diseñado para proporcionar un backend impulsado por IA que permita a los usuarios interactuar con documentos a través de funcionalidades como traducción, resúmenes y modificaciones. Este documento detalla el inicio del desarrollo siguiendo un enfoque TDD (Desarrollo Guiado por Pruebas).

---

Preparación del Entorno

1. Crear un entorno virtual
   Un entorno virtual en Python aísla las dependencias del proyecto:
   o Crear el entorno:
   bash
   Copy code
   python -m venv venv
   o Activar el entorno:
    Linux/Mac:
   bash
   Copy code
   source venv/bin/activate
    Windows:
   bash
   Copy code
   .\venv\Scripts\activate
2. Instalar las dependencias necesarias
   Para ejecutar pruebas unitarias, utiliza pytest:
   bash
   Copy code
   pip install pytest
3. Guardar dependencias
   Registra las dependencias instaladas en un archivo requirements.txt:
   bash
   Copy code
   pip freeze > requirements.txt

---

Estructura Inicial del Proyecto
El proyecto sigue una estructura modular para garantizar escalabilidad y claridad:
plaintext
Copy code
docgpt-backend/
├── src/ # Código fuente principal
│ ├── **init**.py
│ ├── chat_interface.py # Lógica relacionada con la interfaz de chat
│ ├── document_manager.py # Gestión de documentos
│ ├── ai_processor.py # Procesamiento de IA
│ ├── api_controller.py # Controlador de la API
├── tests/ # Pruebas unitarias
│ ├── **init**.py
│ ├── test_chat_interface.py # Pruebas de ChatInterface
│ ├── test_document_manager.py
│ ├── test_ai_processor.py
│ ├── test_api_controller.py
├── requirements.txt # Dependencias del proyecto
└── README.md # Documentación del proyecto

---

Caso de Prueba Inicial
Descripción
El caso de prueba testSendMessageConTextoValido verifica que el método send_message de la clase ChatInterface devuelva una respuesta válida cuando se proporciona un texto de entrada.
Detalles del Caso de Prueba
• Nombre: test_send_message_con_texto_valido
• Clase probada: ChatInterface
• Entrada: Texto válido ("Hola, IA")
• Salida esperada: Un string no vacío.
Código del Caso de Prueba
Archivo: tests/test_chat_interface.py
python
Copy code
import pytest
from src.chat_interface import ChatInterface

def test_send_message_con_texto_valido(): # Precondiciones
chat = ChatInterface()

    # Datos de entrada
    texto = "Hola, IA"

    # Ejecución
    respuesta = chat.send_message(texto)

    # Validación
    assert isinstance(respuesta, str), "La respuesta debe ser un string"
    assert len(respuesta) > 0, "La respuesta no debe estar vacía"

---

Ejecución de las Pruebas

1. Asegúrate de estar en el entorno virtual y en la carpeta raíz del proyecto.
2. Ejecuta las pruebas unitarias con el siguiente comando:
   bash
   Copy code
   pytest
3. El resultado esperado para el caso de prueba inicial es un mensaje indicando que el test ha pasado:
   plaintext
   Copy code
   =================== test session starts ===================
   ...
   tests/test_chat_interface.py .. [100%]
   =================== 1 passed in 0.03s ====================


pip install pytest

pytest
pip install Flask-Testing
pip install pytest-cov
pip freeze > genera una lista de todas las bibliotecas instaladas actualmente en tu entorno virtual
pip install ollama
pip install pytest-cov
pip install requests



# DocGPT

DocGPT es una herramienta diseñada para llevar capacidades de IA a documentos privados. La aplicación permite a los usuarios cargar documentos y realizar tareas como traducciones, resúmenes y modificaciones.

## Requisitos

- Python 3.13
- Flask
- pytest

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. Crear y activar el ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En macOS/Linux
   .\venv\Scripts\activate   # En Windows
   ```

3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

1. Ejecutar la aplicación Flask:
   ```bash
   python src/app.py
   ```

2. Ejecutar las pruebas:
   ```bash
   pytest tests/
   ```

## Estructura del Proyecto

project/ ├── venv/ ├── src/ │ ├── init.py │ ├── app.py │ ├── chat_interface.py │ ├── document_manager.py │ ├── ai_processor.py │ └── api_controller.py └── tests/ ├── init.py ├── test_chat_interface.py ├── test_document_manager.py ├── test_ai_processor.py └── test_api_controller.py

## Contribuir

1. Hacer un fork del proyecto.
2. Crear una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realizar los cambios necesarios y hacer commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Hacer push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Crear un nuevo Pull Request.


