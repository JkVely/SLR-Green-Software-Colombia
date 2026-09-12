# SLR Green Software Engineering en Colombia — Guía del repositorio

Este repositorio contiene la documentación y los artefactos de la Revisión Sistemática de Literatura (SLR) sobre Green Cloud, Green DevOps y Green Software Engineering, con enfoque comparativo Colombia frente a Europa, China y América Latina.

La revisión sigue la metodología **PRISMA 2020** con fase de mapeo sistemático (Kitchenham & Charters 2007; Petersen et al. 2015). El corpus final está conformado por **44 estudios** (2009–2026) extraídos de Scopus, Google Scholar e IEEE Xplore.

## Estructura

```
/
├── README.md                    Resumen del proyecto, estado y DOI
├── CITATION.cff                 Ficha de cita del repositorio (GitHub + Zenodo)
├── LICENSE                      Licencia CC-BY-4.0
├── design_document.md           Diseño metodológico de la revisión
├── 00-Protocolo.md              Pregunta de investigación, objetivo y alcance
├── 01-Criterios.md              Criterios de inclusión/exclusión y consultas
├── 02-Flujo-PRISMA.md           Contadores PRISMA 2020 (generado por script)
├── 03-Matriz.md                 Matriz de extracción de datos
├── 04-Borrador.md               Borrador del artículo
├── 05-Enlaces-Externos.md       Fuentes externas de contexto
├── 06-Encuesta-ACOLDC.md        Encuesta a empresas (ACOLDC)
├── Reunion 1-09.md              Registro de reunión del proyecto
├── latex/                       Artículo IEEEtran (fuente, bibliografía, PDF)
├── scripts/
│   └── update_prisma.py         Actualiza contadores PRISMA y matriz
└── Source/My Library/           Metadatos y notas por estudio (frontmatter)
```

## Flujo de trabajo

1. Cada estudio se registra en `Source/My Library/` con sus metadatos (año, país, región, enfoque, decisión) en el frontmatter.
2. La decisión de inclusión o exclusión PRISMA se registra en el campo `decision`.
3. El script `scripts/update_prisma.py` genera los contadores del flujo PRISMA (`02-Flujo-PRISMA.md`) y la matriz de extracción (`03-Matriz.md`).
4. El artículo se redacta en LaTeX (`latex/gsw-colombia.tex`), con el borrador en markdown como referencia (`04-Borrador.md`).

## Cómo citar

- Pares clave y DOI: consultar `CITATION.cff`.
- DOI del repositorio (Zenodo): `10.5281/zenodo.22716253` — https://doi.org/10.5281/zenodo.22716253
- Licencia: CC-BY-4.0 (uso libre con atribución).