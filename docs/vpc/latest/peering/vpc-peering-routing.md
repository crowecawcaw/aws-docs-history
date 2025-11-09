# Update your route tables for a VPC peering connection

To enable private IPv4 traffic between instances in peered VPCs, you must add a route to the
route tables associated with the subnets for both instances. The route destination is
the CIDR block (or portion of the CIDR block) of the peer VPC and the target is the ID
of the VPC peering connection. For more information, see [Configure route tables](../userguide/VPC_Route_Tables.md "../userguide/VPC_Route_Tables.md") in the _Amazon VPC User Guide_.

The following is an example of the route tables that enables communication between instances
in two peered VPCs, VPC A and VPC B. Each table has a local route and a route that sends
traffic for the peer VPC to the VPC peering connection.

| Route table  | Destination    | Target |
| ------------ | -------------- | ------ |
| VPC A        | `VPC A CIDR`   | Local  |
| `VPC B CIDR` | pcx-`11112222` |
| VPC B        | `VPC B CIDR`   | Local  |
| `VPC A CIDR` | pcx-`11112222` |

Similarly, if the VPCs in the VPC peering connection have associated IPv6 CIDR blocks,
you can add routes that enable communication with the peer VPC over IPv6.

For more information about supported route table configurations for VPC peering
connections, see [Common VPC peering connection configurations](peering-configurations.md "peering-configurations.md").

###### Considerations

- If you have a VPC peered with multiple VPCs that have overlapping or matching IPv4 CIDR
  blocks, ensure that your route tables are configured to avoid sending response traffic from
  your VPC to the incorrect VPC. AWS currently does not support unicast reverse path
  forwarding in VPC peering connections that checks the source IP of packets and routes reply
  packets back to the source. For more information, see [Routing for response traffic](peering-configurations-partial-access.md#peering-incorrect-response-routing "peering-configurations-partial-access.md#peering-incorrect-response-routing").
- Your account has a [quota](../userguide/amazon-vpc-limits.md "../userguide/amazon-vpc-limits.md")
  on the number of entries you can add per route table. If the number of VPC peering
  connections in your VPC exceeds the route table entry quota for a single route
  table, consider using multiple subnets that are each associated with a custom route
  table.
- You can add a route for a VPC peering connection that's in the
  `pending-acceptance` state. However, the route has a state of
  `blackhole`, and has no effect until the VPC peering connection is in
  the `active` state.

###### To add an IPv4 route for a VPC peering connection

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Route tables**.
3. Select the check box next to the route table that's associated with the subnet in
   which your instance resides.

If you do not have a route table explicitly associated with that subnet, the main route
table for the VPC is implicitly associated with the subnet. 4. Choose **Actions**, **Edit routes**. 5. Choose **Add route**. 6. For **Destination**, enter the IPv4 address range to which the
network traffic in the VPC peering connection must be directed. You can specify the entire
IPv4 CIDR block of the peer VPC, a specific range, or an individual IPv4 address, such as
the IP address of the instance with which to communicate. For example, if the CIDR block
of the peer VPC is `10.0.0.0/16`, you can specify a portion
`10.0.0.0/24`, or a specific IP address `10.0.0.7/32`. 7. For **Target**, select the VPC peering connection. 8. Choose **Save changes**.
The owner of the peer VPC must also complete these steps to add a route to direct
traffic back to your VPC through the VPC peering connection.

If you have resources in different AWS Regions that use IPv6 addresses, you can create an
inter-Region peering connection. You can then add an IPv6 route for communication
between the resources.

###### To add an IPv6 route for a VPC peering connection

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Route tables**.
3. Select the check box next to the route table that's associated with the subnet
   in which your instance resides.

###### Note

If you do not have a route table associated with that subnet, select the
main route table for the VPC, as the subnet then uses this route table by
default. 4. Choose **Actions**, **Edit routes**. 5. Choose **Add route**. 6. For **Destination**, enter the IPv6 address range for the peer VPC.
You can specify the entire IPv6 CIDR block of the peer VPC, a specific range, or an
individual IPv6 address. For example, if the CIDR block of the peer VPC is
`2001:db8:1234:1a00::/56`, you can specify a portion
`2001:db8:1234:1a00::/64`, or a specific IP address
`2001:db8:1234:1a00::123/128`. 7. For **Target**, select the VPC peering connection. 8. Choose **Save changes**.
For more information, see [Route tables](../userguide/VPC_Route_Tables.md "../userguide/VPC_Route_Tables.md")
in the _Amazon VPC User Guide_.

###### To add or replace a route using the command line

- [create-route](../../../cli/latest/reference/ec2/create-route.md "../../../cli/latest/reference/ec2/create-route.md") and
  [replace-route](../../../cli/latest/reference/ec2/replace-route.md "../../../cli/latest/reference/ec2/replace-route.md")(AWS CLI)
- [New-EC2Route](../../../powershell/latest/reference/items/New-EC2Route.md "../../../powershell/latest/reference/items/New-EC2Route.md") and
  [Set-EC2Route](../../../powershell/latest/reference/items/Set-EC2Route.md "../../../powershell/latest/reference/items/Set-EC2Route.md")(AWS Tools for Windows PowerShell)
