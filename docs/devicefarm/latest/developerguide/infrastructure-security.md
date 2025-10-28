# Infrastructure security in AWS Device Farm

As a managed service, AWS Device Farm is protected by the AWS global network security. For information about
AWS security services and how AWS protects infrastructure, see [AWS
Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS environment using the best practices for infrastructure security,
see [Infrastructure Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access Device Farm through the network. Clients must support the
following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE
  (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these
  modes.
  Additionally, requests must be signed by using an access key ID and a secret access key that is associated with
  an IAM principal. Or you can use the [AWS Security Token Service](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") (AWS STS) to generate temporary security credentials to sign requests.

## Infrastructure security for physical device

testing

Devices are physically separated during physical device testing. Network isolation prevents cross-device
communication over wireless networks.

Public devices are shared, and Device Farm makes a best-effort attempt at keeping devices safe over time. Certain
actions, such as attempts to acquire complete administrator rights on a device (a practice referred to as
_rooting_ or _jailbreaking_), cause public
devices to become quarantined. They are removed from the public pool automatically and placed into manual
review.

Private devices are accessible only by AWS accounts explicitly authorized to do so. Device Farm physically
isolates these devices from other devices and keeps them on a separate network.

On privately managed devices, tests can be configured to use an Amazon VPC endpoint to secure connections in and
out of your AWS account.

## Infrastructure security for desktop browser

testing

When you use the desktop browser testing feature, all test sessions are separated from one another. Selenium
instances cannot cross-communicate without an intermediate third party, external to AWS.

All traffic to Selenium WebDriver controllers must be made through the HTTPS endpoint generated with
`createTestGridUrl`.

You are responsible for making sure that each Device Farm test instance has secure access to resources it tests. By default, Device Farm's desktop browser testing instances have access to the public internet. When you attach your instance to a VPC, it behaves like any other EC2 instance, with access to resources determined by the VPC's configuration and its associated networking components. AWS provides [security groups](../../../vpc/latest/userguide/vpc-security-groups.md "../../../vpc/latest/userguide/vpc-security-groups.md") and [network Access Control Lists (ACLs)](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md") to increase security in your VPC. Security groups control inbound and outbound traffic for your resources, and network ACLs control inbound and outbound traffic for your subnets. Security groups provide enough access control for most subnets. You can use network ACLs if you want an additional layer of security for your VPC. For general guidelines on security best practices when using Amazon VPCs, see [security best practices](../../../vpc/latest/userguide/vpc-security-best-practices.md "../../../vpc/latest/userguide/vpc-security-best-practices.md") for your VPC in the *Amazon Virtual Private Cloud User Guide*.
