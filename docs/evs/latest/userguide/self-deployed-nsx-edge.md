

# Step 5: Configure NSX networking

After the VMware Cloud Foundation (VCF) Installer completes bringup, NSX Manager is operational. The NSX Edge cluster and the Tier-0 gateway aren’t yet configured for connectivity with Amazon VPC Route Server. In this step, you deploy the Edge cluster, create the Tier-0 gateway, and configure Border Gateway Protocol (BGP) peering with the route server in NSX Manager.

You can create your overlay networks with Tier-0 and Tier-1 gateways on the NSX Edges directly, or by configuring NSX VPCs, a centralized NSX transit gateway, and Edge clusters. For design guidance, see [Plan NSX Edge and VPC Route Server design](plan-nsx-design.md).

**Note**  
NSX defines its own **VPC** and **transit gateway** abstractions, which are different from Amazon VPC and AWS Transit Gateway. On this page, VPC and transit gateway refer to the AWS resources unless the name starts with NSX.

Before you begin, confirm that the following are in place.
+ VCF installation completed successfully, and NSX Manager and your VCF management appliances are accessible.
+ Your route server is created with endpoints, peers, and propagations. For more information, see [Set up VPC Route Server and on-premises connectivity](network-route-server.md).
+ You have the two route server endpoint IP addresses. Both endpoints are in the service access subnet, which provides redundancy.
+ You have the route server peer IP addresses that you chose from the NSX uplink VLAN subnet. You assign them to the Tier-0 external interfaces.
+ You have chosen two private BGP autonomous system numbers (ASNs). They must match the values that you configured on the route server peers.
  + NSX Edge Tier-0 local ASN (for example, `65000`)
  + VPC Route Server (remote) ASN (for example, `65022`)

    Private ASNs are in the range 64512 to 65534 (16-bit) or 4200000000 to 4294967294 (32-bit).

## Prepare the Edge networking objects
<a name="sd-nsx-prepare-objects"></a>

The NSX Edge nodes need the following vSphere and NSX objects before you deploy the Edge cluster. Create them in the vSphere Client and in NSX Manager.
+ A distributed port group with VLAN trunking (VLAN range 0 to 4094) for the Edge uplink and Edge TEP traffic.
+ An IP pool for the Edge tunnel endpoint (TEP) addresses. Take the addresses from the Edge overlay (`edgeVTep`) VLAN subnet of your environment.
+ A VLAN transport zone for the Edge uplinks.

