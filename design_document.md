# Documento de Diseño: Revisión Sistemática de Literatura sobre Green Software Engineering en Colombia

**Versión:** 1.0 · Septiembre de 2026
**Estado:** Implementado — define el diseño metodológico del artículo `latex/gsw-colombia.tex`.
**Alcance:** SLR con mapeo sistemático (PRISMA 2020 + Kitchenham & Charters 2007; Petersen et al. 2015) sobre Green Cloud, Green DevOps y Green Software Engineering, con foco comparativo Colombia frente a Europa, China y América Latina.

---

## 1. Preguntas de investigación

| RQ | Pregunta | Secciones del artículo que la responden |
|----|----------|------------------------------------------|
| **RQ1** | ¿Cuál es el estado actual de la investigación sobre Green Cloud, Green DevOps y Green Software Engineering en Colombia, en comparación con Europa, China y América Latina? | Dimensiones técnicas y métricas; Brechas de política y formación; Aplicaciones y casos de uso; Software verde para gestión y turismo |
| **RQ2** | ¿Colombia acumula evidencia técnica aislada pero carece de la infraestructura política, normativa y formativa necesaria para escalar el Green Software Engineering? | Comparación regional (tabla comparativa); Brechas de política y formación; Vulnerabilidad energética |
| **RQ3** | ¿Qué brechas específicas existen entre la producción global y la realidad colombiana en Green Software Engineering? | Brechas de política y formación; Matriz comparativa regional; Discusión de brechas |
| **RQ4** | ¿Qué insumos para la definición de políticas y líneas de investigación futuras se pueden derivar de esta SLR para el contexto colombiano? | Conclusiones (7 recomendaciones); Líneas de investigación futuras |

---

## 2. Evaluación de calidad (rúbrica de 8 criterios, adaptada de Kitchenham)

Cada estudio incluido se puntúa de 0 a 1 por criterio (0 = no cumple, 0.5 = cumple parcialmente, 1 = cumple plenamente), lo que da un máximo de 8 puntos por estudio.

| # | Criterio | Nivel 0 | Nivel 0.5 | Nivel 1 |
|---|----------|---------|-----------|---------|
| **C1** | Pregunta de investigación clara | No está explícita o es vaga | Parcial (solo en resumen) | Formulada explícitamente en introducción u objetivos |
| **C2** | Diseño de investigación apropiado | No hay claridad sobre el tipo de estudio | Se infiere pero no se justifica | Tipo y diseño especificados explícitamente |
| **C3** | Validez de la evidencia | Sin métricas ni datos de respaldo | Datos aislados o incompletos | Métricas operativas con datos cuantificables (PUE, SCI, huella de carbono) |
| **C4** | Completitud del reporte | Faltan datos críticos (país, año, fuente) | Algunos datos faltantes pero recuperables | Campos clave presentes (país, región, enfoque, año, título) |
| **C5** | Adecuación del tipo de fuente | No es un artículo de investigación | Tipo mixto (p. ej. revisión narrativa) | Artículo de investigación primario con datos reproducibles |
| **C6** | Contexto geográfico documentado | No se informa el contexto | País informado sin región | País y región documentados con claridad |
| **C7** | Coherencia del enfoque metodológico | Enfoque no coincide con la contribución | Coincidencia parcial | Enfoque (técnico, político, educativo, de gestión) alineado con la contribución |
| **C8** | Actualidad | Anterior a 2015 sin valor histórico relevante | 2015–2019, valor de contexto limitado | 2020 o posterior (o clásico fundamental) |

**Rangos de interpretación:**

| Categoría | Puntaje | Interpretación |
|-----------|---------|----------------|
| Alta | 7 – 8 | Datos completos, metodología clara, contexto documentado |
| Media | 4 – 6 | Algunos datos faltantes o enfoque parcial |
| Baja | 0 – 3 | Datos insuficientes, metodología poco clara o fuera de alcance |

**Uso en el artículo:** la distribución de bandas de calidad sustenta los hallazgos técnicos citados (índice SCI, métricas PUE, reducciones contrastadas), permite identificar sesgos de representación (los estudios de bandas bajas tienden a ser de años previos a 2015 o fuera de Colombia) y respalda las cinco brechas identificadas en la discusión.

---

## 3. Clasificación del tipo de investigación (Wieringa et al.)

| Tipo | Definición |
|------|------------|
| **1. Solution proposal** | Propone una solución o artefacto concreto para un problema de sostenibilidad del software |
| **2. Evaluation** | Evalúa una solución o enfoque contra criterios de desempeño o eficiencia |
| **3. Validation** | Valida teórica o empíricamente un modelo, teorema o propiedad |
| **4. Philosophical** | Análisis conceptual, fundamentación teórica o posicionamiento |
| **5. Opinion** | Paper de posición, visión de futuro o editorial, sin datos empíricos nuevos |
| **6. Experience** | Reporte de experiencia o estudio de caso en contexto real |

