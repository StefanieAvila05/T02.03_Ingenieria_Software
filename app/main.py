from fastapi import FastAPI
from app.controller.endpoints import router

app = FastAPI(
    title="Sistema de Gestión Clínica - API Backend",
    description="""
    ## Especificación de Servicios REST obligatorios para la Tarea T02.3.
    
    ### Alcance del Sistema:
    * **Módulo de Citas Externas**: Permite la consulta rápida de agendas médicas por medio del identificador nacional de identidad (Cédula).
    * **Arquitectura**: Implementación basada en el patrón de diseño de Arquitectura en Capas (MS-RC).
    """,
    version="1.0.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Soporte Técnico de Desarrollo - Ingeniería de Software",
        "url": "https://github.com/StefanieAvila05",
        "email": "stefanie.avila2005@outlook.es",
    }
)

app.include_router(router)

@app.get("/", tags=["Raíz"])
def read_root():
    return {"status": "Servicio Backend Operativo con éxito"}