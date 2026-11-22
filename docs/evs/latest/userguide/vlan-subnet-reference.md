

# VLAN subnets, VLAN IDs, and IP addresses

Amazon Elastic VMware Service creates the VLAN subnets for your environment from the CIDR blocks that you provide. For a short explanation of what a VLAN subnet is, see [Concepts and components of Amazon EVS](concepts.md). For how to size the VPC and choose CIDR blocks, see [Plan your VPC and VLAN subnets](plan-network-sizing.md).

## Rules for all VLAN subnets
<a name="vlan-subnet-rules"></a>

An Amazon EVS VLAN subnet is an Amazon VPC subnet that Amazon EVS manages. Each VLAN subnet has a VLAN tag that segments its traffic from the other VLAN subnets.

**Important**  
Amazon EVS creates all VLAN subnets when you create the environment, from the CIDR blocks that you provide. You can’t add VLAN subnets or change their CIDR blocks after you create the environment. Size each CIDR block for the maximum number of hosts and appliances that you expect over the life of the environment.

The following rules apply to the CIDR block of every VLAN subnet.
+ The netmask must be from /28 to /24.
+ The CIDR block must be inside a CIDR block that’s associated with the VPC. The block can be the primary CIDR block or a secondary CIDR block.
+ The CIDR block must not overlap with any other subnet in the VPC, including the other VLAN subnets and the service access subnet.
+ The vMotion, vSAN, and VTEP VLAN subnets must be the same size as the host management VLAN subnet.

We recommend /24 for each VLAN subnet, the largest size that Amazon EVS allows, because a larger subnet leaves room for more hosts and appliances.

When Amazon EVS creates the VLAN subnets, it associates them implicitly with the main route table of the VPC. After deployment, you must associate each VLAN subnet explicitly with a route table. We recommend a custom route table. For the steps, see [Associate VLAN subnets with a route table](evs-env-config-custom-rt.md). For more information, see [Associate VLAN subnets with a route table](evs-env-config-custom-rt.md).

**Important**  
Amazon EC2 security group rules aren’t enforced on the Amazon EVS elastic network interfaces that are attached to VLAN subnets. To control traffic to and from VLAN subnets, use a network access control list. For more information, see [Create a network ACL for VLAN subnet traffic](evs-env-nacl-cong.md).

## VLAN subnet types
<a name="vlan-subnet-types"></a>

Amazon EVS creates 10 VLAN subnets of nine types. The Expansion type has two subnets. The following table lists them. The columns show the subnet type, the key that you use for its CIDR block in the `initialVlans` parameter of `create-environment`, and what the subnet carries.


| VLAN subnet |  `initialVlans` key | Used for | 
| --- | --- | --- | 
|  Host management |  `vmkManagement`  | ESX host management. The host management VMkernel interface connects to this subnet, which separates management traffic from user traffic. Plan one IP address for each host. | 
|  Management VM |  `vmManagement`  | VMware Cloud Foundation (VCF) management appliances, such as vCenter Server, NSX Manager, NSX Edge nodes, and SDDC Manager or VCF Operations. | 
|  vMotion |  `vMotion`  | vMotion traffic that moves virtual machines between hosts. | 
|  vSAN |  `vSan`  | vSAN storage traffic, separated from other network traffic. | 
|  VTEP (host overlay) |  `vTep`  | NSX tunnel endpoints (TEPs) on the ESX hosts, which encapsulate and decapsulate overlay (Geneve) traffic. The host VTEP network uses two IP addresses for each host. | 
|  Edge VTEP (Edge overlay) |  `edgeVTep`  | NSX Edge overlay tunnel endpoints, for overlay traffic between the NSX Edge nodes and the ESX hosts. | 
|  NSX uplink |  `nsxUplink`  | The Tier-0 gateway uplinks on the NSX Edge nodes, which connect the NSX overlay networks to the rest of your VPC and to external networks. | 
|  HCX uplink |  `hcx`  | Communication between the HCX Interconnect (HCX-IX) and HCX Network Extension (HCX-NE) appliances, and the HCX service mesh uplink. For HCX over the internet, this subnet uses a public CIDR block. For more information, see [Plan HCX connectivity](plan-hcx-connectivity.md). | 
|  Expansion (two subnets) |  `expansionVlan1`, `expansionVlan2`  | Space for other VCF-supported functions, such as NSX Federation. | 

## MTU by network function
<a name="vlan-subnet-mtu"></a>

The following table lists the MTU that you configure in VCF for each VLAN subnet. The columns show the VLAN subnet, with its function name in parentheses where the guide gives one, and its MTU.


| VLAN subnet | MTU (bytes) | 
| --- | --- | 
| Host management (`vmkManagement`) | 1500 | 
| Management VM (`vmManagement`) | 1500 | 
| vMotion | 8500 | 
| vSAN | 8500 | 
| VTEP (host overlay, `vTep`) | 8500 | 
| Edge VTEP (Edge overlay, `edgeVTep`) | 8500 | 
| NSX uplink (`nsxUplink`) | 1500 | 

**Important**  
Configure jumbo frames (MTU 8500) on the vMotion, vSAN, and overlay (TEP) networks. The management and uplink networks use MTU 1500. The MTU must be the same across the network path, or vSAN and overlay traffic fails.

## VLAN IDs
<a name="vlan-subnet-ids"></a>

Amazon EVS assigns a VLAN ID to each VLAN subnet when it creates the environment. You use these VLAN IDs when you configure the distributed switch, port groups, uplink profiles, and host networking in VCF.

To find the VLAN IDs for your environment, use one of the following methods.
+ Open the Amazon EVS console. In the navigation pane, choose **Environments**, choose your environment, and then choose the **Networks and connectivity** tab.
+ Run the `list-environment-vlans` command, and match each VLAN on its `functionName` value, for example `vmManagement` or `edgeVTep`.

  In the following command, replace `<environment-id>` with the ID of your environment. Replace `<region-code>` with the Region where you created the environment.

  ```bash
  aws evs list-environment-vlans \
      --environment-id <environment-id> \
      --region <region-code>
  ```

  The response lists each VLAN subnet with its `vlanId`, `cidr`, `functionName`, `subnetId`, and `vlanState`. For the full response, see [ListEnvironmentVlans](https://docs.aws.amazon.com/evs/latest/APIReference/API_ListEnvironmentVlans.html) in the *Amazon EVS API Reference*.

## Reserved IP addresses
<a name="vlan-subnet-reserved-addresses"></a>

VLAN subnets are VPC subnets, so the standard Amazon VPC rules for reserved addresses apply. The first four IP addresses and the last IP address in each VLAN subnet CIDR block aren’t available for your hosts or appliances. For example, a /24 VLAN subnet has 251 addresses that you can use. For more information, see [Subnet CIDR blocks](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-sizing.html) in the *Amazon VPC User Guide*.

The gateway address of a VLAN subnet doesn’t respond to ICMP ping from outside the subnet. A gateway reachability check can fail even when routing is correct.

## MTU and throughput on the network path
<a name="vlan-subnet-mtu-throughput"></a>

Traffic that leaves the VPC is limited by the MTU of each AWS network component on the path. The following table lists the maximum MTU of each component.


| Network component | Maximum MTU (bytes) | 
| --- | --- | 
| Amazon EC2 instances in a VPC | 9001 | 
|  AWS Transit Gateway | 8500 | 
|  Direct Connect transit virtual interface | 8500 | 

All north-south traffic between the NSX overlay and the VPC goes through the active NSX Edge node. An undersized Edge node can limit throughput. For more information, see [Plan NSX Edge and VPC Route Server design](plan-nsx-design.md).