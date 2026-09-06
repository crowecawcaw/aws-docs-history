

# AWS PrivateLink for AWS Organizations
<a name="orgs_security_privatelink"></a>

With AWS PrivateLink for AWS Organizations, you can access the AWS Organizations service from within the Virtual Private Cloud (VPC) without having to cross the public internet.

Amazon VPC lets you launch AWS resources in a custom virtual network. You can use a VPC to control your network settings, such as the IP address range, subnets, route tables, and network gateways. For more information about VPCs, see the [*Amazon VPC User Guide*](https://docs.aws.amazon.com/vpc/latest/userguide/).

To connect your Amazon VPC to AWS Organizations, you must first define an interface VPC endpoint (interface endpoints). Interface endpoints are represented by one or more elastic network interfaces (ENIs) that are assigned private IP addresses from subnets in your VPC. Requests from your VPC to AWS Organizations over interface endpoints stay on the Amazon network.

For general information about interface endpoints, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#vpce-interface-limitations) in the *Amazon VPC User Guide*.

**Topics**
+ [Limitations and restrictions of AWS PrivateLink for AWS Organizations](#limits-restrictions-privatelink)
+ [Creating a VPC endpoint](create-vpc-endpoint.md)
+ [Creating a VPC endpoint policy](create-vpc-endpoint-policy.md)

## Limitations and restrictions of AWS PrivateLink for AWS Organizations
<a name="limits-restrictions-privatelink"></a>

VPC limitations apply to AWS PrivateLink for AWS Organizations. For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#vpce-interface-limitations) and [AWS PrivateLink quotas](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-limits-endpoints.html) in the *Amazon VPC User Guide*. In addition, the following restrictions apply:

**Note**  
AWS Organizations is a global service. You can create an interface VPC endpoint for AWS Organizations only in the Region where the AWS Organizations control plane is located. In commercial AWS Regions, the control plane is located in US East (N. Virginia) (us-east-1). AWS Organizations also supports interface VPC endpoints in the AWS China (Ningxia) Region and the AWS GovCloud (US-West) Region. If your VPC is in a different Region from the control plane Region, you must use AWS Transit Gateway to access the AWS Organizations interface VPC endpoint from another Region. For more information, see [Creating a VPC endpoint for AWS Organizations](create-vpc-endpoint.md).
+ AWS PrivateLink for AWS Organizations does not support Transport Layer Security (TLS) 1.1.