from datetime import datetime
from pathlib import Path

from flask import Flask, render_template

from .dashboards import dashboards_bp
from .methodology import methodology_bp
from .filters import register_filters
from .pages import pages_bp


def create_app():
    """Crea y configura la aplicación Flask."""
    project_root = Path(__file__).resolve().parent.parent
    app = Flask(
        __name__,
        instance_relative_config=False,
        template_folder=str(project_root / "templates"),
        static_folder=str(project_root / "static"),
    )
    app.config.from_object("config.Config")

    register_filters(app)

    app.register_blueprint(pages_bp)
    app.register_blueprint(dashboards_bp)
    app.register_blueprint(methodology_bp)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.context_processor
    def inject_globals():
        return {"current_year": datetime.utcnow().year}

    return app

