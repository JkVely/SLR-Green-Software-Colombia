# Encuesta para mapeo de empresas en Green IT / Green Software
Objetivo: medir madurez cuantitativa y obtener insumos cualitativos para clasificación con Atlas.ti.

## Sección A — Perfil de la organización
**A1. ¿Cuál describe mejor a su organización?**
- Proveedor cloud, hosting o managed services
- Operador o proveedor de centro de datos
- Empresa de desarrollo de software / fábrica de software
- Consultora de cloud, DevOps, SRE o transformación digital
- Startup de producto digital / SaaS
- Organización usuaria de tecnología con infraestructura propia o híbrida
- Universidad, centro de investigación u organización sin ánimo de lucro
- Otro: ____

**A2. Tamaño aproximado en Colombia**
- 1–10 / 11–50 / 51–200 / 201–500 / Más de 500 / Prefiero no responder

**A3. Ciudad(es) principal(es) de operación**
- Bogotá–Región / Medellín–Valle de Aburrá / Cali–Valle del Cauca / Barranquilla/Cartagena/Caribe / Eje Cafetero / Otra / Operación distribuida

**A4. Rol de quien responde**
- Dirección ejecutiva/CTO / Arquitectura / DevOps/SRE / Infraestructura / Desarrollo / Seguridad/ESG / FinOps / Académico / Otro

**A5. Modelo principal de infraestructura**
- On-premise / Nube pública / Híbrido / Multi-cloud / Edge / No aplica

## Sección B — Conocimiento y compromiso
Escala 0 = No existe / 1 = Reconocido sin acciones / 2 = Pilotos aislados / 3 = Práctica documentada parcial / 4 = Integrado, se mide y mejora

**B1. Nivel de conocimiento interno sobre Green IT / sostenibilidad digital.**
**B2. Política, objetivo, KPI o compromiso ambiental relacionado con TI/cloud/software.**
**B3. Inclusión de criterios de energía, carbono o ciclo de vida en decisiones de arquitectura o compra.**
**B4. Formación o sensibilización del personal técnico.**
**B5. Responsables claros para sostenibilidad digital.**
**B6. Integración de sostenibilidad en procesos de proveedores, compras o licitaciones.**

**B7. Abierta. ¿Cómo define su organización Green IT / Green Software y qué términos usa internamente?**

**B8. Abierta. ¿Por qué considera que algunas prácticas de sostenibilidad digital no se han adoptado aún en su organización?**

## Sección C — Medición y observabilidad
**C1. ¿Qué métricas se miden actualmente?** Selección múltiple
Consumo eléctrico, PUE, CUE, WUE, Emisiones CO2e, Intensidad carbono red, Emisiones incorporadas, Energía/carbono por servicio/transacción, Utilización servidores/VMs, Ninguna/No sé

**C2. ¿En qué nivel se pueden observar/atribuir métricas de energía/carbono?** Selección múltiple
Instalación/data center / Servidor / VM / Clúster Kubernetes / Contenedor / Aplicación/microservicio / Solicitud API/transacción / Job de datos/IA / No se mide

**C3. ¿Qué herramientas o fuentes usa?** Selección múltiple
BMS/DCIM, Facturas/medidores, Dashboards cloud, Prometheus/Grafana, OpenTelemetry, Kepler/eBPF, Cloud Carbon Footprint, Herramienta ESG, Hojas de cálculo, Otra

**C4. Frecuencia de revisión de indicadores de energía/eficiencia/emisiones**
Nunca / Solo en proyecto o incidente / Anualmente / Trimestral / Mensual / Semanal/tiempo casi real / No aplica

**C5. ¿Usa unidad funcional para relacionar impacto y valor?**
Sí sistemática / Sí en pilotos / No pero interesa / No y no está en planes / No sé

**C6. Si mide impacto, ¿qué dificulta más atribuir energía o carbono a un servicio?** Máx 3
Falta de sensores / Infraestructura compartida / Dependencia de proveedores cloud / Falta datos intensidad carbono local / Falta herramientas / Costos / Falta tiempo / Falta conocimiento / No hay necesidad de negocio clara / Otro

**C7. Abierta. Describa un caso donde la falta de datos o herramientas impidió actuar sobre la huella de un servicio.**

