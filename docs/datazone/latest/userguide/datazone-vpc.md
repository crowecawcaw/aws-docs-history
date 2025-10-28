# Using Interface VPC Endpoints for Amazon DataZone

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can
establish a connection between your Amazon VPC and Amazon DataZone. You can use this connection
with Amazon DataZone without crossing the public internet.

Amazon VPC lets you launch AWS resources in a custom virtual network. You can use a VPC
to control your network settings, such as the IP address range, subnets, route tables, and
network gateways. For more information about VPCs, see the [Amazon VPC
User Guide](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md").

To connect your Amazon VPC to Amazon DataZone, you must first define an interface VPC endpoint,
which lets you connect your VPC to other AWS services. The endpoint provides reliable,
scalable connectivity, without requiring an internet gateway, network address translation
(NAT) instance, or VPN connection. For more information and detailed steps on how to create a
VPC endpoint, see [Interface VPC Endpoints (AWS PrivateLink)](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the Amazon VPC User Guide.

###### Important

In VPC, an endpoint policy is a resource-based policy that you can attach to a VPC
endpoint to control which AWS principals can use the endpoint to access an AWS
service.

The current release of Amazon DataZone supports the use of endpoint policies for establishing
and using connections between your Amazon VPC and Amazon DataZone endpoints.
