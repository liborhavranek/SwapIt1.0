"""
Module Name: test_base_template.py
Author: Made with love by Libor Raven
Date: 05.10.2024
"""
import unittest

from flask import Flask
from flask.testing import FlaskClient
from app import create_app


class BaseBlueprintTestCase(unittest.TestCase):
    """Testy pro base template."""

    def setUp(self) -> None:
        """Nastavení testovacího prostředí před každým testem."""
        self.app: Flask = create_app()
        self.app.config['TESTING'] = True
        self.client: FlaskClient = self.app.test_client()

    def test_base_template_have_title_swap(self) -> None:
        """Test, zda route `/` má správný title."""
        response = self.client.get('/')
        self.assertIn(b'<title>SwapIt</title>', response.data)


if __name__ == '__main__':    # pragma: no cover
    unittest.main()
