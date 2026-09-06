

# VPC examples
<a name="vpc-examples-intro"></a>

Amazon Virtual Private Cloud (VPC) is a fundamental building block within the AWS ecosystem, allowing you to provision isolated virtual networks tailored to your specific needs. By creating and managing your own VPCs, you gain full control over the networking environment, including the ability to define IP address ranges, subnets, routing tables, and connectivity options.

This section contains three example configurations for your virtual private clouds (VPCs), each designed to address a different set of requirements:
+ VPC for a test environment: This configuration shows how to create a VPC that you can use as a development or test environment.
+ VPC for Web and database servers: This configuration shows how to create a VPC that you can use for a resilent architecture in a production environment.
+ VPC with servers in private subnets and NAT: In this more advanced configuration, all EC2 instances are provisioned within private subnets, with a NAT gateway facilitating secure outbound internet access. This is an example where you need to limit direct internet connectivity to your resources while still enabling necessary outbound communication.

By providing these example VPC configurations, we hope to illustrate the flexibility and customization options available when designing your cloud networking environment. The specific VPC setup you choose should be based on your application's architecture, security requirements, and overall business objectives. Carefully planning your VPC infrastructure can help you create a robust, scalable, and secure virtual network that supports the growth and evolution of your cloud-based workloads.

**Topics**
+ [Test environment](vpc-example-dev-test.md)
+ [Web and database servers](vpc-example-web-database-servers.md)
+ [Private servers](vpc-example-private-subnets-nat.md)

**Related examples**
+ To connect your VPCs to each other, see [VPC peering configurations](https://docs.aws.amazon.com/vpc/latest/peering/peering-configurations.html) in the *Amazon VPC Peering Guide*.
+ To connect your VPCs to your own network, see [Site-to-Site VPN scenarios](https://docs.aws.amazon.com/vpn/latest/s2svpn/site-site-architectures.html) in the *AWS Site-to-Site VPN User Guide*.
+ To connect your VPCs to each other and to your own network, see [Example transit gateway scenarios](https://docs.aws.amazon.com/vpc/latest/tgw/how-transit-gateways-work.html#TGW_Scenarios) in the *Amazon VPC Transit Gateways*.

**Additional resources**
+ [Understand resiliency patterns and trade-offs](https://aws.amazon.com/blogs/architecture/understand-resiliency-patterns-and-trade-offs-to-architect-efficiently-in-the-cloud/) (AWS Architecture Blog)
+ [Plan your network topology](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-your-network-topology.html) (AWS Well-Architected Framework)
+ [Amazon Virtual Private Cloud Connectivity Options](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/introduction.html) (AWS Whitepapers)