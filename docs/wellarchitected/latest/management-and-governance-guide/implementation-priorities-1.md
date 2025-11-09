# Implementation priorities

Network connectivity is typically implemented in the early phases
of a cloud journey. As you evolve your network strategy, the
following items should be prioritized.

## Plan your IP address space (IP address management – IPAM)

Similar to private networks, VPCs typically use private or RFC
1918 IPv4 space. However, you can also use publicly routable
non-RFC 1918 CIDR blocks for your VPC. Carefully plan the IP
address space that you will be allocating to your VPCs,
particularly if you are using an IPv4 range. The best practice for
IPv4 planning is to first allocate a non-overlapping and
contiguous address block. Subdividing address space into subnets
based on attributes like environment or AWS Region helps you to
create separate network boundaries more easily. You might also
consider other CIDR grouping approaches based on regulatory
requirements or the sensitivity of their workloads. This approach
can simplify routing, security policies and the ability to query
logs.

In the following example, VPCs have been assigned a contiguous IP
space aligned by VPC environment to simplify application of
security groups and NACLs.

| Example VPC CIDR ranges |             | Dev VPCs     | Test VPCs     | QA VPCs       | Prod VPCs |
| ----------------------- | ----------- | ------------ | ------------- | ------------- | --------- |
| AWS Region 1            | 10.0.0.0/16 | 10.64.0.0/16 | 10.128.0.0/16 | 10.192.0.0/16 |
| AWS Region 2            | 10.1.0.0/16 | 10.65.0.0/16 | 10.129.0.0/16 | 10.193.0.0/16 |

- 10.0.0.0/15 represents all Dev VPCs
- 10.64.0.0/15 represents all Test VPCs
- 10.128.0.0/15 represents all QA VPCs
- 10.192.0.0/15 represents all Prod VPCs

In the next example, VPCs have been assigned contiguous IP
space aligned by AWS Region to simplify routing.

| Example VPC CIDR ranges |             | Dev VPCs    | Test VPCs   | QA VPCs     | Prod VPCs |
| ----------------------- | ----------- | ----------- | ----------- | ----------- | --------- |
| AWS Region 1            | 10.0.0.0/16 | 10.1.0.0/16 | 10.2.0.0/16 | 10.3.0.0/16 |
| AWS Region 2            | 10.4.0.0/16 | 10.5.0.0/16 | 10.6.0.0/16 | 10.7.0.0/16 |

- 10.0.0.0/14 represents all VPCs in AWS Region 1
- 10.4.0.0/14 represents all VPCs in AWS Region 2

