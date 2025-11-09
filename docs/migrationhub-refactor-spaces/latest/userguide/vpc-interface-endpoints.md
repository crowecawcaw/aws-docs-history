AWS Migration Hub Refactor Spaces is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub Refactor Spaces, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Access Refactor Spaces using an interface endpoint

(AWS PrivateLink)

You can use AWS PrivateLink to create a private connection between your VPC and
AWS Migration Hub Refactor Spaces (Refactor Spaces). You can access Refactor Spaces as if it were in your VPC, without the use of an
internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC
don't need public IP addresses to access Refactor Spaces.

You establish this private connection by creating an _interface
endpoint_, powered by AWS PrivateLink. We create an endpoint network interface
in each subnet that you enable for the interface endpoint. These are requester-managed
network interfaces that serve as the entry point for traffic destined for Refactor Spaces.

For more information, see [Access AWS services
through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the
_AWS PrivateLink Guide_.

## Considerations for Refactor Spaces

Before you set up an interface endpoint for Refactor Spaces, review [Considerations](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the _AWS PrivateLink Guide_.

Refactor Spaces supports making calls to all of its API actions through the interface
endpoint.

VPC endpoint policies are not supported for Refactor Spaces. By default, full access to
Refactor Spaces is allowed through the interface endpoint. Alternatively, you can associate a
security group with the endpoint network interfaces to control traffic to Refactor Spaces
through the interface endpoint.

## Create an interface endpoint for Refactor Spaces

You can create an interface endpoint for Refactor Spaces using either the Amazon VPC console or
the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the
_AWS PrivateLink Guide_.

Create an interface endpoint for Refactor Spaces using the following service name:

```
com.amazonaws.`region`.refactor-spaces
```

If you enable private DNS for the interface endpoint, you can make API requests to
Refactor Spaces using its default Regional DNS name. For example,
`refactor-spaces.us-east-1.amazonaws.com`.

For information about the Refactor Spaces API, see the [AWS Migration Hub Refactor Spaces
API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

## Availability

Refactor Spaces currently supports VPC endpoints in the following AWS Regions.

| Region Name               | Region         |
| ------------------------- | -------------- |
| US East (Ohio)            | us-east-2      |
| US East (N. Virginia)     | us-east-1      |
| US West (N. California)   | us-west-1      |
| US West (Oregon)          | us-west-2      |
| Asia Pacific (Mumbai)     | ap-south-1     |
| Asia Pacific (Seoul)      | ap-northeast-2 |
| Asia Pacific (Singapore)  | ap-southeast-1 |
| Asia Pacific (Sydney)     | ap-southeast-2 |
| Asia Pacific (Tokyo)      | ap-northeast-1 |
| Canada (Central)          | ca-central-1   |
| Europe (Frankfurt)        | eu-central-1   |
| Europe (Ireland)          | eu-west-1      |
| Europe (London)           | eu-west-2      |
| Europe (Paris)            | eu-west-3      |
| Europe (Stockholm)        | eu-north-1     |
| South America (São Paulo) | sa-east-1      |
