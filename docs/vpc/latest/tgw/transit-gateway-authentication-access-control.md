# Identity and access management in

AWS Transit Gateway

AWS uses security credentials to identify you and to grant you access to your AWS
resources. You can use features of AWS Identity and Access Management (IAM) to allow other users, services, and
applications to use your AWS resources fully or in a limited way, without sharing your
security credentials.

By default, IAM users don't have permission to create, view, or modify AWS resources.
To allow a user to access resources such as a transit gateway, and to perform tasks, you must create
an IAM policy that grants the user permission to use the specific resources and API
actions they'll need, then attach the policy to the group to which that user belongs. When
you attach a policy to a user or group of users, it allows or denies the users permission to
perform the specified tasks on the specified resources.

To work with a transit gateway, one of the following AWS managed policies might meet your needs:

- [AmazonEC2FullAccess](../../../aws-managed-policy/latest/reference/AmazonEC2FullAccess.md "../../../aws-managed-policy/latest/reference/AmazonEC2FullAccess.md")
- [AmazonEC2ReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonEC2ReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonEC2ReadOnlyAccess.md")
- [PowerUserAccess](../../../aws-managed-policy/latest/reference/PowerUserAccess.md "../../../aws-managed-policy/latest/reference/PowerUserAccess.md")
- [ReadOnlyAccess](../../../aws-managed-policy/latest/reference/ReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/ReadOnlyAccess.md")

## Example policies to manage transit gateways

The following are example IAM policies for working with transit gateways.

###### Create a transit gateway with required tags

The following example enables users to create transit gateway. The
`aws:RequestTag` condition key requires users to tag the transit
gateway with the tag `stack=prod`. The `aws:TagKeys` condition
key uses the `ForAllValues` modifier to indicate that only the key
`stack` is allowed in the request (no other tags can be specified).
If users don't pass this specific tag when they create the transit gateway, or if
they don't specify tags at all, the request fails.

The second statement uses the `ec2:CreateAction` condition key to allow
users to create tags only in the context of `CreateTransitGateway`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCreateTaggedTGWs",
 "Effect": "Allow",
 "Action": "ec2:CreateTransitGateway",
 "Resource": "arn:aws:ec2:`us-east-1`:`123456789012`:transit-gateway/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/stack": "prod"
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": [
 "stack"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": "arn:aws:ec2:`us-east-1`:`123456789012`:transit-gateway/*",
 "Condition": {
 "StringEquals": {
 "ec2:CreateAction": "CreateTransitGateway"
 }
 }
 }
 ]
}`

```

###### Working with transit gateway route tables

The following example enables users to create and delete transit gateway route
tables for a specific transit gateway only (`tgw-11223344556677889`).
Users can also create and replace routes in any transit gateway route table, but
only for attachments that have the tag `network=new-york-office`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DeleteTransitGatewayRouteTable",
 "ec2:CreateTransitGatewayRouteTable"
 ],
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`123456789012`:transit-gateway/tgw-`11223344556677889`",
 "arn:aws:ec2:*:*:transit-gateway-route-table/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTransitGatewayRoute",
 "ec2:ReplaceTransitGatewayRoute"
 ],
 "Resource": "arn:aws:ec2:*:*:transit-gateway-attachment/*",
 "Condition": {
 "StringEquals": {
 "ec2:ResourceTag/network": "new-york-office"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTransitGatewayRoute",
 "ec2:ReplaceTransitGatewayRoute"
 ],
 "Resource": "arn:aws:ec2:*:*:transit-gateway-route-table/*"
 }
 ]
}`

```
