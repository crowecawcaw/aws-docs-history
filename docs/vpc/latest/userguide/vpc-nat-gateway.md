# NAT gateways

A NAT gateway is a Network Address Translation (NAT) service. You can use a NAT gateway
so that instances in a private subnet can connect to services outside your VPC but external
services can't initiate a connection with those instances.

When you create a NAT gateway, you specify one of the following connectivity types:

- **Public** – (Default) Instances in private subnets
  can connect to the internet through a public NAT gateway, but the instances can't receive
  unsolicited inbound connections from the internet. You create a public NAT gateway in a
  public subnet and must associate an Elastic IP address with the NAT gateway at creation. You
  route traffic from the NAT gateway to the internet gateway for the VPC. Alternatively, you
  can use a public NAT gateway to connect to other VPCs or your on-premises network. In this
  case, you route traffic from the NAT gateway through a transit gateway or a virtual private
  gateway.
- **Private** – Instances in private subnets can
  connect to other VPCs or your on-premises network through a private NAT gateway, but the
  instances can't receive unsolicited inbound connections from the other VPCs or the
  on-premises network. You can route traffic from the NAT gateway through a transit gateway or
  a virtual private gateway. You can't associate an Elastic IP address with a private NAT
  gateway. You can attach an internet gateway to a VPC with a private NAT gateway, but if you
  route traffic from the private NAT gateway to the internet gateway, the internet gateway
  drops the traffic.
  A NAT gateway is for use with IPv4 or IPv6 traffic (using [DNS64 and NAT64](nat-gateway-nat64-dns64.md "nat-gateway-nat64-dns64.md") ). Another option for enabling outbound-only internet
  communication over IPv6 is using an [egress-only internet gateway](egress-only-internet-gateway.md "egress-only-internet-gateway.md").

Both private and public NAT gateways map the source private IPv4 address of the instances to the private IPv4 address of the NAT gateway, but in the case of a public NAT gateway, the internet gateway then maps the private IPv4 address of the public
NAT gateway to the Elastic IP address associated with the NAT gateway. When sending response traffic to the instances, whether it's a
public or private NAT gateway, the NAT gateway translates the address back to the original source IP address.

###### Considerations

- Connections must always be initiated from within the VPC containing the NAT
  gateway.
- You can use either a public or private NAT gateway to route traffic to transit gateways
  and virtual private gateways.
- If you use a private NAT gateway to connect to a transit gateway or virtual private gateway,
  traffic to the destination will come from the private IP address of the private NAT gateway.
- If you use a public NAT gateway to connect to a transit gateway or virtual private
  gateway, traffic to the destination will come from the private IP address of the public NAT
  gateway. The public NAT gateway only uses its Elastic IP address as the source IP
  address when used in conjunction with an internet gateway in the same VPC.

###### Contents

- [NAT gateway basics](nat-gateway-basics.md "nat-gateway-basics.md")
- [Work with NAT gateways](nat-gateway-working-with.md "nat-gateway-working-with.md")
- [Regional NAT gateways for automatic multi-AZ expansion](nat-gateways-regional.md "nat-gateways-regional.md")
- [Use cases](nat-gateway-scenarios.md "nat-gateway-scenarios.md")
- [DNS64 and NAT64](nat-gateway-nat64-dns64.md "nat-gateway-nat64-dns64.md")
- [Inspect traffic from NAT gateways](nat-gateway-inspect-traffic.md "nat-gateway-inspect-traffic.md")
- [CloudWatch metrics](vpc-nat-gateway-cloudwatch.md "vpc-nat-gateway-cloudwatch.md")
- [Troubleshooting](nat-gateway-troubleshooting.md "nat-gateway-troubleshooting.md")
- [Pricing](nat-gateway-pricing.md "nat-gateway-pricing.md")
