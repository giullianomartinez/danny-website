# DVJ Danny Website

Sitio web profesional para DVJ Danny, desarrollado como landing page de servicios para eventos, visuales en vivo y edicion audiovisual en Iquique, Chile.

El objetivo del proyecto es presentar la propuesta comercial de forma clara, facilitar la cotizacion por WhatsApp y dejar una base tecnica simple de mantener, desplegar y evolucionar.

## Sitio en produccion

https://danny-website-pi.vercel.app

## Vista previa

[![Vista previa del sitio DVJ Danny](public/img/site-preview.png)](https://danny-website-pi.vercel.app)

## Caracteristicas principales

- Landing page responsive orientada a conversion.
- Navegacion por secciones: servicios, paquetes, proceso y contacto.
- CTA principal hacia WhatsApp con mensaje prellenado.
- Contenido centralizado para facilitar ediciones futuras.
- Endpoints JSON para estado, contenido, contacto y documentacion OpenAPI.
- Configuracion preparada para despliegue en Vercel.

## Tecnologias

- Python 3
- Flask 3
- Jinja templates
- CSS responsive sin framework pesado
- OpenAPI / Swagger UI
- Vercel

## Estructura del proyecto

```text
backend/              Configuracion, contenido, leads y especificacion OpenAPI
public/               Hojas de estilo, imagenes y assets publicos
templates/            Vistas Jinja de la aplicacion
tests/                Pruebas unitarias del backend
app.py                Punto de entrada de Flask
requirements.txt      Dependencias Python
vercel.json           Configuracion de despliegue en Vercel
```

## Configuracion

El repositorio no incluye credenciales ni datos privados. El numero real de contacto debe configurarse mediante variables de entorno.

| Variable | Requerida | Descripcion |
| --- | --- | --- |
| `WHATSAPP_NUMBER` | Si, en produccion | Numero usado para generar enlaces de WhatsApp. Debe ir sin `+`, espacios ni guiones. |
| `LEAD_STORAGE_PATH` | No | Ruta local para guardar solicitudes recibidas en formato JSONL. |

Si `WHATSAPP_NUMBER` no esta definido, la app usa `56900000000` como valor de demostracion para desarrollo.

## Ejecucion local

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:WHATSAPP_NUMBER = "569XXXXXXXX"
python app.py
```

Abrir en el navegador:

```text
http://127.0.0.1:5000
```

## Endpoints disponibles

- `GET /api/health`: estado del servicio.
- `GET /api/landing`: contenido principal de la landing.
- `POST /api/contact`: recibe una solicitud y devuelve un enlace de WhatsApp.
- `GET /api/openapi.json`: especificacion OpenAPI.
- `GET /api/docs`: documentacion interactiva con Swagger UI.

## Pruebas

```powershell
python -m unittest discover
```

## Despliegue

El proyecto esta preparado para Vercel. El flujo recomendado es:

1. Mantener la rama `main` como version estable.
2. Configurar `WHATSAPP_NUMBER` en Vercel desde `Project > Settings > Environment Variables`.
3. Publicar cambios mediante `git push` al repositorio conectado.
4. Verificar la URL de produccion despues de cada despliegue.

## Estado

Primera version publica del sitio.
