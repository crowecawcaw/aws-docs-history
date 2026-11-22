

# Set up VPC Route Server and on-premises connectivity

Amazon Elastic VMware Service uses Amazon VPC Route Server for dynamic routing between NSX and your VPC underlay network by using Border Gateway Protocol (BGP). Create a route server with endpoints and peers in your VPC, and then optionally connect your on-premises network through a transit gateway. You can use the Amazon VPC console or the AWS CLI. The VPC Route Server tutorial in the * Amazon VPC User Guide* has the steps for both.

Your environment deployment fails if you don’t meet the following requirements for VPC Route Server.
+ You must create at least two route server endpoints in the service access subnet.
+ The peer autonomous system number (ASN) on the route server peers must match the ASN of the NSX Tier-0 gateway.
+ Each route server peer must use a unique IP address from the NSX uplink VLAN subnet.
+ Every route table that you propagate to must have at least one explicit subnet association.

## Before you begin
<a name="evs-env-rs-prereq"></a>

Make sure that the following are true.
+ You’ve created the VPC and the service access subnet. For instructions, see [Create a VPC with subnets and route tables](network-create-vpc.md).
+ You have IAM permissions to manage VPC Route Server resources.
+ You’ve chosen the Amazon-side ASN for the route server. The value must be in the range 1 to 4294967295. You can use any private ASN, for example `65022`.
+ You’ve chosen the peer ASN for the NSX Tier-0 gateway. The default ASN for an NSX Edge appliance is `65000`.
+ You’ve chosen the peer IP addresses from the NSX uplink VLAN CIDR block that you pass as `initialVlans.nsxUplink` when you create the environment. Amazon EVS creates the NSX uplink VLAN subnet during environment creation, so it doesn’t exist yet. The addresses must fall within that CIDR block and must remain unused.

How the peer values are used differs by deployment mode:
+ In Self-deployed mode, you configure the NSX Edge Tier-0 gateway yourself. Use the Amazon-side ASN as the BGP neighbor (remote) ASN, and use the peer ASN as the Tier-0 local ASN. For more information, see [Step 5: Configure NSX networking](self-deployed-nsx-edge.md).
+ In EVS-deployed mode, Amazon EVS assigns the peer IP addresses to the NSX Edge nodes during environment deployment.

## Create the route server, endpoints, and peers
<a name="evs-env-rs-steps"></a>

Follow the [VPC Route Server get started tutorial](https://docs.aws.amazon.com/vpc/latest/userguide/route-server-tutorial.html) in the * Amazon VPC User Guide* and use these Amazon EVS values:

1. Create a route server with the Amazon-side ASN that you chose.

   We recommend that you enable persistent routes with a persist duration of 1 to 5 minutes. Persistent routes keep the routes in the routing database of the route server even if all BGP sessions end. For more information, see [Create a route server](https://docs.aws.amazon.com/vpc/latest/userguide/route-server-tutorial-create.html).

1. Associate the route server with your VPC.

1. Create two route server endpoints, both in the service access subnet.

1. Create the route server peers. Use a unique IP address from the NSX uplink VLAN CIDR block for each peer, and set the peer ASN to the NSX Tier-0 ASN.

   We recommend four peers in a full mesh, so that each of the two NSX Edge nodes peers with both endpoints. A full mesh keeps routes propagating if one endpoint goes into maintenance. You must create at least two peers.

1. Enable route server propagation on the route table that is associated with the service access subnet. That route table must have at least one explicit subnet association. BGP route advertisement fails if a propagated route table has no explicit subnet association.

   If you configure HCX internet connectivity, also enable propagation on the route table of the public subnet. For more information, see [Plan HCX connectivity](plan-hcx-connectivity.md).

   If you use a NAT gateway or a transit gateway, make sure that the route server propagates NSX routes to the VPC route tables that need them.

1. Verify that both endpoints and all peers appear in the route server. BGP sessions stay down until the Amazon EVS environment is deployed and operational.

You have created the VPC Route Server resources that Amazon EVS needs.

**Note**  
For peer liveness detection, Amazon EVS supports only the default BGP keepalive mechanism. Amazon EVS does not support multi-hop Bidirectional Forwarding Detection (BFD).

## Connect your on-premises network (optional)
<a name="getting-started-connect-on-prem"></a>

You can connect your on-premises data center to your VPC with Direct Connect and an associated transit gateway, or with an AWS Site-to-Site VPN attachment to a transit gateway. To reach on-premises systems during environment deployment, add the routes to the VPC main route table. For more information, see [Create a VPC with subnets and route tables](network-create-vpc.md).
+ For Direct Connect, see [Direct Connect gateways and transit gateway associations](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-transit-gateways.html).
+ For AWS Site-to-Site VPN, see [AWS Site-to-Site VPN attachments in Amazon VPC Transit Gateways](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpn-attachments.html) in the * Amazon VPC Transit Gateways Guide*.

**Note**  
Amazon EVS does not support connectivity through an Direct Connect private virtual interface (VIF), or through an AWS Site-to-Site VPN connection that terminates directly in the underlay VPC. For the connection types that Amazon EVS supports, see [Supported network configurations](plan-network-supported.md).

### After you create the environment
<a name="getting-started-config-tgw-assoc"></a>

Complete these steps after you create the environment.

1. Update the transit gateway route tables with the VPC CIDR blocks that the Amazon EVS environment creates. For more information, see [Transit gateway route tables in Amazon VPC Transit Gateways](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html).

1. If you use Direct Connect, update your allowed prefixes so that the Direct Connect gateway sends and receives the updated routes from the VPC. For more information, see [Allowed prefixes interactions for Direct Connect gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/allowed-to-prefixes.html).

## Troubleshoot VPC Route Server
<a name="evs-env-rs-troubleshoot"></a>

If routes don’t propagate or BGP sessions don’t come up after deployment, see [Routes don’t propagate or BGP sessions don’t come up](troubleshoot-networking.md#troubleshoot-rs-routes). If the environment deployment fails because of the route server configuration, see [The deployment fails because of the VPC Route Server configuration](troubleshoot-networking.md#troubleshoot-rs-deploy-fails).

Next, create a network ACL for the VLAN subnets. For instructions, see [Create a network ACL for VLAN subnet traffic](evs-env-nacl-cong.md).