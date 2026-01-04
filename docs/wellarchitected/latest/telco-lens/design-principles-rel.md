# Design principles

- **Scalability:** Telecommunication networks need to
  dynamically adapt to subscriber growth and usage patterns. The network needs to be elastic
  and adjusted to the changes. Reliability can be achieved by distributing users and data to
  multiple resources and scale horizontally instead of vertically. The Communication
  Services Providers (CSPs) can use micro-services architecture and container-based
  technologies for agile delivery. This architecture provides high resiliency, better
  failure handling, efficient use of resources and scale.
- **Failure recovery:** Telecommunication networks need to
  provide reliable connectivity to the subscribers. Failure can occur from a small component
  level in software or hardware to a site level. CSPs should have a mechanism to detect
  service level SLAs which can be translated to technical Key Performance Indicators (KPIs)
  and try to automatically recover from the failure or have a fail-over to other working
  resource or site. The KPIs should be used to proactively detect failures and be able to
  mitigate prior to the occurrence.
- **Application architecture:** The reliability requirements
  vary from application to application. While some applications are tolerant to latency,
  other applications such as Ultra Reliable and Low Latency Communication (uRLLC) have
  stringent latency and jitter requirements. The CSPs prefer to have the network closer to
  the customer to offer better user experience and to provide high performance multimedia,
  real-time applications. The user plane is usually brought closer to the end user, and the
  control plane network functions can be placed in the central location.
- **Regulatory adherence:** Telecommunication industry is
  highly regulated and needs to meet regulatory requirements and standards. Special design
  considerations are needed to meet regulatory requirements. For example, the network should
  allow emergency calls reliably and to achieve that, resilient systems and networks are
  needed across the global cloud infrastructure.
