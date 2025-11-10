# Data Warehouse Project (Flask)

Aplicación web en Flask para mostrar dashboards embebidos de Power BI y documentar la metodología del proyecto de data warehouse.

## Estructura

- `app/`: Código de la aplicación Flask.
  - `dashboards/`: Blueprint con rutas y datos de ejemplo de dashboards.
  - `methodology/`: Blueprint con rutas y datos de ejemplo de metodología.
  - `pages/`: Rutas informativas que resumen el proyecto y plan de integración con Power BI.
  - `filters.py`: Filtros personalizados reutilizados en las plantillas.
- `templates/`: Plantillas Jinja reutilizadas por toda la aplicación.
- `static/`: Recursos estáticos (CSS, JS, imágenes).
- `run.py`: Punto de entrada para ejecutar el servidor de desarrollo.
- `config.py`: Configuración base de la app.

## Puesta en marcha

1. Crear y activar un entorno virtual (opcional pero recomendado).
2. Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3. (Opcional) Definir variables en `.env`, por ejemplo `SECRET_KEY`.
4. Ejecutar el servidor de desarrollo:
    ```bash
    flask --app run:app --debug run
    ```
    También puedes ejecutar directamente con Python:
    ```bash
    python run.py
    ```

La aplicación quedará disponible en `http://127.0.0.1:5000/`.

## Personalización

- Sustituye los datos de ejemplo ubicados en `app/dashboards/data.py` y `app/methodology/data.py` por información real o conecta una base de datos.
- Ajusta estilos en `static/css/style.css` y scripts en `static/js/main.js`.
- Actualiza el contenido narrativo en `app/pages/content.py` si deseas adaptar la descripción del proyecto o detallar el tablero de Power BI.
- Agrega nuevos blueprints o templates según sea necesario para extender la funcionalidad.