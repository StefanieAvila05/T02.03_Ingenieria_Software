from fastapi import APIRouter, HTTPException, status
from app.service.business_logic import ClinicaService

router = APIRouter(prefix="/api/citas", tags=["Módulo Citas Externas"])

@router.get("/{cedula}")
def get_citas_por_cedula(cedula: str):
    # Invocación de la lógica de negocio central
    resultado = ClinicaService.consultar_agenda_externa(cedula)
    
    # Manejo explícito de excepciones utilizando códigos estandarizados REST
    if "error" in resultado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=resultado["error"]
        )
        
    return resultado