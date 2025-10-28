# Dual-stack endpoint support

AWS KMS provides a dual-stack public endpoint that supports both IPv4 and IPv6 clients. A
dual-stack endpoint enables clients to communicate with AWS KMS using either IPv4 or IPv6
addresses. For more information on the AWS KMS endpoints, see [AWS Key Management Service endpoints and quotas.](../../../general/latest/gr/kms.md "../../../general/latest/gr/kms.md")

The AWS KMS dual-stack public endpoint at
`https://kms.`your-region`.api.aws` supports both IPv4
and IPv6 clients. AWS KMS is also privately accessible over IPv4 and IPv6 from your virtual
private cloud (VPC) using AWS PrivateLink. For more information about creating private interface
VPC endpoints for AWS KMS, see [Connect to AWS KMS through a VPC endpoint](kms-vpc-endpoint.md "kms-vpc-endpoint.md").

For more information about IPv6 addressing for your VPCs, see [How Amazon VPC works](../../../vpc/latest/userguide/how-it-works.md#vpc-ip-addressing "../../../vpc/latest/userguide/how-it-works.md#vpc-ip-addressing") in the
_Amazon Virtual Private Cloud User Guide_. For more information about how to configure your
VPC for dual-stack mode, see [IP addressing for your VPCs and
subnets](../../../vpc/latest/userguide/vpc-ip-addressing.md#vpc-ipv6 "../../../vpc/latest/userguide/vpc-ip-addressing.md#vpc-ipv6") in the _Amazon Virtual Private Cloud User Guide_.

## Features not available over IPv6

AWS KMS cannot communicate over IPv6 with AWS CloudHSM key stores or External key stores. This
limitation does not prevent you from calling AWS KMS APIs over IPv6.
