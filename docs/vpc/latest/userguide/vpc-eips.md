# Associate Elastic IP addresses with resources in your VPC

An Elastic IP address is a static, public IPv4 address designed specifically for the
dynamic nature of cloud computing. This feature allows you to associate an Elastic IP
address with any instance or network interface within any Virtual Private Cloud (VPC) in
your AWS account. By leveraging Elastic IP addresses, you can unlock a host of benefits that
simplify the management and resilience of your cloud-based infrastructure.

One of the primary advantages of Elastic IP addresses is their ability to mask the failure
of an instance. Should an instance experience an unexpected outage or need to be replaced,
you can remap the associated Elastic IP address to another instance within your VPC. This
failover process ensures that your applications and services maintain a consistent and
reliable public endpoint, minimizing downtime and providing a superior user
experience.

Furthermore, Elastic IP addresses offer flexibility in how you manage your network
resources. You can programmatically associate and disassociate these addresses as needed,
allowing you to direct traffic to different instances based on your evolving business
requirements. This dynamic allocation of public IP addresses empowers you to adapt to
changing demand, scale your infrastructure, and implement innovative architectures without
the constraints of static IP assignments.

Beyond their use for instance failover, Elastic IP addresses can also serve as stable
identifiers for your cloud-based resources. This can be beneficial when configuring external
services, such as DNS records or firewall rules, to communicate with your AWS-hosted
applications. By associating a persistent public IP address, you can future-proof your
networking configurations and avoid the need to update external references when underlying
instances are replaced or scaled.

###### Contents

- [Elastic IP address concepts and rules](vpc-eip-overview.md "vpc-eip-overview.md")
- [Start using Elastic IP addresses](WorkWithEIPs.md "WorkWithEIPs.md")
