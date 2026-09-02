---
citationKey: yaidelsanchezreyesEditorialSpeedwriting
title: "Informe Ejecutivo: Principios y Mejores Prácticas en la Ingeniería de Software Verde (Memorias Speedwriting 2023)"
itemType: conferencePaper
creators:
  - Ricardo Antonio Botero Rios
  - Yaidel Sánchez Reyes
publication: "Memorias 2da. Convención Científica Internacional Speedwriting 2023"
date: "2023-11"
year: 2023
anio: 2023
pais: Colombia
region: LAC
enfoque: policy
base-datos: Google Scholar
url: https://tecnologicospeedwriting.com/editorial-speedwriting/
doi: ""
tags:
  - "#Green_Software"
  - "#Green_Software_Engineering"
  - "#Green_Software_Foundation"
  - "#Energy_Efficiency"
  - "#Hardware_Efficiency"
  - "#Carbon_Awareness"
  - "#SCI_Index"
  - "#Software_Sostenible"
  - "#Colombia"
  - "#Quindío"
  - "#EducaAmbienteWeb"
zotflow-locked: false
zotero-key: MDTHZ3DF
item-version: 448
library-id: 20202832
fuente: Google Scholar
decision: incluido
---
# Editorial Speedwriting
## Abstract

# Informe Ejecutivo: Principios y Mejores Prácticas en la Ingeniería de Software Verde

## 1. Visión General y Contexto

El desarrollo y despliegue de soluciones informáticas genera un impacto ambiental directo a través del consumo de infraestructura física y energía eléctrica. La **Ingeniería de Software Verde** (_Green Software_) se establece como una disciplina orientada al diseño, construcción y mantenimiento de aplicaciones optimizadas para minimizar el uso de recursos de hardware y reducir la huella de carbono, sin comprometer la eficiencia ni la experiencia del usuario.

Con proyecciones que estiman que los centros de datos representarán entre un **3 % y un 8 % de la demanda energética mundial**, la sostenibilidad se convierte en un requisito de arquitectura y un indicador de calidad fundamental en el ciclo de vida del software.

## 2. Pilares Fundamentales del Software Sostenible

La construcción de software con conciencia ambiental se fundamenta en cinco dimensiones operativas:

- **Optimización de recursos:** Maximización de la eficiencia del procesamiento y memoria.

- **Mitigación de la huella de carbono:** Reducción de las emisiones indirectas de $CO_2$.

- **Mantenibilidad y durabilidad:** Extensión del ciclo de vida del código y compatibilidad de hardware.

- **Eficiencia energética:** Reducción del consumo de kilovatios-hora ($kWh$) por transacción.

- **Gestión responsable de datos:** Reducción de la transferencia y almacenamiento innecesario de información.

## 3. Estándares de la _Green Software Foundation_

La _Green Software Foundation_ —coalición conformada por líderes de la industria tecnológica— establece tres ejes estratégicos para lograr una reducción del **45 % en las emisiones de gases de efecto invernadero para el año 2030**:

### A. Eficiencia Energética (_Energy Efficiency_)

El objetivo primordial es reducir al mínimo el consumo de electricidad por cada ejecución de proceso.

- **Métrica PUE (_Power Usage Effectiveness_):** Evalúa la eficiencia energética de la infraestructura del centro de datos:

$$\text{PUE} = \frac{\text{Energía Total de la Instalación}}{\text{Energía Consumida por el Equipo TI}}$$

    Un valor cercano a **1.0** indica máxima eficiencia energética, mientras que un PUE de **2.0** implica que por cada vatio consumido por los servidores, se requiere un vatio adicional para soporte operacional (refrigeración y distribución).

- **Proporcionalidad Energética:** Medición que evalúa la relación entre la tasa de utilización del hardware y el consumo energético efectivo.


### B. Eficiencia de Hardware (_Hardware Efficiency_)

Enfocada en amortizar el **carbono incorporado**, el cual representa la totalidad de las emisiones generadas durante la fabricación, transporte y disposición final de los dispositivos informáticos.

  

$$\text{Emisión Anual Amortizada} = \frac{\text{Carbono Incorporado Total}}{\text{Años de Vida Útil}}$$

