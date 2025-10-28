# Enable outbound IPv6 traffic using an egress-only internet gateway

An egress-only internet gateway is a horizontally scaled, redundant, and highly available
VPC component that allows outbound communication over IPv6 from instances in your VPC to the
internet, and prevents the internet from initiating an IPv6 connection with your
instances.

An egress-only internet gateway is for use with IPv6 traffic only. To enable outbound-only
internet communication over IPv4, use a NAT gateway instead. For more information, see
[NAT gateways](vpc-nat-gateway.md "vpc-nat-gateway.md").

###### Pricing

There is no charge for an egress-only internet gateway, but there are data transfer charges for EC2 instances that use internet gateways. For more information, see [Amazon EC2 On-Demand Pricing](https://aws.amazon.com/ec2/pricing/on-demand/ "https://aws.amazon.com/ec2/pricing/on-demand/").

###### Contents

- [Egress-only internet gateway basics](#egress-only-internet-gateway-basics "#egress-only-internet-gateway-basics")
- [Add egress-only internet access to a subnet](egress-only-internet-gateway-working-with.md "egress-only-internet-gateway-working-with.md")

## Egress-only internet gateway basics

IPv6 addresses are globally unique, and are therefore public by default. If you want
your instance to be able to access the internet, but you want to prevent resources on
the internet from initiating communication with your instance, you can use an
egress-only internet gateway. To do this, create an egress-only internet gateway in your
VPC, and then add a route to your route table that points all IPv6 traffic
(`::/0`) or a specific range of IPv6 address to the egress-only internet
gateway. IPv6 traffic in the subnet that's associated with the route table is routed to
the egress-only internet gateway.

An egress-only internet gateway is stateful: it forwards traffic from the instances in
the subnet to the internet or other AWS services, and then sends the response back to
the instances.

You can't associate a security group with an egress-only internet gateway to control
the traffic that is allowed to reach or leave the egress-only internet gateway. You can
use a network ACL to control the traffic to and from the subnet for which the egress-only
internet gateway routes traffic.

In the following diagram, the VPC has both IPv4 and IPv6 CIDR blocks, and the subnet
both IPv4 and IPv6 CIDR blocks. The VPC has an egress-only internet gateway.

![Using an egress-only internet gateway](images/egress-only-igw.png)

The following is an example of the route table associated with the subnet. There is a
route that sends all internet-bound IPv6 traffic (::/0) to the egress-only internet gateway.

| Destination            | Target    |
| ---------------------- | --------- |
| 10.0.0.0/16            | Local     |
| 2001:db8:1234:1a00:/64 | Local     |
| ::/0                   | `eigw-id` |
