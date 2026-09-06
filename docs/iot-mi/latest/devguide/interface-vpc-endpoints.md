

# Use Managed Integrations with interface VPC endpoints
<a name="interface-vpc-endpoints"></a>

You can establish a private connection between your Amazon VPC and AWS IoT Managed Integrations by creating an interface Amazon VPC endpoint. Interface endpoints are powered by AWS PrivateLink, a technology that enables you to privately access services by using private IP addresses. AWS PrivateLink restricts all network traffic between your VPC and IoT Managed Integrations to the Amazon network. You don't need an internet gateway, NAT device, or VPN connection.

You are not required to use AWS PrivateLink, but it's recommended. For more information about AWS PrivateLink and VPC endpoints, see [ Accessing AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) in the *AWS PrivateLink Guide*. 

**Topics**
+ [Considerations for AWS IoT Managed Integrations VPC endpoints](vpc-endpoints-considerations.md)
+ [Creating an interface VPC endpoint for AWS IoT Managed Integrations](vpc-endpoints-creating.md)
+ [Testing your VPC endpoint](vpc-endpoints-testing.md)
+ [Controlling access to services over VPC endpoints](vpc-endpoints-access-control.md)
+ [Pricing](vpc-endpoints-pricing.md)
+ [Limitations](vpc-endpoints-limitations.md)