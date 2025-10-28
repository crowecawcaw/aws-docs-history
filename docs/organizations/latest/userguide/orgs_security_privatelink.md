# AWS PrivateLink for AWS Organizations

With AWS PrivateLink for AWS Organizations, you can access the AWS Organizations service
from within the Virtual Private Cloud (VPC) without having to cross the public
internet.

Amazon VPC lets you launch AWS resources in a custom virtual network. You can use a VPC to
control your network settings, such as the IP address range, subnets, route tables, and
network gateways. For more information about VPCs, see the [_Amazon VPC User Guide_](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md").

To connect your Amazon VPC to AWS Organizations, you must first define an interface VPC endpoint
(interface endpoints). Interface endpoints are represented by one or more elastic
network interfaces (ENIs) that are assigned private IP addresses from subnets in your VPC.
Requests from your VPC to AWS Organizations over interface endpoints stay on the Amazon
network.

For general information about interface endpoints, see [Access an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#vpce-interface-limitations "../../../vpc/latest/privatelink/create-interface-endpoint.md#vpce-interface-limitations") in the
_Amazon VPC User Guide_.

###### Topics

- [Limitations and restrictions of AWS PrivateLink for AWS Organizations](#limits-restrictions-privatelink "#limits-restrictions-privatelink")
- [Creating a VPC endpoint](create-vpc-endpoint.md "create-vpc-endpoint.md")
- [Creating a VPC endpoint policy](create-vpc-endpoint-policy.md "create-vpc-endpoint-policy.md")

## Limitations and restrictions of AWS PrivateLink for AWS Organizations

VPC limitations apply to AWS PrivateLink for AWS Organizations. For more information,
see [Access an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#vpce-interface-limitations "../../../vpc/latest/privatelink/create-interface-endpoint.md#vpce-interface-limitations") and [AWS PrivateLink quotas](../../../vpc/latest/privatelink/vpc-limits-endpoints.md "../../../vpc/latest/privatelink/vpc-limits-endpoints.md") in the _Amazon VPC User Guide_. In
addition, the following restrictions apply:

- Only available in the `us-east-1` region
- Doesn’t support Transport Layer Security (TLS) 1.1
