

# Plan your VPC and VLAN subnets

Your Amazon Elastic VMware Service environment uses address space from one VPC CIDR block for the service access subnet and the 10 VLAN subnets that Amazon EVS creates. Size this space for the hosts and VMware Cloud Foundation (VCF) management appliances that you plan to run over the lifetime of the environment, because you can’t add space later.

You can’t change these settings after you create the environment.
+ The VPC CIDR block
+ The CIDR blocks of the VLAN subnets
+ The number of VLAN subnets

## VPC CIDR block
<a name="plan-network-sizing-vpc"></a>

Amazon EVS deploys your environment into a VPC that you provide. The VPC CIDR block must meet these requirements:
+ It is an IPv4 CIDR block. Amazon EVS doesn’t support IPv6.
+ It is /22 or larger.
+ It has room for the service access subnet and all 10 VLAN subnets. It also needs room for any other subnets that you create in the VPC, for example a public subnet for a NAT gateway.
+ It belongs to one environment only. A VPC can’t be used by more than one deployed Amazon EVS environment.

Use a CIDR block that is unique across your environments.

The /22 minimum doesn’t leave room for /24 VLAN subnets. A /22 holds four /24 blocks. If you use /24 for the service access subnet and for each of the 10 VLAN subnets, you need 11 /24 blocks, so choose a /20 or larger. The example values in the [Deployment prerequisite checklist](evs-deployment-prereq-checklist.md) use this layout.

An Amazon EVS environment runs in one Availability Zone. All VPC subnets that Amazon EVS uses must be in that Availability Zone, in a [Region where Amazon EVS is available](regions-reference.md). For more information, see [VPC and subnets](plan-network-supported.md#plan-network-supported-vpc).

For HCX internet connectivity, you also add a public IPv4 CIDR block to the VPC as an additional CIDR. For more information, see [Plan HCX connectivity](plan-hcx-connectivity.md).

## Service access subnet
<a name="plan-network-sizing-service-access"></a>

The service access subnet is a standard VPC subnet that you create before you create the environment. Amazon EVS uses it for service access to your environment, and the endpoints of Amazon VPC Route Server run in it.

Follow these guidelines for the service access subnet.
+ Create it in the same Availability Zone as the rest of the environment.
+ We recommend a /24 netmask, so that the subnet has room to grow.
+ Leave room in it for the two route server endpoints.

For more information, see [Concepts and components of Amazon EVS](concepts.md).

## VLAN subnets
<a name="plan-network-sizing-vlans"></a>

Amazon EVS creates 10 VLAN subnets in your VPC when you create the environment. You enter a CIDR block for each one. Every VLAN subnet CIDR block must meet these requirements:
+ Its size is between /28 and /24.
+ It is inside a CIDR block that is associated with the VPC. The block can be the primary CIDR block or a secondary CIDR block.
+ It doesn’t overlap with any other subnet in the VPC, including the other VLAN subnets and the service access subnet.

The following table lists the VLAN subnets. The API name column shows the name that you use in the `initialVlans` parameter.


| VLAN subnet | API name | Carries | Size rule | Sizing guidance | 
| --- | --- | --- | --- | --- | 
| Host management |  `vmkManagement`  | ESX host management traffic. | /28 to /24. | One IP address per host. Plan for the largest number of hosts that you expect in the environment. | 
| vMotion |  `vMotion`  | vMotion traffic between hosts. | Same size as host management. | One or more IP addresses per host, depending on your VCF configuration. | 
| vSAN |  `vSan`  | vSAN traffic between hosts. | Same size as host management. | One or more IP addresses per host, depending on your VCF configuration. | 
| VTEP |  `vTep`  | Host overlay (Geneve) traffic. | Same size as host management. | Two IP addresses per host. | 
| Edge VTEP |  `edgeVTep`  | NSX Edge overlay traffic. | /28 to /24. | IP addresses for the NSX Edge nodes. | 
| Management VM |  `vmManagement`  | VCF management appliances. | /28 to /24. | IP addresses for the appliances that you plan to deploy, for example vCenter, the NSX Manager cluster, the NSX Edge nodes, and SDDC Manager or VCF Operations. | 
| HCX uplink |  `hcx`  | VMware HCX appliances. | /28 to /24. Exactly /28 for a public HCX VLAN. | IP addresses for the HCX appliances, if you use HCX. For the public HCX VLAN rules, see [Plan HCX connectivity](plan-hcx-connectivity.md). | 
| NSX uplink |  `nsxUplink`  | NSX Edge uplinks to the VPC. | /28 to /24. | IP addresses for the NSX Edge uplink interfaces. The route server peers use addresses from this subnet. For more information, see [Plan NSX Edge and VPC Route Server design](plan-nsx-design.md). | 
| Expansion VLAN 1 |  `expansionVlan1`  | Not assigned. You use it to extend your VCF deployment. | /28 to /24. | Reserve space to extend your deployment, for example for NSX Federation. | 
| Expansion VLAN 2 |  `expansionVlan2`  | Not assigned. You use it to extend your VCF deployment. | /28 to /24. | Reserve space to extend your deployment, for example for NSX Federation. | 

As a starting point, use /24 for each VLAN subnet unless you have a specific reason to choose otherwise. Because you can’t add or resize VLAN subnets later, extra address space after creation can come only from the expansion VLANs.

The VLAN subnets use these MTU values:
+ 1500 for host management, Management VM and NSX uplink.
+ 8500 for vMotion, vSAN, VTEP, and Edge VTEP.

## Reserved IP addresses
<a name="plan-network-sizing-reserved"></a>

Amazon EVS VLAN subnets are VPC subnets, so the standard VPC reserved addresses apply. In each VLAN subnet and in the service access subnet, AWS reserves the first four IP addresses and the last IP address of the CIDR block. You can’t assign these addresses to hosts, appliances, or route server peers. For example, in `10.1.1.0/24` the reserved addresses are `10.1.1.0` to `10.1.1.3` and `10.1.1.255`. For more information, see [Subnet CIDR blocks](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-sizing.html) in the *Amazon VPC User Guide*.

Count the reserved addresses when you size each subnet. A /28 has 16 addresses, of which 11 are usable.

The public HCX VLAN has its own reserved addresses. For more information, see [Plan HCX connectivity](plan-hcx-connectivity.md).

## VLAN IDs
<a name="plan-network-sizing-vlan-ids"></a>

Amazon EVS assigns a VLAN ID to each VLAN subnet. You use these IDs when you configure VCF networking, for example the Edge VTEP VLAN ID in the NSX uplink profile. For more information, see [VLAN subnets, VLAN IDs, and IP addresses](vlan-subnet-reference.md).

After you create the environment, you can look up the IDs in the Amazon EVS console. In the navigation pane, choose **Environments**, choose your environment, and then choose the **Networks and connectivity** tab. You can also run `aws evs list-environment-vlans`.

When you have sized your subnets, record the values in the [Deployment prerequisite checklist](evs-deployment-prereq-checklist.md). To create the VPC and the service access subnet, see [Create a VPC with subnets and route tables](network-create-vpc.md).