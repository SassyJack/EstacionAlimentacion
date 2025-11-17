from flask import Blueprint, abort, render_template

from .content import power_bi_features, project_sections, power_bi_dashboards

bp = Blueprint("pages", __name__, url_prefix="/")


@bp.get("/proyecto")
def project_overview():
    return render_template("project/overview.html", sections=project_sections)


@bp.get("/power-bi")
def power_bi():
    return render_template("project/power_bi.html", info=power_bi_features, dashboards=power_bi_dashboards)


@bp.get("/power-bi/<slug>")
def power_bi_detail(slug: str):
    dashboard = next((d for d in power_bi_dashboards if d["slug"] == slug), None)
    if dashboard is None:
        abort(404)
    return render_template("project/power_bi_detail.html", dashboard=dashboard)


pages_bp = bp

