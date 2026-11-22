

# Plan NSX Edge and VPC Route Server design

An NSX Edge cluster connects the NSX overlay networks of your environment to the VPC underlay. The Tier-0 gateway on that cluster exchanges routes with Amazon VPC Route Server over BGP, so plan the ASNs and peer addresses before you create the environment.

## NSX components
<a name="plan-nsx-design-components"></a>

 **Tier-0 gateway**   
The Tier-0 gateway handles all north-south traffic between the NSX overlay networks and the VPC. Amazon Elastic VMware Service supports only one Tier-0 gateway, on an Active/Standby NSX Edge cluster with two NSX Edge nodes. This Tier-0 gateway connects to and advertises all overlay networks that you configure.

 **Tier-1 gateways**   
A Tier-1 gateway handles east-west traffic between routed segments. It has downlinks to segments and an uplink to the Tier-0 gateway. You can create additional Tier-1 gateways if you need them.

 **NSX Edge cluster**   
The Edge cluster has two NSX Edge nodes in Active/Standby mode. It runs the Tier-0 and Tier-1 gateways and their BGP routing. The active Edge node carries all north-south traffic, so an undersized Edge node can become a bottleneck. We recommend the Large form factor for the Edge nodes.

 **Amazon VPC Route Server**   
VPC Route Server is a VPC service that Amazon EVS uses for BGP-based dynamic routing between the NSX Edge nodes and your VPC route tables. You create the route server, its endpoints and its peers yourself.

## How the deployment modes differ
<a name="plan-nsx-design-modes"></a>

The route server requirements are the same in both modes. Who deploys the Edge cluster and configures BGP differs.


| Item | VCF 9.x (Self-deployed) | VCF 5.2.x (EVS-deployed) | 
| --- | --- | --- | 
| Edge cluster and Tier-0 gateway | You deploy them in NSX Manager after you install VMware Cloud Foundation (VCF). | Amazon EVS deploys them when it creates the environment. | 
| Route server peers at environment creation | You don’t enter peers when you create the environment. | You enter two route server peers when you create the environment. Amazon EVS assigns their IP addresses to the two NSX Edge nodes. | 
| BGP on the Tier-0 gateway | You configure BGP neighbors, route redistribution, and route filters yourself. | Amazon EVS configures BGP peering with the route server peers that you entered. | 
| Peering topology | We recommend a full mesh of four peers, so that each Edge node peers with both route server endpoints. A full mesh keeps routes propagating if a route server endpoint goes into maintenance. You must create at least two peers. | Two peers, one for each NSX Edge node. | 

For the Self-deployed steps, see [Step 5: Configure NSX networking](self-deployed-nsx-edge.md).

## Route server requirements
<a name="plan-nsx-design-route-server"></a>

Your route server must meet these requirements, or the environment deployment fails:
+ The route server is associated with your VPC.
+ The route server has at least two endpoints, both in the service access subnet.
+ The peer ASN on each route server peer matches the ASN of the NSX Edge Tier-0 gateway.
+ Each route server peer uses a unique, unused IP address from the NSX uplink VLAN subnet. The NSX uplink VLAN subnet doesn’t exist yet when you create the peers, so choose the addresses from the CIDR block that you plan to use for it.
+ Route server propagation is enabled on the route table associated with the service access subnet. Every propagated route table has at least one explicit subnet association, otherwise BGP route advertisement fails.

Plan the following values for the route server and the Tier-0 gateway.


| Value | Rule | Example | 
| --- | --- | --- | 
| Amazon-side ASN (route server) | In the range 1 to 4294967295. AWS recommends a private ASN, 64512 to 65534 (16-bit) or 4200000000 to 4294967294 (32-bit). The Tier-0 gateway uses it as the remote ASN. |  `65022`  | 
| NSX Edge Tier-0 ASN | A private ASN. It must match the peer ASN on every route server peer. The NSX Edge default is 65000. |  `65000`  | 
| Route server peer IP addresses | Unique, unused addresses inside the CIDR block that you choose for the NSX uplink VLAN subnet. Don’t use the reserved addresses of the subnet. |  `10.1.8.10`, `10.1.8.200`  | 

Also plan for these behaviors:
+ Amazon EVS supports only the default BGP keepalive mechanism for peer liveness detection. Amazon EVS doesn’t support multi-hop Bidirectional Forwarding Detection (BFD).
+ We recommend that you enable persistent routes on the route server, with a persist duration of 1 to 5 minutes. Routes then stay in the route server’s routing database even if all BGP sessions end.
+ For HCX internet connectivity, configure route server propagation for both the service access subnet and the public subnet of the VPC.
+ BGP connectivity status stays down until the environment is deployed and operational.

## How routes reach the rest of your network
<a name="plan-nsx-design-routes"></a>

The Tier-0 gateway advertises the NSX overlay prefixes to the route server, and route server propagation installs them in your VPC route tables. A transit gateway or AWS Cloud WAN doesn’t learn these routes. Add static routes for your overlay networks to the transit gateway route tables after you create the environment.

In a Self-deployed environment, you choose what the Tier-0 gateway advertises. We recommend that you redistribute only overlay network routes, so that the NSX uplink subnet and the route server endpoint routes aren’t advertised back to AWS. The Edge uplink interfaces and the route server endpoints are in different subnets, so the BGP sessions are multihop sessions with a hop limit of at least 2.

The NSX uplink network uses MTU 1500. The overlay (TEP) networks use MTU 8500.

## Limits
<a name="plan-nsx-design-limits"></a>

Amazon EVS has the following limits.
+ One Tier-0 gateway for each environment
+ One NSX Edge cluster with two Edge nodes in Active/Standby mode for the Tier-0 gateway
+ At least two route server endpoints, in the service access subnet

## Availability Zone failure
<a name="plan-nsx-design-az"></a>

An Amazon EVS environment runs in one Availability Zone. For more information, see [VPC and subnets](plan-network-supported.md#plan-network-supported-vpc). For recovery designs across Availability Zones or Regions, see [Plan for resilience and recovery](plan-resilience.md).

To create the route server, endpoints and peers, see [Set up VPC Route Server and on-premises connectivity](network-route-server.md).