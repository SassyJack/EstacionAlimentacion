from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class MethodologyStep:
    id: int
    title: str
    slug: str
    description: str
    content: str
    order: int
    image: Optional[str] = None


_STEPS: List[MethodologyStep] = [
    MethodologyStep(
        id=1,
        title="Descubrimiento",
        slug="descubrimiento",
        description=(
            "Recolección de requerimientos y análisis del estado actual "
            "para comprender los objetivos de negocio."
        ),
        content=(
            "Durante esta fase se realizan entrevistas con los actores clave, se "
            "identifican fuentes de datos y se delimita el alcance del proyecto.\n\n"
            "El resultado esperado es un listado priorizado de necesidades que guía "
            "las etapas posteriores."
        ),
        order=1,
        image="images/methodology/discovery.jpg",
    ),
    MethodologyStep(
        id=2,
        title="Modelado",
        slug="modelado",
        description=(
            "Diseño del modelo dimensional, definición de KPIs y establecimiento "
            "del gobierno de datos necesario."
        ),
        content=(
            "Se plantean las tablas de hechos y dimensiones, se definen reglas de "
            "negocio y se documentan los cálculos de indicadores clave.\n\n"
            "También se evalúan consideraciones de seguridad y se planifica la "
            "actualización de la información."
        ),
        order=2,
        image="images/methodology/modeling.jpg",
    ),
    MethodologyStep(
        id=3,
        title="Implementación",
        slug="implementacion",
        description=(
            "Construcción de pipelines, pruebas de calidad de datos y despliegue "
            "de dashboards a usuarios finales."
        ),
        content=(
            "En esta fase se automatiza la extracción y transformación de datos, "
            "se validan resultados con las áreas usuarias y se publican los "
            "dashboards.\n\n"
            "Se generan manuales de uso y se planifican capacitaciones para garantizar "
            "la adopción."
        ),
        order=3,
        image="images/methodology/implementation.jpg",
    ),
]


def get_steps() -> List[MethodologyStep]:
    return sorted(_STEPS, key=lambda step: (step.order, step.id))


def get_step_by_slug(slug: str) -> Optional[MethodologyStep]:
    return next((step for step in _STEPS if step.slug == slug), None)

