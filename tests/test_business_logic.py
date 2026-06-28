import pytest
from app.service.business_logic import ClinicaService

# Suite de pruebas unitarias para la capa de servicio (Logica de Negocio)
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

def test_consultar_agenda_paciente_no_registrado():
    """Prueba el comportamiento cuando la cédula es estructuralmente válida pero no existe"""
    resultado = ClinicaService.consultar_agenda_externa("9999999999")
    assert "error" in resultado
    assert "ERROR_PERSISTENCIA" in resultado["error"]

def test_consultar_agenda_exitoso():
    """Prueba el flujo correcto de consulta de un paciente existente"""
    # Usamos la cédula mockeada que devuelve datos en el repositorio
    resultado = ClinicaService.consultar_agenda_externa("0999999999")
    assert "error" not in resultado
    assert "paciente" in resultado
    assert "citas_agendadas" in resultado