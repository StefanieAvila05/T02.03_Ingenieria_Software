# T02.3 - Ingeniería de Software - Grupo 05 (Desarrollo Individual)
Nombre: Stefanie Avila J.
Grupo:2
Materia: Ingenieria de Software

## 1. Requerimientos Funcionales Asociados (T02.01)
* **RF-10 (Consulta Externa de Citas):** El sistema debe permitir la consulta de citas programadas mediante el número de cédula del paciente a través de un endpoint seguro.
* **RF-17 (Automatización Contable):** Registro automático de transacciones en el Libro Diario al procesar comprobantes.

## 2. Arquitectura y Diseño (T02.02)
El sistema implementa una arquitectura limpia distribuida en 4 capas estrictas:
* **Modelo:** Definición de entidades de negocio mediante esquemas Pydantic.
* **Repositorio:** Abstracción y acceso a los almacenes de datos.
* **Servicio:** Centralización de las reglas de negocio y validaciones del sistema.
* **Controlador:** Exposición de endpoints REST e interacción HTTP.

## 3. Matriz de Tareas y Seguimiento Operativo
Para alcanzar el volumen de desarrollo exigido y la métrica de control de cambios, las actividades se organizaron de la siguiente manera:
* **Tarea 01:** Configuración base del entorno, inicialización del framework y dependencias.
* **Tarea 02:** Modelado de entidades del negocio (`entities.py`).
* **Tarea 03:** Simulación de persistencia y capa de datos (`data_store.py`).
* **Tarea 04:** Lógica de validación operativa y servicios (`business_logic.py`).
* **Tarea 05:** Publicación de endpoints REST y enrutadores (`endpoints.py`).
* **Tarea 06:** Pruebas unitarias de endpoints, manejo de excepciones HTTP y documentación en Swagger.