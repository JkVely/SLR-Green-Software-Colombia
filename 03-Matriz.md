# 03-Matriz.md

Tabla maestra de extracción de datos. **Se genera automáticamente con Dataview** — no editar a mano. Cada vez que añades o modificas los frontmatter de las fuentes, puedes refrescar el query para ver los cambios.

> **Nota:** Los campos `anio`, `pais`, `region`, `enfoque`, `decision`, `base-datos` deben estar en el frontmatter de cada archivo de `Source/My Library/` para que aparezcan en la tabla. Los fields `titulo` y `year` vienen definidos en la mayoría de los frontmatter ya. Los campos adicionales se van poblando según se completa el análisis de cada paper.

```dataview
TABLE titulo, year, pais, region, enfoque, decision, base-datos
FROM "Source/My Library"
WHERE file.name != "_Plantilla-fuente" AND decision = "incluido"
SORT year DESC
```

> **Cómo usar:**
> 1. Tener Dataview activado en Obsidian Settings > Community plugins.
> 2. Abrir esta nota y Dataview renderizará la tabla automáticamente con los campos del frontmatter de cada fuente.
> 3. Si agregas una nueva nota en `Source/My Library/`, regresa a esta nota y Dataview se actualizará (o recarga la ventana).
> 4. Esta tabla es la fuente que usarás para sintetizar resultados en `04-Borrador.md` y para el análisis de gaps Colombia vs resto.

---

## Scripts de automatización

Ejecuta `python3 scripts/update_prisma.py` para:
- Actualizar automáticamente los contadores en `02-Flujo-PRISMA.md`
- Verificar que cada paper tenga los campos requeridos (`pais`, `region`, `enfoque`)
- Detectar papers faltantes o incompletos

### Requisitos
- Python 3.8+
- No requiere dependencias externas (usa solo stdlib)

### Salida esperada
El script genera:
1. `02-Flujo-PRISMA.md` - Tabla PRISMA actualizada con papers incluidos
2. `03-Matriz.md` - Código Dataview optimizado
3. Resumen en consola con estadísticas

### Campos requeridos en frontmatter
Para que un paper sea contabilizado como "incluido", debe tener:
```yaml
---
pais: Colombia  # o Global, etc.
region: LAC     # o Europa, China, etc.
enfoque: policy # o technical, education, management
---
```

### Filtros aplicados
- **Incluidos:** Artículos con `pais`, `region` y `enfoque` definidos
- **Excluidos:** Artículos sin esos campos completos
- **Libros/otros:** Elementos con `itemType` de tipo book, thesis, other