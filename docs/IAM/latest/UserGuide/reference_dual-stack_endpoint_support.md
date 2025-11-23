# Dual-stack endpoint support

Dual-stack endpoints enable clients to communicate with AWS services using either IPv4
or IPv6 addresses. Both IAM and AWS STS provide dual-stack endpoint support. For more
information about how to configure your VPC for dual-stack mode, see [IPv6 support for
your VPC](../../../vpc/latest/userguide/vpc-migrate-ipv6.md "../../../vpc/latest/userguide/vpc-migrate-ipv6.md") in the _Amazon VPC User Guide_.

If you use IAM policies that include the `aws:sourceIp` or
`aws:vpcSourceIp` condition keys, you need to update these policies to
support IPv6 clients. For more information about IPv6 addressing for your VPCs, see [IP addressing for
your VPCs and subnets](../../../vpc/latest/userguide/vpc-ip-addressing.md "../../../vpc/latest/userguide/vpc-ip-addressing.md") in the _Amazon VPC User Guide_.

## IAM dual-stack endpoint

support

IAM provides a dual-stack public endpoint that supports both IPv4 and IPv6 clients.
The IAM dual-stack public endpoint can also be accessed privately from your virtual
private cloud (VPC) using AWS PrivateLink. For more information about creating private
interface VPC endpoints for IAM, see [Create a VPC endpoint for IAM](reference_iam_vpc_endpoint_create.md "reference_iam_vpc_endpoint_create.md").

The IAM dual-stack public endpoint is `https://iam.global.api.aws`.

The IAM public endpoint at `https://iam.amazonaws.com`, unlike the dual-stack
public endpoint, supports only IPv4 clients. When accessed privately from your VPC using
AWS PrivateLink, the IAM public endpoint can support both IPv4 and IPv6 clients.

## AWS STS dual-stack endpoint

support

AWS STS provides dual-stack regional endpoints that support both IPv4 and IPv6 clients.
The AWS STS dual-stack regional endpoints can also be accessed privately from your virtual
private cloud (VPC) using AWS PrivateLink. For more information about creating private
interface VPC endpoints for AWS STS, see [Create a VPC endpoint for AWS STS](reference_sts_vpc_endpoint_create.md "reference_sts_vpc_endpoint_create.md").

The following table shows the AWS STS dual-stack regional endpoints by partition:

| Partition                 | Dual-stack endpoint URL                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Commercial AWS Regions    | **Regular endpoints:**<br>`https://sts.`<region>`.api.aws`<br>**FIPS endpoints:**<br>`https://sts-fips.`<region>`.api.aws` |
| AWS GovCloud (US) Regions | **Regular endpoints:**<br>`https://sts.`<region>`.api.aws`                                                                 |
| China Regions             | **Regular endpoints:**<br>`https://sts.`<region>`.api.amazonwebservices.com.cn`                                            |

###### Note

FIPS endpoints only apply to US and Canada regions.

###### Limitations

The following limitations apply to AWS STS dual-stack endpoint support:

- IPv6 clients are not supported on the global endpoint
  `https://sts.amazonaws.com`. You must use dual-stack regional
  endpoints for IPv6 client support.
- IPv6-only AWS STS VPC endpoints are not supported. VPC endpoints can be
  configured for IPv4 or dual-stack connectivity.
