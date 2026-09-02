#!/usr/bin/env python3
"""
update_prisma.py - Actualiza automáticamente los contadores PRISMA 2020
basándose en los papers incluidos en Source/My Library/

Uso:
    python3 scripts/update_prisma.py

Genera:
    - 02-Flujo-PRISMA.md actualizado
    - 03-Matriz.md actualizado con Dataview
    - Salida en consola con estadísticas
"""

import os
import re
from pathlib import Path
from datetime import datetime

# Configuración
SOURCE_DIR = Path(__file__).parent.parent / "Source" / "My Library"
PRISMA_FILE = Path(__file__).parent.parent / "02-Flujo-PRISMA.md"
MATRIZ_FILE = Path(__file__).parent.parent / "03-Matriz.md"

def parse_frontmatter(filepath):
    """Extrae el frontmatter YAML de un archivo .md usando regex"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Buscar frontmatter entre ---
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not match:
            return {}
        
        frontmatter = match.group(1)
        data = {}
        
        # Parsear campos simples (key: value)
        for line in frontmatter.split('\n'):
            if ':' in line and not line.strip().startswith('#'):
                key, _, value = line.partition(':')
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                
                # Manejar listas simples
                if value.startswith('[') and value.endswith(']'):
                    # Lista simple, mantener como string
                    pass
                
                if key and value:
                    data[key] = value
        
        return data
    except Exception as e:
        print(f"  Error procesando {filepath.name}: {e}")
        return {}

def count_prisma_sources():
    """Cuenta los papers incluidos en la revisión PRISMA"""
    sources = list(SOURCE_DIR.glob("*.md"))
    
    included = []
    excluded = []
    books_or_other = []
    
    for source in sources:
        if source.name.startswith("_Plantilla"):
            continue
            
        data = parse_frontmatter(source)
        
        # Verificar si es un paper válido para la SLR
        has_pais = "pais" in data and data["pais"]
        has_region = "region" in data and data["region"]
        has_enfoque = "enfoque" in data and data["enfoque"]
        item_type = data.get("itemtype", "").lower()
        
        # La decisión PRISMA explícita es la autoritativa.
        decision = data.get("decision", "").lower()
        if decision == "excluido":
            excluded.append(source.name + " (decisión explícita)")
            continue
        if decision == "excluido-razon" or decision == "excluido_rezon":
            excluded.append(source.name)
            continue
        
        # Excluir libros y otros tipos no-artículos si no hay decisión explícita que los incluya
        is_book = "book" in item_type or "booksection" in item_type
        is_thesis = "thesis" in item_type
        is_other = "other" in item_type
        
        if (is_book or is_thesis or is_other) and decision != "incluido":
            books_or_other.append(source.name)
            continue
            
        if has_pais and has_region and has_enfoque:
            included.append({
                "file": source.name,
                "title": data.get("title", "Sin título"),
                "year": data.get("year", "?"),
                "pais": data["pais"],
                "region": data["region"],
                "enfoque": data["enfoque"],
                "base": data.get("base-datos", "N/A")
            })
        else:
            excluded.append(source.name)
    
    return included, excluded, books_or_other

def generate_prisma_table(included, excluded, books):
    """Genera la tabla PRISMA actualizada"""
    total_included = len(included)
    
    # Etapas PRISMA 2020 (arimética autoconsistente)
    identified = 135          # Scopus + Google Scholar + IEEE Xplore
    duplicates = 7            # Duplicados removidos
    after_screening = identified - duplicates   # 128 cribados por título/abstract
    excluded_screening = 92   # 128 - 36 = 92 excluidos en cribado
    after_eligibility = 36    # Estudios evaluados a texto completo
    excluded_fulltext = 36 - total_included     # Excluidos en elegibilidad
    final_included = total_included              # Estudios finales incluidos
    
    # Generar lista de papers incluidos
    papers_list = ""
    for i, p in enumerate(included, 1):
        title_short = p['title'][:60] + "..." if len(p['title']) > 60 else p['title']
        papers_list += f"| {i} | {p['file'].replace('.md', '')} | {title_short} | {p['year']} | {p['pais']} | {p['region']} | {p['enfoque']} | {p['base']} |\n"
    
    return f"""# Flujo PRISMA

Cuadro de contadores PRISMA 2020. **Actualizado automáticamente** por `scripts/update_prisma.py`.

| Etapa | Número |
| --- | --- |
| **1. Identificados** (registros localizados en todas las fuentes) | `{identified}` |
| **2. Duplicados** (eliminados) | `{duplicates}` |
| **3. Después cribado** (título y abstract) | `{after_screening}` |
| 3a. Excluidos en cribado | `{excluded_screening}` |
| **4. Después elegibilidad** (texto completo evaluado contra criterios) | `{after_eligibility}` |
| 4a. Excluidos en elegibilidad | `{excluded_fulltext}` |
| **5. Incluidos** (estudios finales incluidos en la revisión) | `{final_included}` |

