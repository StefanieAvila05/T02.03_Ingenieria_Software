from app.repository.data_store import ClinicaRepository

# Capa encargada de aislar las reglas operativas del negocio
class ClinicaService:
    @staticmethod
    def consultar_agenda_externa(cedula: str):
        # Control de longitud mínima según estándar nacional (10 dígitos)
        if not cedula or len(cedula) < 10:
            return {"error": "ERROR_VALIDACION: LA CEDULA INGRESADA ES INVALIDA O ESTA INCOMPLETA"}
        
        if not cedula.isdigit(): 
            return {"error": "ERROR_SEGURIDAD: LA CEDULA DEBE CONTENER UNICAMENTE CARACTERES NUMERICOS"}
        
        paciente = ClinicaRepository.obtener_paciente_por_cedula(cedula)
        if not paciente:
            return {"error": "ERROR_PERSISTENCIA: EL PACIENTE NO SE ENCUENTRA REGISTRADO EN EL SISTEMA"}
        
        citas = ClinicaRepository.buscar_citas_por_paciente(paciente.id_paciente)
        return {
            "paciente": paciente.nombre,
            "cedula": paciente.cedula,
            "citas_agendadas": citas
        }