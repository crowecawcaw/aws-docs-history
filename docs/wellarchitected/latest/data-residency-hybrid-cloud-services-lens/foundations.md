# Foundations

| DRHCREL01: How do you manage Service Quotas for resources running in AWS Local Zones and AWS Outposts? |
| ------------------------------------------------------------------------------------------------------ |
|                                                                                                        |

For cloud-based workload architectures, there are Service Quotas
(also referred to as service limits). These quotas exist to
prevent accidentally provisioning more resources than you need and
to limit request rates on API operations to protect services from
abuse. Both
[AWS Local Zones](../../../local-zones/latest/ug/what-is-aws-local-zones.md "../../../local-zones/latest/ug/what-is-aws-local-zones.md") and
[AWS Outposts](../../../outposts/latest/userguide/what-is-outposts.md "../../../outposts/latest/userguide/what-is-outposts.md") are homed to specific
[AWS Regions](../../../AmazonRDS/latest/UserGuide/Concepts.md "../../../AmazonRDS/latest/UserGuide/Concepts.md"). Regional
[service
quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md") apply to AWS resources (for example, Amazon EC2
instances) running on Local Zones or Outposts.

| DRHCREL02: Do you have redundant power<br>and network to on-premises AWS components? |
| ------------------------------------------------------------------------------------ |
|                                                                                      |

AWS Outposts depends on a resilient connection to its anchor
Availability Zone for management, monitoring, and service
operations to function properly. Redundant network connections
for each Outpost are needed for reliable connectivity back to
the anchor points in the AWS Cloud. Outposts have
[documented
power requirements](../../../outposts/latest/userguide/outposts-requirements.md "../../../outposts/latest/userguide/outposts-requirements.md"), and it is recommended to provide dual
power sources for resilience in case of power failure.

###### Best practices

- [DRHCREL01-BP01 Set service quotas to accommodate for the peak usage of AWS resources on Outposts for their homed Regions](drhcrel01-bp01.md "drhcrel01-bp01.md")
- [DRHCREL02-BP01 Provision redundant power and network to on-premises components](drhcrel02-bp01.md "drhcrel02-bp01.md")
- [DRHCREL02-BP02 Use AWS Direct Connect with redundant tunnels and connections to the AWS Region for Outposts control plane actions and high availability requirements](drhcrel02-bp02.md "drhcrel02-bp02.md")
