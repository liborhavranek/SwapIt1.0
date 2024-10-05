"""
Module Name: base.py
Author: Made with love by Libor Raven
Date: 05.10.2024
"""
from flask import Blueprint, render_template
from flask.typing import ResponseReturnValue
from flask.views import MethodView

base_bp = Blueprint('base', __name__)


class HomeView(MethodView):
    """Class-based view pro základní route."""

    def get(self) -> ResponseReturnValue:
        """GET request pro zobrazení úvodní zprávy."""
        return render_template("base.html")


base_bp.add_url_rule('/', view_func=HomeView.as_view('home'))
