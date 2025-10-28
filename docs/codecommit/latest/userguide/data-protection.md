AWS CodeCommit is no longer available to new customers. Existing customers of
AWS CodeCommit can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider "https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider")

# Data protection in AWS CodeCommit

As a managed service, is protected by AWS global network security. For
information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
environment using the best practices for infrastructure security, see [Infrastructure
Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.
  CodeCommit repositories are automatically encrypted at rest. No customer action is required.
  CodeCommit also encrypts repository data in transit. You can use either the HTTPS protocol, the SSH
  protocol, or both with CodeCommit repositories. For more information, see [Setting up for AWS CodeCommit](setting-up.md "setting-up.md"). You can also configure [cross-account access](cross-account.md "cross-account.md") to CodeCommit repositories.

###### Topics

- [AWS Key Management Service and encryption for AWS CodeCommit repositories](encryption.md "encryption.md")
- [Connecting to AWS CodeCommit repositories with rotating credentials](temporary-access.md "temporary-access.md")
