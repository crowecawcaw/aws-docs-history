# Security in AWS Transfer Family

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a
data center and network architecture that is built to meet the requirements of the most
security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
describes this as security _of_ the cloud and security
_in_ the cloud:

To learn whether an AWS service is within the scope of specific compliance programs, see
[AWS services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/") and choose the compliance program that you are
interested in. For general information, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/").

You can download third-party audit reports using AWS Artifact. For more
information, see [Downloading Reports in AWS Artifact](../../../artifact/latest/ug/downloading-documents.md "../../../artifact/latest/ug/downloading-documents.md").

Your compliance responsibility when using AWS services is determined by the sensitivity
of your data, your company's compliance objectives, and applicable laws and
regulations. For more information about your compliance responsibility when using AWS services, see
[AWS Security Documentation](../../../security.md "../../../security.md").

This documentation helps you understand how to apply the shared responsibility model when
using AWS Transfer Family. The following topics show you how to configure AWS Transfer Family to meet your
security and compliance objectives. You also learn how to use other AWS services that help
you to monitor and secure your AWS Transfer Family resources.

We offer a workshop that provides prescriptive guidance and a hands on lab on how you can build
a scalable and secure file transfer architecture on AWS without needing to modify existing applications or manage server infrastructure.
You can view the details for this workshop
[here](https://catalog.workshops.aws/basic-security-workshop-transfer-family/en-US "https://catalog.workshops.aws/basic-security-workshop-transfer-family/en-US").

###### Topics

- [VPC connectivity security benefits](#vpc-connectivity-security "#vpc-connectivity-security")
- [Security policies for AWS Transfer Family servers](security-policies.md "security-policies.md")
- [Security policies for AWS Transfer Family SFTP
  connectors](security-policies-connectors.md "security-policies-connectors.md")
- [Using hybrid post-quantum key exchange with
  AWS Transfer Family](post-quantum-security-policies.md "post-quantum-security-policies.md")
- [Data protection and encryption](encryption-at-rest.md "encryption-at-rest.md")
- [Managing SSH and PGP keys in Transfer Family](key-management.md "key-management.md")
- [Identity and access management for AWS Transfer Family](security-iam.md "security-iam.md")
- [Compliance validation for AWS Transfer Family](transfer-compliance.md "transfer-compliance.md")
- [Resilience in AWS Transfer Family](disaster-recovery-resiliency.md "disaster-recovery-resiliency.md")
- [Create a private connection between a VPC and AWS Transfer Family
  APIs](vpc-api-endpoints.md "vpc-api-endpoints.md")
- [Infrastructure security in AWS Transfer Family](infrastructure-security.md "infrastructure-security.md")
- [Add a web application firewall](web-application-firewall.md "web-application-firewall.md")
- [Cross-service confused deputy prevention](confused-deputy.md "confused-deputy.md")
- [AWS managed policies for AWS Transfer Family](security-iam-awsmanpol.md "security-iam-awsmanpol.md")

## VPC connectivity security benefits

SFTP connectors with VPC egress type provide enhanced security benefits through
Cross-VPC Resource Access:

- **Network isolation**: All traffic remains within
  your VPC environment, providing complete network isolation from the public
  internet for private endpoint connections.
- **Source IP control**: Remote SFTP servers only
  see IP addresses from your VPC CIDR range, giving you full control over the
  source IP addresses used for connections.
- **Private endpoint access**: Connect directly to
  SFTP servers in your VPC using private IP addresses, eliminating exposure to the
  public internet.
- **Hybrid connectivity**: Securely access
  on-premises SFTP servers through established VPN or Direct Connect connections
  without additional internet exposure.
- **VPC security controls**: Leverage existing VPC
  security groups, NACLs, and routing policies to control and monitor SFTP
  connector traffic.

### VPC Lattice security model

VPC connectivity for SFTP connectors uses AWS VPC Lattice with service networks
to provide secure multi-tenant access:

- **Confused deputy prevention**:
  Authentication and authorization checks ensure that connectors can only
  access the specific resources they are configured for, preventing
  unauthorized cross-tenant access.
- **IPv6-only service network**: Uses IPv6
  addressing to avoid potential IP address conflicts and enhance security
  isolation.
- **Forward Access Session (FAS)**: Temporary
  credential handling eliminates the need for long-term credential storage or
  manual resource sharing.
- **Resource-level access control**: Each
  connector is associated with a specific Resource Configuration, ensuring
  granular access control to individual SFTP servers.

### Security best practices for VPC

connectivity

When using VPC egress type connectors, follow these security best
practices:

- **Security groups**: Configure security
  groups to allow SFTP traffic (port 22) only between necessary resources.
  Restrict source and destination IP ranges to the minimum required.
- **Resource Gateway placement**: Deploy
  Resource Gateways in private subnets when possible, and ensure they span at
  least two Availability Zones for high availability.
- **Network monitoring**: Use VPC Flow Logs and
  Amazon CloudWatch to monitor network traffic patterns and detect anomalous
  activity.
- **Access logging**: Enable connector logging
  to track file transfer activities and maintain audit trails for compliance
  requirements.
- **Resource Configuration management**:
  Regularly review and update Resource Configurations to ensure they point to
  the correct SFTP servers and use appropriate network settings.
