# Danny DJ Landing

Landing page en Python/Flask para un DJ y editor de video con trayectoria en Iquique.

## Stack

- Python 3
- Flask
- Jinja templates
- CSS responsive sin framework pesado
- Asset hero generado para el proyecto

## Herramientas gratis

No necesitas pagar por herramientas adicionales para trabajar este sitio fuera de Codex.

- Python: gratis y open source.
- Flask: gratis y open source.
- pip/venv: incluidos en el ecosistema gratuito de Python.
- Editor recomendado: VS Code o cualquier editor de texto gratis.
- Navegador: Chrome, Edge, Firefox o similar, gratis.
- WhatsApp link: el enlace `wa.me` es gratis; solo debes reemplazar el numero por el real.
- Deploy opcional: Render, PythonAnywhere o Fly.io tienen alternativas gratuitas o free tier, sujeto a sus limites vigentes.

El sitio no depende de servicios pagados, CDNs pagos, plantillas premium ni librerias comerciales.

## Ejecutar

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Luego abre `http://127.0.0.1:5000`.

## Deploy en Vercel

Esta app esta lista para Vercel como proyecto Flask. Vercel detecta `Flask`
en `requirements.txt` y usa el objeto `app` definido en `app.py`.

### Opcion recomendada: GitHub + Vercel

1. Sube este proyecto a un repositorio en GitHub.
2. Entra a [vercel.com](https://vercel.com) y crea una cuenta o inicia sesion.
3. Ve a **Add New... > Project**.
4. Importa el repositorio de GitHub.
5. En la pantalla de configuracion deja:
   - Framework Preset: **Other** o el valor detectado automaticamente.
   - Root Directory: `./`
   - Build Command: vacio.
   - Output Directory: vacio.
   - Install Command: vacio o automatico.
6. Haz clic en **Deploy**.

Cada vez que hagas `git push` a la rama principal, Vercel publicara una nueva
version automaticamente.

### Opcion alternativa: Vercel CLI

```powershell
npm i -g vercel
vercel login
vercel
vercel --prod
```

Si usas CLI, responde las preguntas de Vercel aceptando el directorio actual
como proyecto. Para pruebas locales con el entorno de Vercel puedes usar:

```powershell
vercel dev
```

## Planning

### Objetivo

Crear una landing que convierta visitas en contactos por WhatsApp para contratar servicios de DJ, visuales en vivo y edicion de video en Iquique.

### Audiencia

- Personas organizando matrimonios, cumpleanos, fiestas privadas y eventos corporativos.
- Marcas locales que necesitan musica, registro y contenido para redes.
- Productoras que buscan un perfil con experiencia y criterio audiovisual.

### Estructura de la landing

1. Hero con propuesta clara, ubicacion y CTA.
2. Indicadores de trayectoria para generar confianza.
3. Presentacion del perfil y valor diferencial.
4. Servicios: DJ, video/aftermovie y visuales en vivo.
5. Paquetes iniciales para facilitar la cotizacion.
6. Proceso de trabajo para reducir dudas.
7. Testimonios editables.
8. CTA final a WhatsApp.

### Siguiente iteracion

- Reemplazar nombre, telefono y precios por datos reales.
- Agregar videos o reels embebidos desde Instagram/YouTube.
- Conectar formulario o tracking de conversiones.
- Optimizar SEO local con palabras clave de Iquique y tipos de evento.
- Agregar galeria con fotos reales de eventos.
