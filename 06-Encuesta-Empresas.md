# Encuesta para mapeo de las empresas en green IT

## Cuestionario

### Sección A — Perfil de la organización

**A1. ¿Cuál describe mejor a su organización?**

- [ ] Proveedor cloud, hosting o managed services
- [ ] Operador o proveedor de centro de datos
- [ ] Empresa de desarrollo de software / fábrica de software
- [ ] Consultora de cloud, DevOps, SRE o transformación digital
- [ ] Startup de producto digital / SaaS
- [ ] Organización usuaria de tecnología con infraestructura propia o híbrida
- [ ] Universidad, centro de investigación u organización sin ánimo de lucro
- [ ] Otro: ______

**A2. Tamaño aproximado de la organización en Colombia**

- [ ] 1–10 personas
- [ ] 11–50
- [ ] 51–200
- [ ] 201–500
- [ ] Más de 500
- [ ] Prefiero no responder

**A3. Ciudad(es) principal(es) de operación en Colombia**

- [ ] Bogotá–Región
- [ ] Medellín–Valle de Aburrá
- [ ] Cali–Valle del Cauca
- [ ] Barranquilla/Cartagena/Caribe
- [ ] Eje Cafetero
- [ ] Otra(s): ______
- [ ] Operación distribuida/nacional

**A4. Rol de quien responde**

- [ ] Dirección ejecutiva / CTO
- [ ] Arquitectura cloud o de software
- [ ] DevOps / SRE / plataforma
- [ ] Infraestructura / centro de datos
- [ ] Desarrollo de software
- [ ] Seguridad, riesgo, compliance o ESG
- [ ] FinOps / gestión financiera cloud
- [ ] Académico/investigación
- [ ] Otro: ______

**A5. Modelo principal de infraestructura utilizado por la organización**

- [ ] Principalmente on-premise
- [ ] Principalmente nube pública
- [ ] Híbrido
- [ ] Multi-cloud
- [ ] Edge / infraestructura distribuida
- [ ] No aplica / no conozco

---

### Sección B — Conocimiento y compromiso organizacional

Para las preguntas B1–B6 use la escala:

| Valor | Significado                                                            |
| ----: | ---------------------------------------------------------------------- |
|     0 | No existe / no se conoce                                               |
|     1 | Reconocemos el tema, pero no hay acciones formales                     |
|     2 | Hay iniciativas aisladas o pilotos                                     |
|     3 | Existe una práctica documentada y aplicada en parte de la organización |
|     4 | Está integrada, se mide periódicamente y se mejora                     |

**B1. Nivel de conocimiento interno sobre Green IT o sostenibilidad digital.**

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

**B2. Existencia de una política, objetivo, KPI o compromiso ambiental relacionado específicamente con TI, cloud o software.**

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

**B3. Inclusión de criterios de energía, carbono, hardware o ciclo de vida en decisiones de arquitectura o compra tecnológica.**

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

**B4. Formación o sensibilización del personal técnico en eficiencia energética, Green IT, cloud sostenible o Green Software.**

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

**B5. Existencia de responsables claros para sostenibilidad digital (rol, equipo o comité).**

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

**B6. Integración de sostenibilidad en procesos de proveedores, compras o licitaciones tecnológicas.**

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

**B7. ¿Qué términos conoce o utiliza su organización?** *(selección múltiple)*

- [ ] Green IT
- [ ] Green Cloud
- [ ] GreenOps
- [ ] Green Software Engineering
- [ ] Software Carbon Intensity (SCI)
- [ ] PUE (Power Usage Effectiveness)
- [ ] CUE (Carbon Usage Effectiveness)
- [ ] WUE (Water Usage Effectiveness)
- [ ] Scope 1, Scope 2 o Scope 3
- [ ] Ninguno de los anteriores

---

### Sección C — Medición y observabilidad

**C1. ¿Qué métricas de infraestructura o sostenibilidad se miden actualmente?** *(selección múltiple)*

