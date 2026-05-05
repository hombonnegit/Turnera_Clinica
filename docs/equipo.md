# Equipo y responsabilidades

## Homero (Líder)
- Definición de la arquitectura general del sistema.
- Creación del proyecto Django y estructura de aplicaciones.
- Coordinación de revisiones de código (Code Review).
- Despliegue final en plataforma en la nube (Railway / Render).
- Archivos clave:
  - `clinica/settings.py`
  - `clinica/urls.py`
  - `manage.py`
  - `requirements.txt`
  - `.gitignore`

## Carlos (Backend)
- Diseño de todos los modelos principales.
- Lógica de negocio de turnos: disponibilidad, validaciones y reglas.
- Reportes y estadísticas.
- Signals y tareas automáticas (por ejemplo, liberación de turnos por no-show).
- Seguridad y permisos por rol.
- Archivos clave:
  - `core/models.py`
  - `core/admin.py`
  - `core/signals.py`
  - `pacientes/views.py`
  - `clinica/settings.py`

## Juan (Frontend + UX)
- Implementación de todos los flujos del paciente.
- Interacciones HTMX y experiencia de usuario.
- Flujos de recepcionista y médico.
- Usabilidad y simplicidad con máximo 3 clics.
- Pruebas con usuarios cuando sea posible.
- Archivos clave:
  - `pacientes/templates/pacientes/sacar_turno.html`
  - `templates/base.html`
  - `templates/navbar.html`
  - `templates/footer.html`
  - `static/css/tailwind.css`
  - `static/js/main.js`

## Sebastián (UI + Diseño)
- Diseño del sistema visual, paleta de colores y tipografía.
- Creación del sistema de diseño con componentes reutilizables.
- Implementación de Tailwind CSS.
- Aseguramiento de accesibilidad: contraste, tamaños y legibilidad.
- Archivos clave:
  - `templates/base.html`
  - `templates/navbar.html`
  - `templates/footer.html`
  - `static/css/tailwind.css`
  - `static/js/main.js`

## Notas
- El proyecto usa una arquitectura modular con apps separadas para `core`, `pacientes`, `recepcion`, `medicos`, `reportes`, `authentication` y `notifications`.
- Se recomienda mantener actualizada la documentación en `docs/` para los avances de cada rol.
