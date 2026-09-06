

# AWS PrivateLink for Neptune Analytics
<a name="gettingStarted-connecting-private-link"></a>

 With AWS PrivateLink for Neptune Analytics, you can provision interface Amazon VPC endpoints (interface endpoints) in your virtual private cloud (Amazon VPC). These endpoints are directly accessible from applications that are on premises over VPN and AWS Direct Connect, or in a different AWS region over [Amazon VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html). Using AWS PrivateLink and interface endpoints, you can simplify private network connectivity from your applications to Neptune Analytics. 

 Applications in your VPC do not need public IP addresses to communicate with Neptune Analytics interface VPC endpoints for Neptune Analytics operations. Interface endpoints are represented by one or more elastic network interfaces (ENIs) that are assigned private IP addresses from subnets in your Amazon VPC. Requests to Neptune Analytics over interface endpoints stay on the Amazon network. You can also access interface endpoints in your Amazon VPC from on-premises applications through AWS Direct Connect or AWS Virtual Private Network (Site-to-Site VPN). For more information about how to connect your Amazon VPC with your on-premises network, see the [AWS Direct Connect user guide](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) and the [AWS Site-to-Site VPN user guide](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html). 

 For general information about interface endpoints, see [ Interface Amazon VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html) in the AWS PrivateLink guide. 

## Creating an Amazon VPC endpoint
<a name="gettingStarted-connecting-private-link-create"></a>

 To create an Amazon VPC interface endpoint, see [ Create an Amazon VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) in the AWS PrivateLink Guide. 

**Topics**
+ [Creating an Amazon VPC endpoint](#gettingStarted-connecting-private-link-create)
+ [Types of interface endpoint services for Neptune Analytics](gettingStarted-connecting-private-link-types.md)
+ [Considerations when using AWS PrivateLink for Neptune Analytics](gettingStarted-connecting-private-link-considerations.md)
+ [Accessing Neptune Analytics interface endpoints](gettingStarted-connecting-private-link-access.md)
+ [Accessing Neptune Analytics graph from Neptune Analytics interface endpoints](gettingStarted-connecting-private-link-access-interface.md)
+ [Creating an Amazon VPC endpoint policy for Neptune Analytics data plane](gettingStarted-connecting-private-link-create-policy.md)