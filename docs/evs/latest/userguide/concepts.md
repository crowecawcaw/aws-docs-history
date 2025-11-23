# Concepts and components of Amazon EVS

This section explains some key Amazon EVS concepts and components.

## Amazon EVS environment

An Amazon EVS _environment_ is a logical container for VMware Cloud Foundation (VCF) resources, such as vSphere hosts, vSAN, NSX, and SDDC Manager.
An environment contains a consolidated VCF domain with a vSphere cluster that hosts the components for managing, monitoring, and instantiating the VCF software stack.
Each environment directly maps to an SDDC Manager appliance.
For more information, see [Amazon EVS architecture](architecture.md "architecture.md").

## Amazon EVS host

An Amazon EVS _host_ is a VMware ESXi host that runs on Amazon EC2 bare metal instances.

## Service access subnet

The _service access subnet_ is a standard VPC subnet that allows Amazon EVS to access the VCF deployment.
During Amazon EVS environment creation, you specify the VPC and subnet for Amazon EVS to use for service access.

When you create an Amazon EVS environment, Amazon EVS provisions elastic network interfaces into the service access subnet to facilitate management connectivity to VCF appliances and ESXi hosts.
This connectivity is required for Amazon EVS to be able to deploy, manage, and monitor the VCF deployment.

## Amazon EVS VLAN subnet

An _Amazon EVS VLAN subnet_ is an Amazon VPC subnet that is managed by Amazon EVS.
VLAN subnets provide VPC connectivity for Amazon EVS hosts, and VCF appliances such as VMware NSX, VMware HCX, and VMware vCenter Server.
Each VLAN subnet has a VLAN tag to allow VLAN network traffic to be segmented logically.

Amazon EVS creates all of the VLAN subnets that the service uses when the Amazon EVS environment is created.
You provide the CIDR block inputs that the VLAN subnets use.
You should ensure that your VLAN subnet CIDR blocks are properly sized according to the number of hosts that will be configured, taking into account future scaling needs.
CIDR blocks must have a minimum size of /28 netmask and a maximum size of /24 netmask.
CIDR blocks must not overlap with any existing CIDR block that’s associated with the VPC.

On creation, VLAN subnets are implicitly associated your VPC’s main route table.
Post-deployment you can explicitly associate VLAN subnets with a custom route table.
For more information, see [Amazon EVS networking considerations](architecture.md#evs-subnets "architecture.md#evs-subnets").

###### Important

Amazon EVS VLAN subnets can only be created during Amazon EVS environment creation, and cannot be modified after the environment is created.
You must ensure that the VLAN subnet CIDR blocks are properly sized before creating the environment.
You will not be able to add VLAN subnets after the environment is deployed.

###### Important

EC2 security group rules are not enforced on Amazon EVS elastic network interfaces that are attached to VLAN subnets.
To control traffic to and from VLAN subnets, you must use a network access control list.

### Host management VLAN subnet

The _host management VLAN subnet_ separates management traffic from user traffic, and allows for remote management of hosts.
The EVS host management vmkernel network interface connects to this subnet.

### vMotion VLAN subnet

The _vMotion VLAN subnet_ logically segments VMware vMotion traffic, and is used during a vMotion process to move virtual machines between hosts.

### vSAN VLAN subnet

The _vSAN VLAN subnet_ is used by VMware vSAN to separate traffic related to vSAN’s storage operations from other network traffic.

### VTEP VLAN subnet

The _VTEP VLAN subnet_ uses VMware NSX virtual tunnel endpoints (VTEP) to encapsulate and decapsulate overlay network traffic for the Amazon EVS ESXi hosts.

### Edge VTEP VLAN subnet

The _Edge VTEP VLAN subnet_ is a specialized VTEP VLAN subnet that is dedicated for NSX Edge appliance overlay traffic.
This VLAN is used for overlay communication between NSX edges and ESXi hosts.

### Management VM VLAN subnet

The _Management VM VLAN subnet_ is used for managing virtual appliances, including NSX Manager, vCenter Server, and SDDC Manager.

### HCX uplink VLAN subnet

The _HCX uplink VLAN subnet_ is used for communication between the HCX Interconnect (HCX-IX) and HCX Network Extension (HCX-NE) appliances, and enables the creation of the HCX service mesh uplink.

### NSX uplink VLAN subnet

The _NSX uplink VLAN subnet_ is used for connecting your NSX overlay networks to the rest of your VPC and any other external networks that you configure.
The NSX uplink VLAN subnet is configured on the NSX Edge node uplinks.

### Expansion VLAN subnet

The _expansion VLAN subnet_ can be used to enable additional VCF-supported functions, such as NSX Federation.
Amazon EVS creates two expansion VLAN subnets during environment creation.

## VMware NSX

VMware NSX is a software-defined networking (SDN) platform that enables network virtualization.
Amazon EVS uses VMware NSX to create and manage the overlay network where VMware Cloud Foundation (VCF) appliances and workloads run.
Amazon EVS deploys a pair of Active/Standby NSX Edge nodes, along with an NSX overlay network.
Amazon EVS automatically configures all of the NSX routing and uplinks on your behalf as part of deployment.
For more information about common NSX concepts, see [Key Concepts](https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/installation-guide/overview-of-nsx/key-concepts-nsxt.html "https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/installation-guide/overview-of-nsx/key-concepts-nsxt.html") in the _VMware NSX Installation Guide_.

## VMware Hybrid Cloud Extension (HCX)

VMware Hybrid Cloud Extension (VMware HCX) is an application mobility platform designed for simplifying application migration, rebalancing workloads, and optimizing disaster recovery across data centers and clouds.
You can use HCX to migrate your VMware-based workloads to Amazon EVS.

You can configure connectivity for VMware HCX using Direct Connect with an associated transit gateway, or using an AWS Site-to-Site VPN attachment to a transit gateway.
For more information, see [Migrate workloads to Amazon EVS using VMware HCX](migrate-evs-hcx.md "migrate-evs-hcx.md").
