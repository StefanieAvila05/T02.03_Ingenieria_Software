import pytest
from app.service.business_logic import ClinicaService

def test_consultar_agenda_cedula_invalida_o_corta():
    """Prueba que el sistema rechace cédulas menores a 10 dígitos"""
    resultado = ClinicaService.consultar_agenda_externa("12345")
    assert "error" in resultado
    assert "ERROR_VALIDACION" in resultado["error"]

def test_consultar_agenda_cedula_no_numerica():
    """Prueba que el sistema detecte y rechace caracteres no numéricos"""
    resultado = ClinicaService.consultar_agenda_externa("09a65a4d56")
    assert "error" in resultado
    assert "ERROR_SEGURIDAD" in resultado["error"]