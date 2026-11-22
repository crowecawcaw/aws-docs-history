

# Amazon EVS architecture

An Amazon Elastic VMware Service environment runs VMware Cloud Foundation (VCF) on Amazon EC2 bare metal instances inside your own Amazon VPC.

## VCF components
<a name="architecture-components"></a>

Amazon EVS implements a VCF consolidated architecture model. In this model, VCF management components and customer workloads run together on a consolidated domain. The environment is managed from a single vCenter Server, with vSphere resource pools that isolate management workloads from customer workloads.

The consolidated domain contains the following VCF management components:
+ ESX hosts
+ A vCenter Server instance
+ The VCF management appliance (SDDC Manager for VCF 5.2.x)
+ A vSAN datastore, on hosts with local storage
+ An NSX Manager cluster (three nodes in the standard topology, one node in a simple deployment)
+ A vSphere cluster
+ An NSX Edge cluster

The following diagram shows an example Amazon EVS architecture and how the components in the environment are connected. The area labeled **Consolidated domain** is the Amazon EVS environment with a consolidated domain architecture. The area labeled **Amazon EVS networks** is the underlying Amazon EVS network topology.

![NSX Edge nodes connect NSX overlay networks to VPC VLAN subnets through VPC Route Server in a consolidated VCF domain.](https://docs.aws.amazon.com/evs/latest/userguide/images/amazon-evs-architecture.png)


## Network topology
<a name="network-architecture"></a>

An Amazon EVS environment has two network layers, as follows.

 ** Amazon VPC underlay**   
The VPC and the Amazon EVS VLAN subnets that Amazon EVS creates in it form the underlay network for your VCF deployment. The underlay provides connectivity for NSX overlay networks, host management, vMotion, and vSAN. Amazon VPC Route Server provides dynamic routing between the underlay network and the overlay networks. For more information, see [Amazon EVS VLAN subnet](concepts.md#concepts-evs-network).

 **VMware NSX overlay**   
The NSX overlay network carries the VCF management appliances and your workloads. You can configure additional NSX overlay networks to isolate workloads or applications from each other within your environment. For VCF 5.2.x, see [Overlay Design for VMware Cloud Foundation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-design-5-2/nsx-t-design-for-the-management-domain/overlay-design-for-nsx-t-data-center-for-the-management-domain.html#GUID-025420AC-D915-439A-BF2A-D3C9F2FAB433-en) in the Broadcom documentation.

An Amazon EVS environment runs in one Availability Zone. All VPC subnets that Amazon EVS uses must be in that Availability Zone. For more information, see [VPC and subnets](plan-network-supported.md#plan-network-supported-vpc).

### Where workloads run
<a name="architecture-workload-placement"></a>

**Important**  
Deploy the guest virtual machines that run your workloads on NSX overlay networks. Amazon EVS VLAN subnets carry VCF underlay traffic only, and Amazon EVS doesn’t support guest virtual machines on them.

### How the layers connect
<a name="architecture-edge-routing"></a>

An Active/Standby NSX Edge cluster with two NSX Edge nodes connects the two network layers. The NSX Edge nodes carry traffic between the overlay networks and the VPC. They also carry internet traffic, and traffic for private connectivity through Direct Connect or AWS Site-to-Site VPN with a transit gateway.

Who sets up the NSX Edge cluster and its routing depends on the deployment mode. For the comparison, see [Differences between deployment modes](deployment-mode-differences.md).

### NSX Edge cluster
<a name="evs-nsx-edge"></a>

The NSX Edge cluster has two NSX Edge nodes that run in Active/Standby mode. It provides the platform on which the Tier-0 and Tier-1 gateways run, along with IPsec VPN connections and their Border Gateway Protocol (BGP) routing.

For design guidance for the NSX Edge cluster and VPC Route Server, see [Plan NSX Edge and VPC Route Server design](plan-nsx-design.md).

### Tier-0 gateway
<a name="evs-t0-gateway"></a>

The Tier-0 gateway handles all north-south traffic between the logical and physical networks, and is created on the NSX overlay network. It runs on the NSX Edge cluster and peers with VPC Route Server over BGP.

Amazon EVS supports only one Tier-0 gateway for an Active/Standby NSX Edge cluster with two NSX Edge nodes. This Tier-0 gateway connects to and advertises all overlay networks that you configure for use with Amazon EVS.

### Tier-1 gateway
<a name="evs-t1-gateway"></a>

The Tier-1 gateway handles east-west traffic between routed network segments within an environment, and is created on the NSX overlay network. The Tier-1 gateway has downlink connections to segments and uplink connections to the Tier-0 gateway. You can create and configure additional Tier-1 gateways if you need them.

### Before you begin
<a name="evs-subnets"></a>

Before you create an environment, you need the following:
+ A VPC
+ A service access subnet
+ DNS and NTP settings
+ CIDR blocks for the VLAN subnets
+ A VPC Route Server instance

For the requirements, the sizes, and the settings that you can’t change after creation, see [Plan your VPC and VLAN subnets](plan-network-sizing.md). For instructions, see [Build the network foundation](network-foundation.md).

## Amazon EVS resources
<a name="evs-resources"></a>

Amazon EVS provisions the following AWS resources in the VPC that you allow Amazon EVS to access. You can see them in the AWS Management Console and the AWS CLI after they are created.
+ Amazon EVS elastic network interfaces that provide connectivity to your VCF appliances and hosts
+ Amazon EVS ESX hosts that run on Amazon EC2 bare metal instances (see [Amazon EVS host](concepts.md#concepts-evs-host))
+ Amazon EVS VLAN subnets that connect your VPC to VCF appliances (see [Amazon EVS VLAN subnet](concepts.md#concepts-evs-network))

**Important**  
Changing these resources outside of the Amazon EVS console and API can affect the availability and stability of your Amazon EVS environment.