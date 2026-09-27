# Encuesta para mapeo de empresas en Green IT / Green Software

**Objetivo:** medir madurez cuantitativa y obtener insumos cualitativos para análisis temático con Taguette.
**Formato:** Google Forms. **Tiempo estimado:** 15–20 minutos. **Perfil de respuesta:** perfiles técnicos o gerenciales de empresas de tecnología (CTO, arquitectura, DevOps/SRE, infraestructura, desarrollo, ESG, FinOps, academia).

---

## Portada del formulario (texto inicial)

> **Sostenibilidad digital en empresas de tecnología colombianas**
>
> Esta encuesta busca entender cómo las empresas de tecnología en Colombia incorporan (o no) la eficiencia energética y la sostenibilidad en su infraestructura y su software. Forma parte de una investigación académica de la Universidad Distrital Francisco José de Caldas basada en una revisión sistemática de literatura (PRISMA 2020) sobre Green Cloud, Green DevOps y Green Software Engineering.
>
> - No hay respuestas correctas ni incorrectas; esto no es un examen.
> - Duración estimada: 15 a 20 minutos.
> - Puede responder "No sé" o "No aplica" en cualquier punto.
> - Puede saltarse preguntas abiertas que no quiera contestar.
>
> **Consentimiento informado:** La participación es voluntaria y las respuestas son confidenciales. Los datos se tratarán conforme a la Ley 1581 de 2012 y el Decreto 1377 de 2013. No se identificará su organización en ningún reporte final; los resultados se reportarán de forma agregada. Al continuar, usted acepta que sus respuestas se usen con fines de investigación académica.
>
> - [ ] Acepto participar *(obligatorio para continuar)*

---

## Sección A — Perfil de la organización

> *Intro en Forms:* "Primero, unos datos básicos para contextualizar sus respuestas."

**A1. ¿Cuál de estas descripciones se acerca más a su organización?** *(opción múltiple / lista desplegable)*
- Proveedor de cloud, hosting o servicios administrados
- Operador o proveedor de centro de datos
- Empresa de desarrollo de software / fábrica de software
- Consultora de cloud, DevOps, SRE o transformación digital
- Startup de producto digital / SaaS
- Organización usuaria de tecnología con infraestructura propia o híbrida
- Universidad, centro de investigación u organización sin ánimo de lucro
- Otro: ______

**A2. ¿Qué tan grande es su organización en Colombia?** *(opción múltiple / lista desplegable)*
- 1–10 personas
- 11–50
- 51–200
- 201–500
- Más de 500
- Prefiero no responder

**A3. ¿Desde dónde opera principalmente?** *(casillas de verificación)*
- Bogotá y región
- Medellín / Valle de Aburrá
- Cali / Valle del Cauca
- Barranquilla, Cartagena o Caribe
- Eje Cafetero
- Otra(s): ______
- Operación distribuida a nivel nacional

**A4. ¿Cuál es su rol?** *(opción múltiple / lista desplegable)*
- Dirección ejecutiva / CTO
- Arquitectura de cloud o de software
- DevOps / SRE / plataformas
- Infraestructura / centro de datos
- Desarrollo de software
- Seguridad, riesgo, compliance o ESG
- FinOps / gestión financiera de cloud
- Académico o investigación
- Otro: ______

**A5. Responde en nombre de...** *(opción múltiple)*
- Mi equipo o área
- Toda la organización
- No estoy seguro(a)

**A6. ¿Cuál es el modelo principal de infraestructura de su organización?** *(opción múltiple / lista desplegable)*
- Principalmente servidores propios (on-premise)
- Principalmente nube pública
- Híbrido (propios + nube)
- Varias nubes a la vez (multi-cloud)
- Edge / infraestructura distribuida
- No aplica / No sé

---

## Sección B — Conocimiento y compromiso

> *Intro en Forms:* "Ahora, qué tan presente está la sostenibilidad en su organización. Marque el número que mejor describa la situación real de hoy:"
>
> **Escala 0–4 (se muestra en la cabecera de la cuadrícula):**
> - 0 = No existe o no conozco
> - 1 = Conocemos el tema, pero no hay acciones formales
> - 2 = Hay pilotos o iniciativas aisladas
> - 3 = Práctica documentada, aplicada en parte de la organización
> - 4 = Integrada: se mide periódicamente y se mejora

**B. ¿Cómo está la sostenibilidad digital en su organización?** *(cuadrícula de opción múltiple; una sola pregunta en Forms; filas B1–B6)*