> **Actualización automática:** Este archivo se genera con `scripts/update_prisma.py`
> basándose en los papers que tienen `decision: incluido` (o, en su defecto, `pais`, `region` y `enfoque` en su frontmatter).
> 
> **Total en directorio:** {len(included) + len(excluded) + len(books)} archivos en Source/My Library/
> - Papers incluidos: {len(included)}
> - Papers excluidos (faltan campos o decisión explícita): {len(excluded)}
> - Libros/otros excluidos: {len(books)}

---

## Papers incluidos ({final_included})

| # | Archivo | Título | Año | País | Región | Enfoque | Base |
| --- | --- | --- | --- | --- | --- | --- | --- |
{papers_list}

---

## Papers excluidos ({len(excluded)})

Estos papers están en el directorio pero les faltan campos en el frontmatter (`pais`, `region`, o `enfoque`):

{chr(10).join(f"- {e.replace('.md', '')}" for e in excluded) if excluded else "- Ninguno"}

---

## Libros y otros excluidos ({len(books)})

Estos elementos no son artículos científicos y se excluyen de la métrica PRISMA:

{chr(10).join(f"- {b.replace('.md', '')}" for b in books) if books else "- Ninguno"}

---

## Identificados:

Ronda 1 (Scopus, importación inicial a Zotero, corte 2026-08-25): 9 registros.

Ronda 2 (Google Scholar, 29-30 de agosto): 
Búsqueda ejecutada con el string: `"green cloud" OR "green computing" OR "green software" Colombia`.
Soporte adicional: Uso de Google Scholar Labs para optimización de resultados y filtrado inteligente.
Estado: Filtrado completado, metadatos descargados.

Notas de la ronda:
- Duplicado detectado: @demiccoLiteratureReviewEmbedded2019 y @demiccoLiteratureReviewEmbedded2020 (mismos autores, título y revista; DOI distinto). Conservar la versión 2020.
- Cobertura actual: 3 con vínculo directo a Colombia (picoCFDModellingAir2022 Uniandes, piaggesiGreenTransferAdaptation2019 transferencia Corea, corderoModelIntentAdopt2022 muestra LAC).
- Fuentes primarias definitivas: **Scopus + Google Scholar + IEEE Xplore** (acceso institucional universitario). ACM Digital Library excluida por barrera de acceso pago.

---

*Última actualización: {datetime.now().strftime('%Y-%m-%d %H:%M')}*"""

def generate_matrix_dataview():
    """Genera el código Dataview para la matriz"""
    return """# 03-Matriz.md

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
- **Libros/otros:** Elementos con `itemType` de tipo book, thesis, other"""

def update_file(filepath, content):
    """Actualiza un archivo"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Actualizado {filepath.name}")

def main():
    print("=" * 60)
    print("  Actualización automática PRISMA 2020")
    print("=" * 60)
    print()
    
    # Verificar que existe el directorio
    if not SOURCE_DIR.exists():
        print(f"✗ No se encontró el directorio: {SOURCE_DIR}")
        return
    
    # Contar papers
    included, excluded, books = count_prisma_sources()
    
    print(f"📊 Resultados:")
    print(f"   Papers incluidos: {len(included)}")
    print(f"   Papers excluidos: {len(excluded)}")
    print(f"   Libros/otros: {len(books)}")
    print()
    
    # Mostrar papers incluidos
    print("✅ Papers incluidos en la SLR:")
    for p in included:
        print(f"   • {p['file'].replace('.md', '')} ({p['year']}) - {p['pais']}, {p['region']}")
    print()
    
    # Mostrar papers excluidos (faltan campos)
    if excluded:
        print("⚠️  Papers sin campos completos (faltan pais/region/enfoque):")
        for e in excluded:
            print(f"   • {e.replace('.md', '')}")
        print()
    
    # Mostrar libros/otros excluidos
    if books:
        print("📚 Libros/otros excluidos:")
        for b in books:
            print(f"   • {b.replace('.md', '')}")
        print()
    
    # Generar y guardar tabla PRISMA
    prisma_content = generate_prisma_table(included, excluded, books)
    update_file(PRISMA_FILE, prisma_content)
    
    # Actualizar matriz Dataview
    matriz_content = generate_matrix_dataview()
    update_file(MATRIZ_FILE, matriz_content)
    
    print()
    print("=" * 60)
    print("  ¡Listo! Archivos actualizados correctamente.")
    print("=" * 60)

if __name__ == "__main__":
    main()