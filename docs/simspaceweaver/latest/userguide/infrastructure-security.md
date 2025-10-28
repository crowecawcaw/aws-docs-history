End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Infrastructure Security in AWS SimSpace Weaver

As a managed service, AWS SimSpace Weaver is protected by AWS global network security. For
information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
environment using the best practices for infrastructure security, see [Infrastructure
Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access SimSpace Weaver through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.

## Network connectivity security model

Your simulations run on compute instances within an Amazon VPC located within an AWS Region that you select.
An Amazon VPC is a virtual network in the AWS Cloud, which isolates infrastructure by workload or organizational
entity. Communications between compute instances within the Amazon VPC stay within the AWS network and don't
travel over the internet. Some internal service communication crosses the internet, and is encrypted.
Simulations for all customers running in the same AWS Region share the same Amazon VPC. Simulations for different
customers use separate compute instances within the same Amazon VPC.

Communications between your simulation clients and your simulations running in SimSpace Weaver travel over
the internet. SimSpace Weaver does not handle these connections. It is your responsibility to secure your
client connections.

Your connections to the SimSpace Weaver service cross the internet and are encrypted. This includes connections
using the AWS Management Console, AWS Command Line Interface (AWS CLI), AWS software development kits (SDK), and the SimSpace Weaver app SDK.
