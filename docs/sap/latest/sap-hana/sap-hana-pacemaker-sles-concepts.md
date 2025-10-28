# Concepts

## SAP – SAP HANA and Hana System Replication

SAP HANA is an in-memory, column-oriented, relational database management system developed by SAP. It uses HANA System Replication (HSR) to replicate data and changes from a primary system to one or more secondary systems. In scale-out deployments, this replication occurs between corresponding nodes across the primary and secondary systems, with each service having its counterpart in the secondary system. HSR ensures changes are continuously replicated to minimize the Recovery Point Objective (RPO).
While takeovers can be manually triggered using HANA tooling, the addition of a Pacemaker cluster automates the failover process through monitoring, orchestration, and integration with resource agents for hardware connectivity and management.

## AWS – Availability Zones

An Availability Zone is one or more discreet data centers with redundant power, networking, and connectivity in an AWS Region. For more information, see Regions and Availability Zones.

For mission critical deployments of SAP on AWS where the goal is to minimise the recovery time objective (RTO), we suggest distributing single points of failure across Availability Zones. Compared with single instance or single Availability Zone deployments, this increases resilience and isolation against a broad range of failure scenarios and issues, including natural disasters.

Each Availability Zone is physically separated by a meaningful distance (many kilometers) from another Availability Zone. All Availability Zones in an AWS Region re interconnected with high-bandwidth, low-latency network, over fully redundant, dedicated metro fiber. This enables synchronous replication. All traffic between Availability Zones is encrypted.

## AWS – Overlay IP

An Overlay IP enables a connection to the application, regardless of which Availability Zone (and subnet) contains the active primary node.

When deploying an Amazon EC2 instance in AWS, IP addresses are allocated from the CIDR range of the allocated subnet. The subnet cannot span across multiple Availability Zones, and therefore the subnet IP addresses may be unavailable after faults, including network connectivity or hardware issues which require a failover to the replication target in a different Availability Zone.

To address this, we suggest that you configure an overlay IP, and use this in the connection parameters for the application. This IP address is a non-overlapping RFC1918 private IP address from outside of VPC CIDR block and is configured as an entry in the route table or tables. The route directs the connection to the active node and is updated during a failover by the cluster software.

You can select any one of the following RFC1918 private IP addresses for your overlay IP address:

- 10.0.0.0 – 10.255.255.255 (10/8 prefix)
- 172.16.0.0 – 172.31.255.255 (172.16/12 prefix)
- 192.168.0.0 – 192.168.255.255 (192.168/16 prefix)

If, for example, you use the 10/8 prefix in your SAP VPC, selecting a 172 or a 192 IP address may help to differentiate the overlay IP. Consider the use of an IP Address Management (IPAM) tool such as Amazon VPC IP Address Manager to plan, track, and monitor IP addresses for your AWS workloads. For more information, see [What is IPAM?](../../../vpc/latest/ipam/what-it-is-ipam.md "../../../vpc/latest/ipam/what-it-is-ipam.md")

The overlay IP agent in the cluster can also be configured to update multiple route tables which contain the Overlay IP entry if your subnet association or connectivity requires it.

### Access to the Overlay IP

The overlay IP is outside of the range of the VPC, and therefore cannot be reached from locations that are not associated with the route table, including on-premises and other VPCs.

Use AWS Transit Gateway as a central hub to facilitate the network connection to an overlay IP address from multiple locations, including Amazon VPCs, other AWS Regions, and on-premises using AWS Direct Connect or AWS Client VPN.

If you do not have AWS Transit Gateway set up as a network transit hub or if it is not available in your preferred AWS Region, you can use a Network Load Balancer to enable network access to an overlay IP.

For more information, see [SAP on AWS High Availability Setup](sap-oip-sap-on-aws-high-availability-setup.md "sap-oip-sap-on-aws-high-availability-setup.md").

## AWS – Shared VPC

An enterprise landing zone setup or security requirements may require the use of a separate cluster account to restrict the route table access required for the Overlay IP to an isolated account. For more information, see [Share your VPC with other accounts](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md").

Evaluate the operational impact against your security posture before setting up shared VPC.

## Pacemaker - STONITH Fencing Agent

In SAP HANA deployments, whether in a scale-up configuration (two-node) or a scale-out configuration (two or more nodes per site), it is crucial that data consistency is maintained by ensuring only the designated primary node or nodes can process write operations at any given time. When a node becomes unresponsive or incommunicable, maintaining data consistency may require that the faulty node is isolated by powering it down before the cluster commences other actions, such as promoting a new primary. This arbitration is the role of the fencing agent.

In a two-node scale-up scenario, fence racing is a critical concern. This occurs when a communication failure causes both nodes to simultaneously attempt to fence (power off) each other, believing the other node has failed. The fencing agent addresses this risk by providing an external witness. In scale-out deployments, while fence racing is less likely due to the presence of multiple nodes that can participate in quorum decisions, proper fencing remains critical for maintaining data consistency across the larger node set.

SUSE supports several fencing agents, including the one recommended for use with Amazon EC2 Instances (external/ec2).
