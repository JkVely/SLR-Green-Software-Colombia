# 03-Matriz.md

Tabla maestra de extracción de datos. **Se genera automáticamente con Dataview** — no editar a mano. Cada vez que añades o modificas una nota en `Fuentes/`, puedes refrescar el query para ver los cambios.

```dataview
TABLE titulo, anio, pais, region, enfoque, decision, razon-exclusion, fecha-consulta, base-datos
FROM "Fuentes"
WHERE file.name != "_Plantilla-fuente"
SORT anio DESC
```

> **Cómo usar:**
> 1. Tener Dataview activado en Obsidian Settings > Community plugins.
> 2. Abrir esta nota y Dataview renderizará la tabla automáticamente con los campos del frontmatter de cada fuente.
> 3. Si agregas una nueva nota en `Fuentes/`, regresa a esta nota y Dataview se actualizará (o recarga la ventana).
> 4. Esta tabla es la fuente que usarás para sintetizar resultados en `04-Borrador.md` y para el análisis de gaps Colombia vs resto.