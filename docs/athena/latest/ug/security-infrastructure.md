# Infrastructure security in Athena

As a managed service, Amazon Athena is protected by AWS global network security. For
information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
environment using the best practices for infrastructure security, see [Infrastructure
Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access Athena through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.
  Use IAM policies to restrict access to Athena operations. Whenever you use IAM policies, make sure that you follow IAM best practices. For more information, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

Athena [managed policies](managed-policies.md "managed-policies.md") are easy to use, and are
automatically updated with the required actions as the service evolves. Customer-managed and
inline policies allow you to fine tune policies by specifying more granular Athena actions
within the policy. Grant appropriate access to the Amazon S3 location of the data. For detailed
information and scenarios about how to grant Amazon S3 access, see [Example walkthroughs:
Managing access](../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access.md "../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access.md") in the _Amazon Simple Storage Service Developer
Guide_. For more information and an example of which Amazon S3 actions to allow,
see the example bucket policy in [Cross-Account
Access](cross-account-permissions.md "cross-account-permissions.md").

###### Topics

- [Connect to Amazon Athena using an interface VPC endpoint](interface-vpc-endpoint.md "interface-vpc-endpoint.md")