Filas:
1. El tema de Green IT / sostenibilidad digital es conocido internamente
2. Existe una política, meta o indicador escrito sobre el impacto ambiental de TI, cloud o software
3. Al diseñar arquitectura o comprar tecnología se tiene en cuenta el consumo de energía, las emisiones o el ciclo de vida de los equipos
4. El personal técnico recibe formación o sensibilización sobre sostenibilidad digital
5. Hay personas con responsabilidad clara sobre estos temas
6. La sostenibilidad se tiene en cuenta al contratar proveedores, hacer compras o participar en licitaciones

**B7. Abierta — ¿Cómo entiende su organización el Green IT o el software verde? ¿Qué términos usan internamente para hablar de esto?** *(párrafo)* **[abierta de oro para el codebook]**

**B8. Abierta — Si piensa en por qué todavía no se han adoptado estas prácticas a fondo, ¿qué cree que pesa más?** *(párrafo)*

---

## Sección D — Infraestructura y nube

> *Intro en Forms:* "Ahora las prácticas concretas de infraestructura y nube. Misma escala 0–4 de la sección anterior."

**D. Prácticas de infraestructura y nube** *(cuadrícula de opción múltiple; filas D1–D7)*

Filas:
1. Apagamos o consolidamos recursos que no se usan (servidores ociosos, ambientes encendidos sin uso)
2. Ajustamos la capacidad (CPU, memoria, almacenamiento) a la demanda real, sin sobre-dimensionar
3. Usamos autoescalado o planificación de capacidad para evitar recursos de sobra
4. Elegimos región, proveedor o hardware considerando eficiencia energética o uso de renovables
5. Gestionamos el fin de vida de los equipos: reutilización, extensión de uso o disposición adecuada de residuos electrónicos (RAEE)
6. Usamos virtualización, contenedores u orquestación para aprovechar mejor la infraestructura
7. Compramos o usamos energía renovable (acuerdos directos de compra, certificados de energía limpia, microrredes)

**D8. ¿Han considerado mover cargas de trabajo a horarios o regiones donde hay más energía renovable disponible (computación consciente del carbono)?** *(opción múltiple)*
- Sí, ya lo hacemos en producción
- Sí, como piloto o prueba
- Lo hemos discutido, pero no lo hemos implementado
- No lo hemos considerado
- No aplica

**D9. ¿Qué tanto pesa la seguridad energética del país (sequías, racionamientos, variabilidad asociada a El Niño) en la planeación de su infraestructura de TI?** *(escala lineal 1 a 5)*
- 1 = No se considera para nada
- 5 = Es un eje central de nuestra planeación

**D10. Abierta — ¿Qué práctica de infraestructura les ha generado el mayor ahorro, o la mayor resistencia interna, y por qué?** *(párrafo)* **[abierta de oro para el codebook]**

---

## Sección E — Desarrollo de software

> *Intro en Forms:* "Y ahora, en el software en sí. Misma escala 0–4."

**E. Prácticas en el desarrollo y la operación del software** *(cuadrícula de opción múltiple; filas E1–E6)*

Filas:
1. Los requisitos del software incluyen metas de eficiencia, consumo energético o huella de carbono
2. Evaluamos arquitecturas considerando cómputo, transferencia de datos, caché y almacenamiento
3. Las pruebas de rendimiento revisan también consumo de energía o emisiones
4. Nuestros pipelines de CI/CD evitan compilaciones redundantes o ambientes encendidos sin uso
5. Aplicamos prácticas de eficiencia de datos: retención, compresión, deduplicación, caché
6. Consideramos el impacto de dependencias, librerías, modelos de IA o servicios externos que usamos

**E7. Abierta — ¿Qué es lo que más les cuesta para incorporar eficiencia energética al diseñar software?** *(párrafo)*

---

## Sección C — Medición y observabilidad

> *Intro en Forms:* "¿Cómo miden (o no) el impacto energético de lo que operan?"

**C1. ¿Qué miden hoy sobre consumo y emisiones de su infraestructura o servicios?** *(casillas de verificación)*
- Consumo eléctrico (kWh)
- PUE (eficiencia energética del centro de datos: cuánta energía se pierde en refrigeración y soporte vs. en cómputo)
- Emisiones de carbono (CO₂e)
- Intensidad de carbono de la red eléctrica (gCO₂e por kWh)
- Emisiones incorporadas del hardware (fabricación, transporte, disposición)
- Energía o carbono por servicio, por transacción o por usuario
- Utilización de servidores o máquinas virtuales
- Uso de agua
- Ninguna *(opción exclusiva)*
- No sé *(opción exclusiva)*

**C2. ¿Hasta qué nivel pueden saber cuánto gasta cada cosa?** *(casillas de verificación)*
- Instalación o centro de datos completo
- Servidor individual
- Máquina virtual
- Clúster de contenedores (Kubernetes)
- Contenedor
- Aplicación o microservicio
- Solicitud API o transacción
- Job de datos o IA
- No se mide

