# Access Amazon Inspector using an interface endpoint (AWS PrivateLink

You can use AWS PrivateLink to create a private connection between your VPC and Amazon Inspector.
You can access Amazon Inspector as if it were in your VPC, without the use of an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.
Instances in your VPC don't need public IP addresses to access Amazon Inspector.

You establish this private connection by creating an _interface endpoint_, powered by AWS PrivateLink.
We create an endpoint network interface in each subnet that you enable for the interface endpoint.
These are requester-managed network interfaces that serve as the entry point for traffic destined for Amazon Inspector.

For more information, see [Access AWS services through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the _AWS PrivateLink Guide_.

## Considerations for Amazon Inspector

Before you set up an interface endpoint for Amazon Inspector, review [Considerations](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the _AWS PrivateLink Guide_.

Amazon Inspector supports making calls to all of its API actions through the interface endpoint.

VPC endpoint policies are not supported for Amazon Inspector.
By default, full access to Amazon Inspector is allowed through the interface endpoint.
Alternatively, you can associate a security group with the endpoint network interfaces to control traffic to Amazon Inspector through the interface endpoint.

## Create an interface endpoint for Amazon Inspector

You can create an interface endpoint for Amazon Inspector using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI).
For more information, see [Create an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _AWS PrivateLink Guide_.

When you create an interface endpoint for Amazon Inspector, use one of the following service names:

```
com.amazonaws.`region`.inspector2
```

```
com.amazonaws.`region`.inspector-scan
```

Replace `region` with the AWS Region code for the applicable AWS Region.

If you enable private DNS for the interface endpoint, you can make API requests to Amazon Inspector using its default Regional DNS name, for example, `service-name.us-east-1.amazonaws.com` or `service-name.us-east-1.api.aws.com` for the US East (N. Virginia).
