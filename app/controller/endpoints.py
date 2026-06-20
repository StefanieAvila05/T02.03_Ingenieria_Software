from fastapi import APIRouter, HTTPException
from app.service.business_logic import ClinicaService

# Definicion de enrutadores publicos de la API

router = APIRouter(prefix="/api/citas", tags=["Módulo Citas Externas"])

@router.get("/{cedula}")
def get_citas_por_cedula(cedula: str):
    resultado = ClinicaService.consultar_agenda_externa(cedula)
    if "error" in resultado:
        raise HTTPException(status_code=404, detail=resultado["error"])
    return resultado