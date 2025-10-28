# Summary of key DRHC practices across the six Well-Architected Framework pillars

## Operations: Achieving operational excellence for hybrid edge workloads

Operational excellence for hybrid edge workloads focuses on
effective system operations, gaining operational insights, and
continuous process improvement to deliver business value. It
involves understanding data residency regulations and
organizational policies, considering Recovery Time Objective
(RTO) and Recovery Point Objective (RPO), and being aware of
consequences of data residency violations or data loss. Key
steps include monitoring performance, managing incidents,
centralizing oversight, automating processes, updating policies,
and fostering continuous improvement to enhance operational
efficiency and reliability. For more information on Operational
excellence, see
[Operational
excellence pillar](../data-residency-hybrid-cloud-lens/operational-excellence.md "../data-residency-hybrid-cloud-lens/operational-excellence.md").

## Security: Protect information, systems, and assets through risk assessments and mitigation strategies, balanced with delivering business value

The security design principles for data residency focuses on
establishing control objectives, separating workloads based on
data residency needs. Configuring detection mechanisms for
unauthorized resource creation. Restrict physical access to AWS Outposts locations, and comply with environmental and networking
requirements. Control data access tightly, and use data recovery
mechanisms like snapshots, versioning, and replication on
Outposts. For more information on Security, see
[Security
pillar](../data-residency-hybrid-cloud-lens/security.md "../data-residency-hybrid-cloud-lens/security.md").

## Reliability: Build reliable infrastructure services

Verify application recovery or availability during component
failures (network, server, rack, and application). Deploy
multiple Outposts anchored to multiple Availability Zones for
high-availability and resiliency, and plan for disaster recovery
with Outposts or Local Zones. Monitor and forecast storage,
compute, and network capacity regularly while planning for high
availability during on-premises maintenance activities. For more
information on Reliability, see
[Reliability
pillar](../data-residency-hybrid-cloud-lens/reliability.md "../data-residency-hybrid-cloud-lens/reliability.md").

## Performance: Align services, configurations, and monitoring for efficient and adaptable workloads

Select the appropriate AWS services, Regions, and configurations
that align with your workload requirements, and consider factors
like latency, bandwidth, and data residency. Monitor performance
metrics end-to-end, and adjust resources accordingly. Embrace
modularity and loose coupling to easily integrate new
technologies as they emerge. Periodically review your
architecture, and make informed trade-offs based on evolving
application needs, technical requirements, and the expanding AWS
service offerings. For more information on Performance, see
[Performance
pillar](../data-residency-hybrid-cloud-lens/performance.md "../data-residency-hybrid-cloud-lens/performance.md").

## Cost optimization: Optimizing costs in hybrid cloud environments through tagging, monitoring, and workload placement strategies

Evaluate workload requirements to help determine the optimal
placement across on-premises, cloud, and hybrid edge
environments. Implement a tagging strategy for cost attribution
and resource governance across hybrid environments. Monitor and
optimize the utilization of fixed-capacity resources like
Outposts to provide maximum value. Optimize network
configuration and data transfer costs between these
environments. Hybrid architectures should be designed with cost
in mind, using local VPC peering and following networking best
practices. Regularly monitor and review your workloads to
identify opportunities for ongoing cost optimization over time.
For more information on Cost optimization, see
[Cost
optimization pillar](../data-residency-hybrid-cloud-lens/cost-optimization.md "../data-residency-hybrid-cloud-lens/cost-optimization.md").

## Sustainability: Prioritizing renewable energy, efficient resource utilization, and continuous optimization

While designing sustainable cloud solutions, prioritize Region
selection based on proximity to renewable energy sources and CO2
emissions. Align infrastructure scaling with demand through auto
scaling, monitoring, and right-sizing to optimize usage with
minimum resources. Optimize software architecture by refactoring
unnecessary components and resizing over-provisioned instances.
Manage data efficiently by removing redundant or unneeded data
to reduce storage requirements. Use the minimum hardware and
services necessary, continuously monitoring for more
energy-efficient options. Foster a culture of keeping workloads
up to date to adopt efficient features and improve overall
sustainability. For more information on Sustainability, see
[Sustainability
pillar](../data-residency-hybrid-cloud-lens/sustainability.md "../data-residency-hybrid-cloud-lens/sustainability.md").