- [ ] Consumo eléctrico total (kWh/MWh)
- [ ] Potencia (W/kW)
- [ ] Uso de CPU, memoria, disco o red
- [ ] Utilización de servidores/VMs/contenedores
- [ ] PUE
- [ ] CUE
- [ ] WUE
- [ ] Emisiones de carbono (CO2e)
- [ ] Intensidad de carbono de la red eléctrica
- [ ] Emisiones incorporadas/embodied carbon del hardware
- [ ] Residuos electrónicos o vida útil del hardware
- [ ] Energía o carbono por servicio, transacción, usuario, API o workload
- [ ] Ninguna de las anteriores
- [ ] No sé

**C2. ¿En qué nivel se pueden observar o atribuir métricas de energía/carbono?** *(selección múltiple)*

- [ ] Instalación / data center
- [ ] Servidor físico
- [ ] Máquina virtual
- [ ] Clúster Kubernetes
- [ ] Contenedor o pod
- [ ] Aplicación o microservicio
- [ ] Solicitud API / transacción / usuario
- [ ] Job de datos o IA
- [ ] No se mide a ese nivel
- [ ] No sé

**C3. ¿Qué herramientas o fuentes de datos utiliza?** *(selección múltiple)*

- [ ] Dashboard/BMS/DCIM del centro de datos
- [ ] Facturas o medidores eléctricos
- [ ] Cloud provider carbon dashboards
- [ ] Prometheus / Grafana
- [ ] OpenTelemetry
- [ ] Kepler / eBPF / RAPL / NVML
- [ ] Cloud Carbon Footprint u otra herramienta de estimación
- [ ] Herramienta ESG o de reporte corporativo
- [ ] Hojas de cálculo/manual
- [ ] Ninguna
- [ ] Otra: ______

**C4. ¿Con qué frecuencia se revisan indicadores de energía, eficiencia o emisiones de TI?**

- [ ] Nunca
- [ ] Sólo cuando hay un proyecto o incidente
- [ ] Anualmente
- [ ] Trimestralmente
- [ ] Mensualmente
- [ ] Semanalmente o en tiempo casi real
- [ ] No aplica / no sé

**C5. ¿La organización usa una unidad funcional para relacionar impacto y valor entregado?**

Ejemplos: kWh por transacción, gCO2e por llamada API, energía por usuario activo, energía por inferencia de IA.

- [ ] Sí, de manera sistemática
- [ ] Sí, en pilotos o algunos servicios
- [ ] No, pero nos interesa implementarlo
- [ ] No y no está en planes
- [ ] No sé

**C6. Si mide impacto, ¿qué dificulta más atribuir energía o carbono a un servicio concreto?** *(escoja hasta 3)*

- [ ] Falta de sensores o telemetría
- [ ] Infraestructura compartida/multi-tenant
- [ ] Dependencia de proveedores cloud
- [ ] Falta de datos de intensidad de carbono local
- [ ] Falta de herramientas o integración técnica
- [ ] Costos de implementación
- [ ] Falta de tiempo del equipo técnico
- [ ] Falta de conocimiento o capacitación
- [ ] No existe una necesidad de negocio clara
- [ ] Confidencialidad o gobernanza de datos
- [ ] Otro: ______

---

### Sección D — Prácticas de Green Cloud, GreenOps e infraestructura

Use nuevamente la escala 0–4 de madurez de la Sección B.

**D1. Consolidación, apagado programado o eliminación de recursos ociosos (servidores, VMs, entornos de prueba, almacenamiento).**

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

**D2. Rightsizing: ajuste de CPU, memoria, almacenamiento o capacidad de recursos a la demanda real.**

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

**D3. Autoscaling, planificación de capacidad o escalado basado en demanda.**

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

**D4. Selección de regiones/proveedores/tipos de hardware considerando eficiencia energética, renovables o huella de carbono.**

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