- **Prolongación de ciclo de vida:** Incrementar la vida útil de un servidor (por ejemplo, de 4 a 5 años) reduce significativamente la tasa de emisión amortizada por año.

- **Consolidación en la Nube:** La adopción de arquitecturas multi-inquilino (_multi-tenant_) e infraestructura pública optimiza la tasa de ocupación de los servidores y evita la capacidad ociosa.

### C. Conciencia del Carbono (_Carbon Awareness_)

Estrategia orientada a modular la ejecución de procesos según la intensidad de carbono de la red eléctrica en tiempo real ($gCO_2eq/kWh$).

  

- **Desplazamiento Temporal y Geográfico:** Programación de tareas intensivas de procesamiento (batch, entrenamiento de modelos o actualizaciones de sistema) en horarios o ubicaciones geográficas donde predomine la generación de energía renovable.
    
      
    

## 4. Métricas y Herramientas de Evaluación

|**Herramienta / Métrica**|**Descripción y Aplicación Técnica**|
|---|---|
|**Índice SCI (_Software Carbon Intensity_)**|Estándar para medir la tasa de emisiones por unidad funcional (ej. por consulta API, por usuario activo o por transacción):<br><br>  <br><br>$$SCI = \frac{(E \times I) + M}{m}$$<br><br>Don de $E$ es energía, $I$ es intensidad de carbono, $M$ es carbono incorporado y $m$ representa la unidad funcional.|
|**QGIS**|Sistema de información geográfica de código abierto para el análisis y delimitación de impacto ambiental.|
|**EPA ProUCL & Aermod**|Herramientas para el modelamiento estadístico de contaminantes y análisis de dispersión atmosférica.|

## 5. Caso de Aplicación y Resultados

La implementación de plataformas educativas computarizadas desarrolladas bajo estos criterios (tales como _EducaAmbienteWeb_) demuestra que la aplicación de software optimizado facilita la gestión integral de Residuos de Aparatos Eléctricos y Electrónicos (RAEE). La combinación de código eficiente con software libre permite escalar soluciones sostenibles a nivel institucional con una huella operativa reducida.

## Notas clave
- **Síntesis de la Green Software Foundation:** Resumen ejecutivo de los tres pilares estratégicos (Eficiencia Energética, Eficiencia de Hardware, Conciencia de Carbono) con métricas accionables (PUE, SCI, carbono incorporado amortizado).
- **Datos duros de referencia:** Centros de datos = 3-8% demanda energética mundial; meta GSF: reducción 45% emisiones GEI para 2030; PUE ideal ≈ 1.0.
- **Métricas operativas listas para usar:** PUE (infraestructura), SCI (software por unidad funcional), carbono incorporado amortizado (hardware), intensidad de carbono (gCO2eq/kWh).
- **Estrategias accionables:** Prolongar vida útil hardware (ej. servidor 4→5 años reduce emisión amortizada 20%), consolidación en nube multi-tenant, desplazamiento temporal/geográfico de cargas según intensidad de carbono de la red.
- **Caso Colombia (Quindío):** Implementación _EducaAmbienteWeb_ en colegios (Armenia, Calarcá) - caso real de software verde + educación ambiental + RAEE, con resultados medibles en comunidad estudiantil.
- **Herramientas de evaluación:** SCI (Microsoft/GSF), PUE (Green Grid), QGIS (geoespacial), EPA ProUCL/Aermod (modelado contaminantes).
- **Gap para Colombia:** El paper de Botero (2023) señala que en LatAm **solo Brasil** ha abordado el tema formalmente; Colombia tiene avances puntuales (caso Quindío) pero **carece de política nacional, estándares obligatorios y formación sistemática** en Green Software Engineering.
- **Uso sugerido:** Sección de "Estado del arte - Green Software Engineering" y "Discusión - Gap de políticas y formación en Colombia". Métricas SCI/PUE directamente citables en tabla comparativa.

## Attachments
- [Libro-Memorias-Congreso-Speedwriting-2023-comprimido.pdf](obsidian://zotflow?type=open-attachment&libraryID=20202832&key=Z2DPGAL9)

## Notes
