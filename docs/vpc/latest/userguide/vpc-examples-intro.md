# VPC examples

Amazon Virtual Private Cloud (VPC) is a fundamental building block within the AWS ecosystem, allowing you to provision isolated virtual networks tailored to your specific needs. By creating and managing your own VPCs, you gain full control over the networking environment, including the ability to define IP address ranges, subnets, routing tables, and connectivity options.

This section contains three example configurations for your virtual private clouds (VPCs), each designed to address a different set of requirements:

- VPC for a test environment: This configuration shows how to create a VPC that you can use as a development or test environment.
- VPC for Web and database servers: This configuration shows how to create a VPC that you can use for a resilent architecture in a production environment.
- VPC with servers in private subnets and NAT: In this more advanced configuration, all EC2 instances are provisioned within private subnets, with a NAT gateway facilitating secure outbound internet access. This is an example where you need to limit direct internet connectivity to your resources while still enabling necessary outbound communication.
  By providing these example VPC configurations, we hope to illustrate the flexibility and customization options available when designing your cloud networking environment. The specific VPC setup you choose should be based on your application's architecture, security requirements, and overall business objectives. Carefully planning your VPC infrastructure can help you create a robust, scalable, and secure virtual network that supports the growth and evolution of your cloud-based workloads.

###### Examples

- [Test environment](vpc-example-dev-test.md "vpc-example-dev-test.md")
- [Web and database servers](vpc-example-web-database-servers.md "vpc-example-web-database-servers.md")
- [Private servers](vpc-example-private-subnets-nat.md "vpc-example-private-subnets-nat.md")

###### Related examples

- To connect your VPCs to each other, see [VPC peering configurations](../peering/peering-configurations.md "../peering/peering-configurations.md") in the _Amazon VPC Peering Guide_.
- To connect your VPCs to your own network, see [Site-to-Site VPN scenarios](../../../vpn/latest/s2svpn/site-site-architectures.md "../../../vpn/latest/s2svpn/site-site-architectures.md") in the _AWS Site-to-Site VPN User Guide_.
- To connect your VPCs to each other and to your own network, see [Example transit gateway scenarios](../tgw/how-transit-gateways-work.md#TGW_Scenarios "../tgw/how-transit-gateways-work.md#TGW_Scenarios") in the _Amazon VPC Transit Gateways_.

###### Additional resources

- [Understand resiliency patterns and trade-offs](https://aws.amazon.com/blogs/architecture/understand-resiliency-patterns-and-trade-offs-to-architect-efficiently-in-the-cloud/ "https://aws.amazon.com/blogs/architecture/understand-resiliency-patterns-and-trade-offs-to-architect-efficiently-in-the-cloud/") (AWS Architecture Blog)
- [Plan your network topology](../../../wellarchitected/latest/reliability-pillar/plan-your-network-topology.md "../../../wellarchitected/latest/reliability-pillar/plan-your-network-topology.md") (AWS Well-Architected Framework)
- [Amazon Virtual Private Cloud Connectivity Options](../../../whitepapers/latest/aws-vpc-connectivity-options/introduction.md "../../../whitepapers/latest/aws-vpc-connectivity-options/introduction.md") (AWS Whitepapers)
