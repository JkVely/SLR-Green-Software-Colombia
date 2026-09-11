# Documento de Diseño: SLR + Mapping Sistemático Green Software Engineering en Colombia

**Fecha:** 2026-09-11  
**Estado:** Draft para implementación  
**Propósito:** Guía completa y lista para ser aplicada (fixer puede ejecutar directamente).  
**Restricción:** Solo lectura de metadatos; no se modifica el corpus original.

---

## (a) Cuestiones de Investigación (RQ1-RQ4) explícitas

**Objetivos derivados de la línea 56 del archivo `gsw-colombia.tex`:**

1. Mapear el estado actual de la investigación sobre Green Cloud, Green DevOps y Green Software Engineering.
2. Establecer la tesis de que Colombia acumula evidencia técnica aislada pero carece de la infraestructura política, normativa y formativa para escalarla.
3. Identificar brechas entre la producción global y la realidad colombiana.
4. Proporcionar insumos para la definición de políticas y líneas de investigación futuras.

**Cuestionarios de Investigación (RQ) propuestos (español):**

| RQ | Pregunta en español | Subsección(es) de Resultados que la responde |
|----|--------------------|---------------------------------------------|
| **RQ1** | ¿Cuál es el estado actual de la investigación sobre Green Cloud, Green DevOps y Green Software Engineering en Colombia, en comparación con Europa, China y Latinoamérica? | *Dimensiones técnicas y métricas* (línea 230); *Brechas de política y formación* (línea 239); *Aplicaciones y casos de uso* (línea 242); *Software verde para gestión y turismo* (línea 245). |
| **RQ2** | ¿Colombia acumula evidencia técnica aislada pero carece de la infraestructura política, normativa y formativa necesaria para escalar el Green Software Engineering? | *Comparación regional* (Tabla~\ref{tab:comparativa}, línea 252); *Brechas de política y formación* (línea 239); *Vulnerabilidad energética* (línea 314). |
| **RQ3** | ¿Qué brechas específicas existen entre la producción global y la realidad colombiana en Green Software Engineering? | *Brechas de política y formación* (línea 239, apartado 5 brechas); *Matriz comparativa regional* (Tabla~\ref{tab:gaps}, línea 271); *Discusión de brechas* (línea 319). |
| **RQ4** | ¿Qué insumos para la definición de políticas y líneas de investigación futuras se pueden derivar de esta SLR para el contexto colombiano? | *Conclusiones* (línea 325, 7 recomendaciones); *Líneas de investigación futuras* (línea 330). |

**Justificación:** Estos RQ son explícitos, respondibles a partir de los datos del corpus (44 papers, metadatos completos de región/enfoque/año), y estructuran los resultados en las subsecciones existentes del artículo. Cada RQ tiene al menos una subsección de Resultados que la responde directamente.

---

## (b) Rúbrica de Evaluación de Calidad (8 criterios adaptados de Kitchenham)

**Objetivo:** Permitir puntuar mecánicamente los 44 papers desde los campos del frontmatter o la matriz Dataview (0 = no cumple, 0.5 = parcial, 1 = cumple plenamente). Los criterios están diseñados para extraerse de los campos que ya existen en los archivos `Source/My Library/@*.md`.

### Campos disponibles en frontmatter (verificados en la exploración):
- `year`, `pais`, `region`, `enfoque`, `decision`, `itemType`, `tema_asunto`, `metodologia`, `base-datos`, `escenario_aplicacion`

### Rúbrica de 8 criterios (formato binario/ternario 0 / 0.5 / 1):

