

# Concepts and components of Amazon EVS

Learn the Amazon Elastic VMware Service resources and VMware components before you plan an environment.

## Amazon EVS environment
<a name="concepts-evs-virt-env"></a>

An Amazon EVS *environment* is a logical container for VMware Cloud Foundation (VCF) resources, such as ESX hosts, VMware vSAN, VMware NSX, and VMware vCenter Server. When you create an environment, Amazon EVS creates the VLAN subnets in your VPC that VCF uses. Each Amazon EVS environment contains its own dedicated set of VLAN subnets. You then add hosts and connect the environment to your VCF management appliance with connectors.

In EVS-deployed environments (VCF 5.2.x), the environment contains a consolidated VCF domain, and each environment maps directly to an SDDC Manager appliance. For how the two deployment modes differ, see [Differences between deployment modes](deployment-mode-differences.md). For the components and how they connect, see [Amazon EVS architecture](architecture.md).

## Amazon EVS host
<a name="concepts-evs-host"></a>

An Amazon EVS *host* is a VMware ESX host that runs on an Amazon EC2 bare metal instance. Hosts with local storage use their local NVMe instance store volumes for vSAN datastores, which store your management and workload virtual machines. Diskless hosts, which need VCF 9.x, have no instance store and use external storage instead. For the storage choices, see [Choose storage](plan-storage.md).

**Warning**  
Instance store volumes are ephemeral. Data on these volumes doesn’t persist if you stop or terminate the underlying Amazon EC2 instance. If you stop or terminate an Amazon EC2 instance that Amazon EVS uses before you decommission its host in VCF, you can lose data.  
For more information about host maintenance, see [Host maintenance and retirement events](evs-host-maintenance.md).

## Service access subnet
<a name="concepts-service-access-subnet"></a>

The *service access subnet* is a standard VPC subnet that allows Amazon EVS to access the VCF deployment. When you create an Amazon EVS environment, you specify the VPC and the subnet for Amazon EVS to use for service access.

Amazon EVS provisions elastic network interfaces into the service access subnet to provide management connectivity to VCF appliances and ESX hosts. Amazon EVS needs this connectivity to deploy, manage, and monitor the VCF deployment.

## Amazon EVS VLAN subnet
<a name="concepts-evs-network"></a>

An *Amazon EVS VLAN subnet* is an Amazon VPC subnet that Amazon EVS manages. VLAN subnets provide VPC connectivity for Amazon EVS hosts and for VCF appliances such as NSX, VMware HCX, and vCenter Server. Each VLAN subnet has a VLAN tag, so that VLAN network traffic is segmented logically.

Amazon EVS creates all of the VLAN subnets that the service uses when you create the environment. You provide the CIDR blocks that the VLAN subnets use. Each CIDR block must be between a `/28` and a `/24` netmask. It must be inside a CIDR block that’s associated with the VPC, and it must not overlap with any other subnet in the VPC, including the other VLAN subnets.

Separate VLAN subnets carry host management, vMotion, vSAN, NSX overlay, NSX Edge, management appliance, HCX uplink, and NSX uplink traffic. Expansion VLAN subnets support other VCF functions, such as NSX Federation. For the list of VLAN subnet types, their VLAN IDs, and their IP address rules, see [VLAN subnets, VLAN IDs, and IP addresses](vlan-subnet-reference.md).

You can’t add VLAN subnets or change their CIDR blocks after you create the environment. Size the VLAN subnet CIDR blocks for the number of hosts that you plan to run, including future growth, before you create the environment. For sizing guidance, see [Plan your VPC and VLAN subnets](plan-network-sizing.md).

When Amazon EVS creates the VLAN subnets, it associates them with the main route table of your VPC. After deployment, you must explicitly associate each VLAN subnet with a route table. We recommend a custom route table. For the steps, see [Associate VLAN subnets with a route table](evs-env-config-custom-rt.md). For more information, see [Associate VLAN subnets with a route table](evs-env-config-custom-rt.md).

**Important**  
 Amazon EC2 security group rules are not enforced on Amazon EVS elastic network interfaces that are attached to VLAN subnets. To control traffic to and from VLAN subnets, you must use a network access control list. For more information, see [Create a network ACL for VLAN subnet traffic](evs-env-nacl-cong.md).

## VMware NSX
<a name="concepts-nsx"></a>

NSX is a software-defined networking platform that provides network virtualization. Amazon EVS environments use NSX to create and manage the overlay network where VCF appliances and workloads run. NSX Edge nodes connect the overlay network to your VPC through the NSX uplink VLAN subnet and Amazon VPC Route Server.

Who configures the NSX Edge cluster and NSX routing depends on the deployment mode. For the comparison, see [Differences between deployment modes](deployment-mode-differences.md).

For more information about common NSX concepts, see [Key Concepts](https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/installation-guide/overview-of-nsx/key-concepts-nsxt.html) in the *VMware NSX Installation Guide* in the Broadcom documentation.

## Amazon EVS connectors
<a name="concepts-connector"></a>

An Amazon EVS *connector* lets Amazon EVS communicate with one VCF management appliance in your environment. Each connector uses the fully qualified domain name (FQDN) of the appliance and credentials that you store in an AWS Secrets Manager secret. Amazon EVS uses the management connector to stay in sync with your VCF deployment and to monitor vSAN capacity. It uses the optional vCenter connector to monitor virtual machines for Windows Server entitlements. For more information about the vSAN capacity notification, see [vSAN capacity warning received in AWS Health](troubleshoot-hosts.md#troubleshoot-vsan-capacity).

The management connector type depends on the deployment mode. Self-deployed environments use a VCF Operations connector (`OPERATIONS_MANAGER`). EVS-deployed environments use an SDDC Manager connector (`SDDC_MANAGER`). For connector types, reachability checks, and procedures, see [Manage connectors and credentials](connectors-overview.md).

## Windows Server license entitlement
<a name="concepts-windows-server-license-entitlement"></a>

A *Windows Server license entitlement* lets virtual machines in your Amazon EVS environment use AWS-provided Windows Server licenses. An entitlement depends on a vCenter connector. For requirements and procedures, see [Windows Server entitlements](entitlements.md).

## VMware HCX
<a name="concepts-hcx"></a>

VMware Hybrid Cloud Extension (HCX) is an application mobility platform for application migration, workload rebalancing, and disaster recovery across data centers and clouds. You can use HCX to migrate your VMware-based workloads to Amazon EVS. To choose how HCX connects to your on-premises site, see [Plan HCX connectivity](plan-hcx-connectivity.md). To migrate workloads, see [Migrate workloads with HCX](migrate-evs-hcx.md).