# VPC endpoints for AWS IoT SiteWise

An _interface VPC endpoint_ establishes a private connection between your
virtual private cloud (VPC) and AWS IoT SiteWise. [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/") powers interface endpoints, enabling private access to AWS IoT SiteWise
API operations. AWS IoT SiteWise supports both IPv4 and IPv6 (dual-stack) through its interface
endpoints. You can bypass the need for an internet gateway, NAT device, VPN connection, or
AWS Direct Connect. Instances in your VPC don't need public IP addresses to communicate with
AWS IoT SiteWise API operations. Traffic between your VPC and AWS IoT SiteWise doesn't leave the AWS
network.

Each interface endpoint is represented by one or more [elastic network interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

Before you set up an interface VPC endpoint for AWS IoT SiteWise, review the [Access an
AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the _AWS PrivateLink Guide_.