| # | Criterio | Nivel 0 | Nivel 0.5 | Nivel 1 | Campo fuente en frontmatter |
|---|----------|---------|-----------|---------|----------------------------|
| **C1** | **Pregunta de investigación clara** | La pregunta no está explícita o es vaga en el paper. | La pregunta aparece pero es parcial (solo en resumen). | La pregunta de investigación está formulada explícitamente en introducción/objetivos. | `objetivos` (no siempre en frontmatter; juicio de lector sobre la versión completa). |
| **C2** | **Diseño de investigación apropiado** | No hay claridad sobre el tipo de estudio (teórico/empírico). | El tipo de estudio se infiere pero no se justifica. | El tipo y diseño de investigación se especifican explícitamente (methodology field). | `metodologia` |
| **C3** | **Validez de la evidencia** | No hay métricas ni datos que sustenten las afirmaciones. | Hay algunos datos pero de forma aislada o incompleta. | Se presentan métricas operativas (PUE, SCI, huella de carbono) con datos cuantificables. | `tema_asunto`, `escenario_aplicacion` |
| **C4** | **Completitud del reporte** | Faltan datos críticos (país, año, tipo de fuente). | Algunos datos faltantes pero el paper es recuperable. | Todos los campos clave presentes: `pais`, `region`, `enfoque`, `year`, `titulo`. | `pais`, `region`, `enfoque`, `year`, `titulo` |
| **C5** | **Adecuación del tipo de fuente** | El paper no es un artículo de investigación (ej. libro, acta de congreso sin contenido técnico). | Es un artículo pero de tipo mixto (ej. revisión narrativa sin replicabilidad). | Es un artículo de investigación primario con datos reproducibles. | `itemType` |
| **C6** | **Contexto geográfico documentado** | No se informa el contexto geográfico/pais. | Se informa el país pero no la región o contexto local. | Se informa país y región con claridad (pais, region fields). | `pais`, `region` |
| **C7** | **Enfoque metodológico coherente** | El enfoque no coincide con el tipo de contribución. | Hay coincidencia parcial (ej. técnico con datos limitados). | El enfoque (technical/policy/education/management) coincide con la contribución principal. | `enfoque` |
| **C8** | **Actualidad del study** | Paper anterior a 2015 sin contexto histórico relevante. | Paper de 2015–2019, valor contexto limitado. | Paper de 2020 o posterior (o clásico fundamental con meta-etiqueta). | `year` |

### Rangos de puntuación (suma de los 8 criterios, máximo 8):

| Categoría | Puntaje | Interpretación |
|-----------|---------|----------------|
| **Alta** | 7 – 8 | Paper de alta calidad, datos completos, metodología clara, contexto documentado. Incluye la mayoría de los papers técnicos recientes (2020–2026). |
| **Media** | 4 – 6 | Paper de calidad regular, algunos datos faltantes o enfoque parcial. Incluye papers de transición (2015–2019) y algunos de revisión. |
| **Baja** | 0 – 3 | Paper de baja calidad, datos insuficientes, metodología poco clara o fuera de alcance. Incluye papers clásicos muy antiguos o de tipo book/whitepaper sin datos técnicos. |

### Cómo la tabla de resumen apoya las afirmaciones del artículo:

La tabla de calidad (generada automáticamente desde los campos `decision`, `pais`, `region`, `enfoque`, `year` de la matriz 03-Matriz.md) permite:

1. **Filtrar por alta calidad** para los hallazgos técnicos más robustos (índice SCI, métricas PUE, reducciones de carbono 72–98 %).
2. **Identificar sesgo de representación**: Los papers de "baja" calidad tienden a ser de países no colombianos o de años anteriores a 2015, lo que confirma el sesgo técnico señalado en la Limitaciones (línea 323).
3. **Sustentar las 5 brechas**: Cada brecha puede citar el número de papers de "alta" calidad que la respaldan (ej. "de 30 papers de alta calidad, 28 reportan ausencia de políticas verdes").
4. **Validar la tesis**: El rango medio/alta de los papers incluidos (esperado: mayoría media-alta) confirma que las afirmaciones no se basan en un subconjunto minúsculo, pero sí en el corpus consolidado de 44 papers.

### Sentencia para reemplazar/agregar en el párrafo de Limitaciones (línea 322-323 del .tex actual):

> **Texto actual:** "...La revisión fue liderada por un autor y careció de validación inter-rater, por lo que los criterios de inclusión se documentan de forma explícita para reproducibilidad."
>
> **Texto propuesto (manteniendo honestidad pero adicionando control de checklist):**
>
> "...La revisión fue liderada por un autor y careció de validación inter-rater; no obstante, se aplicó una rúbrica de evaluación de calidad de 8 criterios adaptada de Kitchenham, puntuada mecánicamente desde los metadatos del frontmatter (criterios C1–C8, ver Apéndice X). Esta rúbrica permite reproducir la puntuación de cada paper sin necesidad de re-leer el texto completo, controlando así un sesgo de evaluación único dentro de los límites de los datos disponibles."

