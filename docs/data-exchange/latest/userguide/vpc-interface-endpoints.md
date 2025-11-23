# AWS Data Exchange and interface VPC endpoints

(AWS PrivateLink)

You can establish a private connection between your virtual private cloud (VPC) and
AWS Data Exchange by creating an _interface VPC endpoint_. Interface endpoints
are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology
that enables you to privately access AWS Data Exchange API operations without an internet gateway, NAT
device, VPN connection, or Direct Connect connection. Instances in your VPC don't need public IP
addresses to communicate with AWS Data Exchange API operations. Traffic between your VPC and AWS Data Exchange does
not leave the Amazon network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

###### Note

Every AWS Data Exchange action, except for `SendAPIAsset`, is supported for VPC.

For more information, see [Interface VPC
endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User
Guide_.

## Considerations for AWS Data Exchange VPC

endpoints

Before you set up an interface VPC endpoint for AWS Data Exchange, ensure that you review [Interface
endpoint properties and limitations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_.

AWS Data Exchange supports making calls to all of its API operations from your VPC.

## Creating an interface VPC endpoint for

AWS Data Exchange

You can create a VPC endpoint for the AWS Data Exchange service using either the Amazon VPC console or
the AWS Command Line Interface (AWS CLI). For more information, see [Creating an
interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create a VPC endpoint for AWS Data Exchange using the following service name:

- `com.amazonaws.`region`.dataexchange`

If you enable private DNS for the endpoint, you can make API requests to AWS Data Exchange using
its default DNS name for the AWS Region, for example,
`com.amazonaws.us-east-1.dataexchange`.

For more information, see [Accessing a service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

## Creating a VPC endpoint policy for AWS Data Exchange

You can attach an endpoint policy to your VPC endpoint that controls access to AWS Data Exchange.
The policy specifies the following information:

- The principal that can perform actions
- The actions that can be performed
- The resources on which actions can be performed

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy for AWS Data Exchange actions

The following is an example of an endpoint policy for AWS Data Exchange. When attached to an
endpoint, this policy grants access to the listed AWS Data Exchange actions for all principals
on all resources.

This example VPC endpoint policy allows full access only to the user `bts`
in AWS account `123456789012` from `vpc-12345678`. The user
`readUser` is allowed to read the resources, but all other IAM
principals are denied access to the endpoint.

JSON

```
`{
 "Id": "example-policy",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow administrative actions from vpc-12345678",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::123456789012:user/bts"
 ]
 },
 "Action": "*",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:sourceVpc": "vpc-12345678"
 }
 }
 },
 {
 "Sid": "Allow ReadOnly actions",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::123456789012:user/readUser"
 ]
 },
 "Action": [
 "dataexchange:list*",
 "dataexchange:get*"
 ],
 "Resource": "*"
 }
 ]
}`

```
