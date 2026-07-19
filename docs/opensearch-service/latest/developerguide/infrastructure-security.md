# Infrastructure Security in Amazon OpenSearch Service

As a managed service, Amazon OpenSearch Service is protected by AWS global network security. For
information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
environment using the best practices for infrastructure security, see [Infrastructure
Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access OpenSearch Service through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.
  As a managed service, Amazon OpenSearch Service is protected by AWS global network security. For more
  information, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/").

You use AWS published API calls to access Amazon OpenSearch Service through the network.
To configure the minimum required TLS version for your domain, specify the
`TLSSecurityPolicy` value in the domain endpoint options:

```
aws opensearch update-domain-config --domain-name `my-domain` --domain-endpoint-options '{"TLSSecurityPolicy": "Policy-Min-TLS-1-2-2019-07"}'
```

For details, see the [AWS CLI command
reference](../../../cli/latest/reference/opensearch/update-domain-config.md "../../../cli/latest/reference/opensearch/update-domain-config.md").

Depending on your domain configuration, you might also need to sign requests to the
OpenSearch APIs. For more information, see [Making and signing OpenSearch Service requests](managedomains-signing-service-requests.md "managedomains-signing-service-requests.md").

OpenSearch Service supports public access domains, which can receive requests from any internet-connected
device, and [VPC access domains](vpc.md "vpc.md"), which are isolated from the public
internet.

If you enable the VPC egress option on a VPC domain, OpenSearch Service places requester-managed egress
ENIs in your subnets to carry egress traffic from the domain. For more information, see
[Routing domain egress traffic through your VPC](vpc-egress.md "vpc-egress.md").
