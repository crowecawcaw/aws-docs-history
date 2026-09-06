

# VPC peering configurations with routes to an entire VPC
<a name="peering-configurations-full-access"></a>

You can configure VPC peering connections so that your route tables have access to the entire CIDR block of the peer VPC. For more information about scenarios in which you might need a specific VPC peering connection configuration, see [VPC peering connection networking scenarios](peering-scenarios.md). For more information about creating and working with VPC peering connections, see [VPC peering connections](working-with-vpc-peering.md).

 For more information about updating your route tables, see [Update your route tables for a VPC peering connection](vpc-peering-routing.md).

**Topics**
+ [Two VPCs peered together](#two-vpcs-full-access)
+ [One VPC peered with two VPCs](#one-to-two-vpcs-full-access)
+ [Three VPCs peered together](#three-vpcs-full-access)
+ [Multiple VPCs peered together](#many-vpcs-full-access)

## Two VPCs peered together
<a name="two-vpcs-full-access"></a>

In this configuration, there is a peering connection between VPC A and VPC B (`pcx-11112222`). The VPCs are in the same AWS account and their CIDR blocks do not overlap.

![Two VPCs peered together.](http://docs.aws.amazon.com/vpc/latest/peering/images/two-vpcs-peered.png)


You might use this configuration when you have two VPCs that require access to each others' resources. For example, you set up VPC A for your accounting records and VPC B for your financial records, and these each VPC must be able to access resources from the other VPC without restriction.

**Single VPC CIDR**  
Update the route table for each VPC with a route that sends traffic for the CIDR block of the peer VPC to the VPC peering connection.



- **VPC A**
  - **Destination:** {{VPC A CIDR}} / **Target:** Local
  - **Destination:** {{VPC B CIDR}} / **Target:** pcx-11112222

- **VPC B**
  - **Destination:** {{VPC B CIDR}} / **Target:** Local
  - **Destination:** {{VPC A CIDR}} / **Target:** pcx-11112222



**Multiple IPv4 VPC CIDRs**  
If VPC A and VPC B have multiple associated IPv4 CIDR blocks, you can update the route table for each VPC with routes for some or all of the IPv4 CIDR blocks of the peer VPC.



- **VPC A**
  - **Destination:** {{VPC A CIDR 1}} / **Target:** Local
  - **Destination:** {{VPC A CIDR 2}} / **Target:** Local
  - **Destination:** {{VPC B CIDR 1}} / **Target:** pcx-11112222
  - **Destination:** {{VPC B CIDR 2}} / **Target:** pcx-11112222

- **VPC B**
  - **Destination:** {{VPC B CIDR 1}} / **Target:** Local
  - **Destination:** {{VPC B CIDR 2}} / **Target:** Local
  - **Destination:** {{VPC A CIDR 1}} / **Target:** pcx-11112222
  - **Destination:** {{VPC A CIDR 2}} / **Target:** pcx-11112222



**IPv4 and IPv6 VPC CIDRs**  
If VPC A and VPC B have associated IPv6 CIDR blocks, you can update the route table for each VPC with routes for both the IPv4 and IPv6 CIDR blocks of the peer VPC.



- **VPC A**
  - **Destination:** {{VPC A IPv4 CIDR}} / **Target:** Local
  - **Destination:** {{VPC A IPv6 CIDR}} / **Target:** Local
  - **Destination:** {{VPC B IPv4 CIDR}} / **Target:** pcx-11112222
  - **Destination:** {{VPC B IPv6 CIDR}} / **Target:** pcx-11112222

- **VPC B**
  - **Destination:** {{VPC B IPv4 CIDR}} / **Target:** Local
  - **Destination:** {{VPC B IPv6 CIDR}} / **Target:** Local
  - **Destination:** {{VPC A IPv4 CIDR}} / **Target:** pcx-11112222
  - **Destination:** {{VPC A IPv6 CIDR}} / **Target:** pcx-11112222



## One VPC peered with two VPCs
<a name="one-to-two-vpcs-full-access"></a>

In this configuration, there is a central VPC (VPC A), a peering connection between VPC A and VPC B (`pcx-12121212`), and a peering connection between VPC A and VPC C (`pcx-23232323`). All three VPCs are in the same AWS account and their CIDR blocks do not overlap.

![One VPC peered with two VPCs.](http://docs.aws.amazon.com/vpc/latest/peering/images/one-vpc-peered-to-two.png)


VPC B and VPC C can't send traffic directly to each other through a VPC A, because VPC peering does not support transitive peering relationships. You can create a VPC peering connection between VPC B and VPC C, as shown in [Three VPCs peered together](#three-vpcs-full-access). For more information about unsupported peering scenarios, see [VPC peering limitations](vpc-peering-basics.md#vpc-peering-limitations).

You might use this configuration when you have resources on a central VPC, such as a repository of services, that other VPCs need to access. The other VPCs do not need access to each others' resources; they only need to access resources in the central VPC.

Update the route table for each VPC as follows to implement this configuration using one CIDR block per VPC. 



- **VPC A**
  - **Destination:** {{VPC A CIDR}} / **Target:** Local
  - **Destination:** {{VPC B CIDR}} / **Target:** pcx-12121212
  - **Destination:** {{VPC C CIDR}} / **Target:** pcx-23232323

- **VPC B**
  - **Destination:** {{VPC B CIDR}} / **Target:** Local
  - **Destination:** {{VPC A CIDR}} / **Target:** pcx-12121212

- **VPC C**
  - **Destination:** {{VPC C CIDR}} / **Target:** Local
  - **Destination:** {{VPC A CIDR}} / **Target:** pcx-23232323



You can extend this configuration to additional VPCs. For example, VPC A is peered with VPC B through VPC G using both IPv4 and IPv6 CIDRs, but the other VPCs are not peered to each other. In this diagram, the lines represent VPC peering connections.

![One VPC peered with two VPCs.](http://docs.aws.amazon.com/vpc/latest/peering/images/one-to-many-vpcs.png)


Update the route table as follows.



- **VPC A**
  - **Destination:** {{VPC A IPv4 CIDR}} / **Target:** Local
  - **Destination:** {{VPC A IPv6 CIDR}} / **Target:** Local
  - **Destination:** {{VPC B IPv4 CIDR}} / **Target:** pcx-aaaabbbb
  - **Destination:** {{VPC B IPv6 CIDR}} / **Target:** pcx-aaaabbbb
  - **Destination:** {{VPC C IPv4 CIDR}} / **Target:** pcx-aaaacccc
  - **Destination:** {{VPC C IPv6 CIDR}} / **Target:** pcx-aaaacccc
  - **Destination:** {{VPC D IPv4 CIDR}} / **Target:** pcx-aaaadddd
  - **Destination:** {{VPC D IPv6 CIDR}} / **Target:** pcx-aaaadddd
  - **Destination:** {{VPC E IPv4 CIDR}} / **Target:** pcx-aaaaeeee
  - **Destination:** {{VPC E IPv6 CIDR}} / **Target:** pcx-aaaaeeee
  - **Destination:** {{VPC F IPv4 CIDR}} / **Target:** pcx-aaaaffff
  - **Destination:** {{VPC F IPv6 CIDR}} / **Target:** pcx-aaaaffff
  - **Destination:** {{VPC G IPv4 CIDR}} / **Target:** pcx-aaaagggg
  - **Destination:** {{VPC G IPv6 CIDR}} / **Target:** pcx-aaaagggg

- **VPC B**
  - **Destination:** {{VPC B IPv4 CIDR}} / **Target:** Local
  - **Destination:** {{VPC B IPv6 CIDR}} / **Target:** Local
  - **Destination:** {{VPC A IPv4 CIDR}} / **Target:** pcx-aaaabbbb
  - **Destination:** {{VPC A IPv6 CIDR}} / **Target:** pcx-aaaabbbb

- **VPC C**
  - **Destination:** {{VPC C IPv4 CIDR}} / **Target:** Local
  - **Destination:** {{VPC C IPv6 CIDR}} / **Target:** Local
  - **Destination:** {{VPC A IPv4 CIDR}} / **Target:** pcx-aaaacccc
  - **Destination:** {{VPC A IPv6 CIDR}} / **Target:** pcx-aaaacccc

- **VPC D**
  - **Destination:** {{VPC D IPv4 CIDR}} / **Target:** Local
  - **Destination:** {{VPC D IPv6 CIDR}} / **Target:** Local
  - **Destination:** {{VPC A IPv4 CIDR}} / **Target:** pcx-aaaadddd
  - **Destination:** {{VPC A IPv6 CIDR}} / **Target:** pcx-aaaadddd

- **VPC E**
  - **Destination:** {{VPC E IPv4 CIDR}} / **Target:** Local
  - **Destination:** {{VPC E IPv6 CIDR}} / **Target:** Local
  - **Destination:** {{VPC A IPv4 CIDR}} / **Target:** pcx-aaaaeeee
  - **Destination:** {{VPC A IPv6 CIDR}} / **Target:** pcx-aaaaeeee

- **VPC F**
  - **Destination:** {{VPC F IPv4 CIDR}} / **Target:** Local
  - **Destination:** {{VPC F IPv6 CIDR}} / **Target:** Local
  - **Destination:** {{VPC A IPv4 CIDR}} / **Target:** pcx-aaaaffff
  - **Destination:** {{VPC A IPv6 CIDR}} / **Target:** pcx-aaaaffff

- **VPC G**
  - **Destination:** {{VPC G IPv4 CIDR}} / **Target:** Local
  - **Destination:** {{VPC G IPv6 CIDR}} / **Target:** Local
  - **Destination:** {{VPC A IPv4 CIDR}} / **Target:** pcx-aaaagggg
  - **Destination:** {{VPC A IPv6 CIDR}} / **Target:** pcx-aaaagggg



## Three VPCs peered together
<a name="three-vpcs-full-access"></a>

In this configuration, there are three VPCs in the same AWS account with CIDR blocks that do not overlap. The VPCs are peered in a full mesh as follows:
+ VPC A is peered to VPC B through VPC peering connection `pcx-aaaabbbb`
+ VPC A is peered to VPC C through VPC peering connection `pcx-aaaacccc`
+ VPC B is peered to VPC C through VPC peering connection `pcx-bbbbcccc`

![Three VPCs peered together.](http://docs.aws.amazon.com/vpc/latest/peering/images/three-vpcs-peered.png)


You might use this configuration when you have VPCs that need to share resources with each other without restriction. For example, as a file sharing system.

Update the route table for each VPC as follows to implement this configuration.



- **VPC A**
  - **Destination:** {{VPC A CIDR}} / **Target:** Local
  - **Destination:** {{VPC B CIDR}} / **Target:** pcx-aaaabbbb
  - **Destination:** {{VPC C CIDR}} / **Target:** pcx-aaaacccc

- **VPC B**
  - **Destination:** {{VPC B CIDR}} / **Target:** Local
  - **Destination:** {{VPC A CIDR}} / **Target:** pcx-aaaabbbb
  - **Destination:** {{VPC C CIDR}} / **Target:** pcx-bbbbcccc

- **VPC C**
  - **Destination:** {{VPC C CIDR}} / **Target:** Local
  - **Destination:** {{VPC A CIDR}} / **Target:** pcx-aaaacccc
  - **Destination:** {{VPC B CIDR}} / **Target:** pcx-bbbbcccc



If VPC A and VPC B have both IPv4 and IPv6 CIDR blocks, but VPC C does not have an IPv6 CIDR block, update the route tables as follows. Resources in VPC A and VPC B can communicate using IPv6 over the VPC peering connection. However, VPC C cannot communicate with either VPC A or VPC B using IPv6.



- **VPC A**
  - **Destination:** {{VPC A IPv4 CIDR}} / **Target:** Local
  - **Destination:** {{VPC A IPv6 CIDR}} / **Target:** Local
  - **Destination:** {{VPC B IPv4 CIDR}} / **Target:** pcx-aaaabbbb
  - **Destination:** {{VPC B IPv6 CIDR}} / **Target:** pcx-aaaabbbb
  - **Destination:** {{VPC C IPv4 CIDR}} / **Target:** pcx-aaaacccc

- **VPC B**
  - **Destination:** {{VPC B IPv4 CIDR}} / **Target:** Local
  - **Destination:** {{VPC B IPv6 CIDR}} / **Target:** Local
  - **Destination:** {{VPC A IPv4 CIDR}} / **Target:** pcx-aaaabbbb
  - **Destination:** {{VPC A IPv6 CIDR}} / **Target:** pcx-aaaabbbb
  - **Destination:** {{VPC C IPv4 CIDR}} / **Target:** pcx-bbbbcccc

- **VPC C**
  - **Destination:** {{VPC C IPv4 CIDR}} / **Target:** Local
  - **Destination:** {{VPC A IPv4 CIDR}} / **Target:** pcx-aaaacccc
  - **Destination:** {{VPC B IPv4 CIDR}} / **Target:** pcx-bbbbcccc



## Multiple VPCs peered together
<a name="many-vpcs-full-access"></a>

In this configuration, there are seven VPCs peered in a full mesh configuration. The VPCs are in the same AWS account and their CIDR blocks do not overlap.


| VPC | VPC | VPC peering connection | 
| --- | --- | --- | 
| A | B | pcx-aaaabbbb | 
| A | C | pcx-aaaacccc | 
| A | D | pcx-aaaadddd | 
| A | E | pcx-aaaaeeee | 
| A | F | pcx-aaaaffff | 
| A | G | pcx-aaaagggg | 
| B | C | pcx-bbbbcccc | 
| B | D | pcx-bbbbdddd | 
| B | E | pcx-bbbbeeee | 
| B | F | pcx-bbbbffff | 
| B | G | pcx-bbbbgggg | 
| C | D | pcx-ccccdddd | 
| C | E | pcx-cccceeee | 
| C | F | pcx-ccccffff | 
| C | G | pcx-ccccgggg | 
| D | E | pcx-ddddeeee | 
| D | F | pcx-ddddffff | 
| D | G | pcx-ddddgggg | 
| E | F | pcx-eeeeffff | 
| E | G | pcx-eeeegggg | 
| F | G | pcx-ffffgggg | 

You might use this configuration when you have multiple VPCs that must be able to access each others' resources without restriction. For example, as a file sharing network. In this diagram, the lines represent VPC peering connections.

![Seven VPCs in a full mesh configuration.](http://docs.aws.amazon.com/vpc/latest/peering/images/full-mesh.png)


Update the route table for each VPC as follows to implement this configuration.



- **VPC A**
  - **Destination:** {{VPC A CIDR}} / **Target:** Local
  - **Destination:** {{VPC B CIDR}} / **Target:** pcx-aaaabbbb
  - **Destination:** {{VPC C CIDR}} / **Target:** pcx-aaaacccc
  - **Destination:** {{VPC D CIDR}} / **Target:** pcx-aaaadddd
  - **Destination:** {{VPC E CIDR}} / **Target:** pcx-aaaaeeee
  - **Destination:** {{VPC F CIDR}} / **Target:** pcx-aaaaffff
  - **Destination:** {{VPC G CIDR}} / **Target:** pcx-aaaagggg

- **VPC B**
  - **Destination:** {{VPC B CIDR}} / **Target:** Local
  - **Destination:** {{VPC A CIDR}} / **Target:** pcx-aaaabbbb
  - **Destination:** {{VPC C CIDR}} / **Target:** pcx-bbbbcccc
  - **Destination:** {{VPC D CIDR}} / **Target:** pcx-bbbbdddd
  - **Destination:** {{VPC E CIDR}} / **Target:** pcx-bbbbeeee
  - **Destination:** {{VPC F CIDR}} / **Target:** pcx-bbbbffff
  - **Destination:** {{VPC G CIDR}} / **Target:** pcx-bbbbgggg

- **VPC C**
  - **Destination:** {{VPC C CIDR}} / **Target:** Local
  - **Destination:** {{VPC A CIDR}} / **Target:** pcx-aaaacccc
  - **Destination:** {{VPC B CIDR}} / **Target:** pcx-bbbbcccc
  - **Destination:** {{VPC D CIDR}} / **Target:** pcx-ccccdddd
  - **Destination:** {{VPC E CIDR}} / **Target:** pcx-cccceeee
  - **Destination:** {{VPC F CIDR}} / **Target:** pcx-ccccffff
  - **Destination:** {{VPC G CIDR}} / **Target:** pcx-ccccgggg

- **VPC D**
  - **Destination:** {{VPC D CIDR}} / **Target:** Local
  - **Destination:** {{VPC A CIDR}} / **Target:** pcx-aaaadddd
  - **Destination:** {{VPC B CIDR}} / **Target:** pcx-bbbbdddd
  - **Destination:** {{VPC C CIDR}} / **Target:** pcx-ccccdddd
  - **Destination:** {{VPC E CIDR}} / **Target:** pcx-ddddeeee
  - **Destination:** {{VPC F CIDR}} / **Target:** pcx-ddddffff
  - **Destination:** {{VPC G CIDR}} / **Target:** pcx-ddddgggg

- **VPC E**
  - **Destination:** {{VPC E CIDR}} / **Target:** Local
  - **Destination:** {{VPC A CIDR}} / **Target:** pcx-aaaaeeee
  - **Destination:** {{VPC B CIDR}} / **Target:** pcx-bbbbeeee
  - **Destination:** {{VPC C CIDR}} / **Target:** pcx-cccceeee
  - **Destination:** {{VPC D CIDR}} / **Target:** pcx-ddddeeee
  - **Destination:** {{VPC F CIDR}} / **Target:** pcx-eeeeffff
  - **Destination:** {{VPC G CIDR}} / **Target:** pcx-eeeegggg

- **VPC F**
  - **Destination:** {{VPC F CIDR}} / **Target:** Local
  - **Destination:** {{VPC A CIDR}} / **Target:** pcx-aaaaffff
  - **Destination:** {{VPC B CIDR}} / **Target:** pcx-bbbbffff
  - **Destination:** {{VPC C CIDR}} / **Target:** pcx-ccccffff
  - **Destination:** {{VPC D CIDR}} / **Target:** pcx-ddddffff
  - **Destination:** {{VPC E CIDR}} / **Target:** pcx-eeeeffff
  - **Destination:** {{VPC G CIDR}} / **Target:** pcx-ffffgggg

- **VPC G**
  - **Destination:** {{VPC G CIDR}} / **Target:** Local
  - **Destination:** {{VPC A CIDR}} / **Target:** pcx-aaaagggg
  - **Destination:** {{VPC B CIDR}} / **Target:** pcx-bbbbgggg
  - **Destination:** {{VPC C CIDR}} / **Target:** pcx-ccccgggg
  - **Destination:** {{VPC D CIDR}} / **Target:** pcx-ddddgggg
  - **Destination:** {{VPC E CIDR}} / **Target:** pcx-eeeegggg
  - **Destination:** {{VPC F CIDR}} / **Target:** pcx-ffffgggg



If all VPCs have associated IPv6 CIDR blocks, update the route tables as follows.



- **VPC A**
  - **Destination:** {{VPC A IPv4 CIDR}} / **Target:** Local
  - **Destination:** {{VPC A IPv6 CIDR}} / **Target:** Local
  - **Destination:** {{VPC B IPv4 CIDR}} / **Target:** pcx-aaaabbbb
  - **Destination:** {{VPC B IPv6 CIDR}} / **Target:** pcx-aaaabbbb
  - **Destination:** {{VPC C IPv4 CIDR}} / **Target:** pcx-aaaacccc
  - **Destination:** {{VPC C IPv6 CIDR}} / **Target:** pcx-aaaacccc
  - **Destination:** {{VPC D IPv4 CIDR}} / **Target:** pcx-aaaadddd
  - **Destination:** {{VPC D IPv6 CIDR}} / **Target:** pcx-aaaadddd
  - **Destination:** {{VPC E IPv4 CIDR}} / **Target:** pcx-aaaaeeee
  - **Destination:** {{VPC E IPv6 CIDR}} / **Target:** pcx-aaaaeeee
  - **Destination:** {{VPC F IPv4 CIDR}} / **Target:** pcx-aaaaffff
  - **Destination:** {{VPC F IPv6 CIDR}} / **Target:** pcx-aaaaffff
  - **Destination:** {{VPC G IPv4 CIDR}} / **Target:** pcx-aaaagggg
  - **Destination:** {{VPC G IPv6 CIDR}} / **Target:** pcx-aaaagggg

- **VPC B**
  - **Destination:** {{VPC B IPv4 CIDR}} / **Target:** Local
  - **Destination:** {{VPC B IPv6 CIDR}} / **Target:** Local
  - **Destination:** {{VPC A IPv4 CIDR}} / **Target:** pcx-aaaabbbb
  - **Destination:** {{VPC A IPv6 CIDR}} / **Target:** pcx-aaaabbbb
  - **Destination:** {{VPC C IPv4 CIDR}} / **Target:** pcx-bbbbcccc
  - **Destination:** {{VPC C IPv6 CIDR}} / **Target:** pcx-bbbbcccc
  - **Destination:** {{VPC D IPv4 CIDR}} / **Target:** pcx-bbbbdddd
  - **Destination:** {{VPC D IPv6 CIDR}} / **Target:** pcx-bbbbdddd
  - **Destination:** {{VPC E IPv4 CIDR}} / **Target:** pcx-bbbbeeee
  - **Destination:** {{VPC E IPv6 CIDR}} / **Target:** pcx-bbbbeeee
  - **Destination:** {{VPC F IPv4 CIDR}} / **Target:** pcx-bbbbffff
  - **Destination:** {{VPC F IPv6 CIDR}} / **Target:** pcx-bbbbffff
  - **Destination:** {{VPC G IPv4 CIDR}} / **Target:** pcx-bbbbgggg
  - **Destination:** {{VPC G IPv6 CIDR}} / **Target:** pcx-bbbbgggg

- **VPC C**
  - **Destination:** {{VPC C IPv4 CIDR}} / **Target:** Local
  - **Destination:** {{VPC C IPv6 CIDR}} / **Target:** Local
  - **Destination:** {{VPC A IPv4 CIDR}} / **Target:** pcx-aaaacccc
  - **Destination:** {{VPC A IPv6 CIDR}} / **Target:** pcx-aaaacccc
  - **Destination:** {{VPC B IPv4 CIDR}} / **Target:** pcx-bbbbcccc
  - **Destination:** {{VPC B IPv6 CIDR}} / **Target:** pcx-bbbbcccc
  - **Destination:** {{VPC D IPv4 CIDR}} / **Target:** pcx-ccccdddd
  - **Destination:** {{VPC D IPv6 CIDR}} / **Target:** pcx-ccccdddd
  - **Destination:** {{VPC E IPv4 CIDR}} / **Target:** pcx-cccceeee
  - **Destination:** {{VPC E IPv6 CIDR}} / **Target:** pcx-cccceeee
  - **Destination:** {{VPC F IPv4 CIDR}} / **Target:** pcx-ccccffff
  - **Destination:** {{VPC F IPv6 CIDR}} / **Target:** pcx-ccccffff
  - **Destination:** {{VPC G IPv4 CIDR}} / **Target:** pcx-ccccgggg
  - **Destination:** {{VPC G IPv6 CIDR}} / **Target:** pcx-ccccgggg

- **VPC D**
  - **Destination:** {{VPC D IPv4 CIDR}} / **Target:** Local
  - **Destination:** {{VPC D IPv6 CIDR}} / **Target:** Local
  - **Destination:** {{VPC A IPv4 CIDR}} / **Target:** pcx-aaaadddd
  - **Destination:** {{VPC A IPv6 CIDR}} / **Target:** pcx-aaaadddd
  - **Destination:** {{VPC B IPv4 CIDR}} / **Target:** pcx-bbbbdddd
  - **Destination:** {{VPC B IPv6 CIDR}} / **Target:** pcx-bbbbdddd
  - **Destination:** {{VPC C IPv4 CIDR}} / **Target:** pcx-ccccdddd
  - **Destination:** {{VPC C IPv6 CIDR}} / **Target:** pcx-ccccdddd
  - **Destination:** {{VPC E IPv4 CIDR}} / **Target:** pcx-ddddeeee
  - **Destination:** {{VPC E IPv6 CIDR}} / **Target:** pcx-ddddeeee
  - **Destination:** {{VPC F IPv4 CIDR}} / **Target:** pcx-ddddffff
  - **Destination:** {{VPC F IPv6 CIDR}} / **Target:** pcx-ddddffff
  - **Destination:** {{VPC G IPv4 CIDR}} / **Target:** pcx-ddddgggg
  - **Destination:** {{VPC G IPv6 CIDR}} / **Target:** pcx-ddddgggg

- **VPC E**
  - **Destination:** {{VPC E IPv4 CIDR}} / **Target:** Local
  - **Destination:** {{VPC E IPv6 CIDR}} / **Target:** Local
  - **Destination:** {{VPC A IPv4 CIDR}} / **Target:** pcx-aaaaeeee
  - **Destination:** {{VPC A IPv6 CIDR}} / **Target:** pcx-aaaaeeee
  - **Destination:** {{VPC B IPv4 CIDR}} / **Target:** pcx-bbbbeeee
  - **Destination:** {{VPC B IPv6 CIDR}} / **Target:** pcx-bbbbeeee
  - **Destination:** {{VPC C IPv4 CIDR}} / **Target:** pcx-cccceeee
  - **Destination:** {{VPC C IPv6 CIDR}} / **Target:** pcx-cccceeee
  - **Destination:** {{VPC D IPv4 CIDR}} / **Target:** pcx-ddddeeee
  - **Destination:** {{VPC D IPv6 CIDR}} / **Target:** pcx-ddddeeee
  - **Destination:** {{VPC F IPv4 CIDR}} / **Target:** pcx-eeeeffff
  - **Destination:** {{VPC F IPv6 CIDR}} / **Target:** pcx-eeeeffff
  - **Destination:** {{VPC G IPv4 CIDR}} / **Target:** pcx-eeeegggg
  - **Destination:** {{VPC G IPv6 CIDR}} / **Target:** pcx-eeeegggg

- **VPC F**
  - **Destination:** {{VPC F IPv4 CIDR}} / **Target:** Local
  - **Destination:** {{VPC F IPv6 CIDR}} / **Target:** Local
  - **Destination:** {{VPC A IPv4 CIDR}} / **Target:** pcx-aaaaffff
  - **Destination:** {{VPC A IPv6 CIDR}} / **Target:** pcx-aaaaffff
  - **Destination:** {{VPC B IPv4 CIDR}} / **Target:** pcx-bbbbffff
  - **Destination:** {{VPC B IPv6 CIDR}} / **Target:** pcx-bbbbffff
  - **Destination:** {{VPC C IPv4 CIDR}} / **Target:** pcx-ccccffff
  - **Destination:** {{VPC C IPv6 CIDR}} / **Target:** pcx-ccccffff
  - **Destination:** {{VPC D IPv4 CIDR}} / **Target:** pcx-ddddffff
  - **Destination:** {{VPC D IPv6 CIDR}} / **Target:** pcx-ddddffff
  - **Destination:** {{VPC E IPv4 CIDR}} / **Target:** pcx-eeeeffff
  - **Destination:** {{VPC E IPv6 CIDR}} / **Target:** pcx-eeeeffff
  - **Destination:** {{VPC G IPv4 CIDR}} / **Target:** pcx-ffffgggg
  - **Destination:** {{VPC G IPv6 CIDR}} / **Target:** pcx-ffffgggg

- **VPC G**
  - **Destination:** {{VPC G IPv4 CIDR}} / **Target:** Local
  - **Destination:** {{VPC G IPv6 CIDR}} / **Target:** Local
  - **Destination:** {{VPC A IPv4 CIDR}} / **Target:** pcx-aaaagggg
  - **Destination:** {{VPC A IPv6 CIDR}} / **Target:** pcx-aaaagggg
  - **Destination:** {{VPC B IPv4 CIDR}} / **Target:** pcx-bbbbgggg
  - **Destination:** {{VPC B IPv6 CIDR}} / **Target:** pcx-bbbbgggg
  - **Destination:** {{VPC C IPv4 CIDR}} / **Target:** pcx-ccccgggg
  - **Destination:** {{VPC C IPv6 CIDR}} / **Target:** pcx-ccccgggg
  - **Destination:** {{VPC D IPv4 CIDR}} / **Target:** pcx-ddddgggg
  - **Destination:** {{VPC D IPv6 CIDR}} / **Target:** pcx-ddddgggg
  - **Destination:** {{VPC E IPv4 CIDR}} / **Target:** pcx-eeeegggg
  - **Destination:** {{VPC E IPv6 CIDR}} / **Target:** pcx-eeeegggg
  - **Destination:** {{VPC F IPv4 CIDR}} / **Target:** pcx-ffffgggg
  - **Destination:** {{VPC F IPv6 CIDR}} / **Target:** pcx-ffffgggg

