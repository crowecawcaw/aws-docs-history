# Securing Amazon SNS traffic with VPC

endpoints

An Amazon Virtual Private Cloud (Amazon VPC) endpoint for Amazon SNS is a logical entity within a VPC that allows
connectivity only to Amazon SNS. The VPC routes requests to Amazon SNS and routes responses back to the
VPC. The following sections provide information about working with VPC endpoints and creating
VPC endpoint policies.

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a private
connection between your VPC and Amazon SNS. With this connection, you can publish messages to your
Amazon SNS topics without sending them through the public internet.

Amazon VPC is an AWS service that you can use to launch AWS resources in a virtual network
that you define. With a VPC, you have control over your network settings, such the IP address
range, subnets, route tables, and network gateways. To connect your VPC to Amazon SNS, you define an
_interface VPC endpoint_. This type of endpoint enables you
to connect your VPC to AWS services. The endpoint provides reliable, scalable connectivity to
Amazon SNS without requiring an internet gateway, network address translation (NAT) instance, or VPN
connection. For more information, see [Access an AWS service using an interface VPC endpoint](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User Guide_.

The information in this section is for users of Amazon VPC. For more information, and to get
started with creating a VPC, see [Plan your VPC](../../../vpc/latest/userguide/vpc-getting-started.md "../../../vpc/latest/userguide/vpc-getting-started.md") in the _Amazon VPC User Guide_.

###### Note

VPC endpoints don't allow you to subscribe an Amazon SNS topic to a private IP address.
