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
        self.assertEqual(response.get_json()["artist"], "DVJ Danny")

    def test_navbar_pages_load(self):
        for path in ["/servicios", "/paquetes", "/proceso", "/contacto"]:
            with self.subTest(path=path):
                response = self.client.get(path)

                self.assertEqual(response.status_code, 200)
                self.assertIn("DVJ Danny", response.get_data(as_text=True))

    def test_default_whatsapp_links_use_real_number(self):
        client = create_app(
            Settings(
                whatsapp_number="56953021437",
                lead_storage_path=Path(self.temp_dir.name) / "default-leads.jsonl",
            )
        ).test_client()

        response = client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("https://wa.me/56953021437", response.get_data(as_text=True))

    def test_tiktok_profile_appears_on_contact_surfaces(self):
        for path in ["/", "/contacto"]:
            with self.subTest(path=path):
                response = self.client.get(path)
                html = response.get_data(as_text=True)

                self.assertEqual(response.status_code, 200)
                self.assertIn("dvj._dannyiqq", html)
                self.assertIn("https://www.tiktok.com/@dvj._dannyiqq", html)

    def test_openapi_spec_documents_backend_routes(self):
        response = self.client.get("/api/openapi.json")
        spec = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(spec["openapi"], "3.0.3")
        self.assertIn("/api/health", spec["paths"])
        self.assertIn("/api/landing", spec["paths"])
        self.assertIn("/api/contact", spec["paths"])

    def test_swagger_ui_page_loads(self):
        response = self.client.get("/api/docs")
        html = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("SwaggerUIBundle", html)
        self.assertIn("/api/openapi.json", html)

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
                "message": "Necesito DVJ para un matrimonio.",
                "event_type": "Matrimonio",
                "services": ["DVJ", "Resumen audiovisual"],
            },
        )

        body = response.get_json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(body["lead"]["name"], "Cliente Demo")
        self.assertIn("https://wa.me/56911111111", body["whatsapp_url"])


if __name__ == "__main__":
    unittest.main()
