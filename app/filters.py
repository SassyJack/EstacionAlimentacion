from __future__ import annotations

from datetime import datetime
from typing import Any

from markupsafe import Markup, escape


def truncate_words(value: Any, words: int = 20) -> str:
    if not isinstance(value, str):
        value = str(value)
    tokens = value.split()
    if len(tokens) <= words:
        return value
    truncated = " ".join(tokens[:words])
    return f"{truncated}…"


def format_date(value: Any, date_format: str = "%d/%m/%Y") -> str:
    if isinstance(value, datetime):
        return value.strftime(date_format)
    return str(value)


def linebreaks(value: Any) -> Markup:
    if not isinstance(value, str):
        value = str(value)
    paragraphs = [escape(block.strip()) for block in value.split("\n") if block.strip()]
    html = "".join(f"<p>{paragraph}</p>" for paragraph in paragraphs)
    return Markup(html or "")


def register_filters(app):
    app.jinja_env.filters["truncate_words"] = truncate_words
    app.jinja_env.filters["format_date"] = format_date
    app.jinja_env.filters["linebreaks"] = linebreaks

