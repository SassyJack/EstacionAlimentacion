from flask import Blueprint, abort, render_template

from .data import get_step_by_slug, get_steps

bp = Blueprint("methodology", __name__, url_prefix="/methodology")


@bp.get("/")
def methodology_index():
    steps = get_steps()
    return render_template("methodology/index.html", steps=steps, page_title="Metodología")


@bp.get("/<string:slug>")
def methodology_step(slug: str):
    step = get_step_by_slug(slug)
    if step is None:
        abort(404)
    return render_template("methodology/step.html", step=step)

