from flask import Blueprint, render_template

from .content import power_bi_features, project_sections

bp = Blueprint("pages", __name__, url_prefix="/")


@bp.get("/proyecto")
def project_overview():
    return render_template("project/overview.html", sections=project_sections)


@bp.get("/power-bi")
def power_bi():
    return render_template("project/power_bi.html", info=power_bi_features)


pages_bp = bp

