# Infrastructure security in Amazon S3

As a managed service, Amazon S3 is protected by the AWS global network security procedures that
are described in the security pillar of the [AWS Well-Architected Framework](../../../wellarchitected/latest/security-pillar/welcome.md "../../../wellarchitected/latest/security-pillar/welcome.md").

Access to Amazon S3 via the network is through AWS published APIs. Clients must support
Transport Layer Security (TLS) 1.2. We recommend also supporting TLS 1.3 and hybrid
post-quantum key exchange. To learn about post-quantum cryptography at AWS, including
links to blog posts and research papers, see [Post-Quantum
Cryptography for AWS](https://aws.amazon.com/security/post-quantum-cryptography/ "https://aws.amazon.com/security/post-quantum-cryptography/").

###### Note

TLS 1.3 is supported in all S3 endpoints, except for AWS PrivateLink for Amazon S3 and Multi-Region Access Points.

Clients must also support cipher
suites with Perfect Forward Secrecy (PFS) such as Ephemeral Diffie-Hellman (DHE) or Elliptic
Curve Diffie-Hellman Ephemeral (ECDHE). Additionally, requests must be signed using AWS
Signature V4 or AWS Signature V2, requiring valid credentials to be provided.

These APIs are callable from any network location. However, Amazon S3 does support
resource-based access policies, which can include restrictions based on the source IP
address. You can also use Amazon S3 bucket policies to control access to buckets from specific
virtual private cloud (VPC) endpoints, or specific VPCs. Effectively, this isolates network access to
a given Amazon S3 bucket from only the specific VPC within the AWS network. For more
information, see [Controlling access from VPC
endpoints with bucket policies](example-bucket-policies-vpc-endpoint.md "example-bucket-policies-vpc-endpoint.md").

The following security best practices also address infrastructure security in Amazon S3:

- [Consider VPC endpoints for Amazon S3 access](security-best-practices.md#end-points "security-best-practices.md#end-points")
- [Identify and audit all your Amazon S3 buckets](security-best-practices.md#audit "security-best-practices.md#audit")
