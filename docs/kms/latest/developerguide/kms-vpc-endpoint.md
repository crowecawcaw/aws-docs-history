

# Connect to AWS KMS through a VPC endpoint
<a name="kms-vpc-endpoint"></a>

You can connect directly to AWS KMS through a private interface endpoint in your virtual private cloud (VPC). When you use an interface VPC endpoint, communication between your VPC and AWS KMS is conducted entirely within the AWS network.

AWS KMS supports Amazon Virtual Private Cloud (Amazon VPC) endpoints powered by [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/). Each VPC endpoint is represented by one or more [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) (ENIs) with private IP addresses in your VPC subnets. 

The interface VPC endpoint connects your VPC directly to AWS KMS without an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. The instances in your VPC do not need public IP addresses to communicate with AWS KMS. 

**Regions**  
AWS KMS supports VPC endpoints and VPC endpoint policies in all AWS Regions in which [AWS KMS](https://docs.aws.amazon.com/general/latest/gr/kms.html) is supported.

**Considerations for AWS KMS VPC endpoints**  
Before you set up an interface VPC endpoint for AWS KMS, review the [Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#vpce-interface-limitations) topic in the *AWS PrivateLink Guide*.  
AWS KMS support for a VPC endpoint includes the following.  
+ You can use your VPC endpoint to call all [AWS KMS API operations](https://docs.aws.amazon.com/kms/latest/APIReference/API_Operations.html) from your VPC.
+ You can create an interface VPC endpoint that connects to an AWS KMS region endpoint or an [AWS KMS FIPS endpoint](https://docs.aws.amazon.com/general/latest/gr/kms.html).
+ You can use AWS CloudTrail logs to audit your use of KMS keys through the VPC endpoint. For details, see [Logging AWS KMS requests that use a VPC endpoint](vpce-logging.md).

**Topics**
+ [Create a VPC endpoint for AWS KMS](vpce-create-endpoint.md)
+ [Connect to an AWS KMS VPC endpoint](vpce-connect.md)
+ [Use VPC endpoints to control access to AWS KMS resources](vpce-policy-condition.md)
+ [Logging AWS KMS requests that use a VPC endpoint](vpce-logging.md)