from flask import Flask, render_template


app = Flask(__name__, static_folder="public", static_url_path="")


LANDING = {
    "artist": "Danny DJ",
    "location": "Iquique, Chile",
    "tagline": "Musica en vivo, visuales y edicion con trayectoria nortina.",
    "summary": (
        "Landing page para un DJ con anos de experiencia en eventos, fiestas, "
        "matrimonios, activaciones y produccion audiovisual en Iquique."
    ),
    "stats": [
        {"value": "+12", "label": "anos de trayectoria"},
        {"value": "+500", "label": "eventos musicalizados"},
        {"value": "4K", "label": "edicion y contenido social"},
    ],
    "services": [
        {
            "title": "DJ para eventos",
            "body": "Sesiones adaptadas al publico, lectura de pista, mezcla continua y sonido profesional para celebraciones privadas o corporativas.",
        },
        {
            "title": "Video y aftermovie",
            "body": "Edicion dinamica para reels, clips promocionales, resumen de eventos y contenido listo para redes sociales.",
        },
        {
            "title": "Visuales en vivo",
            "body": "Musica y video coordinados para elevar la energia del show con pantallas, loops, intros y recursos personalizados.",
        },
    ],
    "packages": [
        {
            "name": "Evento Esencial",
            "price": "Desde $180.000",
            "items": ["DJ set hasta 3 horas", "Playlist curada", "Coordinacion previa"],
        },
        {
            "name": "Full Party",
            "price": "Desde $320.000",
            "items": ["DJ set extendido", "Sonido e iluminacion base", "Registro audiovisual corto"],
        },
        {
            "name": "Pro Visual",
            "price": "A medida",
            "items": ["Visuales en vivo", "Aftermovie editado", "Contenido vertical para RRSS"],
        },
    ],
    "timeline": [
        "Brief del evento y estilo musical",
        "Propuesta de show, duracion y recursos",
        "Coordinacion tecnica con el lugar",
        "Presentacion en vivo y entrega de contenido",
    ],
    "testimonials": [
        {
            "quote": "Se noto la experiencia desde el primer minuto. La pista nunca bajo.",
            "author": "Evento privado, Iquique",
        },
        {
            "quote": "El video quedo rapido, moderno y perfecto para redes.",
            "author": "Marca local",
        },
    ],
}


@app.route("/")
def home():
    return render_template("index.html", landing=LANDING)


if __name__ == "__main__":
    app.run(debug=True)
