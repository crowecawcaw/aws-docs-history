# DRHCREL05-BP02 To mitigate the impact of Availability Zone or Region failures, deploy multiple Outposts anchored to different Availability Zones or Regions

Design workloads across multiple AWS Outposts to ensure resilience
against failures through load balancing and failover capabilities,
similar to multi-AZ architectures in AWS Regions.

**Desired outcome:** Achieve a
highly available and fault-tolerant hybrid infrastructure that can
withstand failures while consistently meeting data residency
requirements by using multiple availability zones or Regions for
Outposts.

**Benefits of establishing this best
practice:** Deploying multiple Outposts across different
Availability Zones or Regions enhances reliability and
availability while maintaining data residency compliance.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Design your workload to operate in a distributed, multi-Outpost
deployment model, similar to architectural patterns used on AWS.
Mitigate the risk of rack, data center, or AWS Availability Zone
and Region failures by deploying infrastructure across multiple
locations, carefully architecting applications to run across
separate logical Outposts, and using distributed multi-Outpost
deployment models.

In
[such
architectures](../reliability-pillar/rel_fault_isolation_multiaz_region_system.md "../reliability-pillar/rel_fault_isolation_multiaz_region_system.md"), while the application servers may be
spread across different Outposts, customers can load balance
traffic across Outposts during failover through their
Application Load Balancers (ALB) and Amazon Route 53.
