# Egress VPC

The Egress VPC is primarily used for egress traffic to the Internet and is
composed of public/private subnets in up to three availability zones (AZs).
Network address translation (NAT) gateways are provisioned in the public subnets, and transit gateway (TGW)
VPC attachments are created in the private subnets. Egress, or outbound, internet traffic from all networks enter
through the private subnet via TGW, where it is then routed to a NAT via VPC route tables.

For your VPCs that contain public-facing applications in a public subnet, traffic originating
from the internet is contained within that VPC. Return traffic is not routed to the TGW or Egress VPC,
but routed back through the internet gateway (IGW) in the VPC.

###### Note

Networking VPC CIDR range: When you create a VPC, you must specify a
range of IPv4 addresses for the VPC in the form of a Classless Inter-Domain Routing (CIDR) block;
for example, 10.0.16.0/24. This is the primary CIDR block for your VPC.

The AMS multi-account landing zone team recommends the range of 24 (with more IP address)
to provide some buffer in case other resources/appliances, are deployed in the future.
