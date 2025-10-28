# AWS network connectivity management tools

The following AWS services can be used to help you follow the
guidance provided by the M&G Guide:

[Amazon VPC](https://aws.amazon.com/quickstart/architecture/vpc/ "https://aws.amazon.com/quickstart/architecture/vpc/") is a service that
lets you launch AWS resources in a logically isolated virtual network that you define. This
can be done within one account, or within a multi-account strategy. You have complete control
over this virtual networking environment, including selection of your own IP address range,
creation of subnets, and configuration of route tables and network gateways. You can use both
IPv4 and IPv6 addresses for most resources in your virtual private cloud, helping to ensure
secure and easy access to resources and applications.

[Amazon VPC IP Address
Manager](../../../vpc/latest/ipam/what-it-is-ipam.md "../../../vpc/latest/ipam/what-it-is-ipam.md") (IPAM) is a VPC feature that makes it easier for you to plan, track, and
monitor IP addresses for your AWS workloads. You can use the automated workflows in IPAM to
more efficiently manage IP addresses.

For cloud-to-cloud connectivity, cloud-to-enterprise, and
cloud-to-internet, we recommend using [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/ "https://aws.amazon.com/transit-gateway/") as a
shared service in your multi-account strategy. Transit Gateway
uses a hub and spoke pattern to simplify your network and provide
a central point for network traffic inspection. Connections of AWS accounts to a transit gateway can be deployed automatically by
Control Tower Customizations and AWS Partners.

[AWS Direct Connect](../../../directconnect/index.md "../../../directconnect/index.md") establishes a dedicated network connection
between your on-premises network and AWS. With this connection in
place, you can create virtual interfaces directly to the AWS Cloud, bypassing your internet service provider. This can provide
a more consistent network experience.

[AWS Virtual Private Network](https://aws.amazon.com/vpn/ "https://aws.amazon.com/vpn/") solutions establish secure connections between your
on-premises networks, remote offices, client devices, and the AWS
global network. AWS VPN is comprised of two services:
[AWS Site-to-Site VPN](https://aws.amazon.com/vpn/site-to-site-vpn/ "https://aws.amazon.com/vpn/site-to-site-vpn/") and
[AWS Client VPN](https://aws.amazon.com/vpn/client-vpn/ "https://aws.amazon.com/vpn/client-vpn/"). Each service provides a highly-available,
managed, and elastic cloud VPN solution to protect your network
traffic. AWS Site-to-Site VPN creates encrypted tunnels between
your network and your Amazon Virtual Private Clouds or AWS Transit
Gateways. For managing remote access, AWS Client VPN connects your
users to AWS or on-premises resources using a VPN software client.

[AWS Transit Gateway Network Manager](https://aws.amazon.com/transit-gateway/network-manager/ "https://aws.amazon.com/transit-gateway/network-manager/") reduces the operational
complexity of managing a global network across AWS and
on-premises. With Network Manager, you can set up a global view of
your private network simply by registering your Transit Gateways
and on-premises resources. Your global network can then be
visualized and monitored via a centralized operational dashboard.

To provide preventive security for internet-to-cloud connectivity,
we recommend implementation of [AWS Network Firewall](https://aws.amazon.com/network-firewall/ "https://aws.amazon.com/network-firewall/"). Network
Firewall gives you granular visibility and control of your network
traffic, enabling outbound domain filtering, and intrusion
prevention through event driven logging, and the service
automatically scales with network traffic to provide high
availability protections without the need to set up or maintain
the underlying infrastructure.

By deploying Network Firewall along with Transit Gateway, you can
centrally inspect hundreds or thousands of VPCs and accounts and
centrally configure and manage your network firewall, firewall
policies, and rule groups.

[AWS Firewall Manager](https://aws.amazon.com/firewall-manager/ "https://aws.amazon.com/firewall-manager/") is a security management service that helps
you to simplify management of firewall rules across your accounts,
easily deploy managed rules across accounts, meet compliance
obligations of your existing and new application firewalls, and
centrally deploy protections for your VPCs.

AWS automated reasoning provides tools that detect entire classes
of misconfigurations, including both a VPC and network
configuration tool. [VPC Reachability Analyzer](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md") is a configuration
analysis tool that enables you to perform connectivity testing
between a source resource and a destination resource in your VPCs.
When the destination is reachable, Reachability Analyzer produces
hop-by-hop details of the virtual network path between the source
and the destination. When the destination is not reachable,
Reachability Analyzer identifies the blocking component. For
example, paths can be blocked by configuration issues in a
security group, network ACL, route table, or load balancer.

[Amazon Inspector Network Reachability](../../../inspector/latest/userguide/inspector_network-reachability.md "../../../inspector/latest/userguide/inspector_network-reachability.md") provides rules to analyze
your network configurations to find security vulnerabilities of
your EC2 instances. The findings that
[Amazon Inspector](../../../inspector/latest/userguide/inspector_introduction.md "../../../inspector/latest/userguide/inspector_introduction.md") generates also provide guidance about restricting
access that might not be secure. The Network Reachability rules
package uses the latest technology from the
[AWS Provable Security initiative](https://aws.amazon.com/security/provable-security/ "https://aws.amazon.com/security/provable-security/"). The findings generated by
these rules show whether your ports are reachable from the
internet through an internet gateway (including instances behind
Application Load Balancers or Classic Load Balancers), a
[VPC
peering](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md") connection, or a VPN through a virtual gateway.
These findings also highlight network configurations that allow
for potentially unwanted access, such as mismanaged security
groups, ACLs, and internet gateways. These rules help automate the
monitoring of your AWS networks and identify where network access
to your EC2 instances might be misconfigured. By including this
package in your assessment run, you can implement detailed network
security checks without having to install scanners and send
packets, which are complex and expensive to maintain, especially
across VPC peering connections and VPNs.

If you would like support implementing this guidance, or assisting
you with building the foundational elements prescribed by the
M&G Guide, we recommend you review the offerings provided by
[AWS Professional Services](https://aws.amazon.com/professional-services/ "https://aws.amazon.com/professional-services/") or the AWS Partners in the
[Built
on Control Tower program](https://aws.amazon.com/controltower/partners/ "https://aws.amazon.com/controltower/partners/").

If you are seeking help to operate your workloads in AWS following
this guidance,
[AWS Managed Services (AMS)](https://aws.amazon.com/managed-services/ "https://aws.amazon.com/managed-services/") can augment your operational
capabilities as a short-term accelerator or a long-term solution,
letting you focus on transforming your applications and businesses
in the cloud.
