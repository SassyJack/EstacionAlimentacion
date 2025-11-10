from __future__ import annotations

project_sections = [
    {
        "id": "problema",
        "title": "Definición del problema y ODS asociados",
        "excerpt": (
            "En Chía, Cundinamarca, muchas familias no pueden garantizar una "
            "alimentación equilibrada y puntual para sus mascotas. Las estaciones "
            "inteligentes distribuidas permiten automatizar la dispensación de alimento "
            "y monitorear el consumo en tiempo real."
        ),
        "body": [
            {
                "heading": "Contexto urbano",
                "content": (
                    "La propuesta contempla 10 estaciones distribuidas estratégicamente y "
                    "conectadas mediante IoT para garantizar un control sostenible del "
                    "alimento dispensado."
                ),
            },
            {
                "heading": "ODS relacionados",
                "content": (
                    "* **ODS 11** — Ciudades y comunidades sostenibles.\n"
                    "* **ODS 12** — Producción y consumo responsables.\n"
                    "* **ODS 15** — Vida de ecosistemas terrestres."
                ),
            },
        ],
    },
    {
        "id": "big-data",
        "title": "Justificación del uso de Big Data",
        "excerpt": (
            "Las estaciones inteligentes generan millones de lecturas que permiten "
            "analizar patrones de consumo y anticipar necesidades de mantenimiento."
        ),
        "body": [
            {
                "heading": "Beneficios clave",
                "content": (
                    "* Identificación de patrones por zona y franja horaria.\n"
                    "* Detección de anomalías como sobrealimentación o inactividad.\n"
                    "* Predicción de recargas y optimización de recursos."
                ),
            }
        ],
    },
    {
        "id": "dataset",
        "title": "Dataset y simulación de sensores",
        "excerpt": (
            "Se generó un dataset simulado de hasta 8 millones de registros con datos de "
            "sensores IoT y cámaras en las 10 estaciones de Chía."
        ),
        "body": [
            {
                "heading": "Variables recopiladas",
                "content": (
                    "* Identificador y ubicación de la estación.\n"
                    "* Fecha y hora de lectura.\n"
                    "* Cantidad de alimento dispensado.\n"
                    "* Temperatura ambiental, presencia detectada y nivel de energía."
                ),
            },
            {
                "heading": "Frecuencia y almacenamiento",
                "content": (
                    "Las lecturas se generan cada 5 segundos y se almacenan inicialmente en "
                    "SQL Server antes del proceso analítico."
                ),
            },
        ],
    },
    {
        "id": "etl",
        "title": "Procesamiento ETL y data warehouse",
        "excerpt": (
            "El pipeline ETL desarrollado con SQL Server Integration Services garantiza "
            "datos limpios, transformados y listos para análisis."
        ),
        "body": [
            {
                "heading": "Flujo ETL",
                "content": (
                    "* **Extracción:** lectura de datos crudos de sensores.\n"
                    "* **Transformación:** limpieza, normalización y control de valores atípicos.\n"
                    "* **Carga:** inserción en un data warehouse optimizado para consultas."
                ),
            }
        ],
    },
    {
        "id": "analitica",
        "title": "Analítica, técnicas y conclusiones",
        "excerpt": (
            "El proyecto combina modelos predictivos, análisis de correlación y dashboards en "
            "Power BI para apoyar decisiones basadas en evidencia."
        ),
        "body": [
            {
                "heading": "Técnicas aplicadas",
                "content": (
                    "* Modelos predictivos para anticipar recargas.\n"
                    "* Análisis de correlación entre temperatura y consumo.\n"
                    "* Monitoreo continuo de indicadores clave."
                ),
            },
            {
                "heading": "Recomendaciones",
                "content": (
                    "Ajustar el suministro según la demanda, programar horarios de dispensación, "
                    "priorizar mantenimientos y usar los datos como insumo para velar por el "
                    "bienestar animal."
                ),
            },
        ],
    },
]


power_bi_features = {
    "title": "Integración con Power BI",
    "summary": (
        "El data warehouse de SQL Server se conecta con Power BI para construir dashboards "
        "dinámicos que permitan monitorear las estaciones inteligentes y tomar decisiones "
        "en tiempo real."
    ),
    "capabilities": [
        "Conectividad directa al data warehouse con actualizaciones programadas.",
        "Dashboards interactivos para consumo de alimento, eficiencia energética y alertas.",
        "Distribución segura de reportes web y móviles para los responsables del proyecto.",
    ],
    "next_steps": [
        "Configurar las credenciales de acceso al data warehouse en el servicio de Power BI.",
        "Generar un reporte con gráficos de tendencias, mapas de estaciones y tarjetas KPI.",
        "Obtener el `embed_url` y `report_id` para integrarlos en la vista de tableros.",
    ],
    "placeholder": {
        "heading": "Espacio reservado para el tablero",
        "description": (
            "Cuando se genere el reporte en Power BI, incrusta aquí el iframe o utiliza el SDK "
            "de Microsoft para una integración autenticada."
        ),
    },
}

