import pytest
from fastapi.testclient import TestClient
from app.main import app

# Suite de pruebas automatizadas para la capa de controladores (Endpoints)
cliente = TestClient(app)

def test_endpoint_raiz():
    """Prueba que la ruta base responda exitosamente"""
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200
    assert respuesta.json() == {"status": "Servicio Backend Operativo con éxito"}

def test_endpoint_citas_exitoso():
    """Prueba la respuesta HTTP 200 al consultar un paciente existente"""
    respuesta = cliente.get("/api/citas/0999999999")
    assert respuesta.status_code == 200
    assert "paciente" in respuesta.json()

def test_endpoint_citas_no_encontrado():
    """Prueba la respuesta HTTP 404 cuando la cedula no existe"""
    respuesta = cliente.get("/api/citas/9999999999")
    assert respuesta.status_code == 404