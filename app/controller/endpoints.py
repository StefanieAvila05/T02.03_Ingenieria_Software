from fastapi import APIRouter, HTTPException, Path
from app.service.business_logic import ClinicaService

router = APIRouter()

@router.get(
    "/api/citas/{cedula}",
    summary="Consultar citas médicas por cédula"
)
def get_citas_por_cedula(
    cedula: str = Path(..., description="Número de cédula de 10 dígitos del paciente a consultar", example="0999999999")
):
    # Llama a tu lógica de negocio (que ya tiene cobertura al 100%)
    resultado = ClinicaService.consultar_agenda_externa(cedula)
    
    # Si la lógica detecta un problema, lanza el código HTTP correspondiente en tiempo real
    if "error" in resultado:
        if "ERROR_VALIDACION" in resultado["error"] or "ERROR_SEGURIDAD" in resultado["error"]:
            raise HTTPException(status_code=400, detail=resultado["error"])
        if "ERROR_PERSISTENCIA" in resultado["error"]:
            raise HTTPException(status_code=404, detail=resultado["error"])
            
    # Si todo está correcto, retorna el JSON limpio
    return resultado