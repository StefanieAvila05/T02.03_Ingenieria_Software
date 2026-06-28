import pytest
from fastapi.testclient import TestClient
from app.main import app

cliente = TestClient(app)

def test_endpoint_raiz():
    """Prueba que la ruta base responda exitosamente"""
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200
    assert respuesta.json() == {"status": "Servicio Backend Operativo con éxito"}