from flask import Blueprint, abort, render_template

from .data import get_dashboard, get_dashboards

bp = Blueprint("dashboards", __name__, url_prefix="/dashboards")


@bp.get("/")
def list_dashboards():
    dashboards = get_dashboards()
    return render_template("dashboards/list.html", dashboards=dashboards)


@bp.get("/<int:dashboard_id>")
def dashboard_detail(dashboard_id: int):
    dashboard = get_dashboard(dashboard_id)
    if dashboard is None:
        abort(404)
    return render_template("dashboards/powerbi.html", dashboard=dashboard)