If you deploy with the EVS Deployment Orchestrator (EDO), a tool in the [Solutions for Amazon EVS repository](https://github.com/aws/solutions-for-amazon-evs), EDO creates these objects. If you install VCF with the VCF Installer, you create the objects yourself. For more information, see [Deploy with the EVS Deployment Orchestrator](deploy-with-edo.md).

## Create an uplink profile
<a name="sd-nsx-uplink-profile"></a>

Before you deploy the NSX Edge cluster, create an uplink profile in NSX Manager. The uplink profile defines the teaming policy, transport VLAN, and maximum transmission unit (MTU) that Edge transport nodes use for overlay (Geneve) traffic.

For version-specific field labels and screenshots, see the Broadcom documentation in the following table.


| VCF version | Broadcom documentation | 
| --- | --- | 
| VCF 9.0 |  [Create an Uplink Profile](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/configuring-profiles/create-an-uplink-profile.html)  | 
| VCF 9.1 |  [Add an Uplink Profile](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/advanced-network-management/transport-zones-and-transport-nodes/configuring-profiles/create-an-uplink-profile.html)  | 

Configure the profile with the following values for Amazon Elastic VMware Service.


| Parameter | Value | 
| --- | --- | 
| Name | For example, `edge-uplink-profile`  | 
| Teaming policy | Failover Order | 
| Active Uplinks |  `uplink1`  | 
| Standby Uplinks | Leave empty. NSX Edge VMs don’t support standby uplinks. | 
| Transport VLAN | The Amazon EVS-assigned Edge TEP (`edgeVTep`) VLAN ID. To find the VLAN ID, see the VLAN IDs step in [Prepare the VLAN subnets for VCF](self-deployed-create-env.md#self-deployed-create-env-after). | 
| MTU |  `8500`  | 

Use the uplink name `uplink1` when you configure each Edge transport node in the next section.

## Deploy the NSX Edge cluster
<a name="sd-nsx-edge-cluster"></a>

Deploy two Edge transport nodes and group them into an Edge cluster with the NSX Manager UI. The workflow order differs by VCF version. The following table lists the workflow for each VCF version and the Broadcom documentation for the complete procedure.


| VCF version | Workflow | Broadcom documentation | 
| --- | --- | --- | 
| VCF 9.0 | Create the Edge transport nodes one by one, and then create the Edge cluster. |  [Create an Edge Transport Node](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/create-an-edge-transport-node.html) and [Create an Edge Cluster](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/create-an-edge-cluster.html)  | 
| VCF 9.1 | Start an Edge cluster workflow, and add the nodes within it. |  [Create an NSX Edge Cluster and Add Edge Nodes](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/advanced-network-management/installing-nsx-edge/create-an-edge-transport-node.html)  | 

When you configure the Edge nodes for your Amazon EVS environment, use the following values.


| Parameter | Value | 
| --- | --- | 
| Name | A unique name for each Edge node (for example, `edge-node-01` and `edge-node-02`). | 
| Form factor | Large (recommended) | 
| Compute and datastore | A compute resource and datastore appropriate for your deployment. | 
| Management IP | An IP address from the Amazon EVS VM management VLAN subnet. | 
| Default gateway | The default gateway for the Amazon EVS VM management VLAN subnet. | 
| Management interface | The VM management port group. | 
| Transport networking | The Amazon EVS-assigned transport VLAN and the uplink profile that you created, for datapath connectivity. | 

## Create the Tier-0 gateway
<a name="sd-nsx-tier0"></a>

To create the Tier-0 gateway, do the following.

1. In NSX Manager, choose **Networking**, and then choose **Tier-0 Gateways**.

1. Choose **Add Tier-0 Gateway** and configure the following.

   1. For **Name**, enter a name, for example `evs-tier0-gw`.

   1. For **HA mode**, choose **Active-Standby**, and set the failover mode to **Non-preemptive**.

   1. For **Edge cluster**, choose the Edge cluster that you created.

1. Save the Tier-0 gateway.

1. Expand **Interfaces**, and add one external interface for each Edge node. Each interface is on the NSX uplink VLAN, through the VLAN transport zone that you created.

   1. For **Edge node**, choose Edge node 1 for the first interface and Edge node 2 for the second.

   1. For **IP address**, enter a VPC Route Server peer IP address that you chose in [Set up VPC Route Server and on-premises connectivity](network-route-server.md), with the prefix length of the NSX uplink VLAN subnet. Each interface uses a different peer IP address.

1. Save the interfaces.

The VPC Route Server accepts BGP sessions only from the peer IP addresses that you created, so each external interface must use one of them. The BGP neighbors in the next section use these interfaces as source interfaces.

**Note**  
Make sure that both the Tier-0 and Tier-1 gateways have **Non-preemptive** failover. Non-preemptive is the NSX default. It avoids the BGP session drop that occurs when a recovered Edge node fails back to the preferred node.

## Configure BGP
<a name="sd-nsx-bgp"></a>

We recommend a full mesh, in which each of the two Edge nodes peers with both route server endpoints, for four BGP sessions in total. A full mesh keeps routes propagating if a route server endpoint goes into maintenance. At minimum, configure two sessions, with each Edge node peering with one endpoint.

The Tier-0 external interfaces and the route server endpoints are in different subnets, so these are multihop BGP sessions.

To configure BGP, do the following.

1. Select the Tier-0 gateway and expand **BGP**.

1. Turn on **BGP** and set the **Local AS** number to the NSX Edge Tier-0 ASN that you chose (for example, `65000`).

1. Under **BGP Neighbors**, configure peering between the Edge nodes and the route server endpoints. For a full mesh, add the four neighbors in the following table. Set the **Remote AS** of every neighbor to the VPC Route Server ASN (for example, `65022`) and the **Address family** to IPv4 Unicast.


<table>
<thead>
  <tr><th>Neighbor</th><th>Neighbor address</th><th>Source interface</th></tr>
</thead>
<tbody>
  <tr><td>Edge 1 to endpoint 1</td><td> <code>&lt;route-server-endpoint-1-ip&gt;</code> </td><td>External interface on Edge node 1</td></tr>
  <tr><td>Edge 1 to endpoint 2</td><td> <code>&lt;route-server-endpoint-2-ip&gt;</code> </td><td>External interface on Edge node 1</td></tr>
  <tr><td>Edge 2 to endpoint 1</td><td> <code>&lt;route-server-endpoint-1-ip&gt;</code> </td><td>External interface on Edge node 2</td></tr>
  <tr><td>Edge 2 to endpoint 2</td><td> <code>&lt;route-server-endpoint-2-ip&gt;</code> </td><td>External interface on Edge node 2</td></tr>
</tbody>
</table>


   Set the BGP multihop limit to at least 2. Make sure that the Tier-0 gateway can reach each route server endpoint IP address, for example with a static route to the endpoint through the uplink gateway.

1. Choose **Save**.

1. Wait for the BGP sessions to establish.

1. To advertise only overlay network routes to the VPC Route Server, configure route redistribution and an outbound route filter on the Tier-0 gateway.

   1. On the Tier-0 gateway, expand **Route Re-Distribution**. Turn on redistribution into BGP for your overlay network route types, for example **Tier-1 Connected** (workload segment subnets), **Tier-1 NAT**, and **Tier-1 Static Routes**.

      Don’t select **External Interface Subnet**, and don’t select Tier-0 **Static Routes**. Redistributing **External Interface Subnet** advertises the NSX uplink subnet to AWS. Redistributing **Static Routes** advertises the route server endpoint host routes again.

   1. (Optional) Apply an outbound route filter for RFC 1918 networks to limit the CIDR blocks that are advertised to your VPC. Create an IP prefix list that permits `10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16` (including more-specific routes within them) and denies all other prefixes. Apply it as the out filter on each BGP neighbor.

## Verify BGP peering
<a name="sd-nsx-verify"></a>

To verify BGP peering, do the following.

1. In NSX Manager, choose **Networking**, choose **Tier-0 Gateways**, and then choose **BGP**. Under **BGP Neighbors**, confirm that the neighbors show status **Established**.

1. In the [Amazon VPC console](https://console.aws.amazon.com/vpc), go to **Route Server**, **Routes**, and confirm that NSX overlay routes appear.

1. In NSX Manager, verify that VPC routes are learned under **Routing**, **Forwarding Table**.

If a BGP session doesn’t establish, or routes don’t appear in the VPC route table, see [NSX Edge and BGP symptoms](troubleshoot-self-deployed.md#troubleshoot-sd-nsx).

You have configured NSX networking when the BGP sessions are established and routes are propagating.

Next step: [Step 6: Create connectors](self-deployed-create-connectors.md).