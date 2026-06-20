from app.model.entities import Paciente, Cita
from datetime import datetime

# Mock de datos simulando tablas de base de datos
BD_PACIENTES = [
    {"id_paciente": 1, "cedula": "0999999999", "nombre": "Stefanie Avila"}
]

BD_CITAS = [
    {"id_cita": 101, "fecha_hora": datetime(2026, 7, 20, 10, 0), "estado": "Pendiente", "id_paciente": 1}
]

class ClinicaRepository:

    """
    Componente de acceso a datos (Data Access Object - DAO).
    Responsable de encapsular las operaciones de lectura y filtrado 
    sobre el almacenamiento en memoria de las entidades Paciente y Cita.
    """

    @staticmethod

    # Busqueda por clave candidata o AK
    def obtener_paciente_por_cedula(cedula: str):
        """
        Busca un registro de paciente utilizando la cédula como clave candidata.
        Retorna una instancia de la entidad Paciente o None si no se encuentra.
        """

        for p in BD_PACIENTES:
            if p["cedula"] == cedula:
                return Paciente(**p)
        return None

    @staticmethod

    # Retorna coleccion de objetos tipo Cita
    def buscar_citas_por_paciente(id_paciente: int):
        """
        Recupera la colección de citas médicas vinculadas a un ID específico de paciente.
        Simula una consulta de clave foránea con relación Uno a Muchos (1:N).
        """
        return [Cita(**c) for c in BD_CITAS if c["id_paciente"] == id_paciente]