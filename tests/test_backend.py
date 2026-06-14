from pathlib import Path
import tempfile
import unittest

from app import create_app
from backend.config import Settings


class BackendTestCase(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        settings = Settings(
            whatsapp_number="56911111111",
            lead_storage_path=Path(self.temp_dir.name) / "leads.jsonl",
        )
        self.client = create_app(settings).test_client()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_health_endpoint(self):
        response = self.client.get("/api/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "ok")

    def test_landing_endpoint(self):
        response = self.client.get("/api/landing")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["artist"], "Danny DJ")

    def test_contact_requires_name_contact_and_message(self):
        response = self.client.post("/api/contact", json={"name": "Danny"})

        self.assertEqual(response.status_code, 400)
        self.assertIn("contacto", response.get_json()["error"])

    def test_contact_saves_lead_and_returns_whatsapp_url(self):
        response = self.client.post(
            "/api/contact",
            json={
                "name": "Cliente Demo",
                "contact": "+56 9 1234 5678",
                "message": "Necesito DJ para un matrimonio.",
                "event_type": "Matrimonio",
                "services": ["DJ", "Aftermovie"],
            },
        )

        body = response.get_json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(body["lead"]["name"], "Cliente Demo")
        self.assertIn("https://wa.me/56911111111", body["whatsapp_url"])


if __name__ == "__main__":
    unittest.main()
