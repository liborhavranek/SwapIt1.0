# tests/test_app.py
import unittest
from app import create_app


class TestAppConfig(unittest.TestCase):
    """Test základní konfigurace aplikace."""

    def setUp(self):
        """Nastavení testovacího prostředí před každým testem."""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_app_exists(self):
        """Test ověřující, zda je aplikace správně vytvořena."""
        self.assertIsNotNone(self.app)

    def test_app_is_testing(self):
        """Test, zda je aplikace ve správném testovacím režimu."""
        self.assertTrue(self.app.config['TESTING'])


if __name__ == '__main__':
    unittest.main()
