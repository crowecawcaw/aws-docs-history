# Planning

This section covers the following topics.

###### Topics

- [Prerequisites](#prerequisites "#prerequisites")
- [Reliability](#reliability "#reliability")
- [SAP and SUSE references](#references "#references")
- [Concepts](#concepts "#concepts")
- [Automation and AWS Launch Wizard for SAP](#automation "#automation")
- [Switching architecture to simple-mount](#switching-architecture "#switching-architecture")

## Prerequisites

You must meet the following prerequisites before commencing setup.

###### Topics

- [Deployed cluster infrastructure](#cluster "#cluster")
- [Supported operating system](#supported-os "#supported-os")
- [Required access for setup](#access "#access")

### Deployed cluster infrastructure

Ensure that your AWS networking requirements and Amazon EC2 instances where SAP workloads are installed, are correctly configured for SAP. For more information, see [SAP NetWeaver Environment Setup for Linux on AWS](std-sap-netweaver-environment-setup.md "std-sap-netweaver-environment-setup.md").

See the following ASCS cluster specific requirements.

- Two cluster nodes created in private subnets in separate Availability Zones within the same Amazon VPC and AWS Region
- Access to the route table(s) that are associated with the chosen subnets

For more information, see [AWS – Overlay IP](#overlay-ip "#overlay-ip").

- Targeted Amazon EC2 instances must have connectivity to the Amazon EC2 endpoint via internet or a Amazon VPC endpoint.

### Supported operating system

Protecting ASCS with a pacemaker cluster requires packages from SUSE, including targeted cluster resource agents for SAP and AWS that may not be available in standard repositories.

For deploying SAP applications on SUSE, SAP and SUSE recommend using SUSE Linux Enterprise Server for SAP applications (SLES for SAP). SLES for SAP provides additional benefits, including Extended Service Pack Overlap Support (ESPOS), configuration and tuning packages for SAP applications, and High Availability Extensions (HAE). For more details, see SUSE website at [SUSE Linux Enterprise Server for SAP Applications](https://www.suse.com/products/sles-for-sap/ "https://www.suse.com/products/sles-for-sap/").

SLES for SAP is available at [AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace") with an hourly or annual subscription. You can also use the bring your own subscription (BYOS) model.

### Required access for setup

The following access is required for setting up the cluster.

- An IAM user with the following privileges.
  - modify Amazon VPC route tables
  - modify Amazon EC2 instance properties
  - create IAM policies and roles
  - create Amazon EFS file systems

- Root access to the operating system of both cluster nodes
- SAP administrative user access – `<sid>adm`

In case of a new install, this user is created by the install process.

## Reliability

The SAP Lens of the Well-Architected framework, in particular the Reliability pillar, can be used to understand the reliability requirements for your SAP workload.

ASCS is a single point of failure in a highly available SAP architecture. The impact of an outage of this component must be evaluated against factors, such as, recovery point objective (RPO), recovery time objective (RTO), cost and operation complexity. For more information, see [Reliability](../../../wellarchitected/latest/sap-lens/reliability.md "../../../wellarchitected/latest/sap-lens/reliability.md") in SAP Lens - AWS Well-Architected Framework.

## SAP and SUSE references

In addition to this guide, see the following references for more details.

- [SUSE documentation – SAP S/4 HANA - Enqueue Replication 2 High Availability Cluster With Simple Mount](https://documentation.suse.com/sbp/sap-15/html/SAP-S4HA10-setupguide-simplemount-sle15/index.html "https://documentation.suse.com/sbp/sap-15/html/SAP-S4HA10-setupguide-simplemount-sle15/index.html")
- [SUSE documentation – SAP S/4 HANA - Enqueue Replication 2 High Availability Cluster](https://documentation.suse.com/sbp/all/single-html/SAP-S4HA10-setupguide-sle15/#id-1 "https://documentation.suse.com/sbp/all/single-html/SAP-S4HA10-setupguide-sle15/#id-1")
- [SAP Note: 1656099 - SAP Applications on AWS: Supported DB/OS and Amazon EC2 products](https://launchpad.support.sap.com/#/notes/1656099 "https://launchpad.support.sap.com/#/notes/1656099")
- [SAP Note: 1984787 - SUSE Linux Enterprise Server 12: Installation Notes](https://launchpad.support.sap.com/#/notes/1984787 "https://launchpad.support.sap.com/#/notes/1984787")
- [SAP Note: 2578899 - SUSE Linux Enterprise Server 15: Installation Notes](https://launchpad.support.sap.com/#/notes/2578899 "https://launchpad.support.sap.com/#/notes/2578899")
- [SAP Note: 1275776 - Linux: Preparing SLES for SAP environments](https://launchpad.support.sap.com/#/notes/1275776 "https://launchpad.support.sap.com/#/notes/1275776")

You must have SAP portal access for reading all SAP Notes.

## Concepts

This section covers AWS, SAP, and SUSE concepts.

###### Topics

- [SAP – ABAP SAP Central Services (ASCS)](#ascs "#ascs")
- [SAP – Enqueue Replication Server (ERS)](#ers "#ers")
- [AWS – Availability Zones](#availability-zones "#availability-zones")
- [AWS – Overlay IP](#overlay-ip "#overlay-ip")
- [AWS – Shared VPC](#shared-vpc "#shared-vpc")
- [Pacemaker - STONITH fencing agent](#stonith "#stonith")
- [Pacemaker - simple-mount and classic architecture](#simple-classic "#simple-classic")

### SAP – ABAP SAP Central Services (ASCS)

The ABAP SAP Central Services (ASCS) is an SAP instance consisting of the following two services. It is considered a single point of failure (SPOF) in a resilient SAP system.

- **Message server** – Responsible for application load distribution (GUI and RFC), communication between application servers, and centralised configuration information for web dispatchers and application servers.
- **Enqueue server (standalone)** – Maintains a lock table in main memory (shared memory). Unlike a database lock, an enqueue lock can exist across multiple logical units of work (LUW), and is set by a SAP Dialog work process. The lock mechanism prevents two transactions from changing the same data in the database simultaneously.

###### Note

With ABAP Release 7.53 (ABAP Platform 1809), the new Standalone Enqueue Server 2 (ENSA2) is installed by default. It replaces the previous version (ENSA1) but can be configured for the previous versions. See [SAP Note 2630416 - Support for Standalone Enqueue Server 2](https://launchpad.support.sap.com/#/notes/2630416 "https://launchpad.support.sap.com/#/notes/2630416") (SAP portal access required) for more information.

This document includes modifications to align with the correct ENSA version.

### SAP – Enqueue Replication Server (ERS)

The Enqueue Replication Server (ERS) is an SAP instance containing a replica of the lock table (replication table).

In a resilient setup, if the standalone enqueue server (EN/ENQ) fails, it can be restarted either by restart parameters or by high availability software, such as Pacemaker. The enqueue server retrieves the replication table remotely or by failing over to the host where the ERS is running.

### AWS – Availability Zones

Availability Zone is one or more discreet data centers with redundant power, networking, and connectivity in an AWS Region. For more information, see [Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/").

For mission critical deployments of SAP on AWS where the goal is to minimise the recovery time objective (RTO), we suggest distributing single points of failure across Availability Zones. Compared with single instance or single Availability Zone deployments, this increases resilience and isolation against a broad range of failure scenarios and issues, including natural disasters.

Each Availability Zone is physically separated by a meaningful distance (many kilometers) from another Availability Zone. All Availability Zones in an AWS Region re interconnected with high-bandwidth, low-latency network, over fully redundant, dedicated metro fiber. This enables synchronous replication. All traffic between Availability Zones is encrypted.

### AWS – Overlay IP

Overlay IP enables a connection to the application, regardless of which Availability Zone (and subnet) contains the active primary node.

When deploying an Amazon EC2 instance in AWS, IP addresses are allocated from the CIDR range of the allocated subnet. The subnet cannot span across multiple Availability Zones, and therefore the subnet IP addresses may be unavailable after faults, including network connectivity or hardware issues which require a failover to the replication target in a different Availability Zone.

To address this, we suggest that you configure an overlay IP, and use this in the connection parameters for the application. This IP address is a non-overlapping RFC1918 private IP address from outside of VPC CIDR block and is configured as an entry in the route table or tables. The route directs the connection to the active node and is updated during a failover by the cluster software.

You can select any one of the following RFC1918 private IP addresses for your overlay IP address.

- 10.0.0.0 – 10.255.255.255 (10/8 prefix)
- 172.16.0.0 – 172.31.255.255 (172.16/12 prefix)
- 192.168.0.0 – 192.168.255.255 (192.168/16 prefix)

If, for example, you use the 10/8 prefix in your SAP VPC, selecting a 172 or a 192 IP address may help to differentiate the overlay IP. Consider the use of an IP Address Management (IPAM) tool such as Amazon VPC IP Address Manager to plan, track, and monitor IP addresses for your AWS workloads. For more information, see [What is IPAM?](../../../vpc/latest/ipam/what-it-is-ipam.md "../../../vpc/latest/ipam/what-it-is-ipam.md")

The overlay IP agent in the cluster can also be configured to update multiple route tables which contain the Overlay IP entry if your subnet association or connectivity requires it.

**Access to overlay IP**

The overlay IP is outside of the range of the VPC, and therefore cannot be reached from locations that are not associated with the route table, including on-premises and other VPCs.

Use [AWS Transit Gateway](../../../vpc/latest/tgw/what-is-transit-gateway.md "../../../vpc/latest/tgw/what-is-transit-gateway.md") as a central hub to facilitate the network connection to an overlay IP address from multiple locations, including Amazon VPCs, other AWS Regions, and on-premises using [AWS Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") or [AWS Client VPN](../../../vpn/latest/clientvpn-admin/what-is.md "../../../vpn/latest/clientvpn-admin/what-is.md").

If you do not have AWS Transit Gateway set up as a network transit hub or if it is not available in your preferred AWS Region, you can use a [Network Load Balancer](../../../elasticloadbalancing/latest/network/introduction.md "../../../elasticloadbalancing/latest/network/introduction.md") to enable network access to an overlay IP.

For more information, see [SAP on AWS High Availability with Overlay IP Address Routing](../sap-hana/sap-ha-overlay-ip.md "../sap-hana/sap-ha-overlay-ip.md").

### AWS – Shared VPC

An enterprise landing zone setup or security requirements may require the use of a separate cluster account to restrict the route table access required for the Overlay IP to an isolated account. For more information, see [Share your VPC with other accounts](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md").

Evaluate the operational impact against your security posture before setting up shared VPC. To set up, see [Shared VPC – optional](sles-netweaver-ha-settings.md#sles-netweaver-ha-shared-vpc "sles-netweaver-ha-settings.md#sles-netweaver-ha-shared-vpc").

### Pacemaker - STONITH fencing agent

In a two-node cluster setup for a primary resource and its replication pair, it is important that there is only one node in the primary role with the ability to modify your data. In the event of a failure scenario where a node is unresponsive or incommunicable, ensuring data consistency requires that the faulty node is isolated by powering it down before the cluster commences other actions, such as promoting a new primary. This arbitration is the role of the fencing agent.

Since a two-node cluster introduces the possibility of a fence race in which a dual shoot out can occur with communication failures resulting in both nodes simultaneously claiming, "I can’t see you, so I am going to power you off". The fencing agent is designed to minimise this risk by providing an external witness.

SLES supports several fencing agents, including the one recommended for use with Amazon EC2 Instances (external/ec2). This resource uses API commands to check its own instance status - "Is my instance state anything other than running?" before proceeding to power off its pair. If it is already in a stopping or stopped state it will admit defeat and leave the surviving node untouched.

### Pacemaker - simple-mount and classic architecture

This guide covers two architectures for SAP cluster solutions on SLES for SAP – simple-mount and classic (previous standard). Simple-mount was certified as the SLES for SAP Applications cluster solution in late 2021. It is now the recommended architecture for both ENSA1 and ENSA2 deployments running on SLES for SAP 15 and above. For more details, see SUSE blog [Simple Mount Structure for SAP Application Platform](https://www.suse.com/c/simple-mount-structure-for-sap-application-platform/ "https://www.suse.com/c/simple-mount-structure-for-sap-application-platform/").

If you are configuring a new SAP installation, we recommend the simple-mount architecture. If you already have the classic architecture, and wish to migrate to the simple-mount architecture, see [Switching architecture to simple-mount](#switching-architecture "#switching-architecture").

The following are the differences between the classic and simple-mount architectures.

- Removing file system resources from cluster – a file system is required but it is not mounted and unmounted by the cluster. The executable directory for the ASCS and ERS can be permanently mounted on both nodes.
- Addition of `SAPStartSrv` – `SAPStartSrv` controls the matching `SAPStartSrv` framework process.
- Sapping and sappong services – these services manage the start of `SAPStartSrv` services with sapinit.

See the [Architecture diagrams](sles-netweaver-ha-diagrams.md "sles-netweaver-ha-diagrams.md") for more details.

## Automation and AWS Launch Wizard for SAP

You can set up a cluster manually using the instructions provided here. You can also automate parts of this process to ensure consistency and repeatability.

Use AWS Launch Wizard for SAP for automated deployments of SAP NetWeaver, SAP S/4 HANA, SAP B/4HANA, and Solution Manager. Launch Wizard uses AWS CloudFormation scripts to quickly provision the resources needed to deploy SAP NetWeaver and S/4 HANA. The automation performs SAP enqueue replication and pacemaker setup so that only validation and testing are required. For more information, see [AWS Launch Wizard for SAP](../../../launchwizard/latest/userguide/launch-wizard-sap.md "../../../launchwizard/latest/userguide/launch-wizard-sap.md").

To ensure that the behavior and operation of your cluster is well understood regardless of how your system is set up, we recommend a thorough test cycle. See [Testing](testing.md "testing.md") for more details.

## Switching architecture to simple-mount

Follow along these steps if you want to switch an existing cluster with classic architecture to use the recommended configuration of simple-mount architecture.

These steps must be performed in an outage window, allowing stop/start of services and basic testing.

1. Put the cluster in maintenance mode. See [Maintenance mode](sles-operations.md#maintenance-mode "sles-operations.md#maintenance-mode").
2. Stop SAP services, including application servers connected to the cluster as well as ASCS and ERS.
3. Install any missing operating system packages. See [Package](sles-setup.md#os-packages "sles-setup.md#os-packages").

It might be necessary to install `sapstartsrv-resource-agents`. However, all operating system prerequisites must be checked and updated to ensure that versions are compatible. See [Operating system prerequisites](sles-setup.md#os-prerequisites "sles-setup.md#os-prerequisites"). 4. Add entries for ASCS and ERS mount point on both nodes (if not already added). See [Update /etc/fstab](sles-setup.md#update-file "sles-setup.md#update-file"). 5. Enable `sapping`/`sappong` services. See [Enable sapping/sappongsystemd services (simple-mount only)](sap-cluster.md#enable-services "sap-cluster.md#enable-services"). 6. Disable `systemd` services. See [Align and disable SAP auto start services for systemd](sap-cluster.md#auto-disable "sap-cluster.md#auto-disable"). 7. Backup the configuration with the following command.

```
crm config show >> /tmp/classic_ha_setup.txt
```

See [Prepare for resource creation](cluster-resources.md#resource-creation "cluster-resources.md#resource-creation"). 8. _Optional_ – delete the configuration. You can edit in place but we recommend starting with a blank configuration. This ensures that latest timeout and priority parameters are in place.

```
crm config erase
crm config show
```

9. Configure cluster resources again. See [Create cluster resources](cluster-resources.md "cluster-resources.md"). Ignore the sections pertaining to the classic architecture.
10. Check the cluster and perform some tests. See [Testing](testing.md "testing.md").
11. Resume standard operations by starting any additional services, including application servers.
