from flask import Flask, jsonify, render_template, request

from backend.config import Settings
from backend.content import LANDING
from backend.leads import LeadValidationError, create_lead, lead_to_whatsapp_url
from backend.openapi import OPENAPI_SPEC


WHATSAPP_NUMBER = "56953021437"
WHATSAPP_MESSAGE = (
    "Hola Danny, quiero cotizar un evento. "
    "Fecha: ___ / Lugar: ___ / Tipo de evento: ___"
)


def create_app(settings: Settings | None = None) -> Flask:
    settings = settings or Settings.from_env()
    app = Flask(__name__, static_folder="public", static_url_path="")

    landing = {
        **LANDING,
        "whatsapp_url": (
            "https://wa.me/"
            + settings.whatsapp_number
            + "?text="
            + WHATSAPP_MESSAGE.replace(" ", "%20")
        ),
    }

    @app.route("/")
    def home():
        return render_template("index.html", landing=landing)

    @app.get("/servicios")
    def servicios_page():
        return render_template("section_page.html", landing=landing, page="servicios")

    @app.get("/paquetes")
    def paquetes_page():
        return render_template("section_page.html", landing=landing, page="paquetes")

    @app.get("/proceso")
    def proceso_page():
        return render_template("section_page.html", landing=landing, page="proceso")

    @app.get("/contacto")
    def contacto_page():
        return render_template("section_page.html", landing=landing, page="contacto")

    @app.get("/api/health")
    def health():
        return jsonify({"status": "ok"})

    @app.get("/api/landing")
    def landing_content():
        return jsonify(landing)

    @app.get("/api/openapi.json")
    def openapi_json():
        return jsonify(OPENAPI_SPEC)

    @app.get("/api/docs")
    def swagger_docs():
        return """
        <!doctype html>
        <html lang="es">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>DVJ Danny API Docs</title>
            <link
              rel="stylesheet"
              href="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css"
            >
          </head>
          <body>
            <div id="swagger-ui"></div>
            <script src="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
            <script>
              window.ui = SwaggerUIBundle({
                url: "/api/openapi.json",
                dom_id: "#swagger-ui"
              });
            </script>
          </body>
        </html>
        """

    @app.post("/api/contact")
    def contact():
        try:
            lead = create_lead(request.get_json(silent=True) or {}, settings)
        except LeadValidationError as exc:
            return jsonify({"error": str(exc)}), 400

        return jsonify(
            {
                "lead": lead.public_dict(),
                "whatsapp_url": lead_to_whatsapp_url(lead, settings),
            }
        ), 201

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
