# Planning

This section covers the following topics.

###### Topics

- [Prerequisites](#prerequisites "#prerequisites")
- [Reliability](#reliability "#reliability")
- [SAP and Red Hat references](#references "#references")
- [Concepts](#concepts "#concepts")

## Prerequisites

You must meet the following prerequisites before commencing setup.

###### Topics

- [Deployed cluster infrastructure](#cluster "#cluster")
- [Supported operating system](#supported-os "#supported-os")
- [Required access for setup](#access "#access")

### Deployed cluster infrastructure

Ensure that your AWS networking requirements and Amazon EC2 instances where SAP workloads are installed, are correctly configured for SAP. For more information, see [SAP NetWeaver Environment Setup for Linux on AWS](../sap-netweaver/std-sap-netweaver-environment-setup.md "../sap-netweaver/std-sap-netweaver-environment-setup.md").

See the following SAP ASE cluster specific requirements.

- Two cluster nodes created in private subnets in separate Availability Zones within the same Amazon VPC and AWS Region
- Access to the route table(s) that are associated with the chosen subnets

For more information, see [AWS – Overlay IP](#overlay-ip-rhel "#overlay-ip-rhel").

- Targeted Amazon EC2 instances must have connectivity to the Amazon EC2 endpoint via internet or a Amazon VPC endpoint.

### Supported operating system

Protecting SAP ASE database with a pacemaker cluster requires packages from Red Hat, including targeted cluster resource agents for SAP and AWS that may not be available in standard repositories.

SAP and Red Hat recommend the use of Red Hat Enterprise Linux for SAP. Starting with Red Hat Enterprise Linux 8 (RHEL 8), either RHEL for SAP Solutions or RHEL for SAP Applications are required for running SAP applications in production environments. See [SAP Note 1656099 - SAP Applications on AWS: Supported DB/OS and Amazon EC2 products](https://launchpad.support.sap.com/#/notes/1656099 "https://launchpad.support.sap.com/#/notes/1656099") (requires SAP portal access).

Built on the Red Hat Enterprise Linux operating system, Red Hat Enterprise Linux for SAP expands existing capabilities, lso you can get the most out of SAP’s powerful analytics and data management portfolio. See [Red Hat Enterprise Solutions for SAP](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux/sap "https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux/sap") product page from Red Hat.

Red Hat Enterprise Linux High Availability (HA) provides all the necessary packages for configuring pacemaker-based clusters. Extended Update Support (E4S) provides support on specific minor releases for 4 years from general availability.

Red Hat Enterprise Linux for SAP with HA and US is available on [AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace") under an hourly or an annual subscription model or can be accessed using a BYOS subscription model.

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

SAP ASE database is a single point of failure in a highly available SAP architecture. We recommend evaluating the impact of design decisions on cost, operation, and reliability. For more information, see [Reliability](../../../wellarchitected/latest/sap-lens/reliability.md "../../../wellarchitected/latest/sap-lens/reliability.md") in SAP Lens - AWS Well-Architected Framework.

## SAP and Red Hat references

In addition to this guide, see the following references for more details.

- Red Hat: [Is there a High Availability resource agent for SAP (Sybase) ASE database, and how can I configure it in a Red Hat Enterprise Linux HA Cluster?](https://access.redhat.com/solutions/2969211 "https://access.redhat.com/solutions/2969211")
- Red Hat: [Red Hat Enterprise Linux for SAP offerings on Amazon Web Services FAQ](https://access.redhat.com/solutions/2969211 "https://access.redhat.com/solutions/2969211")
- [SAP Note: 1656099 - SAP Applications on AWS: Supported DB/OS and Amazon EC2 products](https://launchpad.support.sap.com/#/notes/1656099 "https://launchpad.support.sap.com/#/notes/1656099")
- [SAP Note: 1618572 - Linux: Support Statement for RHEL on Amazon Web Services](https://launchpad.support.sap.com/#/notes/1618572 "https://launchpad.support.sap.com/#/notes/1618572")
- [SAP Note: 2002167 - Red Hat Enterprise Linux 7.x: Installation and Upgrade](https://launchpad.support.sap.com/#/notes/2002167 "https://launchpad.support.sap.com/#/notes/2002167")
- [SAP Note: 2772999 - Red Hat Enterprise Linux 8.x: Installation and Upgrade](https://launchpad.support.sap.com/#/notes/2772999 "https://launchpad.support.sap.com/#/notes/2772999")

You must have SAP portal access for reading all SAP Notes.

## Concepts

This section covers AWS, SAP, and Red Hat concepts.

###### Topics

- [AWS – Availability Zones](#availability-zones "#availability-zones")
- [AWS – Overlay IP](#overlay-ip-rhel "#overlay-ip-rhel")
- [AWS – Shared VPC](#rhel-ase-shared-vpc "#rhel-ase-shared-vpc")
- [Amazon FSx for NetApp ONTAP](#fsx-ontap "#fsx-ontap")
- [Pacemaker - STONITH fencing agent](#stonith "#stonith")

### AWS – Availability Zones

Availability Zone is one or more data centers with redundant power, networking, and connectivity in an AWS Region. For more information, see [Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/").

For mission critical deployments of SAP on AWS where the goal is to minimise the recovery time objective (RTO), we suggest distributing single points of failure across Availability Zones. Compared with single instance or single Availability Zone deployments, this increases resilience and isolation against a broad range of failure scenarios and issues, including natural disasters.

Each Availability Zone is physically separated by a meaningful distance (many kilometers) from another Availability Zone. All Availability Zones in an AWS Region re interconnected with high-bandwidth, low-latency network, over fully redundant, dedicated metro fiber. This enables synchronous replication. All traffic between Availability Zones is encrypted.

### AWS – Overlay IP

Overlay IP enables a connection to the application, regardless of which Availability Zone (and subnet) contains the active primary node.

When deploying instances in AWS, it is necessary to allocate an IP from a pre-existing subnet. Subnets have a classless inter-domain routing (CIDR) IP assignment from the VPC which resides entirely within one Availability Zone. This CIDR IP assignment cannot span multiple Availability Zones or be reassigned to an instance in a different Availability Zone after faults, including network connectivity or hardware issues which require a failover to the replication target.

To address this, we suggest that you configure an overlay IP, and use this in the connection parameters for the application. This IP address is a non-overlapping RFC1918 private IP address from outside of VPC CIDR block and is configured as an entry in the route table or tables. The route directs the connection to the active node and is updated during a failover by the cluster software.

You can select any one of the following RFC1918 private IP addresses for your overlay IP address.

- 10.0.0.0 – 10.255.255.255 (10/8 prefix)
- 172.16.0.0 – 172.31.255.255 (172.16/12 prefix)
- 192.168.0.0 – 192.168.255.255 (192.168/16 prefix)

If you use the 10/8 prefix in your SAP VPC, selecting a 172 or a 192 IP address may help to differentiate the overlay IP. Consider the use of an IP Address Management (IPAM) tool such as Amazon VPC IP Address Manager to plan, track, and monitor IP addresses for your AWS workloads. For more information, see [What is IPAM?](../../../vpc/latest/ipam/what-it-is-ipam.md "../../../vpc/latest/ipam/what-it-is-ipam.md")

The overlay IP agent in the cluster can also be configured to update multiple route tables which contain the Overlay IP entry if your subnet association or connectivity requires it.

**Access to overlay IP**

The overlay IP is outside of the range of the VPC, and therefore cannot be reached from locations that are not associated with the route table, including on-premises and other VPCs.

Use [AWS Transit Gateway](../../../vpc/latest/tgw/what-is-transit-gateway.md "../../../vpc/latest/tgw/what-is-transit-gateway.md") as a central hub to facilitate the network connection to an overlay IP address from multiple locations, including Amazon VPCs, other AWS Regions, and on-premises using [AWS Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") or [AWS Client VPN](../../../vpn/latest/clientvpn-admin/what-is.md "../../../vpn/latest/clientvpn-admin/what-is.md").

If you do not have AWS Transit Gateway set up as a network transit hub or if it is not available in your preferred AWS Region, you can use a [Network Load Balancer](../../../elasticloadbalancing/latest/network/introduction.md "../../../elasticloadbalancing/latest/network/introduction.md") to enable network access to an overlay IP.

For more information, see [SAP on AWS High Availability with Overlay IP Address Routing](../sap-hana/sap-ha-overlay-ip.md "../sap-hana/sap-ha-overlay-ip.md").

### AWS – Shared VPC

An enterprise landing zone setup or security requirements may require the use of a separate cluster account to restrict the route table access required for the Overlay IP to an isolated account. For more information, see [Share your VPC with other accounts](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md").

Evaluate the operational impact against your security posture before setting up shared VPC. To set up, see [Shared VPC – optional](../sap-netweaver/rhel-netweaver-ha-settings.md#rhel-ase-ha-shared-vpc "../sap-netweaver/rhel-netweaver-ha-settings.md#rhel-ase-ha-shared-vpc").

### Amazon FSx for NetApp ONTAP

Amazon FSx for NetApp ONTAP is a fully managed service that provides highly reliable, scalable, high-performing, and feature-rich file storage built on NetApp’s popular ONTAP file system. FSx for ONTAP combines the familiar features, performance, capabilities, and API operations of NetApp file systems with the agility, scalability, and simplicity of a fully managed AWS service.

FSx for ONTAP also provides highly available and durable storage with fully managed backups and support for cross-Region disaster recovery. To make it easier to protect and secure your data, FSx for ONTAP supports popular data security and anti-virus applications. For more information, see [What is Amazon FSx for NetApp ONTAP?](../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md "../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md")

### Pacemaker - STONITH fencing agent

In a two-node cluster setup for a primary resource and its replication pair, it is important that there is only one node in the primary role with the ability to modify your data. In the event of a failure scenario where a node is unresponsive or incommunicable, ensuring data consistency that can require you to isolate the faulty node by powering it down before the cluster commences other actions, such as promoting a new primary. This arbitration is the role of the fencing agent.

Since a two-node cluster introduces the possibility of a fence race in which a dual shoot out can occur with communication failures resulting in both nodes simultaneously claiming, "I can’t see you, so I am going to power you off". The fencing agent is designed to minimise this risk by providing an external witness.

Red Hat supports several fencing agents, including the one recommended for use with Amazon EC2 Instances (`fence_aws` ). This resource uses API commands to check its own instance status - "Is my instance state anything other than running?" before proceeding to power off its pair. If it is already in a stopping or stopped state it will admit defeat and leave the surviving node untouched.
