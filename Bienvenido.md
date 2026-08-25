# repositorio-slr-prisma

Vault dedicado a la revisión sistemática (SLR) usando metodología PRISMA, sobre el estado actual de políticas y desarrollos en Green Cloud, Green DevOps y Green Software Engineering, con enfoque comparativo Colombia vs mundo.

## Flujo de trabajo (4 pasos)

1. **Leer paper** → Crear nota en `Fuentes/` usando la plantilla (`_Plantilla-fuente.md`). Editar SOLO ese archivo: metadatos, país, enfoque green, hallazgos, decisión PRISMA (`incluido`/`excluido`).
2. **Aplicar PRISMA** → La decisión vive en cada nota de `Fuentes/`. En `02-Flujo-PRISMA.md` solo se llevan los conteos de las 4 etapas (identificados → cribados → elegibles → incluidos), actualizados al cerrar cada ronda de búsqueda.
3. **Extraer ideas** → `03-Matriz.md` se genera automáticamente con Dataview leyendo todas las notas de `Fuentes/`. No es necesario editar la tabla a mano — al cambiar una nota, la matriz se actualiza sola.
4. **Escribir artículo** → `04-Borrador.md` contiene el borrador en markdown. Al pasar a LaTeX, se usan los citekey del frontmatter y el archivo `referencias.bib` (gestionado por Zotero + Better BibTeX).

## Estructura de carpetas

```
/Fuentes/
  └── _Plantilla-fuente.md     ← plantilla (no borrar ni renombrar)
  └── P01-apellido2024.md      ← UNA nota por paper leído
  └── P02-gonzalez2023.md
  └── ...                      ← tantas como papers incluya

/
├── 00-Protocolo.md            Pregunta de investigación, objetivo, alcance (Colombia vs mundo)
├── 01-Criterios.md            Inclusión/exclusión + queries por base (IEEE/Scopus/ACM/Scholar)
├── 02-Flujo-PRISMA.md         Contadores de las 4 etapas PRISMA 2020
├── 03-Matriz.md               Tabla automática (Dataview)
├── 04-Borrador.md             Artículo en md: Intro, Método, Resultados, Discusión, Conclusión
└── referencias.bib            BibTeX acumulado (Zotero + Better BibTeX, auto-sincronizado)
```

## Plugins recomendados (ya están instalados)

- **Templates** (core, activado) — para instanciar la plantilla de fuente.
- **Dataview** — genera la matriz automáticamente a partir de las notas de `Fuentes/`.
- **Zotero Integration** + **Better BibTeX** (Zotero desktop) — gestiona `referencias.bib` y los citekey; el `.bib` se auto-exporta al vault.
- **obsidian-pandoc** — opcional: convierte `04-Borrador.md` a `.tex` si algún día quieres evitar el copy-paste.

## Cómo empezar

1. Fíjate en `00-Protocolo.md` y `01-Criterios.md` para definir tu pregunta y criterios de búsqueda.
2. Revise la plantilla `_Plantilla-fuente.md` — ese es el único archivo que tocarás por cada paper.
3. Cuando leas un paper, crea una nueva nota desde la plantilla en `Fuentes/` y llénala: resumen + decisión PRISMA.
4. Deja que Dataview arme la matriz y vayas actualizando los contadores en `02-Flujo-PRISMA.md`.

Todo está pensado para que cada paper toque **UN solo archivo** y el resto se genere solo. Sin redundancia, para que puedas sacar ideas rápidas y pasar al artículo en LaTeX.