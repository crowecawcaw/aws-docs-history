# Dual-stack endpoint support

AWS Private Certificate Authority provides a dual-stack public endpoint that supports both IPv4 and IPv6
clients. A dual-stack endpoint enables clients to communicate with AWS Private CA using
either IPv4 or IPv6 addresses. AWS Private CA for Active Directory and AWS Private CA Connector for SCEP also
support dual-stack endpoints.

The AWS Private CA dual-stack public endpoint at
`https://acm-pca.`your-region`.api.aws`
supports both IPv4 and IPv6 clients. AWS Private CA is also privately accessible over IPv4
and IPv6 from your virtual private cloud (VPC) using AWS PrivateLink. For more
information about creating private interface VPC endpoints for AWS Private CA, see [AWS Private CA VPC endpoints (AWS PrivateLink)](vpc-endpoints.md "vpc-endpoints.md").

For more information, see the following resources:

- [IP addressing for your
  VPCs and subnets](../../../vpc/latest/userguide/vpc-ip-addressing.md "../../../vpc/latest/userguide/vpc-ip-addressing.md")
- [IPv6 support for your
  VPC](../../../vpc/latest/userguide/vpc-migrate-ipv6.md "../../../vpc/latest/userguide/vpc-migrate-ipv6.md")
