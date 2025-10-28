# DRHCREL01-BP01 Set service quotas to accommodate for the peak usage of AWS resources on Outposts for their homed Regions

AWS Outposts and Local Zones adhere to the service quotas of their
parent AWS Regions, requiring management of service quotas to
accommodate peak usage.

**Desired outcome:** Proactively
adjust service quotas to meet your capacity requirements in
specific Regions, which helps you maintain data residency in those
Regions.

**Benefits of establishing this best
practice:** Proper service quota management and planning
validates availability of AWS resources on Outposts and Local
Zones, reducing the risk of service disruptions due to resource
limitations.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

[AWS Outposts](../../../outposts/latest/userguide/what-is-outposts.md "../../../outposts/latest/userguide/what-is-outposts.md") and
[AWS Local Zones](../../../local-zones/latest/ug/what-is-aws-local-zones.md "../../../local-zones/latest/ug/what-is-aws-local-zones.md") are homed to specific
[AWS Regions](../../../AmazonRDS/latest/UserGuide/Concepts.md "../../../AmazonRDS/latest/UserGuide/Concepts.md"). Regional
[service
quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md") apply to AWS resources (for example, Amazon EC2
instances) running on Outposts or Local Zones and should be
managed. The best practices
to [manage
service quotas and constraints](../reliability-pillar/manage-service-quotas-and-constraints.md "../reliability-pillar/manage-service-quotas-and-constraints.md") apply to the Regions that
the chosen Outposts or Local Zones are homed to. Apply
[service
quotas best practices](../reliability-pillar/manage-service-quotas-and-constraints.md "../reliability-pillar/manage-service-quotas-and-constraints.md") to Outpost and Local Zones.