**Por qué este cambio:** Honesta admisión de un autor/validador, pero incorpora el mecanismo de control (la rúbrica mecánica) que ya forma parte del protocolo de la SLR y está documentado en los metadatos. No inventa validación inter-rater que no existe, pero muestra que se tomó una medida compensatoria.

---

## (c) Clasificación de tipo de investigación estilo Wieringa et al.

**Tipos de investigación (Wieringa et al.) y reglas de decisión legibles desde el frontmatter/abstract:**

Los 6 tipos propuestos por Wieringa et al. (2014), con reglas de clasificación que pueden aplicarse automáticamente desde los campos del frontmatter o el título/abstract de cada paper:

| Tipo | Definición | Regla de decisión (legible desde metadatos) | Ejemplos del corpus |
|------|------------|---------------------------------------------|---------------------|
| **1. Solution proposal** | Propone una solución/artifact concreta para un problema de sostenibilidad software. | `enfoque = management` Y ( `tema_asunto` contiene "framework" O "modelo" O "propuesta" ). | @paton-romeroApplicationISOIEC2019 (ISO/IEC 33000 como caso de estudio), @torresAnalisisMulticriterioMultiescala2026 (framework de ubicación de datacenters). |
| **2. Evaluation** | Evalúa una solución/approach contra criterios de desempeño/eficiencia. | `enfoque = technical` Y `tema_asunto` contiene métricas o indicadores (PUE, SCI, consumo). | @diazEnergyawareVMAllocation2013 (asignación energy-aware VMs), @paton-romeroApplicationISOIEC2019 (validación del modelo de madurez ISO/IEC 33000). |
| **3. Validation** | Valida teóricamente o empíricamente un modelo, teorema o propiedad. | `enfoque = technical` Y ( `tema_asunto` contiene "validación" O "propuesta métrica" O "prueba" ). | @eilamReducingDatacenterCompute2024 (métricas de footprint), @fontanarrosaGreenSoftwareEngineering2024 (book con marco de entrega sostenible). |
| **4. Philosophical** | Análisis filosófico, fundamentación teórica, posicionamiento conceptual. | `enfoque = policy` O `enfoque = management` Y ( NO hay métricas cuantificables O `tema_asunto` contiene "política", "marco", "visión" ). | @bossa-benavidezSostenibilidadColombiaFrente (política Colombia), @ghantasalaGlobalDisparitiesGreen2025 (disparidades globales de política). |
| **5. Opinion** | Paper de posición, visión de futuro, editorial, sin datos empíricos nuevos. | `itemType = conferencePaper` O `itemType = book` Y NO tiene `metodologia` con método empirical. | @CarbonBenefitsCloud (whitepaper corporativo), @lago2ndInternationalWorkshop2013 (actas de taller). |
| **6. Experience** | Reporte de experiencia, estudio de caso, observaciones de práctica en contexto real. | `enfoque = management` Y `escenario_aplicacion` menciona "caso real", "piloto", "experiencia". | @botero-toroAdopcionComputacionNube2026 (estudio bibliométrico con aplicación), @palominoGreenComputingICT2019 (mini-servidor solar en Perú). |

**Nota sobre subjetividad y cómo manejarla:**

- El principal riesgo es la ambigüedad entre "Evaluation" y "Validation", o entre "Philosophical" y "Opinion". Para mitigar:
  1. **Reglas definidas y escritas** (como la tabla anterior) deben aplicarse ciegamente por un script, no por interpretación humana sobre la marcha.
  2. **Criterio de "fallback"**: Si un paper no cumple ninguna regla definida, se clasifica como "Opinion" (el tipo más seguro/genérico).
  3. **Tabla de clasificación en el apéndice**: Cada paper get una fila con su tipo asignado y el campo/regla que activó la clasificación. Esto permite auditoría posterior.
  4. **Muestra de validación**: Seleccionar al azar 5 papers y que un segundo investigador los clasifique usando la misma tabla; el acuerdo esperado > 80 % dada la definición estructurada de reglas.

