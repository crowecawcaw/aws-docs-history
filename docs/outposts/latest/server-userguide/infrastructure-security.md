# Infrastructure security in AWS Outposts

As a managed service, AWS Outposts is protected by AWS global network security. For
information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
environment using the best practices for infrastructure security, see [Infrastructure
Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access AWS Outposts through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.
  For more information about the infrastructure security provided for the EC2 instances and
  EBS volumes running on your Outpost, see [Infrastructure Security in
  Amazon EC2](../../../AWSEC2/latest/UserGuide/infrastructure-security.md "../../../AWSEC2/latest/UserGuide/infrastructure-security.md").

VPC Flow Logs function the same way as they do in an AWS Region. This means that they can
be published to CloudWatch Logs, Amazon S3, or to Amazon GuardDuty for analysis. Data needs to be sent back to the
Region for publication to these services, so it is not visible from CloudWatch or other services
when the Outpost is in a disconnected state.
