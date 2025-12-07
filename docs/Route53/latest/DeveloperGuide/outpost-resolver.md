# What is Amazon Route 53 on Outposts?

AWS Outposts is a fully managed service that extends AWS infrastructures, services, APIs,
and tools to customer premises. This allows customers to run AWS services with on-premises
workloads by using the same programming interfaces as in AWS Regions. For more
information, see [What is AWS Outposts?](../../../outposts/latest/userguide/what-is-outposts.md "../../../outposts/latest/userguide/what-is-outposts.md") in the
_AWS Outposts User Guide_.

Route 53 on Outposts offers two capabilities:

- A VPC Resolver that caches all DNS queries that originate from the AWS Outposts.
- Hybrid connectivity between an Outpost and an on-premises DNS resolver when you
  deploy inbound and outbound endpoints.
  For more information, see [What is Route 53 VPC Resolver?](resolver.md "resolver.md").

Additionally, Route 53 on Outposts reduces network latency by allowing queries to be resolved within
the Outpost instead of making the round-trip to the nearest AWS Region.

- A VPC Resolver that caches all DNS queries that originate from the AWS Outposts.
- Hybrid connectivity between an Outpost and an on-premises DNS resolver when you
  deploy inbound and outbound endpoints.
  For more information, see [What is Route 53 VPC Resolver?](resolver.md "resolver.md").

Additionally, Route 53 on Outposts reduces network latency by allowing queries to be resolved within
the Outpost instead of making the round-trip to the nearest AWS Region.

###### Note

If you have a version of AWS Outposts racks that aren't compatible with Route 53 on Outposts, an AWS
account team is notified and will contact you to help you upgrade AWS Outposts.

## Architecture overview

Route 53 on Outposts implements a distributed DNS architecture:

- **DNS records and hosted zones** remain managed
  in Amazon Route 53 in the AWS Region
- **Resolver functionality** extends to your AWS Outposts
  rack for local query processing

This design optimizes query performance and availability while maintaining centralized
DNS record management. DNS records continue to be stored in the AWS Region, not
locally on the AWS Outposts rack.

## Amazon Route 53 on Outposts features

The following table describes how Route 53 on Outposts features compare with Amazon Route 53
features.

| Route 53 on Outposts compared to Route 53 | Feature                                                                                                                                                                            | Availability in Route 53 on Outposts |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| VPC Resolver                              | Yes. VPC Resolver maintains a local cache of records for applications<br>hosted on Outpost rack, the peered VPC in the AWS Region, and any<br>publicly accessible host names.      |
| Health checks                             | No. Health checks are calculated and reported from the<br>AWS Region. If an Outpost disconnects from the cloud, the<br>endpoints fail open and can't fail over to a backup.        |
| Resolver endpoints                        | Yes. Resolver endpoints on Outpost rack allow DNS queries to be<br>forwarded and received from DNS servers on-premises.<br>Only the IPv4 endpoint type is available for endpoints. |
| Resolver DNS Firewall                     | Not available.                                                                                                                                                                     |
| Traffic flow                              | Not available.                                                                                                                                                                     |

## VPC Resolver behavior when AWS Outposts is

disconnected from the VPC

If the AWS Outposts is disconnected from the AWS Region, the Resolver on Outpost behaves as follows:

- Control plane changes are not available.
- Health checks and DNS failover capability are not available.
- DNS queries for resources that are hosted locally on the Outposts are resolved
  but in some cases the response might be stale if the IP address for the resource
  was updated while the Outpost was in a disconnected state.
- DNS queries for resources hosted on the in-Region VPC are resolvable. However,
  the resources will not be accessible until the Outpost connection to the
  AWS Region is restored.
- DNS queries for public DNS resources can be resolved if they are available in
  the VPC Resolver cache on Outpost.