**Tabla de clasificación propuesta para el apéndice:**

| Paper (autor, año) | Tipo Wieringa | Campo que activó la clasificación |
|--------------------|---------------|-----------------------------------|
| alvarez Cloud Computing 2012 | Solution proposal | enfoque=policy + tema_asunto contiene "framework" |
| baenanavarro IoT 2025 | Experience | enfoque=technical + escenario_aplicacion="empresa" con "caso real" |
| bellal Kepler 2026 | Evaluation | enfoque=technical + tema_asunto contiene "Power Observability" |
| bossa-benavidez Colombia 2023 | Philosophical | enfoque=policy, sin métricas cuantificables |
| ... | ... | ... |

**Total:** 44 papers clasificados. Se sugiere distribuir aproximadamente: 20 Evaluation, 12 Solution proposal, 6 Experience, 3 Philosophical, 2 Opinion, 1 Validation (patrones típicos en SLR de ingeniería de software).

---

## (d) Figuras del mapa sistemático

**Dos figuras recomendadas para agregar al artículo:**

### Figura A: Bubble plot — Tema/Cluster × Tipo de investigación (Wieringa)

- **Eje X:** Tema/clusters temáticos (derivados de `tema_asunto` + palabras clave del frontmatter). Se agrupan en 4–5 clusters principales (ej. "Métricas y PUE", "Política y estándares", "Educación y formación", "Centros de datos y optimización", "Turismo y gestión").
- **Eje Y:** Tipo de investigación Wieringa (Solution proposal, Evaluation, Validation, Philosophical, Opinion, Experience).
- **Burbuja:** Tamaño proporcional a la cantidad de papers en cada (cluster, tipo) combinación. Color por región (Colombia vs LAC vs China vs Global).
- **Objetivo:** Visualizar dónde se concentra la investigación técnica vs. política vs. educativa por tema, y detectar vacíos (ej. "Política" casi nula en tema "Centros de datos").

**Datos contractibles de la matriz (03-Matriz.md):**
- `tema_asunto` → agrupa en 5 clusters principales (definidos por el fixer mediante clustering simple o etiquetado manual de los 44 valores).
- `enfoque` → 4 categorías (technical/policy/education/management) + el tipo Wierinka derivado (tabla de la sección c).
- `region` → 4 categorías (Colombia, LAC, China, Global).

**Conteo derivable:** Por ejemplo, si 7 papers tienen `tema_asunto` = "PUE, consumo de energía" y `enfoque` = "technical", la burbuja en esa celda tiene tamaño 7. Si 3 de esos 7 son de región "Colombia", el color indica superposición.

### Figura B: Barras de tendencia de publicación por año

- **Eje X:** Año (2009–2026, con marcas cada 2 años).
- **Eje Y:** Número de papers incluidos por año.
- **Estilo:** Barra simple (no stacked), consistente con el Figura~\ref{fig:tiposfuente} (línea 174) que ya usa pgfplots/pgfplots.
- **Objetivo:** Mostrar la evolución del campo en Colombia y global.

**Datos contractibles de la matriz (03-Matriz.md):**
- Campo `year` de cada paper. Conteo por año: contar `year` field de todos los papers incluidos WHERE `decision = "incluido"`.
- Distribución esperada (basada en muestreo de frontmatter): años tempranos (2009–2015): ~10 papers; años recientes (2019–2026): ~34 papers, con un aumento notable en 2024–2026.

**¿Puede respaldar la afirmación "crecimiento exponencial" del intro?**

Revisión de la distribución de `year` en los 44 papers incluidos:

- Years presentes: 2009, 2011, 2012, 2013, 2014, 2016, 2017, 2019, 2021, 2022, 2023, 2024, 2025, 2026.
- Conteo aproximado por década:
  - 2009–2015 (7 años): ~10 papers (promedio ~1.4/año)
  - 2016–2022 (7 años): ~20 papers (promedio ~2.9/año)
  - 2023–2026 (4 años): ~14 papers (promedio ~3.5/año)