**Criterios de asignación:** cada estudio se clasifica con reglas explícitas derivadas de su enfoque, su tipo de fuente y la presencia de métricas cuantificables. Cuando un estudio no cumple ninguna regla definida, se asigna al tipo más conservador (Opinion). La distribución resultante se reporta en el artículo (tipología de investigación) y permite auditar la clasificación de los 44 estudios.

---

## 4. Mapeo sistemático: figuras y tablas

- **Tendencia de publicaciones por año (2009–2026):** distribución temporal del corpus incluido. La evolución es creciente (promedio aproximado de 1.4 publicaciones/año en 2009–2015; ~2.9 en 2016–2022; ~3.5 en 2023–2026), lo que respalda una narrativa de *crecimiento acelerado* y no de crecimiento exponencial estricto en la producción científica.
- **Tablas cruzadas:** combinaciones de tema y escenario de aplicación, y de región y enfoque, derivadas de la matriz de extracción (`03-Matriz.md`).

Estas piezas son complementarias a la matriz comparativa regional (tabla con países de referencia) y a los mapas temáticos ya presentes en el artículo.

---

## 5. Snowballing y comparación con SLR globales

- **Snowballing (Wohlin, 2014, best effort):** se revisaron las referencias y citas de los estudios incluidos para localizar candidatos no capturados por las cadenas de búsqueda primarias. No se modificó el corpus de 44 estudios; los hallazgos se listan como candidatos para futuras actualizaciones de la revisión.
- **SLR de referencia para la comparación:**
  1. **Harmon & Auseklis (2009)** — servicios TI sostenibles, enfoque global.
  2. **Moreira et al. (2024)** — Green Software Engineering y su integración curricular, Europa/global.
  3. **Wu et al. (2025)** — software verde para gestión y turismo, enfoque global.

**Declaración de novedad:** la contribución no es la revisión en sí — existen SLR previas de Green Software — sino la aplicación de PRISMA 2020 con fase de mapeo sistemático al contexto colombiano, produciendo evidencia comparable con la literatura global pero con un foco geográfico inédito. Las brechas identificadas (política pública, estándares, formación universitaria, investigación aplicada e infraestructura) son específicas de Colombia.

---

## 6. Exclusiones a texto completo (10 estudios)

| # | Estudio | Razón de exclusión |
|---|---------|--------------------|
| 1 | abuhabib et al. (2026) | Temática fuera de alcance (ML para desalinización/aguas residuales) |
| 2 | Barua & Roy (2022) | Sin contexto Colombia; alcance global |
| 3 | Carbon Benefits of Cloud (Microsoft/WSP) | Whitepaper corporativo, sin contexto Colombia |
| 4 | CREA (2026) | Fuente no académica (artículo institucional sobre sistemas energéticos) |
| 5 | Eilam et al. (2024) | Fuera del contexto Colombia (alcance global) |
| 6 | Gnibga et al. (2024) | Fuera del contexto Colombia (alcance global) |
| 7 | Korontanis et al. (2025) | Fuera del contexto Colombia (alcance global) |
| 8 | Lago et al. (2013) | Actas de taller, fuera del alcance de la revisión |
| 9 | Saraiva (2021) | Fuera del contexto Colombia (alcance global) |
| 10 | Trejos & Alzate (2016) | Temática de entretenimiento en la nube (cloud gaming), no alineada con Green Software Engineering |

La tabla completa, con la razón PRISMA 2020 asociada, se presenta en el apéndice C del artículo.

---

## 7. Apéndices del artículo

| # | Apéndice | Contenido |
|---|----------|-----------|
| **A** | Estrategia de búsqueda por base de datos | Cadenas de búsqueda completas por base (Scopus, IEEE Xplore, Google Scholar), fechas y filtros |
| **B** | Checklist PRISMA 2020 | Cumplimiento de los ítems del checklist, con referencia a la sección del artículo que lo evidencia |
| **C** | Exclusiones a texto completo | Tabla de los 10 estudios excluidos con su razón PRISMA 2020 |
| **D** | Rúbrica de calidad | Criterios C1–C8 y puntuaciones de los estudios incluidos |
| **E** | Snowballing | Candidatos identificados por revisión de referencias y citas |
| **F** | Comparación con SLR globales | Las 3 revisiones de referencia y la declaración de novedad |

---

## 8. Decisiones de diseño y control de riesgos

| Tema | Decisión adoptada |
|------|-------------------|
| Evolución de la producción científica | Usar "crecimiento acelerado" (no "exponencial") al describir la tendencia del corpus |
| Sesgo de un único autor | La rúbrica mecánica (sección 2) se documenta como control compensatorio en las limitaciones del artículo |
| Proyecciones externas (4.2× emisiones a 2030) | Se citan como escenario de referencia de la literatura (Maji et al., 2025), no como hallazgo de la revisión |
| Vulnerabilidad energética (ENOS) | Se enmarca como argumento contextual sustentado en la literatura climática citada |
| Integridad del corpus | Snowballing exploratorio sin modificación del corpus final de 44 estudios |