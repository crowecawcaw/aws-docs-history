# Using AWS Config with Interface Amazon VPC Endpoints

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a private
connection between your VPC and AWS Config. You can use this connection to communicate with AWS Config
from your VPC without going through the public internet.

Amazon VPC is an AWS service that you can use to launch AWS resources in a virtual network
that you define. With a VPC, you have control over your network settings, such the IP
address range, subnets, route tables, and network gateways. Interface VPC endpoints are
powered by AWS PrivateLink, an AWS technology that enables private communication between
AWS services using an elastic network interface with private IP addresses. To connect your
VPC to AWS Config, you define an _interface VPC endpoint_ for AWS Config. This type
of endpoint enables you to connect your VPC to AWS services. The endpoint provides
reliable, scalable connectivity to AWS Config without requiring an internet gateway, network
address translation (NAT) instance, or VPN connection. For more information, see [What is Amazon VPC](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md") in the
_Amazon VPC User Guide_.

The following steps are for users of Amazon VPC. For more information, see [Getting Started](../../../vpc/latest/userguide/GetStarted.md "../../../vpc/latest/userguide/GetStarted.md") in the
_Amazon VPC User Guide_.
