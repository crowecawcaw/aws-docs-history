

# Concepts
<a name="sap-nw-pacemaker-rhel-concepts"></a>

This section covers AWS, SAP, and Red Hat concepts.

**Topics**
+ [SAP – ABAP SAP Central Services (ASCS)](#ascs-nw-rhel)
+ [SAP – Enqueue Replication Server (ERS)](#ers-nw-rhel)
+ [AWS – Availability Zones](#availability-zones-nw-rhel)
+ [AWS – Overlay IP](#overlay-ip-nw-rhel)
+ [AWS – Shared VPC](#shared-vpc)
+ [Pacemaker - STONITH fencing agent](#stonith-nw-rhel)

## SAP – ABAP SAP Central Services (ASCS)
<a name="ascs-nw-rhel"></a>

The ABAP SAP Central Services (ASCS) is an SAP instance consisting of the following two services. It is considered a single point of failure (SPOF) in a resilient SAP architecture.
+  **Message server** – Responsible for application load distribution (GUI and RFC), communication between application servers, and centralised configuration information for web dispatchers and application servers.
+  **Enqueue server (standalone)** – Maintains a lock table in main memory (shared memory). Unlike a database lock, an enqueue lock can exist across multiple logical units of work (LUW), and is set by a SAP Dialog work process. The lock mechanism prevents two transactions from changing the same data in the database simultaneously.

**Note**  
With ABAP Release 7.53 (ABAP Platform 1809), the new Standalone Enqueue Server 2 (ENSA2) is installed by default. It replaces the previous version (ENSA1) but can be configured for the previous versions. See [SAP Note 2630416 - Support for Standalone Enqueue Server 2](https://me.sap.com/notes/2630416) (SAP portal access required) for more information.  
This document includes modifications to align with the correct ENSA version.

## SAP – Enqueue Replication Server (ERS)
<a name="ers-nw-rhel"></a>

The Enqueue Replication Server (ERS) is an SAP instance containing a replica of the lock table (replication table).

In a resilient setup, if the standalone enqueue server (EN/ENQ) fails, it can be restarted either by restart parameters or by high availability software, such as Pacemaker. The enqueue server retrieves the replication table remotely or by failing over to the host where the ERS is running.

## AWS – Availability Zones
<a name="availability-zones-nw-rhel"></a>

Availability Zone is one or more discreet data centers with redundant power, networking, and connectivity in an AWS Region. For more information, see [Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/).

For mission critical deployments of SAP on AWS where the goal is to minimise the recovery time objective (RTO), we suggest distributing single points of failure across Availability Zones. Compared with single instance or single Availability Zone deployments, this increases resilience and isolation against a broad range of failure scenarios and issues, including natural disasters.

Each Availability Zone is physically separated by a meaningful distance (many kilometers) from another Availability Zone. All Availability Zones in an AWS Region are interconnected with high-bandwidth, low-latency network, over fully redundant, dedicated metro fiber. This enables synchronous replication. All traffic between Availability Zones is encrypted.

## AWS – Overlay IP
<a name="overlay-ip-nw-rhel"></a>

Overlay IP enables a connection to the application, regardless of which Availability Zone (and subnet) contains the active primary node.

When deploying an Amazon EC2 instance in AWS, IP addresses are allocated from the CIDR range of the allocated subnet. The subnet cannot span across multiple Availability Zones, and therefore the subnet IP addresses may be unavailable after faults, including network connectivity or hardware issues which require a failover to the replication target in a different Availability Zone.

To address this, we suggest that you configure an overlay IP, and use this in the connection parameters for the application. This IP address is a non-overlapping RFC1918 private IP address from outside of VPC CIDR block and is configured as an entry in the route table or tables. The route directs the connection to the active node and is updated during a failover by the cluster software.

You can select any one of the following RFC1918 private IP addresses for your overlay IP address.
+ 10.0.0.0 – 10.255.255.255 (10/8 prefix)
+ 172.16.0.0 – 172.31.255.255 (172.16/12 prefix)
+ 192.168.0.0 – 192.168.255.255 (192.168/16 prefix)

If, for example, you use the 10/8 prefix in your SAP VPC, selecting a 172 or a 192 IP address may help to differentiate the overlay IP. Consider the use of an IP Address Management (IPAM) tool such as Amazon VPC IP Address Manager to plan, track, and monitor IP addresses for your AWS workloads. For more information, see [What is IPAM?](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html) 

The overlay IP agent in the cluster can also be configured to update multiple route tables which contain the Overlay IP entry if your subnet association or connectivity requires it.

 **Access to overlay IP** 

The overlay IP is outside of the range of the VPC, and therefore cannot be reached from locations that are not associated with the route table, including on-premises and other VPCs.

Use [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) as a central hub to facilitate the network connection to an overlay IP address from multiple locations, including Amazon VPCs, other AWS Regions, and on-premises using [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) or [AWS Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html).

If you do not have AWS Transit Gateway set up as a network transit hub or if it is not available in your preferred AWS Region, you can use a [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) to enable network access to an overlay IP.

For more information, see [SAP on AWS High Availability with Overlay IP Address Routing](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-ha-overlay-ip.html).

## AWS – Shared VPC
<a name="shared-vpc"></a>

An enterprise landing zone setup or security requirements may require the use of a separate cluster account to restrict the route table access required for the Overlay IP to an isolated account. For more information, see [Share your VPC with other accounts](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html).

Evaluate the operational impact against your security posture before setting up shared VPC. To set up, see [Shared VPC – optional](https://docs.aws.amazon.com/sap/latest/sap-netweaver/rhel-netweaver-ha-settings.html#rhel-netweaver-ha-shared-vpc).

## Pacemaker - STONITH fencing agent
<a name="stonith-nw-rhel"></a>

In a two-node cluster setup for a primary resource and its replication pair, it is important that there is only one node in the primary role with the ability to modify your data. In the event of a failure scenario where a node is unresponsive or incommunicable, ensuring data consistency requires that the faulty node is isolated by powering it down before the cluster commences other actions, such as promoting a new primary. This arbitration is the role of the fencing agent.

Since a two-node cluster introduces the possibility of a fence race in which a dual shoot out can occur with communication failures resulting in both nodes simultaneously claiming, "I can’t see you, so I am going to power you off". The fencing agent is designed to minimise this risk by providing an external witness.

RHEL supports several fencing agents, including the one recommended for use with Amazon EC2 Instances (fence\_aws). This resource uses API commands to check its own instance status - "Is my instance state anything other than running?" before proceeding to power off its pair. If it is already in a stopping or stopped state it will admit defeat and leave the surviving node untouched.