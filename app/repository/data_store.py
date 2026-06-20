from app.model.entities import Paciente, Cita
from datetime import datetime

# Mock de datos simulando tablas de base de datos
BD_PACIENTES = [
    {"id_paciente": 1, "cedula": "0999999999", "nombre": "Stefanie Avila"}
]

BD_CITAS = [
    {"id_cita": 101, "fecha_hora": datetime(2026, 6, 15, 10, 0), "estado": "Pendiente", "id_paciente": 1}
]

class ClinicaRepository:
    @staticmethod

    # Busqueda por clave candidata o AK
    def obtener_paciente_por_cedula(cedula: str):
        for p in BD_PACIENTES:
            if p["cedula"] == cedula:
                return Paciente(**p)
        return None

    @staticmethod

    # Retorna coleccion de objetos tipo Cita
    def buscar_citas_por_paciente(id_paciente: int):
        return [Cita(**c) for c in BD_CITAS if c["id_paciente"] == id_paciente]