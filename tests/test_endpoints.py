import pytest
from fastapi.testclient import TestClient
from app.main import app

# Suite de pruebas automatizadas para la capa de controladores (Endpoints)
cliente = TestClient(app)

def test_endpoint_raiz():
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200

def test_endpoint_citas_exitoso():
    respuesta = cliente.get("/api/citas/0999999999")
    assert respuesta.status_code == 200

def test_endpoint_citas_no_encontrado_404():
    """Prueba el error 404 cuando la cédula no existe en la base de datos"""
    respuesta = cliente.get("/api/citas/9999999999")
    assert respuesta.status_code == 404

def test_endpoint_citas_invalida_400():
    """Prueba el error 400 cuando la cédula tiene letras o es inválida"""
    respuesta = cliente.get("/api/citas/09a65a4d56")
    assert respuesta.status_code == 400