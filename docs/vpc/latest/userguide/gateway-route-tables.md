# Gateway route tables

You can associate a route table with an internet gateway or a virtual private
gateway. When a route table is associated with a gateway, it's referred to as a
_gateway route table_. You can create a gateway
route table for fine-grain control over the routing path of traffic entering your
VPC. For example, you can intercept the traffic that enters your VPC through an
internet gateway by redirecting that traffic to a middlebox appliance (such as a
security appliance) in your VPC.

###### Contents

- [Gateway route table routes](#gateway-route-table-routes "#gateway-route-table-routes")
- [Rules and considerations](#gateway-route-table-rules "#gateway-route-table-rules")

## Gateway route table routes

A gateway route table associated with an internet gateway supports routes with
the following targets:

- The default local route
- A [Gateway Load Balancer endpoint](../../../elasticloadbalancing/latest/gateway.md "../../../elasticloadbalancing/latest/gateway.md")
- A network interface for a middlebox appliance

A gateway route table associated with a virtual private gateway supports routes
with the following targets:

- The default local route
- A [Gateway Load Balancer endpoint](../../../elasticloadbalancing/latest/gateway.md "../../../elasticloadbalancing/latest/gateway.md")
- A network interface for a middlebox appliance

When the target is a Gateway Load Balancer endpoint or a network interface, the following destinations
are allowed:

- The entire IPv4 or IPv6 CIDR block of your VPC. In this case, you replace
  the target of the default local route.
- The entire IPv4 or IPv6 CIDR block of a subnet in your VPC. This is a more
  specific route than the default local route.

If you change the target of the local route in a gateway route table to a network
interface in your VPC, you can later restore it to the default `local`
target. For more information, see [Replace or restore the target for a local route](replace-local-route-target.md "replace-local-route-target.md").

###### Example

In the following gateway route table, traffic destined for a subnet with the
`172.31.0.0/20` CIDR block is routed to a specific network interface.
Traffic destined for all other subnets in the VPC uses the local route.

| Destination   | Target   |
| ------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 172.31.0.0/16 | Local    |
| 172.31.0.0/20 | `eni-id` | ###### Example In the following gateway route table, the target for the local route is replaced with a network interface ID. Traffic destined for all subnets within the VPC is routed to the network interface.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Destination   | Target   |
| ---           | ---      |
| 172.31.0.0/16 | `eni-id` | ## Rules and considerations You cannot associate a route table with a gateway if any of the following applies: <br>• The route table contains existing routes with targets other than a network interface, Gateway Load Balancer endpoint, or the default local route. <br>• The route table contains existing routes to CIDR blocks outside of the ranges in your VPC. <br>• Route propagation is enabled for the route table. In addition, the following rules and considerations apply: <br>• You cannot add routes to any CIDR blocks outside of the ranges in your VPC, including ranges larger than the individual VPC CIDR blocks. <br>• You can only specify `local`, a Gateway Load Balancer endpoint, or a network interface as a target. You cannot specify any other types of targets, including individual host IP addresses. For more information, see [Example routing options](route-table-options.md "route-table-options.md"). <br>• You cannot specify a prefix list as a destination. <br>• You cannot use a gateway route table to control or intercept traffic outside of your VPC, for example, traffic through an attached transit gateway. You can intercept traffic that enters your VPC and redirect it to another target in the same VPC only. <br>• To ensure that traffic reaches your middlebox appliance, the target network interface must be attached to a running instance. For traffic that flows through an internet gateway, the target network interface must also have a public IP address. <br>• When configuring your middlebox appliance, take note of the [appliance considerations](route-table-options.md#appliance-considerations "route-table-options.md#appliance-considerations"). <br>• When you route traffic through a middlebox appliance, the return traffic from the destination subnet must be routed through the same appliance. Asymmetric routing is not supported. <br>• Route table rules apply to all traffic that leaves a subnet. Traffic that leaves a subnet is defined as traffic destined to that subnet's gateway router's MAC address. Traffic that is destined for the MAC address of another network interface in the subnet makes use of data link (layer 2) routing instead of network (layer 3) so the rules do not apply to this traffic. <br>• Not all Local Zones support edge association with virtual private gateways. For more information on available zones, see [Considerations](../../../local-zones/latest/ug/how-local-zones-work.md#considerations "../../../local-zones/latest/ug/how-local-zones-work.md#considerations") in the _AWS Local Zones User Guide_. |
