# Infrastructure security in AWS Cloud Map

As a managed service, AWS Cloud Map is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS environment using the best practices for infrastructure security, see
 [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html "https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html") in *Security Pillar AWS Well‐Architected Framework*.

You use AWS published API calls to access AWS Cloud Map through the network. 
 Clients must support the following:


* Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
* Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
 Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
 such as Java 7 and later support these modes.
Additionally, requests must be signed by using
 an access key ID and a secret access key that is associated with an IAM principal. Or you
 can use the [AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html "https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html") (AWS STS) to generate temporary security credentials to sign requests.

You can improve the security posture of your VPC by configuring AWS Cloud Map to use an interface
 VPC endpoint. For more information, see [Access AWS Cloud Map using an interface endpoint
 (AWS PrivateLink)](vpc-interface-endpoints.md "vpc-interface-endpoints.md").