**C3. ¿Con qué herramientas o fuentes miden o estiman esto?** *(casillas de verificación)*
- BMS o DCIM (sistemas del centro de datos)
- Facturas de energía o medidores
- Paneles del proveedor de nube
- Prometheus / Grafana
- OpenTelemetry
- Kepler / eBPF
- Cloud Carbon Footprint
- Herramienta ESG interna o de terceros
- Hojas de cálculo
- Otra: ______

**C4. ¿Con qué frecuencia revisan estos indicadores?** *(opción múltiple / lista desplegable)*
- Nunca
- Solo cuando hay un proyecto o incidente
- Una vez al año
- Trimestralmente
- Mensualmente
- Semanal o en tiempo casi real
- No aplica

**C5. ¿Relacionan el impacto ambiental con el valor que entrega el servicio?** *(opción múltiple / lista desplegable)*
- Sí, de forma sistemática
- Sí, en pilotos
- No, pero nos interesa
- No, y no está en nuestros planes
- No sé

*Texto de ayuda:* "Ejemplo: saber cuántas emisiones genera cada transacción, cada usuario activo o cada informe generado, para decidir si el gasto energético se justifica."

**C6. Cuando intentan atribuir energía o carbono a un servicio, ¿qué se lo dificulta más?** *(casillas de verificación — texto de ayuda: "Marque máximo 3")*
- Falta de sensores o medición directa
- Infraestructura compartida (es difícil separar quién gasta qué)
- Dependencia de proveedores de nube
- No hay datos de intensidad de carbono de la red en Colombia
- Faltan herramientas
- Costos
- Falta de tiempo
- Falta de conocimiento
- No hay una necesidad de negocio clara
- Otro: ______

**C7. Abierta — Cuéntenos un caso donde la falta de datos o de herramientas les impidió actuar sobre la huella de algún servicio.** *(párrafo)*

---

## Sección F — IA y cargas intensivas

> *Intro en Forms:* "Esta sección solo aplica si su organización opera o desarrolla cargas de IA, analítica pesada o HPC. Si no, puede saltar al final."
> *Configuración en Forms: F1 con salto de sección — "No" o "No sé" llevan a Sección G.*

**F1. ¿Su organización opera o desarrolla cargas de IA, analítica pesada o HPC?** *(opción múltiple)*
- Sí, en producción
- Sí, en piloto
- No
- No sé

**F2. ¿Qué tipo de cargas ejecutan?** *(casillas de verificación)*
- Entrenamiento de modelos de ML/IA
- Inferencia
- LLMs (modelos de lenguaje)
- Analítica / ETL
- Visión por computadora
- HPC (cómputo de alto rendimiento)
- Otro: ______

**F3. ¿Dónde se ejecutan?** *(casillas de verificación)*
- Nube pública
- Servidores propios
- Híbrido
- Edge
- SaaS de terceros

**F4. ¿Miden o estiman la energía o el carbono de esas cargas?** *(opción múltiple)*
- Sí, regularmente
- Sí, como piloto
- No, pero lo tenemos planeado
- No
- No sé

**F5. Si miden, ¿qué métricas usan para la IA?** *(casillas de verificación)*
- Uso de GPU / CPU
- Consumo eléctrico
- Energía por entrenamiento o inferencia
- Energía o carbono por token o por solicitud
- Costo financiero
- Ninguna *(opción exclusiva)*

**F6. ¿Qué acciones de eficiencia aplican en estas cargas?** *(casillas de verificación)*
- Usar modelos más pequeños o locales
- Cuantización
- Procesamiento por lotes (batching)
- Caching
- Límites de recursos
- Autoescalado
- Planificación de jobs en horarios específicos
- Ninguna *(opción exclusiva)*

**F7. ¿Qué tan importante les resulta equilibrar rendimiento, costo y consumo energético en la IA?** *(escala lineal 1 a 5)*
- 1 = No es prioridad
- 5 = Es una decisión de diseño permanente

**F8. Abierta — ¿Cómo equilibran hoy rendimiento, costo y consumo energético en sus cargas de IA?** *(párrafo)* **[abierta de oro para el codebook]**

---

## Sección G — Barreras, incentivos y necesidades

> *Intro en Forms:* "Ya casi terminamos. Estas últimas preguntas son sobre lo que falta para avanzar."

**G1. ¿Cuáles son las principales barreras que hoy les impiden avanzar en sostenibilidad digital?** *(casillas de verificación — texto de ayuda: "Marque hasta 5")*
- Falta de conocimiento o formación del equipo
- Falta de tiempo o prioridad
- Falta de presupuesto
- Faltan herramientas de medición
- No hay datos de contexto (p. ej., intensidad de carbono de la red en Colombia)
- Es difícil atribuir impactos a servicios concretos
- No hay regulación ni incentivos que lo pidan
- No hay demanda de los clientes
- Es difícil demostrar el retorno (ROI)
- Riesgo para el rendimiento o la seguridad
- Dependencia de proveedores de nube
- No hay estándares locales
- Otra: ______
- Ninguna *(opción exclusiva)*

