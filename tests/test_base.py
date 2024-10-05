"""
Module Name: test_base.py
Author: Made with love by Libor Raven
Date: 05.10.2024
"""
import unittest
from flask import Flask
from flask.testing import FlaskClient
from app import create_app


class BaseBlueprintTestCase(unittest.TestCase):
    """Testy pro base blueprint."""

    def setUp(self) -> None:
        """Nastavení testovacího prostředí před každým testem."""
        self.app: Flask = create_app()
        self.app.config['TESTING'] = True
        self.client: FlaskClient = self.app.test_client()

    def test_app_exists(self) -> None:
        """Test ověřující, zda je aplikace správně vytvořena."""
        self.assertIsNotNone(self.app)

    def test_app_is_testing(self) -> None:
        """Test, zda je aplikace ve správném testovacím režimu."""
        self.assertTrue(self.app.config['TESTING'])

    def test_base_home_route(self) -> None:
        """Test, zda route `/` vrací správnou odpověď."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_base_route_have_welcome_text(self) -> None:
        """Test, zda route `/` vrací správnou odpověď."""
        response = self.client.get('/')
        self.assertEqual(response.data.decode('utf-8'), "Welcome")

    def test_base_base_route_have_mimetype(self) -> None:
        """Test, zda base blueprint route `/` vrací správnou odpověď."""
        response = self.client.get('/')
        self.assertEqual(response.mimetype, "text/plain")


if __name__ == '__main__':    # pragma: no cover
    unittest.main()
