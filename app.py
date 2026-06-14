from flask import Flask, jsonify, render_template, request

from backend.config import Settings
from backend.content import LANDING
from backend.leads import LeadValidationError, create_lead, lead_to_whatsapp_url


WHATSAPP_NUMBER = "56900000000"
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

    @app.get("/api/health")
    def health():
        return jsonify({"status": "ok"})

    @app.get("/api/landing")
    def landing_content():
        return jsonify(landing)

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
