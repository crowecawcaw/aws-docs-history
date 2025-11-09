# Connect your VPC to other VPCs and networks using a transit gateway

You can connect your virtual private clouds (VPC) and on-premises networks using a transit
gateway, which acts as a central hub, routing traffic between VPCs, VPN connections, and
AWS Direct Connect connections.

One of the key benefits of using a transit gateway is the ability to centralize and simplify the management of connectivity between your VPCs and on-premises networks. Rather than configuring multiple VPN connections or Direct Connect links, you can leverage the transit gateway as a single point of integration, which can help reduce the overall complexity and operational overhead of your network architecture.

The pricing for using a transit gateway is based on the volume of data transferred
through the gateway. There is a per-GB rate for data transferred in and out of the transit
gateway, as well as a separate per-hour rate for the transit gateway resource itself. The
specific pricing can vary by AWS Region and is subject to change, so it's important to
refer to the current AWS Transit Gateway pricing page for the most up-to-date information. By
understanding the pricing model for transit gateways, you can better plan and budget for the
ongoing costs associated with this AWS networking service. This, combined with the
operational efficiencies and connectivity benefits, makes transit gateways a compelling
choice for organizations looking to build scalable and cost-effective hybrid cloud
solutions.

The following table describes some common use case for transit gateways. For more information
about each use case, see [Example transit gateway scenarios](../tgw/how-transit-gateways-work.md#TGW_Scenarios "../tgw/how-transit-gateways-work.md#TGW_Scenarios") in the _AWS Transit Gateway User Guide_.

| Example                            | Usage                                                                                                                                                                                                                                  |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Centralized router                 | Configure your transit gateway as a centralized router that connects all of your VPCs,<br>AWS Direct Connect, and AWS Site-to-Site VPN connections.                                                                                    |
| Isolated VPCs                      | Configure your transit gateway as multiple isolated routers. This is similar to using multiple<br>transit gateways, but provides more flexibility in cases where the routes and<br>attachments might change.                           |
| Isolated VPCs with shared services | Configure your transit gateway as multiple isolated routers that use a shared service. This is<br>similar to using multiple transit gateways, but provides more flexibility in cases<br>where the routes and attachments might change. |

For more information, see [AWS Transit
Gateway](https://aws.amazon.com/transit-gateway/ "https://aws.amazon.com/transit-gateway/").
