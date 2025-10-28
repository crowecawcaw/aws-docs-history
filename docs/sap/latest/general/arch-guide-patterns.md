# Patterns

In this section, we examine the architecture patterns available to handle the failure scenarios detailed above.

There are two key parameters to consider when selecting a pattern to meet your organization’s specific business requirements:

- Availability of compute for the SAP single points of failure
- Availability of the SAP data persisted on Amazon EBS
  These parameters determine the time taken to recover from a failure scenario, that is, the time taken by your SAP system to return to service.

_Types of architecture patterns_

The architecture patterns are grouped into single Region and multi-Region patterns. The distinguishing factor would be:

1. If you require the data to only reside in a specific geographical location (AWS Region) at all times (for example, data residency requirements).

or 2. If you require the data to reside in two specific geographical locations (AWS Regions) at all times (for example, two copies of SAP data must reside at least 500 miles apart for compliance).
If your production systems are critical to your business and you require minimal downtime in the event of failure, you should select a Multi-Region pattern to ensure that your production systems are highly available at all times. When deploying a Multi-Region pattern, you can benefit from using an automated approach (such as, Cluster solution) for fail over between Availability Zones to minimize the overall downtime and remove the need for human intervention. Multi-Region patterns not only provide high availability but also disaster recovery, thereby lowering overall costs.
