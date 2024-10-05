"""
Module Name: test_app.py
Author: Made with love by Libor Raven
Date: 05.10.2024
"""
import unittest
from app import create_app


class TestAppConfig(unittest.TestCase):
    """Test základní konfigurace aplikace."""

    def setUp(self) -> None:
        """Nastavení testovacího prostředí před každým testem."""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_app_exists(self) -> None:
        """Test ověřující, zda je aplikace správně vytvořena."""
        self.assertIsNotNone(self.app)

    def test_app_is_testing(self) -> None:
        """Test, zda je aplikace ve správném testovacím režimu."""
        self.assertTrue(self.app.config['TESTING'])

    def test_base_blueprint_registered(self) -> None:
        """Test, zda je base blueprint správně zaregistrován v aplikaci."""
        self.assertIn('base', self.app.blueprints)
        self.assertEqual(self.app.blueprints['base'].name, 'base')


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
