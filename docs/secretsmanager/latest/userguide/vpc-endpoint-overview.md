# Using an AWS Secrets Manager VPC endpoint

We recommend that you run as much of your infrastructure as possible on private networks
that are not accessible from the public internet. You can establish a private connection
between your VPC and Secrets Manager by creating an _interface VPC endpoint_.
Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that enables you to privately access Secrets Manager APIs
without an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances
in your VPC don't need public IP addresses to communicate with Secrets Manager APIs. Traffic between
your VPC and Secrets Manager does not leave the AWS network. For more information, see [Interface VPC
endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User
Guide_.

When Secrets Manager [rotates a secret by using a Lambda rotation
function](rotating-secrets.md "rotating-secrets.md"), for example a secret that contains database credentials, the Lambda
function makes requests to both the database and Secrets Manager. When you [turn on automatic rotation by using the
console](rotate-secrets_turn-on-for-db.md "rotate-secrets_turn-on-for-db.md"), Secrets Manager creates the Lambda function in the same VPC as your database. We
recommend that you create a Secrets Manager endpoint in the same VPC so that requests from the Lambda
rotation function to Secrets Manager don't leave the Amazon network.

If you enable private DNS for the endpoint, you can make API requests to Secrets Manager using its
default DNS name for the Region, for example,
`secretsmanager.us-east-1.amazonaws.com`. For more information, see [Accessing
a service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

You can make sure that requests to Secrets Manager come from the VPC access by including a condition
in your permissions policies. For more information, see [Example: Permissions and VPCs](auth-and-access_resource-policies.md#auth-and-access_examples_vpc "auth-and-access_resource-policies.md#auth-and-access_examples_vpc").

You can use AWS CloudTrail logs to audit your use of secrets through the VPC endpoint.

###### To create a VPC endpoint for Secrets Manager

1. See [Creating an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _Amazon VPC User Guide_. Use one of the following service names:
   - `com.amazonaws.`region`.secretsmanager`
   - `com.amazonaws.`region`.secretsmanager-fips`

2. To control access to the endpoint, see [Control access to VPC
   endpoints using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md").
3. To use IPv6 and dual-stack addressing, see [IPv4 and IPv6 access](ip-access.md "ip-access.md").

## Create an endpoint policy for your interface

endpoint

An endpoint policy is an IAM resource that you can attach to an interface endpoint.
The default endpoint policy allows full access to Secrets Manager through the interface
endpoint. To control the access allowed to Secrets Manager from your VPC, attach a custom
endpoint policy to the interface endpoint.

An endpoint policy specifies the following information:

- The principals that can perform actions (AWS accounts, IAM users, and
  IAM roles).
- The actions that can be performed.
- The resources on which the actions can be performed.

For more information, see [Control access to services using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the
_AWS PrivateLink Guide_.

###### Example: VPC endpoint policy for Secrets Manager actions

The following is an example of a custom endpoint policy. When you attach this
policy to your interface endpoint, it grants access to the listed Secrets Manager actions
on the specified secret.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow all users to use GetSecretValue and DescribeSecret on the specified secret.",
 "Effect": "Allow",
 "Principal": "*",
 "Action": [
 "secretsmanager:GetSecretValue",
 "secretsmanager:DescribeSecret"
 ],
 "Resource": "arn:aws:secretsmanager:us-east-1:111122223333:secret:`secretName-AbCdEf`"
 }
 ]
}`

```

## Shared subnets

You can't create, describe, modify, or delete VPC endpoints in subnets that are shared
with you. However, you can use the VPC endpoints in subnets that are shared with you.
For information about VPC sharing, see [Share your VPC with other
accounts](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md") in the _Amazon Virtual Private Cloud User
Guide_.