**D5. Gestión de ciclo de vida de equipos: reutilización, prolongación de vida útil, mantenimiento, disposición de RAEE.**

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

**D6. Uso de virtualización, contenedores, Kubernetes u orquestación para mejorar utilización y reducir capacidad ociosa.**

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

**D7. Uso de energía renovable, PPAs, certificados de energía renovable, microredes o generación propia.**

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4
- [ ] No aplica / no tengo información

**D8. ¿Se han evaluado prácticas de carbon-aware computing?**

Ejemplos: mover cargas no urgentes a horarios/regiones con electricidad de menor intensidad de carbono, limitar recursos, diferir jobs batch.

- [ ] Sí, están operando
- [ ] Sí, se ha hecho un piloto
- [ ] Se han discutido, pero no implementado
- [ ] No se han considerado
- [ ] No aplica / no sé

---

### Sección E — Prácticas de Green Software Engineering

Use la escala 0–4 de madurez.

**E1. Los requisitos no funcionales de sistemas incluyen objetivos de eficiencia, consumo, huella o uso responsable de recursos.**

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

**E2. La arquitectura de software se evalúa considerando consumo de cómputo, transferencia de datos, caché, almacenamiento o uso de infraestructura.**

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

**E3. Se realizan pruebas de rendimiento y carga antes de producción.**

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

**E4. Las pruebas de rendimiento incluyen alguna métrica energética o de carbono, además de latencia, throughput, errores y costo.**

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

**E5. CI/CD incorpora controles para evitar artefactos innecesarios, builds redundantes, ambientes ociosos o despliegues ineficientes.**

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

**E6. Se aplican prácticas de eficiencia de datos: retención, compresión, deduplicación, caché, reducción de transferencia o archivado.**

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

**E7. El equipo considera el impacto de dependencias, librerías, modelos de IA o servicios externos en el consumo de recursos.**

- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4

**E8. ¿Cuáles prácticas ya aplican?** *(selección múltiple)*

- [ ] Caché y reducción de llamadas redundantes
- [ ] Compresión y optimización de transferencia de datos
- [ ] Optimización de consultas y almacenamiento
- [ ] Control de logs, trazas y retención de datos
- [ ] Optimización de imágenes de contenedor
- [ ] Apagado/limpieza de ambientes efímeros
- [ ] Pruebas de rendimiento automatizadas
- [ ] Presupuestos de rendimiento o consumo
- [ ] Selección de algoritmos/modelos por eficiencia
- [ ] Ninguna / no aplica
- [ ] Otra: ______

---

### Sección F — IA, datos y workloads intensivos

**F1. ¿La organización opera o desarrolla workloads de IA, analítica avanzada, entrenamiento, inferencia o procesamiento intensivo de datos?**

- [ ] Sí, en producción
- [ ] Sí, en pilotos o investigación
- [ ] No
- [ ] No sé

> **Lógica:** si responde “No”, pasar a la Sección G.

**F2. ¿Qué cargas se ejecutan?** *(selección múltiple)*

- [ ] Entrenamiento de modelos de ML/IA
- [ ] Inferencia de modelos de ML/IA
- [ ] LLMs / asistentes generativos
- [ ] Analítica/ETL/ELT/big data
- [ ] Visión por computador
- [ ] Procesamiento científico/HPC
- [ ] Otro: ______

**F3. ¿Dónde se ejecutan principalmente esas cargas?**

- [ ] Nube pública
- [ ] On-premise
- [ ] Híbrido
- [ ] Edge/dispositivos locales
- [ ] SaaS/API de terceros
- [ ] No sé

**F4. ¿Miden o estiman el costo energético, de carbono, uso de GPU/CPU o eficiencia por workload de IA?**

- [ ] Sí, regularmente
- [ ] Sí, en experimentos/pilotos
- [ ] No, pero está planificado
- [ ] No
- [ ] No sé