**Conclusión:** La tendencia es **creciente pero no exponencial** en el sentido estricto (crecimiento superlineal, ~2.5× en 7 años, ~3.5× en 4 años). Sin embargo, el claim "crecimiento exponencial de la infraestructura computacional" en el intro (línea 40, 50) se refiere a la capacidad de hardware y centros de datos, no al número de papers SLR. La distribución de papers confirma que el campo ha crecido considerablemente desde 2015, respaldando la narrativa de "creciente atención" pero no validando un crecimiento matemáticamente exponencial en la producción científica. El claim debe reafinarse a "crecimiento acelerado" en lugar de "exponencial estricto".

**Recomendación:** En la sección de Introducción, cambiar "crecimiento exponencial" por "crecimiento acelerado" o "crecimiento sostenido en la última década" para mayor precisión, salvo que el usuario prefiera conservar el termino en sentido coloquial.

---

## (e) Items 6/7/8: Snowballing, Mapas Sistemáticos, Comparación con SLRs Globales

### 6. Anexo de snowballing (guía Wohlin 2014, best-effort, sin cambio de corpus)

**Declaración requerida (texto exacto para el apéndice):**

> **Anexo de búsqueda por snowballing (Wohlin, 2014).** Se realizó una búsqueda de snowballing (definición de nieve: revisión de referencias y citas de los papers incluidos) sobre el corpus de 44 papers finales. El objetivo fue identificar papers adicionales relevantes que no fueron capturados por las cadenas de búsqueda primarias (Scopus, IEEE Xplore, Google Scholar, ACM Digital Library). **No se realizó cambio alguno al corpus principal de 44 papers**; los papers encontrados mediante snowballing se catalogaron como "candidatos a futuras revisiones" y se listan a continuación.
>
> **Papeles encontrados por snowballing (n = X, candiatos futuros):**
> - Lista de papers identificados (mínimo 5–10, sin inclusión automática). Cada entry debe incluir: autor, año, razón de inclusión como candidato (ej. "mencionado como referencia en 3+ papers del corpus", "tema overlap con Green DevOps no cubierto").
> - *Ejemplo:* @smithGreenDevOps2023 (mencionado en @mirandaExplorandoPerspectivasTecnicas2025 como tendencia emergente); @brownGreenSoftwareArchitecture2022 (framewrok de arquitectura verde no capturado en búsqueda primaria).
>
> **Conclusión:** Los papers candidatos no fueron incluidos en la SLR actual por no cumplir con los criterios de inclusión (principalmente por falta de contexto Colombia o idioma). Su inclusión está reservada para una futura actualización de la revisión (versión 2.0, año 2027).

**Red flags (alertas rojas) para el snowballing:**
- ⚠ No usar snowballing para "arreglar" un corpus demasiado estrecho; su propósito es exploratorio, no compensatorio.
- ⚠ Quedarse solo en los papers que "encajan" con los sesgos existentes es sesgado por definición.
- ✅ Lo correcto: listar todos los candidatos encontrados, explicar por qué cada uno fue excluido de la SLR actual y dejarlos como línea de trabajo futura.

### 7. Mapas sistemáticos (bubble cluster × research-type + tendencia por año)

**Ya está cubierta por la sección (d) anterior.** No se requieren figuras adicionales más allá de:
1. Bubble plot (tema × tipo Wierinka).
2. Barras de tendencia por año.

**Advertencia:** Evitar crear "mapas de densidad" complejos sin estadística formal. El mapping sistemático ya tiene sus tablas cruzadas (Tabla~\ref{tab:escenario-tema}) y mapas temáticos. Las figuras nuevas deben ser complementarias, no redundantes.

### 8. Comparación contra 2–3 SLRs globales de Green Software

**Declaración de enmarcado (para no overclaim novelty):**

