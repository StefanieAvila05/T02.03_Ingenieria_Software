from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Entidad que representa al paciente
class Paciente(BaseModel):
    id_paciente: int
    cedula: str
    nombre: str

# Validacion de estructura de datos
class Cita(BaseModel):
    id_cita: int
    fecha_hora: datetime
    estado: str  # Pendiente, Atendida, Cancelada
    id_paciente: int