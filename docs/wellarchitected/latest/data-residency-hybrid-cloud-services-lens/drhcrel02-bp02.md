# DRHCREL02-BP02 Use AWS Direct Connect with redundant tunnels and connections to the AWS Region for Outposts control plane actions and high availability requirements

AWS Outposts maintains connectivity to its parent Region through
encrypted service link tunnels to anchor points in designated
Availability Zones, requiring redundant network paths and dynamic
routing for high availability of control plane operations.

**Desired outcome:** Achieve high
availability and reliability for Outposts management and data
operations while maintaining compliance with data residency
requirements through dedicated, redundant AWS Direct Connect
connections.

**Benefits of establishing this best
practice:** AWS Direct Connect with redundant connections
provides a reliable and low-latency communication channel between
Outposts and AWS Regions, improving the reliability of control
plane operations.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

When you create AWS Outposts, you select an Availability Zone
from an AWS Region. Outposts connects back to its parent Region
through a set of encrypted VPN tunnels called the service link.
The service link ends on a set of anchor points in an
Availability Zone in the Outpost's parent Region. This
Availability Zone supports control plane operations such as
responding to API calls, monitoring Outposts, and updating
Outposts.

To benefit from the reliability provided by Availability Zones,
you can deploy applications on multiple Outposts, each attached
to a different Availability Zone. By doing so, you can build
additional application resilience and avoid a dependence on a
single Availability Zone. For more information about Regions and
Availability Zones, see
[AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

This makes this connectivity to the AWS Region from AWS Outposts
important. Where the data does need to flow to the AWS Region
and has high availability requirements, we recommend using
redundant connectivity back to the AWS Region.
[AWS Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") can be set up with redundant tunnels and
connections to AWS Region.

In the case of AWS Outposts, this connectivity is needed for
control plane actions like launching new Amazon EC2 instances,
which are necessary for auto scaling. Provision redundant
network paths between the Outpost and the anchor points in the
Region with connections that end on separate devices in more
than one location.

Dynamic routing should be configured to automatically reroute
traffic to alternate paths when connections or networking
devices fail. You should provision sufficient network capacity
to verify that the failure of one WAN path does not overwhelm
the remaining paths. For guide to this configuration, see
[Anchor
connectivity](../../../whitepapers/latest/aws-outposts-high-availability-design/anchor-connectivity.md "../../../whitepapers/latest/aws-outposts-high-availability-design/anchor-connectivity.md").
