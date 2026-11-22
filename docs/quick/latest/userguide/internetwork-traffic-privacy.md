

# Inter-network traffic privacy in AWS Quick

To use AWS Quick, users need access to the internet. They also need access to a compatible browser or a mobile device with the AWS Quick mobile app installed. They don't need access to the data sources they want to analyze. This access is handled inside AWS Quick. User connections to AWS Quick are protected through the use of SSL. So that users can access AWS Quick, allow access to HTTPS and Web Sockets Secure (wss://) protocol. 

You can use a Microsoft AD connector and single sign-on (IAM Identity Center) in a corporate network environment. You can further restrict access through the identity provider. Optionally, you can also use MFA. 

AWS Quick accesses data sources by using connection information supplied by the data source owner in AWS Quick. Connections are protected both between AWS Quick and on-premises applications and between AWS Quick and other AWS resources within the same AWS Region. For connections to any source, the data source must allow connections from AWS Quick. 

## Traffic between service and on-premises clients and applications
<a name="internetwork-traffic-privacy-between-qs-and-and-on-premises"></a>

You have two connectivity options between your private network and AWS: 
+ An AWS Site-to-Site VPN connection. For more information, see [What is AWS site-to-site VPN?](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
+ An Direct Connect connection. For more information, see [What is AWS direct connect?](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) 

If you are using AWS API operations to interact with AWS Quick through the network, clients must support Transport Layer Security (TLS) 1.2 or later. Clients must also support cipher suites with Perfect Forward Secrecy (PFS), such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve Diffie-Hellman Ephemeral (ECDHE). Most modern systems such as Java 7 and later support these modes. You must sign requests using an access key ID and a secret access key that are associated with an IAM principal, or you can use the [AWS Security Token Service (STS)](https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html) to generate temporary security credentials to sign requests. 

## Traffic between AWS resources in the same region
<a name="internetwork-traffic-privacy-between-qs-and-and-aws"></a>

An Amazon Virtual Private Cloud (Amazon VPC) endpoint for AWS Quick is a logical entity within a VPC that allows connectivity only to AWS Quick. The VPC routes requests to AWS Quick and routes responses back to the VPC. For more information, see the following:
+ [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html) in the *Amazon VPC User Guide*
+ [Connecting to a Amazon VPC with AWS Quick](https://docs.aws.amazon.com/quicksight/latest/user/working-with-aws-vpc.html)