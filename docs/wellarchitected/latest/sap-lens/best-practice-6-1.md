# Best Practice 6.1 – Ensure that

security and auditing are built into the SAP network design

Protecting access to the network that hosts your SAP workloads is the first line of
defense against malicious activity. Evaluate your business requirements and the specific
SAP solution to determine the ports, protocols, and traffic patterns that need to be
enabled. Consider the security standards of your organization and the tools and patterns
available to simplify network design. Audit on a regular basis or as changes occur.

**Suggestion 6.1.1 – Understand network traffic flows for
SAP**

Start by understanding your traffic flows. Network traffic patterns for SAP workloads
can be categorized as inbound traffic, outbound traffic, and internal traffic. You should
identify whether the source and destination fall within your trusted network boundary to
assist with defining your rule sets.

In addition to known inbound traffic and outbound traffic flows such as user access
and interface connections, consider SAP-specific requirements, including connections to
SAP Support (via SAProuter) and SAP SaaS offerings that restrict access based on source IP
addresses.

For internal traffic, consider traffic between components and systems, as well as
AWS and shared services. Tools such as [VPC Flow
Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md") and [VPC Reachability Analyzer](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md") can help you understand traffic flows into and out of
your Amazon VPC.

For more details, refer to the following information:

- AWS Documentation: [Attack surface reduction](../../../whitepapers/latest/aws-best-practices-ddos-resiliency/attack-surface-reduction.md "../../../whitepapers/latest/aws-best-practices-ddos-resiliency/attack-surface-reduction.md")
- SAP Documentation: [TCP/IP Ports for
  All SAP Products](https://help.sap.com/viewer/ports "https://help.sap.com/viewer/ports")

**Suggestion 6.1.2 – Evaluate options to permit and restrict traffic
flows**

First, understand how you connect users and systems in your on-premises network to the
AWS account in which your SAP systems are running. This is covered in [Network-to-Amazon VPC connectivity options](../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md "../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md").

Two primary methods for controlling the flow of network traffic into and out of your
VPC include the use of [security
groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") and [network
access control lists](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md") (network ACL). A security group acts as a virtual firewall
at the EC2 instance level to control inbound and outbound traffic and is stateful. A
network ACL is an optional layer of security for your VPC that acts as a firewall for
controlling traffic in and out of one or more subnets, and — unlike security groups — a
network ACL is stateless.

Also consider the dependencies of network components outside of your VPC. This can
include external network components provided by AWS such as CloudWatch endpoints.
This also can include internet hosted services such as software repositories for operating
system patches.

In addition to the standard options in AWS, SAP itself provides additional network
security options, including the use of the [SAProuter](https://support.sap.com/content/dam/support/en_us/library/ssp/tools/connectivity-tools/saprouter/SAProuter.pdf "https://support.sap.com/content/dam/support/en_us/library/ssp/tools/connectivity-tools/saprouter/SAProuter.pdf"), the [SAP Web Dispatcher](https://help.sap.com/doc/7b5ec370728810148a4b1a83b0e91070/1610%20002/en-US/frameset.htm?488fe37933114e6fe10000000a421937.html "https://help.sap.com/doc/7b5ec370728810148a4b1a83b0e91070/1610%20002/en-US/frameset.htm?488fe37933114e6fe10000000a421937.html"), and SAP Gateway [network-based access control lists](https://help.sap.com/viewer/62b4de4187cb43668d15dac48fc00732/LATEST/en-US/d0a4956abd904c8d855ee9d368bc510b.html "https://help.sap.com/viewer/62b4de4187cb43668d15dac48fc00732/LATEST/en-US/d0a4956abd904c8d855ee9d368bc510b.html"). These work in tandem with AWS services and
configurations to permit or restrict network access to SAP systems.

For more details, refer to the following information:

- SAP on AWS Blog: [VPC Subnet Zoning Patterns for SAP on AWS](https://aws.amazon.com/blogs/awsforsap/vpc-subnet-zoning-patterns-for-sap-on-aws/ "https://aws.amazon.com/blogs/awsforsap/vpc-subnet-zoning-patterns-for-sap-on-aws/")
- Well-Architected Framework [Security]: [Infrastructure Protection – Protecting Networks](../security-pillar/protecting-networks.md "../security-pillar/protecting-networks.md")
- Well-Architected Framework [Management and Governance Cloud Environment Guide]: [Network Connectivity](../management-and-governance-guide/networkconnectivity.md "../management-and-governance-guide/networkconnectivity.md")
- SAP Documentation: [Network and Communication Security](https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/492f0050d5ac612fe10000000a44176d.html "https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/492f0050d5ac612fe10000000a44176d.html")

**Suggestion 6.1.3 – Use design guidelines and AWS tooling to
simplify network security**

SAP systems often have complex integration requirements, and the cloud offers
additional ways to simplify network security management. Consider the following
approaches:

- Avoid referring to individual IP addresses or IP ranges where possible to simplify
  management.
- Use a standard set of SAP system numbers across all your SAP workloads to reduce
  the range of network ports required.
- [AWS PrivateLink](../../../vpc/latest/userguide/endpoint-services-overview.md "../../../vpc/latest/userguide/endpoint-services-overview.md") removes the requirement for outbound internet access from your
  VPC to access AWS services such as Amazon S3 and CloudWatch. Where possible
  and not mandated by business requirements, you can prevent SAP traffic to and from
  these services from traversing the internet, routing all traffic through AWS
  managed network components.
- Simplify security groups by the use of [VPC
  Prefix Lists](../../../vpc/latest/userguide/managed-prefix-lists.md "../../../vpc/latest/userguide/managed-prefix-lists.md") and/or [security group rules](../../../AWSEC2/latest/UserGuide/security-group-rules.md "../../../AWSEC2/latest/UserGuide/security-group-rules.md") that reference other security groups rather than IP
  address ranges.
- Use automation to create, update, and manage security groups to avoid
  configuration drift.
- Consider the use of [AWS Firewall Manager](../../../waf/latest/developerguide/what-is-aws-waf.md#fms-intro "../../../waf/latest/developerguide/what-is-aws-waf.md#fms-intro") to provide centralized management of security groups across VPCs
  and AWS accounts.
- Consider the use of [SAProuter](https://support.sap.com/en/tools/connectivity-tools/saprouter.html "https://support.sap.com/en/tools/connectivity-tools/saprouter.html"), [SAP Web Dispatcher](https://help.sap.com/doc/7b5ec370728810148a4b1a83b0e91070/1610 002/en-US/frameset.htm?488fe37933114e6fe10000000a421937.html "https://help.sap.com/doc/7b5ec370728810148a4b1a83b0e91070/1610 002/en-US/frameset.htm?488fe37933114e6fe10000000a421937.html"), and Elastic Load Balancing to obfuscate the entry
  points to backend systems.
- Consider the use of multiple [SAP Internet Communication Manager (ICM)](https://help.sap.com/doc/d2ecfdfcaedc4e2ba46a99a6be7d5797/1610 002/en-US/frameset.htm#:~:text=The%20ICM%20is%20a%20component%20of%20the%20SAP%20NetWeaver%20Application%20Server.&text=The%20Internet%20Communication%20Manager%20ensures,processes%20requests%20from%20the%20Internet. "https://help.sap.com/doc/d2ecfdfcaedc4e2ba46a99a6be7d5797/1610 002/en-US/frameset.htm#:~:text=The%20ICM%20is%20a%20component%20of%20the%20SAP%20NetWeaver%20Application%20Server.&text=The%20Internet%20Communication%20Manager%20ensures,processes%20requests%20from%20the%20Internet.") entry points to provide finer
  grain access control.
- Consider [AWS Shield](https://aws.amazon.com/shield/ "https://aws.amazon.com/shield/"), a managed
  Distributed Denial of Service (DDoS) protection service, to safeguard applications
  running on AWS. Use to protect public-facing SAP Fiori or API endpoints.
- Consider [AWS WAF](https://aws.amazon.com/waf/ "https://aws.amazon.com/waf/"), a web
  application firewall that helps protect your web applications or APIs against common web
  exploits and bots that may affect availability, compromise security, or consume
  excessive resources. Use to protect public-facing user interfaces and APIs, for example,
  SAP Fiori applications.
  For more details, refer to the following information:

- SAP Documentation: [Network-based Access Control Lists](https://help.sap.com/viewer/62b4de4187cb43668d15dac48fc00732/LATEST/en-US/d0a4956abd904c8d855ee9d368bc510b.html "https://help.sap.com/viewer/62b4de4187cb43668d15dac48fc00732/LATEST/en-US/d0a4956abd904c8d855ee9d368bc510b.html")
- SAP Documentation: [TCP/IP Ports
  for All SAP Products](https://help.sap.com/viewer/ports "https://help.sap.com/viewer/ports")
