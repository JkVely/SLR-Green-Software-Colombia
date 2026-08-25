# Criterios

## Criterios de inclusión

- Documentos (artículos, conferencias, revisiones) que traten sobre Green Cloud, Green DevOps o Green Software Engineering.
- Documentos con mención explícita a políticas, desarrollos o estado del arte en al menos una región (Colombia, Europa, China, Latinoamérica).
- Disponibles al menos en resumen/abstract en inglés o español.
- Indexados en las bases de búsqueda principales (IEEE Xplore, Scopus, ACM DL) o con DOI/ISBN detectable.

## Criterios de exclusión

- Documentos que solo mencionen "green" o sostenibilidad sin relación con cloud/devops/software engineering.
- Papeles de postura sin fundamentación técnica o evaluación empírica.
- Duplicados (mismo artículo en múltiples bases).
- Documentos puramente teóricos sin componente de desarrollo, política o evaluación.

## Queries de búsqueda por base de datos

### IEEE Xplore

```
("green cloud" OR "green computing" OR "sustainable cloud" OR "energy-efficient computing") 
AND ("Colombia" OR "Bogotá" OR "Medellín" OR "Universidad Nacional" OR "Universidad de los Andes")
```
**Nota:** Los resultados se filtrarán por rango de años (2010-2024) directamente en la interfaz de IEEE Xplore o se anotará el rango en la documentación de búsqueda. El objetivo es capturar la mayor cantidad relevante; después se aplicarán filtros de elegibilidad.

### Scopus

```
TITLE-ABS-KEY(("green cloud" OR "green computing" OR "sustainable cloud" OR "green software engineering" OR "green devops")) 
AND TITLE-ABS-KEY(("Colombia") OR "Latin America")
AND PUBYEAR > 2010 AND PUBYEAR < 2025
```

**Limitación documented:** No permite exportación masiva fiable (>1000 resultados) ni búsqueda reproducible al 100%; usará solo para snowballing/caza de papers que se escapen de las otras 3 bases. Total de registros a reportar en el flujo PRISMA será menor o se anotará como "consulta complementaria".

### ACM Digital Library

```
("Green Cloud" OR "Green Computing" OR "Sustainable Cloud" OR "Green DevOps" OR "Green Software Engineering") 
AND ("Colombia" OR "LatAm" OR "Latin America")
AND PUBYEAR > 2010 AND PUBYEAR < 2025
```

### Google Scholar *(fuente complementaria - documenting limitations)*

```
("Green Cloud" OR "Green Computing" OR "Green Software Engineering" OR "Green DevOps") 
AND ("Colombia" OR "Latin America")
```
**Limitación documented:** No permite exportación masiva fiable (>1000 resultados) ni búsqueda reproducible al 100%; usará solo para snowballing/caza de papers que se escapen de las otras 3 bases. Total de registros a reportar en el flujo PRISMA será menor o se anotará como "consulta complementaria".

## Documentación de búsqueda

## Testing & Refining (iteración de búsquedas)

Tras ejecutar cada query anota:

| Base | n identificados | Papeles irrelevantes principales | Ajuste a aplicar |
|------|----------------|----------------------------------|-----------------|
| IEEE |  |  | Revisar si faltan términos sinónimos ("energy-efficient computing") |
| Scopus |  |  | Añadir `AND PUBYEAR > 2012` si muchos resultados muy antiguos |
| ACM |  |  | Probar con `"Green Software Engineering"` entre comillas simples vs dobles |
| Google Scholar |  |  | Documentar límite 1000 resultados; usar solo para snowballing |

### Ejemplos de ajustes comunes:

1. **Si muchos papers de educación/género** (como el que te salió): Añade `AND (cloud OR computing)` al final, o `AND (sustainable OR energy)` para estrechar.

2. **Si pocos resultados**: Ampliar los sinónimos: añade `"green IT"` o `"sustainable IT"` a la disyunción.

3. **Si papers de China/Europa pero pocos de Colombia**: Verifica que los términos de país no estén en el abstract solo por citar región; quizás añadir `TITLE-ABS-KEY` en Scopus para forzar mención en título.

---

## Documentación de búsqueda

Registrar en `02-Flujo-PRISMA.md`:
- n identificados por cada base
- n duplicados eliminados
- n después cribado (título/abstract)
- n después elegibilidad (texto completo)
- n incluidos en revisión final