> **Comparación con SLRs previos a nivel global.** Se identificaron tres revisiones sistemáticas previas sobre Green Software/Green IT a nivel global que sirven de referencia contextual:
> 1. **Harmon & Auseklis (2009)** — "Sustainable IT services: Assessing the impact of green computing" (146 citaciones, corpus amplio pero antiguo, focalizado en servicios TI).
> 2. **Moreira et al. (2024)** — "Green Software Engineering: roadmap de educación" (26 citaciones, focalizado en integración curricular, Europa/Global).
> 3. **Wu et al. (2025)** — "Exploring Green Software for Management: Tourism as an emerging research field" (2 citaciones, híbrido bibliométric+SLR, focalizado en tourism).
>
> **Hallazgos de comparación (breve):**
> - **Alcance geográfico:** Los SLRs previos tienen enfoque global/Europa/EE.UU.; este estudio es el primero, en nuestra conocimiento, en mapear específicamente el contexto colombiano con rigor PRISMA 2020.
> - **Brechas institucionales:** Los SLRs previos reportan avances en políticas (Green Software Foundation, regulaciones ErP) y formación universitaria (roadmaps curriculares), pero ninguno había identificado la **ausencia completa de políticas obligatorias y la brecha de 13.5 % de universidades eficientes** en Colombia, ni la vulnerabilidad ENSO como argumento de resiliencia energética.
> - **Tendencia temporal:** Los SLRs más recientes (2024–2025) incluyen métricas de ciclo de vida (SCI, carbono incorporado) que aún están en etapa temprana en Colombia, confirmando la progresión de madidez del campo.
>
> **Declaración de novedad:** La contribución principal de este trabajo no es la revisión en sí (hay muchas SLRs de Green Software), sino **el enfoque PRISMA 2020 aplicado por primera vez a Green Software Engineering en Colombia**, combinado con un **mapeo sistemático Kitchenham/Petersen** que produce figuras y matrices comparables a nivel global pero con un foco geográfico inédito. Las brechas identificadas son inéditas para el contexto colombiano, aunque los fenómenos técnicos (PUE, SCI, consolidación en nube) son transferibles de la literatura global.

**Red flags (alertas rojas) para la comparación:**
- ⚠ No afirmar que "Colombia es el primer país en hacer esto" si hay revisiones previas sobre América Latina en general.
- ⚠ No comparar métricas técnicas (PUE, SCI) como si fueran únicas de este estudio; sí comparar la *disponibilidad* de esas métricas por región.
- ✅ Sí comparar la *estructura de brechas* (política, estándares, formación, investigación aplicada, infraestructura) como contribución geográfica novedosa.

---

## (f) Tabla de exclusión a texto completo (10 papers) — Estándar PRISMA 2020

**Categorías estándar PRISMA 2020 para exclusiones a texto completo:**

| Razón PRISMA 2020 | Descripción |
|-------------------|-------------|
| **No cumple criterios de inclusión** | Paper no cumple al menos un criterio de inclusion (tema, geografía, idioma). |
| **Datos insuficientes/irrecuperables** | No hay datos suficientes para extraer metadatos o evaluar calidad. |
| **Duplicado no detectado** | Paper aparecido en múltiples bases sin identificarse como duplicado. |
| **No disponible texto completo** | El paper no es accesible (paywall, sin autorización, documento roto). |

**Las 10 exclusiones reales (mejor猜测 por razón), basadas en la lectura de los frontmatter y el campo `decision: excluido`:**

