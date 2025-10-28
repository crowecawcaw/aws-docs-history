# Route table concepts

The following are the key concepts for route tables:

- **Main route table**—The route table that
  automatically comes with your VPC. It controls the routing for all subnets that
  are not explicitly associated with any other route table.
- **Custom route table**—A route table that
  you create for your VPC.
- **Destination**—The range of IP addresses
  where you want traffic to go (destination CIDR). For example, an external
  corporate network with the CIDR `172.16.0.0/12`.
- **Target**—The gateway, network interface,
  or connection through which to send the destination traffic; for example, an
  internet gateway.
- **Local route**—A default route for
  communication within the VPC. If the VPC has both IPv4 and IPV6 addresses,
  there is a local route for IPv4 and a local route for IPv6.
- **Route table association**—The
  association between a route table and a subnet, internet gateway, or virtual
  private gateway.
- **Subnet route table**—A route table
  that's associated with a subnet.
- **Propagation**—If you've attached a
  virtual private gateway to your VPC and enable route propagation, we
  automatically add routes for your VPN connection to your subnet route tables.
  This means that you don't need to manually add or remove VPN routes. For more
  information, see [Site-to-Site VPN routing
  options](../../../vpn/latest/s2svpn/VPNRoutingTypes.md "../../../vpn/latest/s2svpn/VPNRoutingTypes.md") in the _Site-to-Site VPN User Guide_.
- **Gateway route table**—A route table
  that's associated with an internet gateway or virtual private gateway.
- **Edge association**—A route table that
  you use to route inbound VPC traffic to an appliance. You associate a route
  table with the internet gateway or virtual private gateway, and specify the
  network interface of your appliance as the target for VPC traffic.
- **Transit gateway route table**—A route
  table that's associated with a transit gateway. For more information, see [Transit gateway
  route tables](../tgw/tgw-route-tables.md "../tgw/tgw-route-tables.md") in _Amazon VPC Transit Gateways_.
- **Local gateway route table**—A route
  table that's associated with an Outposts local gateway. For more information,
  see [Local
  gateways](../../../outposts/latest/userguide/outposts-local-gateways.md "../../../outposts/latest/userguide/outposts-local-gateways.md") in the _AWS Outposts User Guide_.

## Example VPC with route tables

The following diagram shows a VPC with five subnets, a main route table, and three custom
route tables. All four route tables have local routes. Custom route table 1 has a route to
an internet gateway, and it is associated with the public subnet in Availability Zone A.
Custom route table 2 has a route to a peered VPC, and it is associated with the private
subnet in Availability Zone B. Custom route table 3 has a route to a virtual private
gateway, and it is associated with the VPN-only subnets in both Availability Zones.

![VPC with subnets in 2 AZs, 3 route tables, internet gateway, and gateway endpoint](images/route-tables.png)
