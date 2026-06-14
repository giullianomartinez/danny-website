# Publicacion - DVJ Danny

Este documento define como desplegar el proyecto segun el planning: una landing
Flask para DVJ Danny, con herramientas gratuitas o planes sin costo, recursos locales y
conversion principal hacia WhatsApp.

## Proyecto incluido

- **Sitio DVJ Danny**: sitio Flask con plantilla Jinja, CSS responsive, recursos
  locales, endpoints JSON y llamado principal a WhatsApp.

## Estrategia recomendada

La opcion recomendada es desplegar en **Vercel** usando el repositorio en GitHub.
El proyecto ya incluye `vercel.json`, `requirements.txt` y el objeto Flask `app`
en `app.py`, por lo que puede publicarse sin build custom.

Esta ruta calza con el planning porque:

- Usa una alternativa gratuita o un plan sin costo.
- No requiere servicios pagos, CDNs pagos ni plantillas premium.
- Permite publicar rapido una URL publica para validar conversion.
- Automatiza nuevas publicaciones con cada `git push`.

## Ambientes

### Local

Uso: desarrollo, reemplazo de contenido provisional y pruebas funcionales.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

URL local:

```text
http://127.0.0.1:5000
```

Validaciones locales:

```powershell
python -m unittest discover
```

### Preview

Uso: revisar cambios antes de publicarlos como version final.

En Vercel, cada envio a una rama distinta de la principal puede generar una
vista previa. Debe usarse para revisar:

- Hero, textos y CTA en desktop y movil.
- Numero de WhatsApp configurado.
- Carga correcta de imagenes locales.
- Respuestas de `/api/health` y `/api/landing`.
- Formulario o endpoint `/api/contact`, si se mantiene activo.

### Produccion

Uso: URL publica para campanas, redes sociales y contacto con clientes.

La rama principal del repositorio debe representar la version lista para
produccion. Cada `git push` a esa rama publicara una nueva version en Vercel.

## Variables de entorno

Configurar en Vercel desde:

```text
Project > Settings > Environment Variables
```

Variables:

| Variable | Requerida | Ejemplo | Uso |
| --- | --- | --- | --- |
| `WHATSAPP_NUMBER` | Si | `569XXXXXXXX` | Numero real usado para generar enlaces `wa.me`. |
| `LEAD_STORAGE_PATH` | No en Vercel | `instance/contact_leads.jsonl` | Ruta local para guardar leads en JSONL. |

Nota: en local, si `WHATSAPP_NUMBER` no existe, se usa `56900000000` como numero de ejemplo.

## Pasos de despliegue en Vercel

1. Crear o usar una cuenta gratuita en GitHub.
2. Subir el proyecto completo a un repositorio.
3. Crear o usar una cuenta en Vercel.
4. En Vercel, ir a **Add New... > Project**.
5. Importar el repositorio desde GitHub.
6. Configurar el proyecto:
   - Configuracion de framework: `Other` o el valor detectado automaticamente.
   - Root Directory: `./`
   - Build Command: vacio.
   - Output Directory: vacio.
   - Install Command: automatico o vacio.
7. Agregar `WHATSAPP_NUMBER` con el numero real.
8. Ejecutar la publicacion.
9. Abrir la URL publica y completar la checklist de verificacion.

## Alternativa con Vercel CLI

```powershell
npm i -g vercel
vercel login
vercel
vercel --prod
```

Para probar localmente con el entorno de Vercel:

```powershell
vercel dev
```

## Alternativas gratuitas o planes sin costo

Si Vercel no se usa, las alternativas compatibles con el planning son:

- **Render**: apropiado para Flask y servicios web simples. Revisar limites del
  plan sin costo antes de publicar.
- **PythonAnywhere**: opcion simple para apps Python pequenas. Revisar limites de
  trafico y dominios.
- **Fly.io**: util si se quiere mas control del runtime. Revisar creditos y
  limites vigentes.

En cualquiera de estas opciones se deben mantener las mismas restricciones:

- No depender de servicios pagos.
- Mantener recursos dentro del proyecto.
- Configurar `WHATSAPP_NUMBER` como variable de entorno.
- Probar desktop, movil y CTA de WhatsApp antes de compartir la URL.

## Consideracion sobre leads

El endpoint `POST /api/contact` guarda solicitudes en un archivo JSONL definido
por `LEAD_STORAGE_PATH`. Esto funciona bien en local, pero no debe considerarse
persistente en un entorno serverless como Vercel.

Para produccion hay dos rutas posibles:

1. Usar el sitio principalmente con CTA directo a WhatsApp, que es la opcion mas
   simple y alineada al planning.
2. Si se necesita guardar leads reales, conectar despues una base de datos o
   servicio gratuito compatible con el presupuesto del proyecto.

Mientras no exista almacenamiento persistente externo, WhatsApp debe ser la
fuente principal de contacto y seguimiento.

## Checklist previo a produccion

- El sitio corre localmente sin errores.
- `python -m unittest discover` pasa correctamente.
- El numero real esta configurado en `WHATSAPP_NUMBER`.
- Los textos provisionales fueron reemplazados por contenido real.
- Los paquetes, precios o rangos estan actualizados.
- Las imagenes reales estan optimizadas y dentro de `public/img`.
- Los CTA abren WhatsApp con un mensaje claro.
- La vista movil no presenta desbordes ni texto cortado.
- El titulo, descripcion y contenido incluyen referencias a DVJ en Iquique.
- La URL publica fue probada en al menos un telefono real.

## Relacion con las fases del planning

### Fase 1 - Base funcional

Publicacion local y prueba inicial en vista previa de Vercel.

### Fase 2 - Contenido real

Actualizar nombre artistico, telefono, precios, imagenes, videos y testimonios
antes de promover a produccion.

### Fase 3 - Conversion

Revisar CTA, mensajes prellenados y flujo hacia WhatsApp desde mobile.

### Fase 4 - SEO local

Publicar metadatos finales y textos optimizados para busquedas relacionadas con
DVJ, eventos, matrimonios, fiestas y marcas en Iquique.

### Fase 5 - Publicacion

Hacer la publicacion productiva, validar la URL publica, revisar responsive final y
compartir el enlace en redes o campanas.