## Sección D — Prácticas Green Cloud e infraestructura
Escala 0-4 como en B.

**D1. Consolidación, apagado programado o eliminación de recursos ociosos.**
**D2. Rightsizing de CPU/memoria/almacenamiento a demanda real.**
**D3. Autoscaling/planificación de capacidad.**
**D4. Selección de región/proveedor/hardware considerando eficiencia, renovables o huella de carbono.**
**D5. Gestión de ciclo de vida de equipos: reutilización, prolongación, RAEE.**
**D6. Virtualización/contenedores/orquestación para mejorar utilización.**
**D7. Uso de energía renovable, PPA, certificados, microred.**

**D8. ¿Se han evaluado prácticas de carbon-aware computing?**
Sí operando / Sí piloto / Discutido no implementado / No considerado / No aplica

**D9. Abierta. ¿Qué práctica de infraestructura le generó mayor ahorro o mayor resistencia interna y por qué?**

## Sección E — Green Software Engineering
Escala 0-4.

**E1. Requisitos no funcionales incluyen objetivos de eficiencia, consumo o huella.**
**E2. Arquitectura se evalúa considerando consumo cómputo, transferencia de datos, caché, almacenamiento.**
**E3. Pruebas de rendimiento incluyen métricas energéticas o de carbono.**
**E4. CI/CD incorpora controles para evitar artefactos innecesarios, builds redundantes o ambientes ociosos.**
**E5. Prácticas de eficiencia de datos: retención, compresión, deduplicación, caché.**
**E6. Se considera impacto de dependencias, librerías, modelos de IA o servicios externos.**

**E7. Abierta. ¿Cuál es el principal obstáculo para incorporar eficiencia energética en el diseño de software?**

## Sección F — IA y workloads intensivos
**F1. ¿Opera o desarrolla workloads de IA/analítica/HPC?**
Sí en producción / Sí piloto / No / No sé

Si No, saltar a G.

**F2. ¿Qué cargas ejecuta?** Entrenamiento ML/IA / Inferencia / LLMs / Analítica/ETL / Visión / HPC / Otro
**F3. ¿Dónde se ejecutan?** Nube pública / On-premise / Híbrido / Edge / SaaS de terceros
**F4. ¿Mide o estima costo energético/carbono por workload de IA?** Sí regularmente / Sí piloto / No pero planificado / No / No sé
**F5. ¿Qué métricas usa para IA?** Uso GPU/CPU, Consumo eléctrico, Energía por entrenamiento/inferencia, Energía/carbono por token/solicitud, Costo financiero, Ninguna
**F6. Acciones de eficiencia aplicadas:** Selección modelos pequeños, Cuantización, Batching, Caching, Límites recursos, Autoscaling, Planificación jobs, Uso modelos locales, Ninguna
**F7. Importancia de equilibrar rendimiento, costo y consumo energético en IA** 1-5

**F8. Abierta. ¿Cómo equilibran rendimiento, costo y consumo energético en sus cargas de IA?**

## Sección G — Barreras, incentivos y necesidades
**G1. Principales barreras para adoptar Green IT/Green Software** Máx 5
Falta conocimiento / Falta formación / Falta tiempo/prioridad / Falta presupuesto / Falta herramientas medición / Falta datos intensidad carbono / Dificultad atribución / Ausencia regulación/incentivos / Falta demanda clientes / Dificultad demostrar ROI / Riesgo rendimiento/seguridad / Dependencia proveedores / Falta estándares locales / Otra

**G2. Incentivos que aumentarían adopción** Máx 3
Ahorro costos / Requisitos clientes/licitaciones / Estándares guías / Capacitación / Herramientas open source / Incentivos tributarios / Certificaciones / Regulación reporte obligatorio / Alianzas U-E-Estado / Acceso datos intensidad carbono / Otro

**G3. Tipo de apoyo más útil**
Diagnóstico madurez / Guía métricas/dashboards / Formación técnica / Guía medición huella cloud / Casos uso IA eficiente / Laboratorio piloto con universidad / Comunidad de práctica / No requiere / Otro

**G4. Abierta. Describa una iniciativa, piloto, logro o dificultad en sostenibilidad digital.**

**G5. Abierta. ¿Qué debería priorizar Colombia para acelerar Green IT y Green Software?**
