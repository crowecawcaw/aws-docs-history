# Identity and access management for AWS Global Networks for Transit Gateways

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. IAM administrators control who can be _authenticated_ (signed in) and _authorized_
(have permissions) to use AWS Global Networks for Transit Gateways resources. IAM is an AWS service that you can use
with no additional charge. You can use features of IAM to allow other users, services, and
applications to use your AWS resources fully or in a limited way, without sharing your
security credentials.

By default, IAM users don't have permission to create, view, or modify AWS resources.
To allow an IAM user to access resources, such as a global network, and perform tasks, you
must:

- Create an IAM policy that grants the IAM user permission to use the specific
  resources and API actions they need
- Attach the policy to the IAM user or to the group to which the IAM user
  belongs
  When you attach a policy to a user or group of users, it allows or denies the user
  permissions to perform the specified tasks on the specified resources.

###### Important

If you grant access to a global network in Network Manager, you grant access to all AWS
service data associated with the registered transit gateways across all Regions.

###### Contents

- [How Network Manager works with IAM](#nm-with-iam "#nm-with-iam")
- [Example policies](#nm-example-iam-policies "#nm-example-iam-policies")
- [Service-linked role](nm-service-linked-roles.md "nm-service-linked-roles.md")
- [AWS managed policies](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
- [Multi-account access roles](nm-custom-multi-role.md "nm-custom-multi-role.md")

## How Network Manager works with IAM

With IAM identity-based policies, you can specify allowed or denied actions and
resources, and specify the conditions under which actions are allowed or denied. Network Manager
supports specific actions, resources, and condition keys. For a complete list, see
[Actions, Resources, and Condition Keys
for AWS Network Manager](../../../service-authorization/latest/reference/list_awsnetworkmanager.md "../../../service-authorization/latest/reference/list_awsnetworkmanager.md") in the _Service Authorization Reference_.

To learn about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Policy actions in Network Manager use the following prefix before the action:
`networkmanager:`. For example, to grant someone permission to create
a global network with the `CreateGlobalNetwork` API operation, you
include the `networkmanager:CreateGlobalNetwork` action in their policy.

For a list of global networks actions, see the [Network Manager API Reference](../../../networkmanager/latest/APIReference.md "../../../networkmanager/latest/APIReference.md").

### Resources

The Resource element specifies the object or objects to which the action applies.
Statements must include either a Resource or a NotResource element. You specify a
resource using an ARN or using the wildcard (\*) to indicate that the statement
applies to all resources.

The global network resource has the following ARN.

```
arn:${Partition}:networkmanager::${Account}:global-network/${GlobalNetworkId}
```

For example, to specify the `global-network-1122334455aabbccd` global
network in your statement, use the following ARN.

```
"Resource": "arn:aws:networkmanager::123456789012:global-network/global-network-1122334455aabbccd"
```

### Condition keys

The `Condition` element (or `Condition`
_block_) lets you specify conditions in which a
statement is in effect. The `Condition` element is optional. You can
build conditional expressions that use [condition operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the
condition in the policy with values in the request.

If you specify multiple `Condition` elements in a statement, or
multiple keys in a single `Condition` element, AWS evaluates them using
a logical `AND` operation. If you specify multiple values for a single
condition key, AWS evaluates the condition using a logical `OR`
operation. All of the conditions must be met before the statement's permissions
are granted.

You can also use placeholder variables when you specify conditions. For example,
you can grant an IAM user permission to access a resource only if it is tagged
with their IAM user name. For more information, see [IAM Policy Elements:
Variables and Tags](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md") in the _IAM User
Guide_.

You can attach tags to global networks resources or pass tags in a request to global networks. To
control access based on tags, you provide tag information in the [condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`aws:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition keys.

To see all AWS global condition keys, see [AWS Global
Condition Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

global networks also supports the following condition keys:

- `networkmanager:tgwArn`—Controls which transit gateways
  can be registered or deregistered in your global network.
- `networkmanager:cgwArn`—Controls which customer gateways
  can be associated or disassociated from devices and links in your global
  network.
- `networkmanager:tgwConnectPeerArn`—Controls which
  Connect peers can be associated or disassociated from devices and
  links in your global network.

## Example policies to manage global networks

The following are example IAM policies for working with global networks.

###### Administrator access

The following IAM policy grants full access to the Amazon EC2, global networks, Direct Connect, and
CloudWatch APIs. This enables administrators to create and manage transit gateways and
their attachments (such as VPCs and Direct Connect gateways), create and manage global networks
resources, and monitor global networks using CloudWatch metrics and events. The policy
also grants user permissions to create any required service-linked roles.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ec2:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "networkmanager:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "cloudwatch:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "events:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "directconnect:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/*"
 }
 ]
}`

```

###### Read-only access

The following IAM policy grants read-only access to the Amazon EC2, global networks, Direct Connect,
CloudWatch, and EventBridge APIs. This enables users to use the global networks console to view and
monitor global networks and their associated resources, and view metrics and events
for the resources. Users cannot create or modify any resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:Get*",
 "ec2:Describe*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "networkmanager:Get*",
 "networkmanager:Describe*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudwatch:List*",
 "cloudwatch:Get*",
 "cloudwatch:Describe*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:Describe*",
 "logs:Get*",
 "logs:List*",
 "logs:StartQuery",
 "logs:StopQuery",
 "logs:TestMetricFilter",
 "logs:FilterLogEvents"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "events:List*",
 "events:TestEventPattern",
 "events:Describe*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "directconnect:Describe*",
 "Resource": "*"
 }
 ]
}`

```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "networkmanager:CreateSite"
 ],
 "Resource": [
 "arn:aws:networkmanager::`111122223333`:global-network/global-network-`1122334455aabbccd`",
 "arn:aws:networkmanager::`111122223333`:site/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "networkmanager:CreateDevice"
 ],
 "Resource": [
 "arn:aws:networkmanager::`111122223333`:global-network/global-network-`1122334455aabbccd`",
 "arn:aws:networkmanager::`111122223333`:site/*",
 "arn:aws:networkmanager::`111122223333`:device/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "networkmanager:CreateLink"
 ],
 "Resource": [
 "arn:aws:networkmanager::`111122223333`:global-network/global-network-`1122334455aabbccd`",
 "arn:aws:networkmanager::`111122223333`:link/*"
 ]
 }
 ]
}`

```

###### Controlling the use of transit gateways and customer gateways

The following IAM policy enables users to work with global networks resources, but they
are explicitly denied permission to do the following:

- Register or deregister a specific transit gateway
  (`tgw-aabbccdd112233445`) in the global network.
- Associate or disassociate a specific customer gateway
  (`cgw-11223344556677abc`) in the global network.

The policy uses the `networkmanager:tgwArn` and
`networkmanager:cgwArn` condition keys to enforce these
conditions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "networkmanager:*"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Deny",
 "Action": [
 "networkmanager:RegisterTransitGateway",
 "networkmanager:DeregisterTransitGateway"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "networkmanager:tgwArn": "arn:aws:ec2:`region`:`account-id`:transit-gateway/tgw-`aabbccdd112233445`"
 }
 }
 },
 {
 "Effect": "Deny",
 "Action": [
 "networkmanager:AssociateCustomerGateway",
 "networkmanager:DisassociateCustomerGateway"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "networkmanager:cgwArn": "arn:aws:ec2:`region`:`account-id`:customer-gateway/cgw-`11223344556677abc`"
 }
 }
 }
 ]
}`

```
