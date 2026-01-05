# Instrucciones para agentes AI (proyecto holamundo)

Breve: repositorio pequeño con scripts Python en `scripts/`. El objetivo
es probar documentación y los flujos básicos sin dependencias externas.

- **Arquitectura:**
  - `scripts/` contiene ejecutables: `main.py` (entrypoint) y `hello.py` (lógica).
  - `docs/` contiene documentación estática/ejemplo.

- **Qué hacer primero:**
  - Ejecutar localmente: `python scripts/main.py` o `python -m scripts.main`.
  - Revisar `scripts/hello.py` para el patrón de docstrings (Google/reST).

- **Convenciones del proyecto:**
  - Mantener `scripts/main.py` como un runner mínimo (no añadir paquetes nuevos ahí).
  - Preferir docstrings en funciones públicas; la docstring en `greet` sirve
    como ejemplo de formato y contenido.
  - Evitar dependencias externas; si una tarea requiere una, propónla y
    documenta el motivo.

- **Flujos de desarrollo relevantes:**
  - Ejecutar script: `python scripts/main.py` — útil para pruebas rápidas.
  - Ejecutar el módulo CLI: `python scripts/hello.py <nombre>` para verificar
    el comportamiento desde la línea de comandos.

- **Patrones detectables (ejemplos):**
  - Función pequeña con docstring -> `scripts/hello.py::greet`.
  - Entry point simple que importa desde `scripts` -> `scripts/main.py`.

- **Qué documentar automáticamente:**
  - Documenta las funciones públicas en `scripts/` usando los docstrings.
  - Si generas archivos `docs/` o artefactos, coloca los resultados en `docs/`.

- **Límites y cosas a evitar:**
  - No cambiar la estructura de carpetas sin una buena razón.
  - No instales dependencias sin aprobación previa.

Si algo no está claro o necesitas más ejemplos (ej. plantilla Sphinx o mkdocs),
pide que añada uno y lo implemento.
