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

---
## Clasificación Wieringa y calidad Kitchenham

> Tabla estática de clasificación manual según reglas de `design_document.md`. Se complementa con Dataview.

| Archivo | Tipo Wieringa | Calidad Banda | Puntuación |
|---|---|---|---|
| @alvarezCloudComputingTecnologia2012.md | Philosophical | medium | 5.0 |
| @baenanavarroCapitulo2Aplicaciones2025.md | Opinion | high | 7.0 |
| @bellalInvestigatingPotentialKepler2026.md | Validation | high | 8.0 |
| @bossa-benavidezSostenibilidadColombiaFrente.md | Philosophical | high | 7.5 |
| @botero-toroAdopcionComputacionNube2026.md | Philosophical | high | 7.5 |
| @bustamanteANALISISAPLICACIONGREEN2014.md | Philosophical | high | 7.0 |
| @corderoModelIntentAdopt2022.md | Philosophical | high | 7.5 |
| @currieBuildingGreenSoftware2024.md | Opinion | medium | 5.5 |
| @demiccoLiteratureReviewEmbedded2020.md | Opinion | high | 7.5 |
| @diazEnergyawareVMAllocation2013.md | Evaluation | high | 7.0 |
| @diazMeteorologicalAssessmentImplementation2017.md | Evaluation | high | 7.5 |
| @fontanarrosaGreenSoftwareEngineering2024.md | Evaluation | high | 7.0 |
| @garciaserranoDesarrolloEstudioTecnicoeconomico2022.md | Evaluation | high | 8.0 |
| @ghantasalaGlobalDisparitiesGreen2025.md | Philosophical | high | 7.5 |
| @harmonSustainableItServices2009.md | Solution proposal | high | 7.0 |
| @hernndezEnergyEfficiencyScalable2011.md | Evaluation | high | 7.0 |
| @jinGreenSoftwareEngineering2025.md | Evaluation | high | 8.0 |
| @karnauskasThreeStudiesPoint2025.md | Opinion | medium | 5.0 |
| @latifNinoSouthernOscillation2009.md | Philosophical | medium | 5.5 |
| @lozoyaarandiaGreenEnergyHPC2022.md | Evaluation | high | 8.0 |
| @majiDataCentersCarbon2025.md | Evaluation | high | 8.0 |
| @mirandaExplorandoPerspectivasTecnicas2025.md | Evaluation | high | 8.0 |
| @nazareGreenComputingEnergy2023a.md | Evaluation | high | 7.5 |
| @ngInfluenceNinoSouthern2017.md | Philosophical | medium | 6.0 |
| @NinoGlobalWarming2016.md | Opinion | medium | 4.5 |
| @palominoGreenComputingICT2019.md | Experience | high | 7.5 |
| @paton-romeroApplicationISOIEC2019.md | Solution proposal | high | 7.0 |
| @petrocelliPlataformaColaborativaDistribuida2021.md | Evaluation | high | 7.0 |
| @piaggesiGreenTransferAdaptation2019.md | Philosophical | high | 7.0 |
| @picoCFDModellingAir2022.md | Evaluation | high | 8.0 |
| @ProceedingsIEEEACM2026.md | Opinion | medium | 5.5 |
| @QuantifyingDataCenter.md | Opinion | medium | 4.5 |
| @rodriguez-correaAdopcionTecnologiasVerdes2023.md | Philosophical | high | 7.5 |
| @rodriguezSurveyVirtualizationTechnologies2022.md | Evaluation | high | 7.5 |
| @sarastiAplicacionesParaRedes2014.md | Evaluation | medium | 6.5 |
| @siddikEnvironmentalFootprintData2021.md | Evaluation | high | 8.0 |
| @torresAnalisisMulticriterioMultiescala2026.md | Solution proposal | high | 7.5 |
| @wangHowCanNational2026.md | Philosophical | high | 7.5 |
| @wangNonlinearImpactIndustrial2026.md | Philosophical | high | 7.5 |
| @wuExploringGreenSoftware2025.md | Philosophical | high | 7.5 |
| @yaidelsanchezreyesEditorialSpeedwriting.md | Philosophical | high | 7.5 |
| @zhangBilevelPlanningModel2026.md | Evaluation | high | 8.0 |
| @zhangGreenComputingGeneral2026.md | Evaluation | high | 8.0 |
| @zhangIntegrationMultimodalFusion2026.md | Evaluation | high | 8.0 |

### Anexo de datos para figuras
**Datos de figura - Tendencia publicaciones por año 2009-2026**
| year | count |
|---|---|
| 2009 | 2 |
| 2011 | 1 |
| 2012 | 1 |
| 2013 | 1 |
| 2014 | 2 |
| 2016 | 1 |
| 2017 | 2 |
| 2019 | 3 |
| 2020 | 1 |
| 2021 | 2 |
| 2022 | 5 |
| 2023 | 4 |
| 2024 | 2 |
| 2025 | 7 |
| 2026 | 9 |

**Tabla cruzada - Distribución por cluster × tipo Wieringa**
Clusters definidos a partir de tema_asunto: Métricas/Eficiencia, Política/Estándares, Educación/Formación, Centros de Datos/Optimización, Gestión Sostenible.

| cluster | Evaluation | Solution proposal | Philosophical | Opinion | Experience | Validation |
|---|---|---|---|---|---|---|
| Métricas/Eficiencia | 14 | 0 | 0 | 0 | 0 | 1 |
| Política/Estándares | 0 | 2 | 10 | 1 | 0 | 0 |
| Educación/Formación | 0 | 0 | 0 | 2 | 1 | 0 |
| Centros de Datos/Optimización | 4 | 0 | 0 | 0 | 0 | 0 |
| Gestión Sostenible | 0 | 1 | 4 | 4 | 0 | 0 |

**Tabla cruzada - Región × tipo Wieringa**
| region | Evaluation | Solution proposal | Philosophical | Opinion | Experience | Validation |
|---|---|---|---|---|---|---|
| Colombia | 4 | 1 | 4 | 1 | 0 | 0 |
| LAC | 7 | 1 | 3 | 1 | 1 | 0 |
| Global | 5 | 0 | 3 | 3 | 0 | 1 |
| China | 2 | 1 | 2 | 0 | 0 | 0 |
| United States | 1 | 0 | 0 | 0 | 0 | 0 |
