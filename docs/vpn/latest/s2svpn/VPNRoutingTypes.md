# AWS Site-to-Site VPN routing options

AWS recommends advertising specific BGP routes to influence routing decisions in the
virtual private gateway. Check your vendor documentation for the commands that are
specific to your device.

When you create multiple VPN connections, the virtual private gateway sends network
traffic to the appropriate VPN connection using statically assigned routes or BGP route
advertisements. Which route depends on how the VPN connection was configured. Statically
assigned routes are preferred over BGP advertised routes in cases where identical routes
exist in the virtual private gateway. If you select the option to use BGP advertisement,
then you cannot specify static routes.

For more information about route priority, see [Route tables and route priority](vpn-route-priority.md "vpn-route-priority.md").

When you create a Site-to-Site VPN connection, you must do the following:

- Specify the type of routing that you plan to use (static or
  dynamic)
- Update the [route table](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md") for your subnet
  There are quotas on the number of routes that you can add to a route table. For
  more information, see the Route Tables section in
  [Amazon VPC quotas](../../../vpc/latest/userguide/amazon-vpc-limits.md "../../../vpc/latest/userguide/amazon-vpc-limits.md") in the
  _Amazon VPC User Guide_.

###### Topics

- [Static and dynamic routing](vpn-static-dynamic.md "vpn-static-dynamic.md")
- [Route tables and route priority](vpn-route-priority.md "vpn-route-priority.md")
- [Routing during VPN tunnel
  endpoint updates](routing-vpn-tunnel-updates.md "routing-vpn-tunnel-updates.md")
- [IPv4 and IPv6 traffic](ipv4-ipv6.md "ipv4-ipv6.md")
