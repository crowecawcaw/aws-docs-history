

# Access APIs using an interface VPC endpoint (AWS PrivateLink)
<a name="private-link"></a>

You can directly call Amazon WorkSpaces Secure Browser API endpoint from within a private cloud (VPC), instead of connecting over the internet. You can do this without the use of an internet gateway, NAT device, VPN connection, or Direct Connect connection.

You establish this private connection by creating an *interface VPC endpoint* that's powered by [AWS PrivateLink](https://aws.amazon.com/privatelink). For each subnet that you specify from your VPC, we create an endpoint network interface in the subnet. An endpoint network interface is a requester-managed network interface that serves as the entry point for Amazon WorkSpaces Secure Browser API traffic.

For more information, see [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html).

**Topics**
+ [Considerations for Amazon WorkSpaces Secure Browser](vpc-endpoint-considerations.md)
+ [Creating an interface VPC endpoint for Amazon WorkSpaces Secure Browser](vpc-endpoint-create.md)
+ [Creating an endpoint policy for your interface VPC endpoint](vpc-endpoint-policy.md)
+ [Troubleshooting](privatelink-troubleshooting.md)

For more information, see [What is AWS PrivateLink?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-privatelink.html) in the *Amazon VPC User Guide*. 