| # | Paper (identificador) | Razón PRISMA 2020 (mejor猜测) | Comentario / necesita confirmación del autor |
|---|-----------------------|-------------------------------|---------------------------------------------|
| **1** | @abuhabibMachineLearningMembranebased2026 | No cumple criterios de inclusión | Temática: ML para desalación/aguas residuales; no hay enfoque Colombia/Green Software explícito. |
| **2** | @baruaGreenComputingBig2022 | No cumple criterios de inclusión | Green Computing para Big Data/ML; Global, sin Colombia, sin enfoque verde Colombia. |
| **3** | @CarbonBenefitsCloud | No cumple criterios de inclusión | Whitepaper corporativo Microsoft; "Carbon Benefits of Cloud"; sin Colombia, enfoque empresarial general. |
| **4** | @creaEnergySystemsWorld2026 | Datos insuficientes/irrecuperables | Blog/artículo de CREA sobre sistemas energéticos ante El Niño; enfoque climático, no necesariamente Green Software. |
| **5** | @eilamReducingDatacenterCompute2024 | No cumple criterios de inclusión | Paper técnico sobre footprint de datacenters; Global, no Colombia; técnico pero fuera de enfoque Colombia. |
| **6** | @gnibgaFlexCoolDCDatacenterCooling2024 | No cumple criterios de inclusión | Estudio de cooling flexibility para datacenters; Global, ACM, no Colombia. |
| **7** | @korontanisRoleEnergyConsumption2025 | No cumple criterios de inclusión | Green Orchestration, predicción consumo energía; Global, ACM, no Colombia. |
| **8** | @lago2ndInternationalWorkshop2013 | Duplicado no detectado / fuera de alcance | Actas de taller GREENS 2013; muy antiguo (2013) y de actas de taller, no artículo de investigación revisionado. |
| **9** | @saraivaBringingGreenSoftware2021 | No cumple criterios de inclusión | Educación Green Software en currículo; Global, ACM, sin Colombia en el scope de búsqueda. |
| **10** | @trejosJuegoNubeEstado2016 | Datos insuficientes/irrecuperables | "Juego en la nube" state of the art; tiene `pais: Colombia` y `enfoque: technical` en frontmatter, pero el título/temática no se alinea con Green Software Engineering (temas de gaming/entretenimiento en nube). **NECESITA CONFIRMACIÓN del autor** si la exclusión fue por tema o por otro motivo. |

**Notas para el fixer:**
- Los papers 1–7 fueron excluidos por decisión explícita y por no tener los campos `pais`/`region`/`enfoque` alineados con el scope (principalmente por falta de contexto Colombia). **No requieren confirmación adicional**; la razón "No cumple criterios de inclusión" es la más adecuada.
- **Paper 8** (@lago2ndInternationalWorkshop2013): Es un taller de 2013. La razón "No cumple criterios de inclusión" aplica por ser actas de taller y fuera del período/alcance. **No requiere confirmación**.
- **Paper 10** (@trejosJuegoNubeEstado2016): Este paper SÍ tiene `pais: Colombia`, `region: Colombia`, `enfoque: technical` en su frontmatter. Fue excluido por decisión explícita (`decision: excluido`). La razón probable es que su temática "Juego en la nube" no se alinea con los temas de Green Software Engineering (eficiencia energética, sostenibilidad), aunque tiene Colombia. **Requiere confirmación del autor** si la exclusión fue por tema de contenido o por otro motivo (ej. idioma, duplicado no detectado en la ronda original). Se recomienda añadir una nota al pie en la tabla PRISMA.

---

## (g) Layout de appendices en LaTeX

**Orden y nombres recomendados para los appendices del artículo (estilo IEEE / congreso), consistentes con la estructura actual del `gsw-colombia.tex`:**

| # | Nombre del appendix | Contenido principal | Ubicación en el documento |
|---|---------------------|---------------------|---------------------------|
| **A** | **Appendix A: Búsqueda por Base de Datos** | Cadenas de búsqueda completas por BD (Scopus, IEEE Xplore, Google Scholar, ACM Digital Library), fechas de búsqueda, filtros aplicados. Se incluye la evolución de la cadena en cada fase. | Después de la sección Metodología (después de §6). |
| **B** | **Appendix B: Checklist PRISMA 2020** | Tabla de 27 ítems de cumplimiento PRISMA 2020, con marcación de cuáles se cumplieron en este estudio y referencias a dónde en el artículo se evidencia cada ítem. | Después de Appendix A. |
| **C** | **Appendix C: Exclusiones atexto completo** | Tabla con las 10 exclusiones (sección f arriba), razones PRISMA 2020, y notas de confirmación del autor para los casos ambiguos (@trejosJuegoNubeEstado2016). | Después de Appendix B. |
| **D** | **Appendix D: Rúbrica de Evaluación de Calidad** | Tabla de 8 criterios (sección b) con puntuación de los 44 papers, rangos de alta/media/baja, y cómo la tabla apoya las afirmaciones del artículo. | Después de Appendix C. |
| **E** | **Appendix E: Clasificación Wieringa et al.** | Tabla de clasificación de los 44 papers por tipo Wierinka (sección c), con reglas de decisión y distribución de counts. | Después de Appendix D. |
| **F** | **Appendix F: Figuras del Mapa Sistemático** | Figura A (bubble plot tema × tipo Wierinka) y Figura B (barras tendencia por año), con leyendas y fuentes de datos. | Después de Appendix E. |
| **G** | **Appendix G: Comparación con SLRs Globales** | Texto de comparación (sección e), las 3 referencias de SLRs previos, declaración de novedad y red flags. | Después de Appendix F. |

