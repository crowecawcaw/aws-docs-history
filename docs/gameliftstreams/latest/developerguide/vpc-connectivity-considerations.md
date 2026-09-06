

# Requirements and considerations
<a name="vpc-connectivity-considerations"></a>

## Requirements
<a name="vpc-connectivity-requirements"></a>

VPC connectivity has the following requirements:
+ **No overlapping CIDR blocks**: Your VPC CIDR blocks cannot overlap with the service VPC CIDR block. When you specify your VPC CIDR blocks in the `Ipv4CidrBlocks` parameter, Amazon GameLift Streams automatically selects a service VPC CIDR block that does not overlap with the CIDR blocks you provided. The service VPC CIDR block is returned in the `InternalVpcIpv4CidrBlock` field when you call `GetStreamGroup`. You must use this value when configuring routes in your VPC.
+ **Same account**: The VPC must be in the same AWS account that created the stream group.
+ **VPC ID is immutable for primary location**: The VPC ID for the stream group's primary location cannot be changed after the stream group is created. However, for other streaming locations, you can change the VPC by deleting the stream group location and recreating it with a different VPC ID. You can update the CIDR blocks for any location by calling [UpdateStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UpdateStreamGroup.html).
+ **VPC Region must match streaming location**: The VPC must be in the same Region as the streaming location. For example, if you add a streaming location in `eu-west-1`, you must specify a VPC that exists in `eu-west-1`.
+ **IPv4 only**: For stream groups with dual stack IPv6 support, only IPv4 VPC traffic is supported at this time.

**Required IAM permissions**

To configure VPC connectivity, your IAM identity must have the following permissions, in addition to the GameLift Streams permissions:
+ `ec2:DescribeVpcs` – Required for Amazon GameLift Streams to validate your VPC configuration.
+ `ec2:CreateTransitGatewayVpcAttachment` – Required to attach your VPC to the transit gateway.
+ `ec2:CreateRoute` – Required to add routes to your VPC route tables.
+ `ram:AcceptResourceShareInvitation` – Required to accept the transit gateway resource share.

## Additional Considerations
<a name="vpc-connectivity-considerations"></a>

Before configuring VPC connectivity, consider the following:
+ **Additional latency**: Traffic routed through the transit gateway may experience slightly higher latency compared to direct connections.
+ **Cost**: Transit gateway attachments incur additional charges. See [AWS Transit Gateway pricing](https://aws.amazon.com/transit-gateway/pricing/) for details.
+ **Quota**: There is a default limit of 5 VPC transit configurations per account per Region.