from datetime import datetime
from typing import Dict, List, Optional


def _build_dashboard(
    dashboard_id: int,
    title: str,
    description: str,
    embed_url: str,
    updated_at: datetime,
) -> Dict:
    return {
        "id": dashboard_id,
        "title": title,
        "description": description,
        "embed_url": embed_url,
        "updated_at": updated_at,
    }


_DASHBOARDS: List[Dict] = [
    _build_dashboard(
        dashboard_id=1,
        title="Ventas por Región",
        description=(
            "Reporte de Power BI para analizar las ventas por región, canal de "
            "distribución y categoría de producto."
        ),
        embed_url="https://app.powerbi.com/view?r=example-dashboard-1",
        updated_at=datetime(2024, 6, 15, 10, 0, 0),
    ),
    _build_dashboard(
        dashboard_id=2,
        title="Inventario en Tiempo Real",
        description=(
            "Supervisa los niveles de inventario en bodegas y centros de "
            "distribución con alertas tempranas de ruptura de stock."
        ),
        embed_url="https://app.powerbi.com/view?r=example-dashboard-2",
        updated_at=datetime(2024, 7, 3, 9, 30, 0),
    ),
]


def get_dashboards() -> List[Dict]:
    return list(_DASHBOARDS)


def get_dashboard(dashboard_id: int) -> Optional[Dict]:
    return next((item for item in _DASHBOARDS if item["id"] == dashboard_id), None)

