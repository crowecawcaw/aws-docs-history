# Interface VPC endpoints in Amazon GameLift Streams

You can improve the security posture of your VPC by configuring Amazon GameLift Streams to use an interface VPC endpoint. Interface endpoints are
powered by AWS PrivateLink, a technology that allows you to privately access Amazon GameLift Streams APIs by using private IP addresses. AWS PrivateLink
restricts all network traffic between your VPC and Amazon GameLift Streams to the Amazon network. You don't need an internet gateway, a NAT device, or a
virtual private gateway.

For more information about AWS PrivateLink and VPC endpoints, see [VPC endpoints](../../../vpc/latest/privatelink/concepts.md#concepts-vpc-endpoints "../../../vpc/latest/privatelink/concepts.md#concepts-vpc-endpoints") in the
_Amazon VPC User Guide_.

###### Note

AWS PrivateLink is only applicable to API endpoints. Amazon GameLift Streams managed stream sessions always use public network addresses.

## Creating the VPC endpoints for Amazon GameLift Streams

To create the VPC endpoint for the Amazon GameLift Streams service, use the [Access an AWS service using an interface VPC
endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") procedure in the _Amazon VPC User Guide_ to create the following endpoint:

- `com.amazonaws.`region`.gameliftstreams`

###### Note

`region` represents the Region identifier for an AWS Region supported by Amazon GameLift Streams, such as
`us-east-2` for the US East (Ohio) Region.

## Creating a VPC endpoint policy for Amazon GameLift Streams

You can attach an endpoint policy to your VPC endpoint that controls access to Amazon GameLift Streams. The policy specifies the following
information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Control access to VPC
endpoints using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy for Amazon GameLift Streams

The following is an example of an endpoint policy for Amazon GameLift Streams. When attached to an endpoint, this policy grants permission to
create and list stream groups.

```
{
  "Statement":[
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "gameliftstreams:CreateStreamGroup",
        "gameliftstreams:ListStreamGroups"
      ],
      "Resource": [
        "*"
      ]
    }
  ]
}

```