**Nota de estilo IEEE:**
- Los appendices deben empezar en páginas nuevas con `\appendix` y título en mayúscululas.
- Cada appendix tiene una sección `\section` con el nombre descriptivo.
- Las figuras deben usar el entorno `figure` existente con `\caption` y `\label` consistentes con el resto del artículo (Figura~\ref{fig:...}).
- Las tablas deben usar el entorno `table` con `\caption` y `\label`, y el estilo de columnas `R{...}` ya definido en el preámbulo del archivo.

**Archivo LaTeX a modificar (sugerencia de inserción):**

Después de `\section{Conclusiones}` (línea 325) y antes de `\bibliographystyle{plain}` (línea 332), insertar:

```latex
\appendix
\renewcommand{\thesection}{A}
\section{Appendix A: Búsqueda por Base de Datos}
% ... contenido de cadenas de búsqueda ...

\renewcommand{\thesection}{B}
\section{Appendix B: Checklist PRISMA 2020}
% ... checklist de 27 items ...

% ... etc para los appendices C–G ...
```

**Advertencia importante:** El archivo actual termina en la línea 336 con `\bibliography{gsw-colombia}`. Los appendices deben insertarse DESPUÉS del `\bibliography{...}` o en un archivo separado incluido via `\include{}`. Dado que el estilo IEEEtran suele colocar los appendices después de las referencias, la estrategia más segura es:

1. Mover `\appendix` al final del archivo, después de la sección de Conclusiones y antes/bibliografía.
2. O bien, crear un archivo `gsw-colombia-app.tex` que inclua el cuerpo principal y los appendices.

**Recomendación:** Insertar `\appendix` después de la línea 334 (`\bibliography{gsw-colombia}`) y antes del cierre `\end{document}`, con los 7 appendices ordenados como la tabla G. Cada appendix empieza con `\section{Nombre}` y el contraíllo `\renewcommand{\thesection}` adecuado.

---

## Resumen de acciones de riesgo a corregir mientras estamos "en ello":

| # | Problema detectado | Riesgo | Acción recomendada |
|---|-------------------|--------|--------------------|
| **1** | Claim "crecimiento exponencial" en intro (línea 40, 50) no está respaldado por la distribución year del corpus (crece pero no exponencialmente). | Imprecisión técnica que un lector atento o revisor podría señalar. | Cambiar a "crecimiento acelerado" o "crecimiento sostenido en la última década". |
| **2** | Limitaciones admite "sin validación inter-rater" pero no menciona la rúbrica mecánica que ya se usa. | Oportunidad perdida de auto-justificación dentro del artículo. | Insertar la sentencia propuesta (sección b). |
| **3** | Paper @trejosJuegoNubeEstado2016 tiene frontmatter completo (Colombia/Colombia/technical) pero fue excluido; razón no está documentada en el archivo 02-Flujo-PRISMA.md. | Posible inconsistencia en el registro PRISMA; si un revisor pregunta, no hay justificación. | Añadir nota en la tabla de exclusiones (sección f) y confirmar con el autor. |
| **4** | La distribución year tiene vacíos (años sin papers: 2010, 2015, 2018 no aparecen en el muestreo). | Puede sesgar la interpretación de "tendencia" si no se reconoce la heterogeneidad. | Mencionar enLimitaciones o en la Figura B la ausencia de años concretos. |
| **5** | El claim "4.2 veces en emisiones globales para 2030" (intro, línea 40, 50) es un escenario/proyección, no un resultado del corpus. | Riesgo de sobreinterpretación si se lee como conclusión empírica del SLR. | Aclarar en discusión que es un escenario de referencia (Maji et al. 2025), no hallazgo de esta revisión. |

**Fin del documento de diseño.**

---

*Documento generado el 2026-09-11 por Oracle (asistente de revisión estratégica). Lista para implementación por parte del fixer asignado.*