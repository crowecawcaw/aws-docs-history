# Concepts and components of Amazon EVS

This section explains some key Amazon EVS concepts and components.

## Amazon EVS environment

An Amazon EVS _environment_ is a logical container for VMware Cloud Foundation (VCF) resources, such as vSphere hosts, vSAN, NSX, and SDDC Manager.
An environment contains a consolidated VCF domain with a vSphere cluster that hosts the components for managing, monitoring, and instantiating the VCF software stack.
Each environment directly maps to an SDDC Manager appliance.
For more information, see [Amazon EVS architecture](architecture.md "architecture.md").

## Amazon EVS host

An Amazon EVS _host_ is a VMware ESX host that runs on Amazon EC2 bare metal instances.
Amazon EVS hosts use local NVMe instance store volumes for vSAN datastores, which store your management and workload virtual machines.

###### Warning

Instance store volumes are ephemeral. Data stored on these volumes do not persist if the underlying EC2 instance is stopped or terminated. Stopping or terminating Amazon EC2 instances used by Amazon EVS without decomissioning within VCF can result in data loss.

For more information about host maintenance, see [Amazon EVS host maintenance](evs-host-maintenance.md "evs-host-maintenance.md").

## Service access subnet

The _service access subnet_ is a standard VPC subnet that allows Amazon EVS to access the VCF deployment.
During Amazon EVS environment creation, you specify the VPC and subnet for Amazon EVS to use for service access.

When you create an Amazon EVS environment, Amazon EVS provisions elastic network interfaces into the service access subnet to facilitate management connectivity to VCF appliances and ESX hosts.
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

The _VTEP VLAN subnet_ uses VMware NSX virtual tunnel endpoints (VTEP) to encapsulate and decapsulate overlay network traffic for the Amazon EVS ESX hosts.

### Edge VTEP VLAN subnet

The _Edge VTEP VLAN subnet_ is a specialized VTEP VLAN subnet that is dedicated for NSX Edge appliance overlay traffic.
This VLAN is used for overlay communication between NSX edges and ESX hosts.

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

## Connector

An Amazon EVS connector enables Amazon EVS to communicate with a VMware Cloud Foundation management appliance in your environment. Each connector maps to a single management appliance, using the fully qualified domain name (FQDN) and credentials that you store in an AWS Secrets Manager secret to authenticate with the appliance.

Amazon EVS supports the following connector types:

- **Operations Manager** (`OPERATIONS_MANAGER`) – The management connector for VCF 9.x. Amazon EVS uses it to connect to and stay in sync with your VMware deployment.
- **SDDC Manager** (`SDDC_MANAGER`) – The management connector for VCF 5.2.x. Amazon EVS uses it to validate host counts and license-key coverage.
- **vCenter** (`VCENTER`) – Used to monitor VM lifecycle events, such as for Windows Server license entitlements. For more information, see [Windows Server License Entitlement for Amazon EVS](#concepts-windows-server-license-entitlement "#concepts-windows-server-license-entitlement").

Amazon EVS periodically performs reachability checks against each appliance through its connector. If a required management connector is not created, or loses reachability, Amazon EVS cannot validate your environment’s license and entitlement coverage, and reports impaired environment health through AWS Health notifications. If the vCenter connector loses reachability, Windows Server entitlements enter an at-risk state, and are dropped if reachability is not restored within the grace period.

- To create a connector, see [Create an Amazon EVS environment connector](evs-env-create-connector.md "evs-env-create-connector.md").
- To update a connector, see [Update an Amazon EVS environment connector](evs-env-update-connector.md "evs-env-update-connector.md").
- To delete a connector, see [Delete an Amazon EVS environment connector](evs-env-delete-connector.md "evs-env-delete-connector.md").

## Windows Server License Entitlement for Amazon EVS

Windows Server license entitlement for Amazon EVS enables virtual machines (VMs) running in your Amazon EVS environment to utilize AWS-offered Windows Server licenses. Windows Server license entitlements are offered per vCPU per hour with a pay-as-you-go model.

To use Windows Server License entitlements, you must first create a connector to establish reachability between Amazon EVS and your vCenter Server appliance. The reachability check on the connector must be passing before you can create an entitlement.

Amazon EVS uses the vCenter connector to monitor VM lifecycle events for entitled VMs. If the connector loses reachability, associated entitlements enter an at risk state. If reachability is not restored within an 8-hour grace period, entitlements are dropped and license usage tracking is stopped from the time the entitlement entered the at risk state.

After you have created an entitlement, and powered on a VM, Amazon EVS starts monitoring the corresponding VM’s Windows Server license usage. If the VM is shutdown or the configured vCPU are scaled up or down based on demand, you only pay for the licensing for the total vCPU hours used.

###### Warning

Supported guest operating systems are Windows Server 2016 and later.

For instructions, see [Create an Amazon EVS environment connector](evs-env-create-connector.md "evs-env-create-connector.md") and [Create an Amazon EVS entitlement](evs-env-create-entitlement.md "evs-env-create-entitlement.md").

After creating entitlements, you can configure each Windows Server VM to activate through a VPC Endpoint. For instructions, see [Configure Windows Server Activation](evs-activate-windows-server.md "evs-activate-windows-server.md").

## VMware Hybrid Cloud Extension (HCX)

VMware Hybrid Cloud Extension (VMware HCX) is an application mobility platform designed for simplifying application migration, rebalancing workloads, and optimizing disaster recovery across data centers and clouds.
You can use HCX to migrate your VMware-based workloads to Amazon EVS.

You can configure connectivity for VMware HCX using Direct Connect with an associated transit gateway, or using an AWS Site-to-Site VPN attachment to a transit gateway.
For more information, see [Migrate workloads to Amazon EVS using VMware HCX](migrate-evs-hcx.md "migrate-evs-hcx.md").
