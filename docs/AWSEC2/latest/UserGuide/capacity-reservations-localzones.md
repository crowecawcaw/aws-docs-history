# Capacity Reservations in Local Zones

A Local Zone is an extension of an AWS Region that is geographically close to your
users. Resources created in a Local Zone can serve local users with very low-latency
communications. For more information, see [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/ "https://aws.amazon.com/about-aws/global-infrastructure/localzones/").

You can extend a VPC from its parent AWS Region into a Local Zone by creating a new
subnet in that Local Zone. When you create a subnet in a Local Zone, your VPC is extended to
that Local Zone. The subnet in the Local Zone operates the same as the other subnets in your
VPC.

By using Local Zones, you can place Capacity Reservations in multiple locations that are closer to your
users. You create and use Capacity Reservations in Local Zones in the same way that you create and use
Capacity Reservations in regular Availability Zones. The same features and instance matching behavior
apply. For more information about the pricing models that are supported in Local Zones, see
[AWS Local Zones FAQs](https://aws.amazon.com/about-aws/global-infrastructure/localzones/faqs/ "https://aws.amazon.com/about-aws/global-infrastructure/localzones/faqs/").

###### Considerations

You can't use Capacity Reservation groups in a Local Zone.

###### To use a Capacity Reservation in a Local Zone

1. Enable the Local Zone for use in your AWS account. For more information, see
   [Getting started with AWS Local Zones](../../../local-zones/latest/ug/getting-started.md "../../../local-zones/latest/ug/getting-started.md") in the _AWS Local Zones
   User Guide_.
2. Create a Capacity Reservation in the Local Zone. For **Availability
   Zone**, choose the Local Zone. The Local Zone is represented by an AWS
   Region code followed by an identifier that indicates the location, for example
   `us-west-2-lax-1a`. For more information, see [Create a Capacity Reservation](capacity-reservations-create.md "capacity-reservations-create.md").
3. Create a subnet in the Local Zone. For **Availability
   Zone**, choose the Local Zone. For more information, see [Create a
   subnet in your VPC](../../../vpc/latest/userguide/create-subnets.md "../../../vpc/latest/userguide/create-subnets.md") in the _Amazon VPC User Guide_.
4. Launch an instance. For **Subnet**, choose the
   subnet in the Local Zone (for example `subnet-123abc |
us-west-2-lax-1a`), and for **Capacity Reservation**, choose
   the specification (either `open` or target it by ID) that's required
   for the Capacity Reservation that you created in the Local Zone. For more information, see [Launch instances into an existing
   Capacity Reservation](capacity-reservations-launch.md "capacity-reservations-launch.md").
