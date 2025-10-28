# Connectivity through service link

During AWS Outposts provisioning, you or AWS creates a service link
connection that connects your Outposts server to your chosen AWS Region or home Region. The service
link is an encrypted set of VPN connections that are used whenever the Outpost communicates
with your chosen home Region. You use a virtual LAN (VLAN) to segment traffic on the service
link. The service link VLAN enables communication between the Outpost and the AWS Region for
both management of the Outpost and intra-VPC traffic between the AWS Region and
Outpost.

The Outpost is able to create the service link VPN back to the AWS
Region through public Region connectivity. To do so, the Outpost needs connectivity to the
AWS Region's public IP ranges, either through the public internet or AWS Direct Connect public
virtual interface. This connectivity can be through specific routes in the service link VLAN,
or through a default route of 0.0.0.0/0. For more information about the public ranges for
AWS, see [AWS IP address ranges](../../../vpc/latest/userguide/aws-ip-ranges.md "../../../vpc/latest/userguide/aws-ip-ranges.md") in
the _Amazon VPC User Guide_.

After the service link is established, the Outpost is in service and
managed by AWS. The service link is used for the following traffic:

- Management traffic to the Outpost through the service link, including internal control
  plane traffic, internal resource monitoring, and updates to firmware and software.
- Traffic between the Outpost and any associated VPCs, including customer data plane
  traffic.

## Service link maximum transmission unit (MTU)

requirements

The maximum transmission unit (MTU) of a network connection is the size, in bytes, of
the largest permissible packet that can be passed over the connection.

Note the following:

- The network **must** support 1500-bytes MTU between the
  Outpost and the service link endpoints in the parent AWS Region.
- The traffic that goes from an instance in Outposts to an instance in the Region has
  an MTU of 1300 bytes, which is lower than the required MTU of 1500 bytes due to packet
  overheads.

## Service link bandwidth

recommendations

For an optimal experience and resiliency, AWS requires that you use
redundant connectivity of at least 500 Mbps and a maximum of 175 ms round trip latency for
the service link connection to the AWS Region. The maximum utilization for each Outposts server
is 500 Mbps. To increase the connection speed, use multiple Outposts servers. For example, if you
have three AWS Outposts servers, the maximum connection speed increases to 1.5 Gbps (1,500 Mbps).
For more information, see [Service link traffic for
servers](local-server.md#lni-sl "local-server.md#lni-sl").

Your AWS Outposts service link bandwidth requirements vary depending on
workload characteristics, such as AMI size, application elasticity, burst speed needs, and
Amazon VPC traffic to the Region. Note that AWS Outposts servers do not cache AMIs. AMIs are downloaded
from the Region with every instance launch.

We strongly recommend consulting with your AWS sales representative or APN partner to
evaluate available home Region options in your geography and seek a custom
recommendation about the service link bandwidth and latency requirements for your workloads.

## Redundant internet connections

When you build connectivity from your Outpost to the AWS Region, we recommend that you
create multiple connections for higher availability and resiliency. For more information,
see [AWS Direct Connect
Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/ "https://aws.amazon.com/directconnect/resiliency-recommendation/").

If you need connectivity to the public internet, you can use redundant internet
connections and diverse internet providers, just as you would with your existing on-premises
workloads.
