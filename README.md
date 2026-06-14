# Danny Website

Landing page para DVJ Danny, enfocada en presentar servicios de DVJ, visuales en vivo y edicion audiovisual para eventos en Iquique.

## URL publica

Produccion en Vercel:

https://danny-website-pi.vercel.app

## Vista previa

![DVJ Danny en cabina](public/media/dvj-danny.jpeg)

![Hero visual del sitio](public/img/hero-dj-iquique.png)

## Tecnologias

- Python 3
- Flask 3
- Jinja templates
- CSS responsive sin framework pesado
- Endpoints JSON para contenido, salud del servicio y contacto
- Vercel para despliegue serverless

## Estructura

```text
backend/              Logica de contenido, configuracion, leads y OpenAPI
public/               CSS e imagenes publicas
templates/            Vistas Jinja
tests/                Pruebas unitarias
app.py                Aplicacion Flask
vercel.json           Configuracion de Vercel
requirements.txt      Dependencias Python
```

## Configuracion

El repositorio no incluye datos privados ni credenciales. El numero real de WhatsApp debe configurarse como variable de entorno:

| Variable | Requerida | Descripcion |
| --- | --- | --- |
| `WHATSAPP_NUMBER` | Si en produccion | Numero usado para generar enlaces `wa.me`, sin `+`, espacios ni guiones. |
| `LEAD_STORAGE_PATH` | No | Ruta local para guardar contactos en JSONL. Por defecto: `instance/contact_leads.jsonl`. |

Si `WHATSAPP_NUMBER` no esta definido, la app usa `56900000000` como valor de ejemplo para desarrollo.

## Ejecutar localmente

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:WHATSAPP_NUMBER = "569XXXXXXXX"
python app.py
```

Luego abre:

```text
http://127.0.0.1:5000
```

## Endpoints

- `GET /api/health`: estado del servicio.
- `GET /api/landing`: contenido principal de la landing.
- `POST /api/contact`: recibe una solicitud de contacto y devuelve un enlace de WhatsApp.
- `GET /api/openapi.json`: especificacion OpenAPI.
- `GET /api/docs`: documentacion interactiva con Swagger UI.

## Pruebas

```powershell
python -m unittest discover
```

## Despliegue

El proyecto esta preparado para Vercel. Para publicar desde GitHub:

1. Subir este repositorio a GitHub.
2. Importarlo en Vercel como proyecto nuevo.
3. Configurar `WHATSAPP_NUMBER` en `Project > Settings > Environment Variables`.
4. Desplegar la rama principal.

La carpeta `.vercel/`, entornos virtuales, caches y archivos de leads locales estan ignorados por Git para evitar subir datos internos o personales.
