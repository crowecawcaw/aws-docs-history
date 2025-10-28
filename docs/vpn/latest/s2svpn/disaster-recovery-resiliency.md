# Resilience in AWS Site-to-Site VPN

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated
Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and
operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly
available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

In addition to the AWS global infrastructure, Site-to-Site VPN offers features to help support your
data resiliency and backup needs.

## Two tunnels per VPN connection

A Site-to-Site VPN connection consists of two tunnels, each terminating in a different
Availability Zone, to provide increased availability to your VPC. If there's a device
failure within AWS, your VPN connection automatically fails over to the second tunnel
so that your access isn't interrupted. From time to time, AWS also performs routine
maintenance on your VPN connection, which may briefly disable one of the two tunnels of
your VPN connection. For more information, see [AWS Site-to-Site VPN tunnel endpoint replacements](endpoint-replacements.md "endpoint-replacements.md"). When you configure your customer gateway,
it's therefore important that you configure both tunnels.

## Redundancy

To protect against a loss of connectivity in case your customer gateway becomes
unavailable, you can set up a second Site-to-Site VPN connection. For more information, see the
following documentation:

- [Redundant AWS Site-to-Site VPN connections for failover](vpn-redundant-connection.md "vpn-redundant-connection.md")
- [Amazon Virtual Private Cloud Connectivity Options](../../../whitepapers/latest/aws-vpc-connectivity-options/welcome.md "../../../whitepapers/latest/aws-vpc-connectivity-options/welcome.md")
- [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.md "../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.md")
