

# Dual-stack endpoint support
<a name="ipv6-kms"></a>

AWS KMS provides a dual-stack public endpoint that supports both IPv4 and IPv6 clients. A dual-stack endpoint enables clients to communicate with AWS KMS using either IPv4 or IPv6 addresses. For more information on the AWS KMS endpoints, see [AWS Key Management Service endpoints and quotas.](https://docs.aws.amazon.com/general/latest/gr/kms.html)

The AWS KMS dual-stack public endpoint at `https://kms.{{your-region}}.api.aws` supports both IPv4 and IPv6 clients. AWS KMS is also privately accessible over IPv4 and IPv6 from your virtual private cloud (VPC) using AWS PrivateLink. For more information about creating private interface VPC endpoints for AWS KMS, see [Connect to AWS KMS through a VPC endpoint](kms-vpc-endpoint.md).

For more information about IPv6 addressing for your VPCs, see [How Amazon VPC works](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html#vpc-ip-addressing) in the *Amazon Virtual Private Cloud User Guide*. For more information about how to configure your VPC for dual-stack mode, see [IP addressing for your VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html#vpc-ipv6) in the *Amazon Virtual Private Cloud User Guide*.

## Features not available over IPv6
<a name="kms-ipv6-limitations"></a>

AWS KMS cannot communicate over IPv6 with AWS CloudHSM key stores or External key stores. This limitation does not prevent you from calling AWS KMS APIs over IPv6.