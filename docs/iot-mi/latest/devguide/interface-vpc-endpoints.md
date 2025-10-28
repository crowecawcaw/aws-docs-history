# Use managed integrations with interface VPC endpoints

You can establish a private connection between your Amazon VPC and AWS IoT Managed integrations by creating an interface Amazon VPC endpoint.
Interface endpoints are powered by AWS PrivateLink, a technology that enables you to privately access services by using private IP addresses. AWS PrivateLink restricts all network traffic between your VPC and IoT Managed Integrations to the Amazon network. You don't need an internet gateway, NAT device, or VPN connection.

You are not required to use AWS PrivateLink, but it's recommended. For more information about AWS PrivateLink and
VPC endpoints, see
[Accessing AWS services through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the _AWS PrivateLink Guide_.

###### Topics

- [Considerations for AWS IoT Managed integrations VPC endpoints](vpc-endpoints-considerations.md "vpc-endpoints-considerations.md")
- [Creating an interface VPC endpoint for AWS IoT Managed integrations](vpc-endpoints-creating.md "vpc-endpoints-creating.md")
- [Testing your VPC endpoint](vpc-endpoints-testing.md "vpc-endpoints-testing.md")
- [Controlling access to services over VPC endpoints](vpc-endpoints-access-control.md "vpc-endpoints-access-control.md")
- [Pricing](vpc-endpoints-pricing.md "vpc-endpoints-pricing.md")
- [Limitations](vpc-endpoints-limitations.md "vpc-endpoints-limitations.md")
