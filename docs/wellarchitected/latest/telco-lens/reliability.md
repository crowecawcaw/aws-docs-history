

# Reliability
<a name="reliability"></a>

 Reliability in telecommunications networks refers to the ability of the network to provide services without interruption or failure under normal and peak network load conditions. The reliability pillar addresses the ability of a network to recover from infrastructure or service disruptions, dynamically acquire computing and networking resources to meet demand, and mitigate disruptions such as misconfigurations or transient network issues. 

## Capabilities
<a name="rel-capabilities"></a>
+ [Foundations](telcorel01.md)
+ [Workload architecture](telcorel02.md)
+ [Change management](telcorel03.md)
+ [Failure management](telcorel04.md)

## Design principles
<a name="rel-design-principles"></a>
+  **Scalability:** Telecommunication networks need to dynamically adapt to subscriber growth and usage patterns. The network needs to be elastic and adjusted to the changes. Reliability can be achieved by distributing users and data to multiple resources and scaling horizontally instead of vertically. The Communication Services Providers (CSPs) can use microservices architecture and container-based technologies for agile delivery. This architecture provides high resiliency, better failure handling, efficient use of resources, and scale. 
+  **Failure recovery:** Telecommunication networks need to provide reliable connectivity to the subscribers. Failure can occur from a small component level in software or hardware to a site level. CSPs should have a mechanism to detect service-level SLAs, which can be translated to technical Key Performance Indicators (KPIs), and try to automatically recover from the failure or fail over to another working resource or site. The KPIs should be used to proactively detect failures and be able to mitigate before the occurrence. 
+  **Application architecture:** The reliability requirements vary from application to application. While some applications are tolerant to latency, other applications such as Ultra-Reliable Low-Latency Communication (URLLC) have stringent latency and jitter requirements. The CSPs prefer to have the network closer to the customer to offer better user experience and to provide high-performance multimedia, real-time applications. The user plane is usually brought closer to the end user, and the control plane network functions can be placed in the central location. 
+  **Regulatory adherence:** The telecommunications industry is highly regulated and needs to meet regulatory requirements and standards. Special design considerations are needed to meet regulatory requirements. For example, the network should allow emergency calls reliably, and to achieve that, resilient systems and networks are needed across the global cloud infrastructure. 