If insufficient IP space is a concern, consider
[VPC
sharing](https://aws.amazon.com/blogs/networking-and-content-delivery/vpc-sharing-a-new-approach-to-multiple-accounts-and-vpc-management/ "https://aws.amazon.com/blogs/networking-and-content-delivery/vpc-sharing-a-new-approach-to-multiple-accounts-and-vpc-management/") to simplify IPv4 address allocation, and preserve
scarce IP addresses. This approach gives you the ability to
centralize control of network maintenance while still granting
builders the ability to self-provision VPC based resources. AWS PrivateLink can also help alleviate IP exhaustion and overlap by
enabling the creation of services in your VPCs that can be
consumed through a PrivateLink endpoint with traffic flowing
across Amazon’s private network. Service consumers don’t have to
worry about overlapping IP addresses, arrange for VPC peering, or
use a Transit Gateway. If exhaustion of IP space is still a
concern, you can evaluate alternative solutions that rely on
[Private
NAT and TGW](https://aws.amazon.com/blogs/networking-and-content-delivery/how-to-solve-private-ip-exhaustion-with-private-nat-solution/ "https://aws.amazon.com/blogs/networking-and-content-delivery/how-to-solve-private-ip-exhaustion-with-private-nat-solution/") to allow for communication between VPCs with
overlapping CIDR ranges.

The IPv6 address space is much larger than the IPv4 address space,
so it’s not currently at risk of exhaustion. However, if you plan
to
[bring
your own IPv6 space into AWS](../../../vpc/latest/userguide/get-started-ipv6.md "../../../vpc/latest/userguide/get-started-ipv6.md"), it’s still a good practice to
structure it in a similar fashion to IPv4.

Continually review and refine your network isolation boundaries
and perform impact analysis for any proposed network changes. VPC
design would be incomplete without a scalable subnet design. As
with other management and governance functions, consider the
operational complexity when designing or refining the allocation
of subnets and be mindful of allocating too many subnet tiers.
Because individual subnets cannot span multiple Availability Zones
(AZs), deploy workloads to multiple subnets across multiple AZs to
allow for workload resiliency using capabilities like Auto Scaling
groups, load balancers, and services that span AZs. Your subnet
design will likely include a combination of public and private
subnets. Public subnets are associated with a route table that has
a route to an Internet Gateway, while private subnets do not have
a route to an Internet Gateway and are typically associated with a
NAT Gateway if they require internet access.

## Design network connectivity

We think of network connectivity in three different areas:

- Connectivity between your on-premises network and your AWS
  environments
- Connectivity to and from the internet
- Connectivity across your AWS environments.

For on-premises connectivity, customers typically start with a
VPN. They add additional VPNs or convert to Direct Connect and add
resilience and bandwidth as time, maturity, and requirements
progress. It is also common for customers to configure VPN over a
Direct Connect connection to achieve consistent levels of
throughput and encryption algorithms that protect data in transit.
AWS Direct Connect also offers IEEE 802.1AE MAC Security Standard
(MACsec) encryption for 10Gbps and 100Gbps Dedicated Connections
at select locations to secure your high-speed, private
connectivity to the cloud.

Decide whether to configure internet traffic in a centralized or
distributed manner, depending on your enterprise needs. You might
choose to centralize inbound or outbound internet traffic with a
hub and spoke model using AWS Transit Gateway or an AWS Partner
solution, or distribute internet traffic flows via appropriate
VPCs in their environment. Establish internet connectivity by
implementing internet gateways, public subnets as well as NAT
gateways. Review the whitepaper on
[building
scalable multi-VPC architectures](https://d1.awsstatic.com/whitepapers/building-a-scalable-and-secure-multi-vpc-aws-network-infrastructure.pdf?did=wp_card&trk=wp_card "https://d1.awsstatic.com/whitepapers/building-a-scalable-and-secure-multi-vpc-aws-network-infrastructure.pdf?did=wp_card&trk=wp_card") to help you decide which
pattern best fits your requirements.

For connectivity across your AWS environments, connect VPCs both
within and across AWS Regions using a transit gateway hub and
spoke model.
[The
Serverless Transit Network Orchestrator solution](https://aws.amazon.com/solutions/implementations/serverless-transit-network-orchestrator "https://aws.amazon.com/solutions/implementations/serverless-transit-network-orchestrator") automates
the process of setting up and managing transit networks in
distributed AWS environments. It creates a web interface to help
control, audit, and approve (transit) network changes. This
includes establishing peering connections between transit gateways
to extend connectivity and build global networks spanning multiple
AWS Regions.

## Define your VPC endpoint and DNS

strategy

To establish private connectivity from your VPC to supported AWS
services, use
[VPC
Interface endpoints](../../../vpc/latest/privatelink/vpce-interface.md "../../../vpc/latest/privatelink/vpce-interface.md"). An interface endpoint is an elastic
network interface with a private IP address from the IP address
range of your VPC subnets. Interface endpoints can be deployed
across multiple AZs for resiliency. Interface endpoints serve as
an entry point for traffic destined to a supported AWS service. In
addition, add
[endpoint
policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") to control access from the endpoint to the
specified service. Amazon Virtual Private Cloud documentation
includes an updated
[list
of services](../../../vpc/latest/privatelink/integrated-services-vpce-list.md "../../../vpc/latest/privatelink/integrated-services-vpce-list.md") that support VPC Interface endpoints.

When deploying your VPC endpoints, consider two approaches. One
approach is to centralize multiple endpoints in a single VPC
reachable from other VPCs using AWS Transit Gateway. This approach
allows you to lower the overall endpoint cost but also means that
access policies and endpoint capacity would be shared between
multiple VPCs. A second approach is to use interface endpoints for
relevant services in each VPC. Access is localized and security
policies and performance are scoped and consumed by a single VPC.
It is important to consider that costs and operational complexity
will rise with each additional VPC deployed.

Gateway VPC endpoints are available for Amazon S3 and Amazon DynamoDB and are recommended when accessing these services from
within a VPC. Gateway VPC endpoints offer a more cost-effective
alternative than the equivalent interface endpoints. For example,
Gateway VPC endpoints don’t have an associated data transfer or
per-hour fee. Access to Gateway VPC endpoints is not directly
accessible from your on-premises network and will require a proxy
farm infrastructure to enable network connectivity.

A well-planned DNS strategy can help avoid complications as your
AWS environments grow. If you maintain on-premises DNS
capabilities, we recommend you design
[hybrid
DNS architectures](../../../prescriptive-guidance/latest/patterns/set-up-integrated-dns-resolution-for-hybrid-networks-in-amazon-route-53.md "../../../prescriptive-guidance/latest/patterns/set-up-integrated-dns-resolution-for-hybrid-networks-in-amazon-route-53.md") that use on-premises DNS infrastructure
along with
[Route 53](https://aws.amazon.com/route53/ "https://aws.amazon.com/route53/")
for any AWS based DNS requirements. Integrate DNS resolution with
on-premises DNS environments using Route 53 Resolver Endpoints and
[Forwarding
rules](../../../Route53/latest/DeveloperGuide/resolver-rules-managing.md "../../../Route53/latest/DeveloperGuide/resolver-rules-managing.md"). Use private hosted zones to hold information about
how you want Amazon Route 53 to respond to DNS queries for a
domain and its subdomains within one or more VPCs that you create
with the Amazon VPC service. Establish distributed management of
your
[private
hosted zones](../../../Route53/latest/DeveloperGuide/hosted-zone-private-associate-vpcs.md "../../../Route53/latest/DeveloperGuide/hosted-zone-private-associate-vpcs.md") by using Route 53 to associate your hosted
zone to VPCs across your AWS accounts and Regions.

## Establish network security

Securing your AWS network must align to your overall security
strategy and follow the recommendations in the
[Well-Architected
security pillar](../security-pillar/welcome.md "../security-pillar/welcome.md"). Understanding the risks that you’re
mitigating will help you apply appropriate network security
controls for specific traffic flows. For instance, the
[Security
Reference Architecture](../../../prescriptive-guidance/latest/security-reference-architecture/architecture.md "../../../prescriptive-guidance/latest/security-reference-architecture/architecture.md") recommends a centralized network
account that isolates inbound, outbound, and inspection VPCs.
Network security should be designed to protect connectivity
between your on-premises network and your AWS environment, to and
from the internet, and across your AWS environments.

[AWS Shield](https://aws.amazon.com/shield/ "https://aws.amazon.com/shield/") is a managed Distributed Denial of Service (DDoS)
protection service that safeguards internet facing applications
running on AWS and is offered in two tiers: standard and advanced.
The standard plan, available to all AWS customers, is included for
all tenants and defends against the most common, frequently
occurring network and transport-layer DDoS attacks that target
sites and applications. AWS Shield Advanced includes features such
as additional capacity for large DDoS events, native integration
with AWS WAF controls, historical reporting, assistance from the
AWS DDoS Response Team, and some cost protection for charges
incurred during an attack.

Configure
[Amazon VPC Security Groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") to allow specific inbound and outbound
traffic. In addition to security groups, you can also configure
[stateless
network ACLs](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md") (NACLs) that operate at the subnet boundary.
Configure security groups with more granular rules to govern
access to specific applications or services. Use NACLs when
security requirements require traffic be governed for an entire
subnet.

Implement web application firewalls to help protect external
facing web applications and APIs against common bugs and bots.
These solutions can help block malicious application attacks like
SQL injection, cross-site scripting (XSS), and others. These may
include common threats such as OWASP Top 10 security risks,
Content Management Systems specific threats, or emerging Common
Vulnerabilities and Exposures (CVE). AWS Solutions also provides
templates and patterns in
[AWS WAF Security Automations](https://aws.amazon.com/solutions/implementations/aws-waf-security-automations "https://aws.amazon.com/solutions/implementations/aws-waf-security-automations"), and centralized
[AWS WAF and VPC Security Group Management](https://aws.amazon.com/solutions/implementations/aws-centralized-waf-and-vpc-security-group-management/ "https://aws.amazon.com/solutions/implementations/aws-centralized-waf-and-vpc-security-group-management/") to assist you in the
deployment of AWS WAF controls in an automated manner.

Select
[deployment
models supported by AWS Network Firewall](https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/ "https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/") that meet your
specific use case. For each deployment model, you can have
AWS Network Firewall chained together with other services (service
chaining). For example, you can
[chain
AWS Network Firewall](https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/ "https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/") and NAT gateway. Extend your security
architecture as you scale to enable
[Amazon Route 53 Resolver DNS Firewall](../../../Route53/latest/DeveloperGuide/resolver-dns-firewall.md "../../../Route53/latest/DeveloperGuide/resolver-dns-firewall.md") to block DNS queries made
for known malicious domains and to allow queries for trusted
domains. Adopt centralized management through AWS Firewall Manager
to streamline operations across your multi-account framework. Save
time by automating the process of provisioning a centralized AWS
Network Firewall to inspect traffic between your Amazon VPCs with
[AWS Network Firewall Deployment Automations for AWS Transit
Gateway](https://aws.amazon.com/solutions/implementations/aws-network-firewall-deployment-automations-for-aws-transit-gateway/ "https://aws.amazon.com/solutions/implementations/aws-network-firewall-deployment-automations-for-aws-transit-gateway/").

Consolidating AWS Partner virtual appliances with Gateway Load
Balancer can reduce operational overhead and cost. Implement and
consolidate AWS Partner security solutions such as intrusion
detection and prevention, next-generation firewalls, and web
application firewalls.

## Establish network monitoring

Although network constructs are unique, you should pair network
monitoring with the full breadth of your observability
implementation, including specifying network metrics captured in
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/"). For visibility into traffic patterns of your
VPC, use
[Amazon VPC Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md"). VPC Flow Logs provide metadata (IP
addresses, ports, number of bytes transferred, etc.) about the
networking flows (to and from interfaces) in your VPC. Collect VPC
Flow Logs in a centralized S3 bucket for use with other log
aggregation and analytics functions. When you need to perform
content inspection, threat monitoring or troubleshooting, you can
copy network traffic to specific monitoring appliances. For
example, to capture the full packets, not just the metadata, use
Amazon
[VPC
Traffic Mirroring](../../../vpc/latest/mirroring/what-is-traffic-mirroring.md "../../../vpc/latest/mirroring/what-is-traffic-mirroring.md") to replicate all traffic, or specific
flows from an elastic network interface, to the destination of
your choice.

Automate the monitoring of your AWS networks and identify where
network access to your environments may be misconfigured by
implementing tools like
[VPC
Reachability Analyzer](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md") and
[Amazon Inspector Network Reachability](../../../inspector/latest/userguide/inspector_network-reachability.md "../../../inspector/latest/userguide/inspector_network-reachability.md") from the
[AWS Provable Security initiative](https://aws.amazon.com/security/provable-security/ "https://aws.amazon.com/security/provable-security/"). These tools let you implement
detailed network security checks without having to install
scanners and send packets. This will reduce complexity by
providing automated monitoring and create a more efficient review
process, especially across VPC peering connections and VPNs.
