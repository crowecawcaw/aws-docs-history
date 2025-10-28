# VPC configuration options

You can specify the following configuration options when you create a VPC.

**Availability Zones**

Discrete data centers with redundant power, networking, and connectivity in an AWS
Region. You can use multiple AZs to operate production applications and databases that
are more highly available, fault tolerant, and scalable than would be possible from a
single data center. If you partition your applications running in subnets across AZs,
you are better isolated and protected from issues such as power outages, lightning
strikes, tornadoes, and earthquakes.

**CIDR blocks**

You must specify IP address ranges for your VPC and subnets. For more information,
see [IP addressing for your VPCs and subnets](vpc-ip-addressing.md "vpc-ip-addressing.md").

**DNS options**

If you need public IPv4 DNS hostnames for the EC2 instances launched
into your subnets, you must enable both of the DNS options. For more information,
see [DNS attributes for your VPC](vpc-dns.md "vpc-dns.md").

- **Enable DNS hostnames**: EC2 instances launched in the VPC
  receive public DNS hostnames that correspond to their public IPv4 addresses.
- **Enable DNS resolution**: DNS resolution for private DNS
  hostnames is provided for the VPC by the Amazon DNS server, called the Route 53 Resolver.

**Internet gateway**

Connects your VPC to the internet. The instances in a public subnet can access
the internet because the subnet route table contains a route that sends traffic bound
for the internet to the internet gateway. If a server doesn't need to be directly
reachable from the internet, you should not deploy it into a public subnet. For more
information, see [Internet gateways](VPC_Internet_Gateway.md "VPC_Internet_Gateway.md").

**Name**

The names that you specify for the VPC and the other VPC resources are used
to create Name tags. If you use the name tag auto-generation feature in the console,
the tag values have the format `name`-`resource`.

**NAT gateways**

Enables instances in a private subnet to send outbound traffic to the internet,
but prevents resources on the internet from connecting to the instances. In
production, we recommend that you deploy a NAT gateway in each active AZ.
For more information, see [NAT gateways](vpc-nat-gateway.md "vpc-nat-gateway.md").

**Route tables**

Contains a set of rules, called routes, that determine where network traffic
from your subnet or gateway is directed. For more information, see
[Route tables](VPC_Route_Tables.md "VPC_Route_Tables.md").

**Subnets**

A range of IP addresses in your VPC. You can launch AWS resources, such as EC2
instances, into your subnets. Each subnet resides entirely within one Availability
Zone. By launching instances in at least two Availability Zones, you can protect
your applications from the failure of a single Availability Zone.

A public subnet has a direct route to an internet gateway. Resources in a public
subnet can access the public internet. A private subnet does not have a direct
route to an internet gateway. Resources in a private subnet require another
component, such as a NAT device, to access the public internet.

For more information, see [Subnets](configure-subnets.md "configure-subnets.md").

**Tenancy**

This option defines if EC2 instances that
you launch into the VPC will run on hardware that's shared with other
AWS accounts or on hardware that's dedicated for your use only. If you choose
the tenancy of the VPC to be `Default`, EC2 instances launched
into this VPC will use the tenancy attribute specified when you launch the
instance -- For more information, see [Launch an
instance using defined parameters](../../../AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.md "../../../AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.md") in the
_Amazon EC2 User Guide_. If you choose the tenancy of the VPC
to be `Dedicated`, the instances will always run as [Dedicated Instances](../../../AWSEC2/latest/UserGuide/dedicated-instance.md "../../../AWSEC2/latest/UserGuide/dedicated-instance.md") on
hardware that's dedicated for your use. If you're using AWS Outposts, your
Outpost requires private connectivity; you must use `Default`
tenancy.
