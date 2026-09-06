

# How AWS Outposts works
<a name="how-outposts-works"></a>

AWS Outposts is designed to operate with a constant and consistent connection between your Outpost and an AWS Region. To achieve this connection to the Region, and to the local workloads in your on-premises environment, you must connect your Outpost to your on-premises network. Your on-premises network must provide wide area network (WAN) access back to the Region. It must also provide LAN or WAN access to the local network where your on-premises workloads or applications reside.

**Topics**
+ [Network components](#outposts-networking-components)
+ [VPCs and subnets](#vpc-subnet)
+ [Routing](#routing-hiw)
+ [Service link](#how-service-link)
+ [Local gateways](#how-racks-work)
+ [Bare-metal networking interfaces](#bare-metal)

## Network components
<a name="outposts-networking-components"></a>

AWS Outposts extends an Amazon VPC from an AWS Region to an Outpost with the VPC components that are accessible in the Region, including internet gateways, virtual private gateways, Amazon VPC Transit Gateways, and VPC endpoints. An Outpost is homed to an Availability Zone in the Region and is an extension of that Availability Zone that you can use for resiliency.

The following diagram shows the network components for your Outpost.
+ An AWS Region and an on-premises network
+ A VPC with multiple subnets in the Region
+ An Outpost in the on-premises network
+ Connectivity between the Outpost and local network provided:
  + For Outposts racks: a local gateway
  + For Outposts servers: a local network interface (LNI)

![The VPC networking components for your Outpost.](http://docs.aws.amazon.com/outposts/latest/network-userguide/images/outpost-networking-components.png)


## VPCs and subnets
<a name="vpc-subnet"></a>

A virtual private cloud (VPC) spans all Availability Zones in its AWS Region. You can extend any VPC in the Region to your Outpost by adding an Outpost subnet. To add an Outpost subnet to a VPC, specify the Amazon Resource Name (ARN) of the Outpost when you create the subnet.

Outposts support multiple subnets. You can specify the EC2 instance subnet when you launch the EC2 instance in your Outpost. You can't specify the underlying hardware where the instance is deployed, because the Outpost is a pool of AWS compute and storage capacity.

Each Outpost can support multiple VPCs that can have one or more Outpost subnets. For information about VPC quotas, see [Amazon VPC Quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html) in the *Amazon VPC User Guide*.

You create Outpost subnets from the VPC CIDR range of the VPC where you created the Outpost. You can use the Outpost address ranges for resources, such as EC2 instances that reside in the Outpost subnet. 

## Routing
<a name="routing-hiw"></a>

By default, every Outpost subnet inherits the main route table from its VPC. You can create a custom route table and associate it with an Outpost subnet.

The route tables for Outpost subnets work as they do for Availability Zone subnets. You can specify IP addresses, internet gateways, local gateways, virtual private gateways, and peering connections as destinations. For example, each Outpost subnet, either through the inherited main route table, or a custom table, inherits the VPC local route. This means that all traffic in the VPC, including the Outpost subnet with a destination in the VPC CIDR remains routed in the VPC.

Outpost subnet route tables can include the following destinations:
+ **VPC CIDR range** – AWS defines this at installation. This is the local route and applies to all VPC routing, including traffic between Outpost instances in the same VPC.
+ **AWS Region destinations** – This includes prefix lists for Amazon DynamoDB gateway endpoint, AWS Transit Gateways, virtual private gateways, internet gateways, and VPC peering.

  If you have a peering connection with multiple VPCs on the same Outpost, the traffic between the VPCs remains in the Outpost and does not use the service link back to the Region.
+ **Intra-VPC communication across Outposts with local gateway** – You can establish communication between subnets in the same VPC across different Outposts with local gateways using direct VPC routing. For more information, see:
  + [Direct VPC routing](https://docs.aws.amazon.com/outposts/latest/network-userguide/routing.html#direct-vpc-routing)
  + [Routing to an AWS Outposts local gateway](https://docs.aws.amazon.com/vpc/latest/userguide/route-table-options.html#route-tables-lgw)

## Service link
<a name="how-service-link"></a>

The service link is a connection from your Outpost back to your chosen AWS Region or Outposts home Region. The service link is an encrypted set of VPN connections that are used whenever the Outpost communicates with your chosen home Region. You use a virtual LAN (VLAN) to segment traffic on the service link. The service link VLAN enables communication between the Outpost and the AWS Region for both management of the Outpost and intra-VPC traffic between the AWS Region and Outpost. 

Your service link is created when your Outpost is provisioned. If you have a server form factor, you create the connection. If you have a rack, AWS creates the service link. For more information, see:
+ [AWS Outposts connectivity to AWS Regions](https://docs.aws.amazon.com/outposts/latest/network-userguide/region-connectivity.html)
+ [Application/workload routing ](https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/applicationworkload-routing.html) in the *AWS Outposts High Availability Design and Architecture Considerations* AWS Whitepaper

**IPv6 support**  
You can create dual-stack (IPv6) subnets on your Outpost. AWS Outposts supports IPv6 traffic only between subnets in the same Outpost. The service link does not support IPv6 between your Outpost and the AWS Region. In addition, AWS Outposts cannot use IPv6 over the internet gateway.

## Local gateways
<a name="how-racks-work"></a>

Outposts racks include a local gateway to provide connectivity to your on-premises network. If you have an Outposts rack, you can include a local gateway as target where the destination is your on-premises network. Local gateways are only available for Outposts racks and can only be used in VPC and subnet route tables that are associated with an Outposts rack. For more information, see:
+ [Local gateways for your Outposts racks](https://docs.aws.amazon.com/outposts/latest/network-userguide/outposts-local-gateways.html)
+ [Application/workload routing ](https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/applicationworkload-routing.html) in the *AWS Outposts High Availability Design and Architecture Considerations* AWS Whitepaper

**IPv6 support**  
The local gateway supports only IPv4 traffic. It does not support IPv6.

## Bare-metal networking interfaces on Bmn instances
<a name="bare-metal"></a>

Instances from the Bmn family include one or more low latency and high throughput bare-metal local networking interfaces. For specialized mission-critical use cases, you can connect to your on-premises network through these high performance interfaces.