**G2. Imaginen que mañana existen estos apoyos: ¿cuáles les moverían más la aguja?** *(casillas de verificación — texto de ayuda: "Marque hasta 3")*
- Ahorro de costos medible
- Requisitos de clientes o de licitaciones públicas
- Estándares o guías claras
- Capacitación técnica
- Herramientas open source
- Incentivos tributarios
- Certificaciones verificables
- Regulación de reporte obligatorio
- Alianzas entre universidades, empresas y el Estado
- Acceso a datos abiertos (p. ej., intensidad de carbono de la red)
- Otro: ______
- Ninguno / no necesitamos incentivos *(opción exclusiva)*

**G3. Si mañana una licitación pública o de un cliente grande pidiera criterios de eficiencia energética o software verde, su organización...** *(opción múltiple)*
- Podría cumplirlos hoy
- Podría cumplirlos con ajustes menores
- Necesitaría apoyo técnico para cumplirlos
- No participaría
- No aplica

**G4. ¿Qué tipo de apoyo externo les sería más útil?** *(opción múltiple / lista desplegable)*
- Diagnóstico de madurez
- Guía de métricas y tableros
- Formación técnica del equipo
- Guía de medición de huella en la nube
- Casos de uso de IA eficiente
- Laboratorio piloto con universidad
- Comunidad de práctica con otras empresas
- No requerimos apoyo
- Otro: ______

**G5. Para cerrar: ¿cuánto de lo que respondió puede respaldarse con documentos, tableros o indicadores reales de su organización?** *(opción múltiple)*
- Todo o casi todo
- Una parte importante
- Poco
- Nada
- Prefiero no responder

**G6. Abierta — Cuéntenos una iniciativa, piloto, logro o dificultad concreta que hayan vivido en torno a la sostenibilidad digital.** *(párrafo)*

**G7. Abierta — Si usted pudiera definir la agenda: ¿qué debería priorizar Colombia para acelerar el Green IT y el software verde?** *(párrafo)* **[abierta de oro para el codebook]**

---

## Cierre del formulario

> **Gracias por su tiempo.**
>
> Si quiere recibir el informe con los resultados agregados del estudio cuando esté listo, o si está dispuesto(a) a una conversación de seguimiento breve, déjenos su correo corporativo (opcional): ______
>
> Los resultados se publicarán de forma agregada y anónima como parte de una investigación académica de la Universidad Distrital Francisco José de Caldas.

---

## Notas para la investigadora (esta sección no va en el formulario)

### Mapeo sección → investigación

| Sección | Alimenta | Dimensión medida |
|---|---|---|
| A | RQ1 (contexto) | Perfil del respondiente |
| B | RQ2, RQ3 + brecha política/estándares/formación | Compromiso organizacional (escala 0–4 anclada) |
| D | RQ2, RQ3 + brecha infraestructura | Prácticas operativas (0–4) + señal ENSO (D9) + carbon-aware (D8) |
| E | RQ3 + brecha formación/estándares | Prácticas de ingeniería (0–4) |
| C | RQ3 + brecha investigación aplicada/infraestructura | Capacidad de medición y atribución |
| F | RQ1, RQ3 | Madurez en workloads intensivos (IA) |
| G | RQ2, RQ4 | Barreras, incentivos, disposición a licitación verde (G3) |

### Escala de madurez (anclajes por punto, se muestran una vez por sección en Forms)

0 = No existe o no conozco · 1 = Conocemos el tema sin acciones formales · 2 = Pilotos o iniciativas aisladas · 3 = Práctica documentada parcial · 4 = Integrada, medida y con mejora continua.

### Limitaciones conocidas del instrumento (declarar en el informe)

1. **Auto-selección:** quienes responden una encuesta de sostenibilidad digital tienden a sobre-representar madurez; los promedios se leen como techo, no como piso.
2. **Auto-reporte:** G5 (filtro de evidencia documental) permite ponderar la confianza de las respuestas al reportar resultados.
3. **Cobertura geográfica:** el plan de contactos debe forzar diversidad fuera de Bogotá para no sesgar a la capital.

### Abiertas priorizadas para el codebook de Taguette

Ejes temáticos (derivados de las brechas del artículo): **(1) definición/delimitación del Green IT interno, (2) barreras y resistencias, (3) prácticas e infraestructura, (4) política pública y agenda nacional.** Las cuatro abiertas de oro (B7, D10, F8, G7) se codifican primero; las demás se codifican en segunda pasada.
