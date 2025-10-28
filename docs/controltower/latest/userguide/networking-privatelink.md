# Access AWS Control Tower using an interface endpoint (AWS PrivateLink)

You can use AWS PrivateLink to create a private connection between your VPC and
AWS Control Tower. You can access AWS Control Tower as if it were in your VPC, without the
use of an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.
Instances in your VPC don't need public IP addresses to access AWS Control Tower.

You establish this private connection by creating an _interface
endpoint_, powered by AWS PrivateLink. We create an endpoint network interface in
each subnet that you enable for the interface endpoint. These are requester-managed network
interfaces that serve as the entry point for traffic destined for AWS Control Tower.

For more information, see [Access AWS services through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the _AWS PrivateLink Guide_.

## Considerations for AWS Control Tower

Before you set up an interface endpoint for AWS Control Tower, review [Considerations](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the _AWS PrivateLink Guide_.

AWS Control Tower supports making calls to all of its API actions through the
interface endpoint.

## Create an interface endpoint for AWS Control Tower

You can create an interface endpoint for AWS Control Tower using either the Amazon VPC
console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _AWS PrivateLink Guide_.

Create an interface endpoint for AWS Control Tower using the following service names:

```
com.amazonaws.`region`.controltower
com.amazonaws.`region`.controltower-fips
```

If you enable private DNS for the interface endpoint, you can make API requests to
AWS Control Tower using its default Regional DNS name. For example,
`controltower.us-east-1.amazonaws.com`.

## Create an endpoint policy for your interface

endpoint

An endpoint policy is an IAM resource that you can attach to an interface endpoint.
The default endpoint policy allows full access to AWS Control Tower through the
interface endpoint. To control the access allowed to AWS Control Tower from your
VPC, attach a custom endpoint policy to the interface endpoint.

An endpoint policy specifies the following information:

- The principals that can perform actions (AWS accounts, IAM users, and
  IAM roles).
- The actions that can be performed.
- The resources on which the actions can be performed.

For more information, see [Control access to services using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the
_AWS PrivateLink Guide_.

###### Example: VPC endpoint policy for AWS Control Tower actions

The following is an example of a custom endpoint policy. When you attach this
policy to your interface endpoint, it grants access to the listed AWS Control Tower
actions for all principals on all resources.

```
{
   "Statement": [
      {
         "Principal": "*",
         "Effect": "Allow",
         "Action": [
            "controltower:ListEnabledControls",
            "controltower:ListLandingZones"
         ],
         "Resource":"*"
      }
   ]
}
```

###### Note

For a complete list of AWS Control Tower API operations, see the [AWS Control Tower API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").
