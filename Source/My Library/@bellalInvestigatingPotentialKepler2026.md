---
citationKey: bellalInvestigatingPotentialKepler2026
title: Investigating the Potential of Kepler Toward Power Observability for Sustainable Cloud Computing
itemType: journalArticle
creators:
  - Zouhir Bellal
  - Laaziz Lahlou
  - Nadjia Kara
  - Timothy Murphy
  - Tan Phat Nguyen
  - Arif Ahmed
  - Mario Perez-Jimenez
publication: IEEE Transactions on Green Communications and Networking
date: "2026"
year: 2026
url: https:__ieeexplore.ieee.org_abstract_document_11371310
doi: 10.1109_TGCN.2026.3660816
tags:
  - "#Accuracy"
  - "#Artificial_intelligence"
  - "#Cloud_computing"
  - "#Containers"
  - "#Energy_consumption"
  - "#Hardware"
  - "#Kepler_accuracy_validation"
  - "#Monitoring"
  - "#Observability"
  - "#Power_demand"
  - "#Power_monitoring"
  - "#Servers"
  - "#cloud_power_observability"
  - "#container-level_power_monitoring"
  - "#power_accuracy_validation_framework"
zotflow-locked: true
zotero-key: RVUUAWG7
item-version: 407
library-id: 20202832
fuente: Google Scholar
---
---
citationKey: bellalInvestigatingPotentialKepler2026
title: Investigating the Potential of Kepler Toward Power Observability for Sustainable Cloud Computing
itemType: journalArticle
creators:
  - Zouhir Bellal
  - Laaziz Lahlou
  - Nadjia Kara
  - Timothy Murphy
  - Tan Phat Nguyen
  - Arif Ahmed
  - Mario Perez-Jimenez
publication: IEEE Transactions on Green Communications and Networking
date: "2026"
year: 2026
url: https:__ieeexplore.ieee.org_abstract_document_11371310
doi: 10.1109_TGCN.2026.3660816
tags:
  - "#Accuracy"
  - "#Artificial_intelligence"
  - "#Cloud_computing"
  - "#Containers"
  - "#Energy_consumption"
  - "#Hardware"
  - "#Kepler_accuracy_validation"
  - "#Monitoring"
  - "#Observability"
  - "#Power_demand"
  - "#Power_monitoring"
  - "#Servers"
  - "#cloud_power_observability"
  - "#container-level_power_monitoring"
  - "#power_accuracy_validation_framework"
zotflow-locked: true
zotero-key: RVUUAWG7
item-version: 407
library-id: 20202832
fuente: Google Scholar
---
# Investigating the Potential of Kepler Toward Power Observability for Sustainable Cloud Computing

## Abstract
> Power monitoring is a cornerstone of sustainability efforts, especially as the energy demands of Artificial Intelligence _AI_ workloads continue to rise. However, accurately measuring power consumption in cloud-native environments remains challenging due to technical constraints such as fine-grained monitoring requirements and the high abstraction introduced by virtualization and containerization. Kepler _Kubernetes-based Efficient Power Level Exporter_, an open-source tool for container-level power monitoring, has emerged as a promising solution for cloud power observability. This paper outlines the key requirements for accurate power tracking in containerized environments and assesses Kepler’s alignment with these criteria. However, its precision remains unvalidated, mainly due to the lack of a systematic evaluation methodology. To fill this gap, we introduce a novel accuracy validation framework tailored to assess container-level power monitoring tools under dynamic controlled multi-tenancy environments, including CPU frequency scaling, C-state transitions, and varying co-runner workloads _i.e., co-hosted containers executing concurrently on other cores of the same processor socket_. Using this framework, we perform the first in-depth evaluation of Kepler’s accuracy in real-world cloud scenarios _e.g., dynamic power configuration settings, dynamic workloads_. Our results show that Kepler’s container-level power estimation exhibits a root mean squared error _RMSE_ of 11.9 Watts against the RAPL ground truth, corresponding to an overestimation of approximately 15_times . Its accuracy is highly sensitive to runtime factors such as CPU configuration and C-state transitions, which reveals critical limitations in Kepler’s current power model and highlights the need for refinement. This work establishes the foundation for more precise and effective power observability in cloud computing and paves the way for sustainable cloud computing.

## Notas clave
- **Análisis crítico de Kepler _Kubernetes-based Efficient Power Level Exporter_:** El paper evalúa la precisión de Kepler para el monitoreo de energía a nivel de contenedores en entornos de nube.
- **Hallazgo Técnico:** Kepler presenta una sobreestimación significativa de la energía _~15x_ con un RMSE de 11.9 W comparado con la verdad fundamental _RAPL ground truth_.
- **Factores de Error:** La precisión de Kepler es altamente sensible a los cambios de frecuencia de CPU y a las transiciones de C-state _estados de ahorro de energía del procesador_.
- **Importancia para la investigación:** Demuestra que confiar ciegamente en herramientas de observabilidad de código abierto puede llevar a errores graves en la medición de la eficiencia energética de la nube.
- **Citable para:** la sección de "Tecnología_Infraestructura" para justificar la necesidad de marcos de validación de precisión antes de implementar soluciones de Green Cloud en Colombia.

## Notes