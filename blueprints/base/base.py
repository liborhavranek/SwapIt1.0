"""
Module Name: base.py
Author: Made with love by Libor Raven
Date: 05.10.2024
"""
from flask import Blueprint, Response

base_bp = Blueprint('base', __name__)


@base_bp.route('/')
def home() -> Response:
    """Základní route, která vrací zprávu Welcome."""
    return Response("Welcome", status=200, mimetype="text/plain")
