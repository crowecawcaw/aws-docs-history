

# RTB Fabric resilience
<a name="advrel05"></a>

 RTB Fabric defaults to single-AZ, single-Region deployment. A failure at either scope, whether an Availability Zone impairment or a regional outage, causes a complete loss of bid connectivity unless every layer of the stack (gateways, compute, and stateful dependencies) is explicitly deployed for multi-AZ and multi-Region availability. Every layer must hold for the design to work. Multi-AZ gateways provide no protection if the bid-processing pipeline depends on a single-AZ database, and a second Region provides no protection if partner failover is undefined or capacity is under-provisioned. 


|  ADVREL05: How do you keep your RTB Fabric workload available during single-AZ and single-Region failures?  | 
| --- | 
| [ADVREL05-BP01 Deploy partner-facing bid gateways across multiple Availability Zones](advrel05-bp01.md) | 
| [ADVREL05-BP02 Monitor Availability Zone-level health and detect asymmetric failures](advrel05-bp02.md) | 
| [ADVREL05-BP03 Deploy partner-facing bid gateways in multiple AWS Regions](advrel05-bp03.md) | 
| [ADVREL05-BP04 Monitor partner-facing bid gateway health independently per Region](advrel05-bp04.md) | 
| [ADVREL05-BP05 Maintain independent operational readiness in each Region](advrel05-bp05.md) | 

## Capability intent
<a name="advrel05-capability-intent"></a>
+  RTB Fabric gateways are deployed across at least two Availability Zones, colocated with the Availability Zones where DSP/SSP compute runs, so that a single-AZ failure doesn't interrupt bid connectivity. 
+  Every stateful dependency in the critical bid path (databases, caches, and message queues) is Multi-AZ with automatic failover tested against the bid response latency budget. 
+  RTB Fabric gateways are deployed in at least two AWS Regions, with exchange partners able to route to either Region through a deliberate failover architecture (partner-managed, [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/), or [Amazon Route 53](https://aws.amazon.com/route53/)). 
+  Availability Zone-aware and Region-aware monitoring detects asymmetric and partial degradation before it erodes bid win rates unnoticed. 
+  Each Region maintains independent operational readiness (deployment artifacts, capacity, and automated failover) so the surviving Region operates without depending on the impaired Region's control plane. 

## Common issues to watch for
<a name="advrel05-common-issues-to-watch-for"></a>
+  Multi-AZ gateways paired with a single-AZ database or cache, leaving the bid pipeline exposed despite gateway redundancy. 
+  Gateways deployed in Availability Zones that have no compute fleet, adding cross-AZ latency without any resilience benefit. 
+  Monitoring that treats Availability Zone health as binary (up or down) and misses partial degradation such as increased latency or packet loss. 
+  Centralizing deployment artifacts or operational tooling in the primary Region, so a regional impairment removes the ability to manage the surviving Region. 
+  Relying on scaling up the secondary Region during an event when the control plane needed to provision gateways may itself be impaired. 
+  Aggregating gateway metrics across Regions, which masks a single degraded Region. 
+  Automatic failback to a still-recovering Region, causing a second outage. 