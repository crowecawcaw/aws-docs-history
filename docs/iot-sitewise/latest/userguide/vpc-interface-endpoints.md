

# VPC endpoints for AWS IoT SiteWise
<a name="vpc-interface-endpoints"></a>

An *interface VPC endpoint* establishes a private connection between your virtual private cloud (VPC) and AWS IoT SiteWise. [AWS PrivateLink](https://aws.amazon.com/privatelink/) powers interface endpoints, enabling private access to AWS IoT SiteWise API operations. AWS IoT SiteWise supports both IPv4 and IPv6 (dual-stack) through its interface endpoints. You can bypass the need for an internet gateway, NAT device, VPN connection, or AWS Direct Connect. Instances in your VPC don't need public IP addresses to communicate with AWS IoT SiteWise API operations. Traffic between your VPC and AWS IoT SiteWise doesn't leave the AWS network.

Each interface endpoint is represented by one or more [elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets. 

Before you set up an interface VPC endpoint for AWS IoT SiteWise, review the [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *AWS PrivateLink Guide*. 