**F5. ¿Qué métricas se usan para cargas de IA?** *(selección múltiple)*

- [ ] Uso de GPU/CPU/memoria
- [ ] Consumo eléctrico (kWh/J)
- [ ] Potencia (W)
- [ ] Energía por entrenamiento/inferencia
- [ ] Energía o carbono por token
- [ ] Energía o carbono por solicitud
- [ ] Latencia, throughput, TTFT u otras métricas de rendimiento
- [ ] Costo financiero por workload
- [ ] No se miden métricas específicas
- [ ] Otro: ______

**F6. ¿Qué acciones de eficiencia se han evaluado o aplicado en IA?** *(selección múltiple)*

- [ ] Selección de modelos más pequeños
- [ ] Cuantización
- [ ] Batch size/continuous batching
- [ ] Caching de resultados o prompts
- [ ] Límites de CPU/GPU/memoria
- [ ] Autoscaling de inferencia
- [ ] Planificación de jobs no urgentes
- [ ] Uso de modelos locales/open-weight
- [ ] Uso de APIs externas para evitar infraestructura propia
- [ ] Ninguna
- [ ] Otra: ______

**F7. En una escala de 1 a 5, ¿qué tan importante considera equilibrar rendimiento, costo y consumo energético en cargas de IA?**

- [ ] 1 — Nada importante
- [ ] 2
- [ ] 3
- [ ] 4
- [ ] 5 — Crítico para la organización

---

### Sección G — Barreras, incentivos y necesidades

**G1. ¿Cuáles son las principales barreras para adoptar Green IT/Green Software?** *(escoja máximo 5)*

- [ ] Falta de conocimiento técnico
- [ ] Falta de formación/capacitación
- [ ] Falta de tiempo o prioridad del equipo
- [ ] Falta de presupuesto
- [ ] Falta de herramientas de medición
- [ ] Falta de datos de energía o intensidad de carbono
- [ ] Dificultad de atribuir consumo a aplicaciones compartidas
- [ ] Ausencia de regulación o incentivos
- [ ] Falta de demanda de clientes
- [ ] Dificultad para demostrar retorno de inversión
- [ ] Riesgo de afectar rendimiento, disponibilidad o seguridad
- [ ] Dependencia de proveedores cloud o SaaS
- [ ] Falta de estándares locales claros
- [ ] No identificamos barreras relevantes
- [ ] Otra: ______

**G2. ¿Qué incentivos aumentarían más la adopción?** *(escoja máximo 3)*

- [ ] Ahorro demostrable de costos operativos
- [ ] Requisitos de clientes o licitaciones
- [ ] Estándares y guías técnicas locales
- [ ] Capacitación especializada
- [ ] Herramientas open source y casos de referencia
- [ ] Incentivos tributarios o financieros
- [ ] Certificaciones/reconocimiento público
- [ ] Regulación o reporte obligatorio
- [ ] Alianzas universidad–empresa–Estado
- [ ] Acceso a datos de intensidad de carbono de la red
- [ ] Otro: ______

**G3. ¿Qué tipo de apoyo sería más útil para su organización?**

- [ ] Diagnóstico de madurez Green IT/Green Software
- [ ] Guía de métricas y dashboards
- [ ] Formación técnica para equipos DevOps/SRE/desarrollo
- [ ] Guía para medición de huella cloud
- [ ] Casos de uso de IA eficiente
- [ ] Laboratorio/piloto con universidad
- [ ] Comunidad de práctica nacional
- [ ] No requerimos apoyo actualmente
- [ ] Otro: ______

**G4. Pregunta abierta: describa una iniciativa, piloto, logro o dificultad que su organización haya tenido en sostenibilidad digital.**

> Respuesta abierta. Máximo sugerido: 1.000 caracteres.

**G5. Pregunta abierta: ¿qué debería priorizar Colombia para acelerar Green IT y Green Software?**

> Respuesta abierta. Máximo sugerido: 1.000 caracteres.