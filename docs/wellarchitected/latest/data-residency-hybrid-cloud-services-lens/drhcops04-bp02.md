# DRHCOPS04-BP02 Design your Outposts and Local Zone workloads to consider network connectivity

With the updated
[shared
responsibility model for Outposts](../../../whitepapers/latest/applying-security-practices-to-network-workload-for-csps/the-shared-responsibility-model.md "../../../whitepapers/latest/applying-security-practices-to-network-workload-for-csps/the-shared-responsibility-model.md"), you own the operations
of the network connectivity and bandwidth.

**Desired outcome:** Architect
Outposts and Local Zone workloads with robust network connectivity
designs that account for factors such as bandwidth requirements,
latency constraints, and secure communication channels.

**Benefits of establishing this best
practice:** You have carefully considered network
connectivity when designing Outposts and Local Zone workloads,
which provides optimal performance, reliability, and security,
helps you seamlessly integrate with on-premises infrastructure and
cloud resources, and verifies that you adhere to data residency
and compliance requirements.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

**Outposts network connectivity**

AWS Outposts provides several network connectivity options to
enable communication between your on-premises resources, Outpost
instances, and AWS services.

- **Local gateway:** Outposts
  establish an external BGP peering from each Outpost network
  device to your local network device for connectivity to your
  on-premises resources.
- **Service link:** This is a
  necessary connection from the Outpost to your chosen AWS Region, allowing management of the Outposts and exchange of
  traffic between Outpost instances and AWS services.
- **Local Network Interfaces
  (LNI):** LNIs enable communication between your VPC
  and your on-premises network over the local gateway. This
  includes traffic from Outpost instances to your local
  network or the internet through your network.
- **Private connectivity:**
  Outposts can connect privately to your datacenter using AWS Direct Connect or a VPN, allowing communication between your
  on-premises resources and Outpost instances without going
  over the public internet.
- **Direct VPC routing:**
  Outpost instances can communicate directly with resources in
  your VPCs in the same AWS Region using private IP addresses
  without the need for a VPN or AWS Direct Connect.

Use the local gateway path instead of the service link path, and
route internet traffic over the local gateway path wherever
possible. Provision redundant network paths between the Outpost
LGW and critical on-premises application resources. Use dynamic
routing to automate traffic redirection around on-premises
network failures. For more detail, see
[Application/workload
routing](../../../whitepapers/latest/aws-outposts-high-availability-design/applicationworkload-routing.md "../../../whitepapers/latest/aws-outposts-high-availability-design/applicationworkload-routing.md").

**Local Zones Network
Connectivity**

Local Zones are built into your network architecture the same
way as an Availability Zone. You can extend any VPC from a
parent Region into a Local Zone by creating a new subnet and
assigning it to the Local Zone. The Local Zone network can have
public subnets, internet gateways, and AWS Direct Connect
gateways to your On-premises data center. For additional guidance, see [Connectivity
options for Local Zones](../../../local-zones/latest/ug/local-zones-connectivity.md "../../../local-zones/latest/ug/local-zones-connectivity.md").
