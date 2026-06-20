from app.repository.data_store import ClinicaRepository

# Capa encargada de aislar las reglas operativas del negocio
class ClinicaService:
    @staticmethod
    def consultar_agenda_externa(cedula: str):
        # Regla de negocio / Validación primaria
        if not cedula or len(cedula) < 10:
            return {"error": "Cédula inválida o incompleta"}
        
        paciente = ClinicaRepository.obtener_paciente_por_cedula(cedula)
        if not paciente:
            return {"error": "Paciente no registrado en el sistema"}
        
        citas = ClinicaRepository.buscar_citas_por_paciente(paciente.id_paciente)
        return {
            "paciente": paciente.nombre,
            "cedula": paciente.cedula,
            "citas_agendadas": citas
        }