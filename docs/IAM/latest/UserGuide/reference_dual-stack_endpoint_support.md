# Dual-stack endpoint support

IAM provides a dual-stack public endpoint that supports both IPv4 and IPv6 clients. A
dual-stack endpoint enables clients to communicate with IAM using either IPv4 or IPv6
addresses.

The IAM dual-stack public endpoint at `https://iam.global.api.aws` supports both IPv4 and IPv6
clients. The IAM dual-stack public endpoint can also be accessed privately from your
virtual private cloud (VPC) using AWS PrivateLink. For more information about creating private
interface VPC endpoints for IAM, see [Create a VPC endpoint for IAM](reference_iam_vpc_endpoint_create.md "reference_iam_vpc_endpoint_create.md").

The IAM public endpoint at `https://iam.amazonaws.com`, unlike the dual-stack
public endpoint, supports only IPv4 clients. When accessed privately from your VPC using
AWS PrivateLink, the IAM public endpoint can support both IPv4 and IPv6 clients.

For more information about IPv6 addressing for your VPCs, see [IP addressing for your VPCs and
subnets](../../../vpc/latest/userguide/vpc-ip-addressing.md "../../../vpc/latest/userguide/vpc-ip-addressing.md") in the _Amazon VPC User Guide_. For more
information about how to configure your VPC for dual-stack mode, see [IPv6 support for
your VPC](../../../vpc/latest/userguide/vpc-migrate-ipv6.md "../../../vpc/latest/userguide/vpc-migrate-ipv6.md") in the _Amazon VPC User Guide_.
