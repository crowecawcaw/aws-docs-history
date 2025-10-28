# Planning

This section covers the following topics.

###### Topics

- [Prerequisites](#prerequisites "#prerequisites")
- [Reliability](#reliability "#reliability")
- [SAP and SUSE references](#references "#references")
- [Concepts](#concepts "#concepts")

## Prerequisites

You must meet the following prerequisites before commencing setup.

###### Topics

- [Deployed cluster infrastructure](#cluster "#cluster")
- [Supported operating system](#supported-os "#supported-os")
- [Required access for setup](#access "#access")

### Deployed cluster infrastructure

Ensure that your AWS networking requirements and Amazon EC2 instances where SAP workloads are installed, are correctly configured for SAP. For more information, see [SAP NetWeaver Environment Setup for Linux on AWS](../sap-netweaver/std-sap-netweaver-environment-setup.md "../sap-netweaver/std-sap-netweaver-environment-setup.md").

See the following SAP ASE pacemaker cluster specific requirements.

- Two cluster nodes created in private subnets in separate Availability Zones within the same Amazon VPC and AWS Region
- Access to the route table(s) that are associated with the chosen subnets

For more information, see [Overlay IP](#overlay-ip "#overlay-ip").

- Targeted Amazon EC2 instances must have connectivity to the Amazon EC2 endpoint via internet or a Amazon VPC endpoint.

### Supported operating system

Protecting SAP ASE database with a pacemaker cluster requires packages from SUSE, including targeted cluster resource agents for SAP and AWS that may not be available in standard repositories.

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
- SAP administrative user access – `<syb>adm`

In case of a new install, this user is created by the install process.

## Reliability

The SAP Lens of the Well-Architected framework, in particular the Reliability pillar, can be used to understand the reliability requirements for your SAP workload.

SAP ASE is a single point of failure in a highly available SAP architecture. The impact of an outage of this component must be evaluated against factors, such as, recovery point objective (RPO), recovery time objective (RTO), cost and operation complexity. For more information, see [Reliability](../../../wellarchitected/latest/sap-lens/reliability.md "../../../wellarchitected/latest/sap-lens/reliability.md") in SAP Lens - AWS Well-Architected Framework.

## SAP and SUSE references

In addition to this guide, see the following references for more details.

- [SAP Note: 1650511 - SYB: High Availability Offerings with SAP Adaptive Server Enterprise](https://me.sap.com/notes/1650511/E "https://me.sap.com/notes/1650511/E")
- [SAP Note: 1656099 - SAP Applications on AWS: Supported DB/OS and Amazon EC2 products](https://launchpad.support.sap.com/#/notes/1656099 "https://launchpad.support.sap.com/#/notes/1656099")
- [SAP Note: 1984787 - SUSE Linux Enterprise Server 12: Installation Notes](https://launchpad.support.sap.com/#/notes/1984787 "https://launchpad.support.sap.com/#/notes/1984787")
- [SAP Note: 2578899 - SUSE Linux Enterprise Server 15: Installation Notes](https://launchpad.support.sap.com/#/notes/2578899 "https://launchpad.support.sap.com/#/notes/2578899")
- [SAP Note: 1275776 - Linux: Preparing SLES for SAP environments](https://launchpad.support.sap.com/#/notes/1275776 "https://launchpad.support.sap.com/#/notes/1275776")

You must have SAP portal access for reading all SAP Notes.

## Concepts

This section covers AWS concepts.

###### Topics

- [Availability Zones](#availability-zones "#availability-zones")
- [Overlay IP](#overlay-ip "#overlay-ip")
- [Shared VPC](#shared-vpc "#shared-vpc")
- [Amazon FSx for NetApp ONTAP](#fsx-ontap "#fsx-ontap")
- [Pacemaker - STONITH fencing agent](#stonith "#stonith")

### Availability Zones

Availability Zone is one or more discreet data centers with redundant power, networking, and connectivity in an AWS Region. For more information, see [Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/").

For mission critical deployments of SAP on AWS where the goal is to minimise the recovery time objective (RTO), we suggest distributing single points of failure across Availability Zones. Compared with single instance or single Availability Zone deployments, this increases resilience and isolation against a broad range of failure scenarios and issues, including natural disasters.

Each Availability Zone is physically separated by a meaningful distance (many kilometers) from another Availability Zone. All Availability Zones in an AWS Region re interconnected with high-bandwidth, low-latency network, over fully redundant, dedicated metro fiber. This enables synchronous replication. All traffic between Availability Zones is encrypted.

### Overlay IP

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

### Shared VPC

An enterprise landing zone setup or security requirements may require the use of a separate cluster account to restrict the route table access required for the Overlay IP to an isolated account. For more information, see [Share your VPC with other accounts](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md").

Evaluate the operational impact against your security posture before setting up shared VPC. To set up, see [Shared VPC – optional](../sap-netweaver/sles-netweaver-ha-settings.md#sles-netweaver-ha-shared-vpc "../sap-netweaver/sles-netweaver-ha-settings.md#sles-netweaver-ha-shared-vpc").

### Amazon FSx for NetApp ONTAP

Amazon FSx for NetApp ONTAP is a fully managed service that provides highly reliable, scalable, high-performing, and feature-rich file storage built on NetApp’s popular ONTAP file system. FSx for ONTAP combines the familiar features, performance, capabilities, and API operations of NetApp file systems with the agility, scalability, and simplicity of a fully managed AWS service.

FSx for ONTAP also provides highly available and durable storage with fully managed backups and support for cross-Region disaster recovery. To make it easier to protect and secure your data, FSx for ONTAP supports popular data security and anti-virus applications. For more information, see [What is Amazon FSx for NetApp ONTAP?](../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md "../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md")

### Pacemaker - STONITH fencing agent

In a two-node cluster setup for a primary resource and its replication pair, it is important that there is only one node in the primary role with the ability to modify your data. In the event of a failure scenario where a node is unresponsive or incommunicable, ensuring data consistency requires that the faulty node is isolated by powering it down before the cluster commences other actions, such as promoting a new primary. This arbitration is the role of the fencing agent.

Since a two-node cluster introduces the possibility of a fence race in which a dual shoot out can occur with communication failures resulting in both nodes simultaneously claiming, "I can’t see you, so I am going to power you off". The fencing agent is designed to minimise this risk by providing an external witness.

SLES supports several fencing agents, including the one recommended for use with Amazon EC2 Instances (external/ec2). This resource uses API commands to check its own instance status - "Is my instance state anything other than running?" before proceeding to power off its pair. If it is already in a stopping or stopped state it will admit defeat and leave the surviving node untouched.
