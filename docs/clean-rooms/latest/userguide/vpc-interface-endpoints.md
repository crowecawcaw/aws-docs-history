

# Access AWS Clean Rooms or AWS Clean Rooms ML using an interface endpoint (AWS PrivateLink)
<a name="vpc-interface-endpoints"></a>

You can use AWS PrivateLink to create a private connection between your virtual private cloud (VPC) and AWS Clean Rooms or AWS Clean Rooms ML. You can access AWS Clean Rooms or AWS Clean Rooms ML as if it were in your VPC, without the use of an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your VPC don't need public IP addresses to access AWS Clean Rooms.

You establish this private connection by creating an *interface endpoint*, powered by AWS PrivateLink. We create an endpoint network interface in each subnet that you enable for the interface endpoint. These are requester-managed network interfaces that serve as the entry point for traffic destined for AWS Clean Rooms.

For more information, see [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) in the *AWS PrivateLink Guide*.

## Considerations for AWS Clean Rooms
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface endpoint for AWS Clean Rooms, review [Considerations](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#considerations-interface-endpoints) in the *AWS PrivateLink Guide*.

AWS Clean Rooms and AWS Clean Rooms ML support making calls to all of their API actions through the interface endpoint.

VPC endpoint policies are not supported for AWS Clean Rooms or AWS Clean Rooms ML. By default, full access to AWS Clean Rooms and AWS Clean Rooms ML is allowed through the interface endpoint. Alternatively, you can associate a security group with the endpoint network interfaces to control traffic to AWS Clean Rooms or AWS Clean Rooms ML through the interface endpoint.

## Create an interface endpoint for AWS Clean Rooms
<a name="vpc-endpoint-create"></a>

You can create an interface endpoint for AWS Clean Rooms or AWS Clean Rooms ML using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) in the *AWS PrivateLink Guide*.

Create an interface endpoint for AWS Clean Rooms using the following service name.

```
com.amazonaws.{{region}}.cleanrooms
```

Create an interface endpoint for AWS Clean Rooms ML using the following service name.

```
com.amazonaws.{{region}}.cleanrooms-ml
```

If you enable private DNS for the interface endpoint, you can make API requests to AWS Clean Rooms using its default Regional DNS name. For example, `cleanrooms-ml.us-east-1.amazonaws.com`.