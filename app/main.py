from fastapi import FastAPI
from app.controller import endpoints

app = FastAPI(
    title="Sistema de Gestión Clínica - Grupo 02",
    description="Implementación de servicios REST obligatorios para la Tarea T02.03 - Arquitectura MS-RC",
    version="1.0.0"
)

# Registro de rutas del controlador
app.include_router(endpoints.router)

@app.get("/", tags=["Raíz"])
def read_root():
    return {"status": "Servicio backend activo", "documentacion": "/docs"}