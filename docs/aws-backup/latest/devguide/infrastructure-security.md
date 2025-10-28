# Infrastructure security in AWS Backup

As a managed service, AWS Backup is protected by AWS global network security.
For more information about AWS security services and how AWS protects infrastructure,
see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your
AWS environment using the best practices for infrastructure security, see [Infrastructure protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md")
in _Security Pillar AWS Well‐Architected Framework_.

You use AWS published API calls to access AWS Backup through the network. Clients
must support Transport Layer Security (TLS) 1.2 or later.
Clients must also support cipher suites with perfect forward secrecy (PFS) such as Ephemeral
Diffie-Hellman (DHE) or Elliptic Curve Diffie-Hellman Ephemeral (ECDHE). Most modern systems
such as Java 7 and later support these modes.

Additionally, requests must be signed by using an access key ID and a secret access key
that is associated with an IAM principal. Or you can use the [AWS Security Token Service](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") (AWS STS) to generate temporary security
credentials to sign requests.
