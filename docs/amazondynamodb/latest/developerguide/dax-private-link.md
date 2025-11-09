# Using AWS PrivateLink for DynamoDB Accelerator (DAX)

AWS PrivateLink for DynamoDB Accelerator (DAX) enables you to securely access DAX management APIs such
as `CreateCluster`, `DescribeClusters`, and `DeleteCluster`
over private IP addresses within your virtual private cloud (VPC). This feature enables you to
access DAX services privately from your applications without exposing traffic to the public
internet.

DAX PrivateLink supports dual-stack endpoints (`dax.{region}.api.aws`), enabling both IPv4 and IPv6
connectivity. With AWS PrivateLink for DAX, customers can access the service using private DNS names. The dual-stack
endpoint support ensures transparent connectivity while maintaining network privacy. This allows you to access DAX
through both public internet and VPC endpoints without making any changes to your SDK configuration.

## Considerations when using AWS PrivateLink for DynamoDB Accelerator (DAX)

When implementing AWS PrivateLink for DynamoDB Accelerator (DAX), several important considerations must be taken into account.

Before you set up an interface endpoint for DAX consider the following:

- DAX interface endpoints only support access to the DAX management APIs within the
  same AWS Region. You can't use an interface endpoint to access DAX management APIs in
  other Regions.
- To access the AWS Management Console privately for DAX management, you may need to create additional VPC endpoints for
  services like `com.amazonaws.region.console` and related services.
- You are charged for creating and using an interface endpoint to DAX. For pricing information,
  see [AWS PrivateLink pricing](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/").

## How AWS PrivateLink works with DAX

When you create an interface endpoint for DAX:

1. AWS creates an endpoint network interface in each subnet you enable for the interface endpoint.
2. These are requester-managed network interfaces that serve as entry points for traffic destined for DAX.
3. You can then access DAX through private IP addresses within your VPC.
4. This architecture allows you to use VPC security groups to manage access to the endpoints.
5. Applications can access both DynamoDB and DAX through their respective interface endpoints within a VPC, while
   also allowing on-premises applications to connect via Direct Connect or VPN.
6. This provides a consistent connectivity model across both services, simplifies architecture, and improves security
   by keeping traffic within the AWS network.

## Creating Interface Endpoints for DAX

You can create an interface endpoint to connect to DAX using the AWS Management Console, AWS SDK, AWS CloudFormation, or the AWS API.

###### To create an interface endpoint for DAX using the console

1. Navigate to the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. Choose **Create Endpoint**.
4. For **Service category**, choose **AWS services**
   and for **Service Name**, search for and select
   `com.amazonaws.region.dax`.
5. For **VPC**, select the VPC from which you want to access DAX and for **Subnets**,
   select the subnets where AWS will create the endpoint network interfaces.
6. For **Security groups**, select or create security groups to associate with the endpoint network interfaces.
7. For **Policy**, keep the default **Full Access** or customize as needed.
8. Select **Enable DNS Name** to enable private DNS for the endpoint.
   Keep the private DNS name enabled to prevent changes in the SDK configuration. When
   enabled, your applications can continue using the standard service DNS name (example:
   `dax.region.amazonaws.com`). AWS creates a private hosted zone in your VPC
   that resolves this name to your endpoint's private IP address.

###### Note

Use Regional DNS names if required. Using zonal DNS names isn't recommended. Also,
select subnets from 3 or more AZs to ensure maximum availability through
PrivateLink. 9. Choose **Create endpoint**.

###### To create an interface endpoint for DAX using the AWS CLI

Use the `create-vpc-endpoint` command with the `vpc-endpoint-type`
parameter set to `Interface` and the `service-name` parameter set to
`com.amazonaws.region.dax`.

```
aws ec2 create-vpc-endpoint \
    --vpc-id vpc-ec43eb89 \
    --vpc-endpoint-type Interface \
    --service-name com.amazonaws.us-east-1.dax \
    --subnet-ids subnet-abcd1234 subnet-1a2b3c4d \
    --security-group-ids sg-1a2b3c4d \
    --private-dns-enabled
```

## Additional resources

For more information about AWS PrivateLink and VPC endpoints, see the following resources:

- [AWS PrivateLink for DynamoDB](privatelink-interface-endpoints.md "privatelink-interface-endpoints.md")
- [AWS PrivateLink for DynamoDB Streams](privatelink-streams.md "privatelink-streams.md")
- [Connect your VPC to services using AWS PrivateLink](../../../vpc/latest/userguide/endpoint-services-overview.md "../../../vpc/latest/userguide/endpoint-services-overview.md")
- [Simplify private connectivity
  to DynamoDB with AWS PrivateLink](https://aws.amazon.com/blogs/database/simplify-private-connectivity-to-amazon-dynamodb-with-aws-privatelink "https://aws.amazon.com/blogs/database/simplify-private-connectivity-to-amazon-dynamodb-with-aws-privatelink")
- [AWS PrivateLink Whitepaper](../../../whitepapers/latest/aws-vpc-connectivity-options/aws-privatelink.md "../../../whitepapers/latest/aws-vpc-connectivity-options/aws-privatelink.md")
