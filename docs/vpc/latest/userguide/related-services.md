# Use Amazon VPC with other AWS services

Amazon Virtual Private Cloud (VPC) is a foundational AWS service that provides a secure,
customizable networking environment for your cloud infrastructure. Beyond creating and
managing your own VPC, you can leverage the integration between VPC and other AWS services
to build comprehensive solutions tailored to your specific needs.

You can connect your VPC to various AWS services using AWS PrivateLink. This enables private connectivity between your VPC and supported AWS services or on-premises applications, keeping network traffic within the AWS network and avoiding exposure to the public internet. This is particularly useful for maintaining strict security boundaries and compliance requirements.

To further strengthen the security of your VPC, you can use AWS Network Firewall. This managed firewall service allows you to define and enforce network-level security policies, filtering both north-south and east-west traffic within your VPC. By pairing Network Firewall with your VPC, you can enhance your defense strategy and protect your cloud resources from unauthorized access or malicious activity.

Additionally, you can filter DNS traffic within your VPC using the Route 53 Resolver DNS Firewall. This capability enables you to create custom DNS filtering rules to control which domains your VPC resources can resolve, providing an additional layer of security and compliance enforcement.

If you encounter reachability issues between resources within your VPC or connected to your VPC, you can leverage Reachability Analyzer. Reachability Analyzer performs virtual connectivity tests, providing detailed hop-by-hop path information and identifying any blocking components. This troubleshooting tool can quickly help you identify and resolve network connectivity problems.

By integrating these complementary AWS services with your VPC, you can build powerful, secure, and resilient cloud solutions that address your unique business and architectural requirements.

###### Contents

- [Connect your VPC to services using AWS PrivateLink](endpoint-services-overview.md "endpoint-services-overview.md")
- [Filter network traffic using AWS Network Firewall](network-firewall.md "network-firewall.md")
- [Filter DNS traffic using Route 53 Resolver DNS Firewall](resolver-dns-firewall.md "resolver-dns-firewall.md")
- [Troubleshoot reachability issues using Reachability Analyzer](reachability-analyzer.md "reachability-analyzer.md")
