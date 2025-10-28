# Infrastructure security in AWS Transfer Family

As a managed service, AWS Transfer Family is protected by AWS global network security. For
information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
environment using the best practices for infrastructure security, see [Infrastructure
Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access AWS Transfer Family through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.

## Avoid placing NLBs and NATs in front of AWS Transfer Family

servers

###### Note

Servers configured with FTP and FTPS protocols only allow a configuration with a
VPC: there is no public endpoint available for FTP/FTPS.

Many customers configure a Network Load Balancer (NLB) to route traffic to their
AWS Transfer Family server. They typically do this either because they created their server before
AWS offered a way to access it from both inside their VPC and from the internet, or to
support FTP on the internet. This configuration not only increases costs for customers,
but can also cause other issues, which we describe in this section.

NAT gateways are a mandatory component when clients are connecting from a customer
private network behind a corporate firewall. However, you should be aware that when many
clients are behind the same NAT gateway, this can impact performance and connection
limits. If there's an NLB or NAT in the communication path from the client to the FTP or
FTPS server, the server can't accurately recognize the client's IP address, because
AWS Transfer Family sees only the IP address of the NLB or NAT.

If you're using the configuration of a Transfer Family server behind an NLB, we recommend that
you move to a VPC endpoint and use an Elastic IP address instead of using an NLB. When
using NAT gateways, be aware of the connection limitations described below.

If you're using the FTPS protocol, this configuration not only reduces your ability to
audit who's accessing your server, but it can also impact performance. AWS Transfer Family uses the
source IP address to shard your connections across our data plane. For FTPS, this means
that instead of having 10,000 simultaneous connections, Transfer Family servers with NLB or NAT
gateways on the communication route are limited to only 300 simultaneous
connections.

Although we recommend avoiding Network Load Balancers in front of AWS Transfer Family servers, if
your FTP or FTPS implementation requires an NLB or NAT in the communication route from
the client, follow these recommendations:

- For an NLB, use port 21 for health checks, instead of ports 8192-8200.
- For the AWS Transfer Family server, enable TLS session resumption by setting
  `TlsSessionResumptionMode = ENFORCED`.

###### Note

This is the recommended mode, as it provides enhanced security:

    + Requires clients to use TLS session resumption for subsequent
     connections.
    + Provides stronger security guarantees by ensuring consistent
     encryption parameters.
    + Helps prevent potential downgrade attacks.
    + Maintains compliance with security standards while optimizing
     performance.

- If possible, migrate away from using an NLB to take full advantage of AWS Transfer Family
  performance and connection limits.

For additional guidance on NLB alternatives, contact the AWS Transfer Family Product Management
team through AWS Support. For more information about improving your security posture,
see the blog post [Six tips to improve the security of your AWS Transfer Family server](https://aws.amazon.com/blogs/security/six-tips-to-improve-the-security-of-your-aws-transfer-family-server/ "https://aws.amazon.com/blogs/security/six-tips-to-improve-the-security-of-your-aws-transfer-family-server/").

## VPC connectivity

infrastructure security

SFTP connectors with VPC egress type provide enhanced infrastructure security through
network isolation and private connectivity:

### Network isolation benefits

- **Private network traffic**: All connector
  traffic to private SFTP servers remains within your VPC, never traversing
  the public internet.
- **Controlled egress**: For public endpoints
  accessed via VPC, traffic routes through your NAT gateways, giving you
  control over egress IP addresses and network policies.
- **VPC security controls**: Leverage existing
  VPC security groups, network ACLs, and route tables to control connector
  network access.
- **Hybrid connectivity**: Access on-premises
  SFTP servers through established VPN or Direct Connect connections without
  additional internet exposure.

### Resource Gateway security

considerations

Resource Gateways provide secure ingress points for Cross-VPC Resource
Access:

- **Multi-AZ deployment**: Resource Gateways
  require subnets in at least two Availability Zones for high availability and
  fault tolerance.
- **Security group controls**: Configure
  security groups to restrict access to SFTP ports (typically port 22) from
  authorized sources only.
- **Private subnet placement**: Deploy Resource
  Gateways in private subnets when connecting to private SFTP servers to
  maintain network isolation.
- **Connection limits**: Each Resource Gateway
  supports up to 350 concurrent connections with a 350-second idle timeout for
  TCP connections.
