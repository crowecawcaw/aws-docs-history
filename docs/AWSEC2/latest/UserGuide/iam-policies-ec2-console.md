# Example policies to control access to the Amazon EC2 console

You can use IAM policies to grant users the permissions required to work with Amazon EC2.
For step-by-step directions, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in
the _IAM User Guide_.

The console uses additional API actions for its features, so these policies may not work
as expected. For example, a user that has permission to use only the
`DescribeVolumes` API action will encounter errors when trying to view
volumes in the console. This section demonstrates policies that enable users to work with
specific parts of the console. For additional information about creating policies for the
Amazon EC2 console, see the following AWS Security Blog post: [Granting Users Permission to Work in the Amazon EC2 Console](https://aws.amazon.com/blogs/security/granting-users-permission-to-work-in-the-amazon-ec2-console/ "https://aws.amazon.com/blogs/security/granting-users-permission-to-work-in-the-amazon-ec2-console/").

The following examples show policy statements that you could use to grant users
permissions to use Amazon EC2. Replace each `user input placeholder`
with your own information. These policies are designed for requests that are made using the AWS Management Console.
The Amazon EC2 console might call multiple API actions to display a single resource, and it might
not be obvious until the user attempts a task and the console displays an error. For more
information, see the following AWS Security Blog post: [Granting Users Permission to Work in the Amazon EC2 Console](https://aws.amazon.com/blogs/security/granting-users-permission-to-work-in-the-amazon-ec2-console/ "https://aws.amazon.com/blogs/security/granting-users-permission-to-work-in-the-amazon-ec2-console/").

###### Examples

- [Read-only access](#ex-read-only "#ex-read-only")
- [Use the EC2 launch instance wizard](#ex-launch-wizard "#ex-launch-wizard")
- [Work with security groups](#ex-security-groups "#ex-security-groups")
- [Work with Elastic IP addresses](#ex-eip "#ex-eip")
- [Work with Reserved Instances](#ex-reservedinstances "#ex-reservedinstances")
  To help you work out which API actions are required to perform tasks in the console,
  you can use a service that logs calls, such as AWS CloudTrail. If your policy does not grant
  permission to create or modify a specific resource, the console displays an encoded
  message with diagnostic information. You can decode the
  message using the [DecodeAuthorizationMessage](../../../STS/latest/APIReference/API_DecodeAuthorizationMessage.md "../../../STS/latest/APIReference/API_DecodeAuthorizationMessage.md") API action for AWS STS, or the [decode-authorization-message](../../../cli/latest/reference/sts/decode-authorization-message.md "../../../cli/latest/reference/sts/decode-authorization-message.md") command in the AWS CLI.

## Example: Read-only access

To allow users to view all resources in the Amazon EC2 console, you can use the
same policy as the following example: [Example: Read-only access](ExamplePolicies_EC2.md#iam-example-read-only "ExamplePolicies_EC2.md#iam-example-read-only"). Users cannot perform any actions on
those resources or create new resources, unless another statement grants them
permission to do so.

**View instances, AMIs, and snapshots**

Alternatively, you can provide read-only access to a subset of resources. To
do this, replace the \* wildcard in the `ec2:Describe` API action with
specific `ec2:Describe` actions for each resource. The following
policy allows users to view all instances, AMIs, and snapshots in the Amazon EC2
console. The `ec2:DescribeTags` action allows users to view public
AMIs. The console requires the tagging information to display public AMIs;
however, you can remove this action to allow users to view only private
AMIs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:DescribeImages",
 "ec2:DescribeTags",
 "ec2:DescribeSnapshots"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Note

The Amazon EC2 `ec2:Describe*` API actions do not support resource-level
permissions, so you cannot control which individual resources users can view in the
console. Therefore, the \* wildcard is necessary in the `Resource` element
of the above statement. For more information about which ARNs you can use with which
Amazon EC2 API actions, see [Actions, resources, and condition keys for Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md "../../../service-authorization/latest/reference/list_amazonec2.md").

**View instances and CloudWatch metrics**

The following policy allows users to view instances in the Amazon EC2 console, as well as CloudWatch
alarms and metrics in the **Monitoring** tab of the
**Instances** page. The Amazon EC2 console uses the CloudWatch API to display
the alarms and metrics, so you must grant users permission to use the
`cloudwatch:DescribeAlarms`,
`cloudwatch:DescribeAlarmsForMetric`,
`cloudwatch:ListMetrics`, `cloudwatch:GetMetricStatistics`, and
`cloudwatch:GetMetricData` actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:DescribeInstanceTypes",
 "cloudwatch:DescribeAlarms",
 "cloudwatch:DescribeAlarmsForMetric",
 "cloudwatch:ListMetrics",
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:GetMetricData"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Example: Use the EC2 launch instance wizard

The Amazon EC2 launch instance wizard is a screen with options to configure and launch an
instance. Your policy must include permission to use the API actions that allow users to
work with the wizard's options. If your policy does not include permission to use those
actions, some items in the wizard cannot load properly, and users cannot complete a
launch.

**Basic launch instance wizard access**

To complete a launch successfully, users must be given permission to use the
`ec2:RunInstances` API action, and at least the following API
actions:

- `ec2:DescribeImages`: To view and select an AMI.
- `ec2:DescribeInstanceTypes`: To view and select an instance
  type.
- `ec2:DescribeVpcs`: To view the available network options.
- `ec2:DescribeSubnets`: To view all available subnets for the chosen VPC.
- `ec2:DescribeSecurityGroups` or `ec2:CreateSecurityGroup`: To view
  and select an existing security group, or to create a new one.
- `ec2:DescribeKeyPairs` or `ec2:CreateKeyPair`: To select an
  existing key pair, or to create a new one.
- `ec2:AuthorizeSecurityGroupIngress`: To add inbound rules.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:DescribeImages",
 "ec2:DescribeInstanceTypes",
 "ec2:DescribeKeyPairs",
 "ec2:DescribeVpcs",
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups",
 "ec2:CreateSecurityGroup",
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:CreateKeyPair"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": "*"
 }
 ]
}`

```

You can add API actions to your policy to provide more options for users, for
example:

- `ec2:DescribeAvailabilityZones`: To view and select a specific Availability
  Zone.
- `ec2:DescribeNetworkInterfaces`: To view and select existing network
  interfaces for the selected subnet.
- To add outbound rules to VPC security groups, users must be granted permission to use
  the `ec2:AuthorizeSecurityGroupEgress` API action. To modify or
  delete existing rules, users must be granted permission to use the relevant
  `ec2:RevokeSecurityGroup*` API action.
- `ec2:CreateTags`: To tag the resources that are created by
  `RunInstances`. For more information, see [Grant permission to tag Amazon EC2 resources during creation](supported-iam-actions-tagging.md "supported-iam-actions-tagging.md"). If users do not have
  permission to use this action and they attempt to apply tags on the tagging page
  of the launch instance wizard, the launch fails.

###### Important

Specifying a **Name** while launching an instance creates a tag and
requires the `ec2:CreateTags` action. Be careful about granting
users permission to use the `ec2:CreateTags` action, because
doing so limits your ability to use the `aws:ResourceTag`
condition key to restrict their use of other resources. If you grant users
permission to use the `ec2:CreateTags` action, they can change a
resource's tag in order to bypass those restrictions. For more information,
see [Control access using attribute-based access](iam-policies-for-amazon-ec2.md#control-access-with-tags "iam-policies-for-amazon-ec2.md#control-access-with-tags").

- To use Systems Manager parameters when selecting an AMI, you must add
  `ssm:DescribeParameters` and `ssm:GetParameters` to
  your policy. `ssm:DescribeParameters` grants your users the
  permission to view and select Systems Manager parameters. `ssm:GetParameters`
  grants your users the permission to get the values of the Systems Manager parameters. You
  can also restrict access to specific Systems Manager parameters. For more information, see
  **Restrict access to specific Systems Manager
  parameters** later in this section.

Currently, the Amazon EC2 `Describe*` API actions do not support resource-level
permissions, so you cannot restrict which individual resources users can view in the
launch instance wizard. However, you can apply resource-level permissions on the
`ec2:RunInstances` API action to restrict which resources users can use
to launch an instance. The launch fails if users select options that they are not
authorized to use.

**Restrict access to a specific instance type, subnet, and
Region**

The following policy allows users to launch `t2.micro` instances using AMIs
owned by Amazon, and only into a specific subnet (`subnet-1a2b3c4d`). Users
can only launch in the specified Region. If users select a different
Region, or select a different instance type, AMI, or subnet in the launch instance
wizard, the launch fails.

The first statement grants users permission to view the options in the launch instance
wizard or to create new ones, as explained in the example above. The second statement
grants users permission to use the network interface, volume, key pair, security group,
and subnet resources for the `ec2:RunInstances` action, which are required to
launch an instance into a VPC. For more information about using the
`ec2:RunInstances` action, see [Launch instances (RunInstances)](ExamplePolicies_EC2.md#iam-example-runinstances "ExamplePolicies_EC2.md#iam-example-runinstances"). The third and fourth statements grant
users permission to use the instance and AMI resources respectively, but only if the
instance is a `t2.micro` instance, and only if the AMI is owned by Amazon, or
certain trusted and verified partners.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:DescribeImages",
 "ec2:DescribeInstanceTypes",
 "ec2:DescribeKeyPairs",
 "ec2:CreateKeyPair",
 "ec2:DescribeVpcs",
 "ec2:DescribeSubnets", "ec2:DescribeSecurityGroups",
 "ec2:CreateSecurityGroup",
 "ec2:AuthorizeSecurityGroupIngress"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action":"ec2:RunInstances",
 "Resource": [
 "arn:aws:ec2:`us-east-2`:`111122223333`:network-interface/*",
 "arn:aws:ec2:`us-east-2`:`111122223333`:volume/*",
 "arn:aws:ec2:`us-east-2`:`111122223333`:key-pair/*",
 "arn:aws:ec2:`us-east-2`:`111122223333`:security-group/*",
 "arn:aws:ec2:`us-east-2`:`111122223333`:subnet/`subnet-1a2b3c4d`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": [
 "arn:aws:ec2:`us-east-2`:`111122223333`:instance/*"
 ],
 "Condition": {
 "StringEquals": {
 "ec2:InstanceType": "`t2.micro`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "ec2:RunInstances",
 "Resource": [
 "arn:aws:ec2:`us-east-2`::image/ami-*"
 ],
 "Condition": {
 "StringEquals": {
 "ec2:Owner": "amazon"
 }
 }
 }
 ]
}`

```

**Restrict access to specific Systems Manager parameters**

The following policy grants access to use Systems Manager parameters with a specific name.

The first statement grants users the permission to view Systems Manager parameters when selecting an
AMI in the launch instance wizard. The second statement grants users the permission to
only use parameters that are named `prod-*`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "ssm:DescribeParameters"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:GetParameters"
 ],
 "Resource": "arn:aws:ssm:`us-east-2`:`123456123456`:parameter/prod-*"
 }
 ]
}`

```

## Example: Work with security groups

**View security groups and add and remove
rules**

The following policy grants users permission to view security groups in the Amazon EC2 console,
to add and remove inbound and outbound rules, and to list and modify rule descriptions
for existing security groups that have the tag `Department=Test`.

In the first statement, the `ec2:DescribeTags` action allows
users to view tags in the console, which makes it easier for users to identify
the security groups that they are allowed to modify.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSecurityGroupRules",
 "ec2:DescribeTags"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:RevokeSecurityGroupIngress",
 "ec2:AuthorizeSecurityGroupEgress",
 "ec2:RevokeSecurityGroupEgress",
 "ec2:ModifySecurityGroupRules",
 "ec2:UpdateSecurityGroupRuleDescriptionsIngress",
 "ec2:UpdateSecurityGroupRuleDescriptionsEgress"
 ],
 "Resource": [
 "arn:aws:ec2:`us-east-2`:`111122223333`:security-group/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/`Department`": "`Test`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:ModifySecurityGroupRules"
 ],
 "Resource": [
 "arn:aws:ec2:`us-east-2`:`111122223333`:security-group-rule/*"
 ]
 }
]}`

```

**Work with the Create Security Group dialog box**

You can create a policy that allows users to work with the **Create
Security Group** dialog box in the Amazon EC2 console. To use this
dialog box, users must be granted permission to use at the least the following
API actions:

- `ec2:CreateSecurityGroup`: To create a new security group.
- `ec2:DescribeVpcs`: To view a list of existing VPCs in the
  **VPC** list.

With these permissions, users can create a new security group successfully,
but they cannot add any rules to it. To work with rules in the **Create
Security Group** dialog box, you can add the following API actions
to your policy:

- `ec2:AuthorizeSecurityGroupIngress`: To add inbound
  rules.
- `ec2:AuthorizeSecurityGroupEgress`: To add outbound rules
  to VPC security groups.
- `ec2:RevokeSecurityGroupIngress`: To modify or delete
  existing inbound rules. This is useful to allow users to use the
  **Copy to new** feature in the console. This
  feature opens the **Create Security Group** dialog box
  and populates it with the same rules as the security group that was
  selected.
- `ec2:RevokeSecurityGroupEgress`: To modify or delete
  outbound rules for VPC security groups. This is useful to allow users to
  modify or delete the default outbound rule that allows all outbound
  traffic.
- `ec2:DeleteSecurityGroup`: To cater for when invalid rules
  cannot be saved. The console first creates the security group, and then
  adds the specified rules. If the rules are invalid, the action fails,
  and the console attempts to delete the security group. The user remains
  in the **Create Security Group** dialog box so that
  they can correct the invalid rule and try to create the security group
  again. This API action is not required, but if a user is not granted
  permission to use it and attempts to create a security group with
  invalid rules, the security group is created without any rules, and the
  user must add them afterward.
- `ec2:UpdateSecurityGroupRuleDescriptionsIngress`: To
  add or update descriptions of ingress (inbound) security group rules.
- `ec2:UpdateSecurityGroupRuleDescriptionsEgress`: To
  add or update descriptions of egress (outbound) security group rules.
- `ec2:ModifySecurityGroupRules`: To modify security group
  rules.
- `ec2:DescribeSecurityGroupRules`: To list security group
  rules.

The following policy grants users permission to use the **Create
Security Group** dialog box, and to create inbound and outbound
rules for security groups that are associated with a specific VPC
(`vpc-1a2b3c4d`). Users can create security groups for
a VPC, but they cannot add any rules to them. Similarly,
users cannot add any rules to any existing security group that's not associated
with VPC `vpc-1a2b3c4d`. Users are also granted permission to view
all security groups in the console. This makes it easier for users to identify
the security groups to which they can add inbound rules. This policy also grants
users permission to delete security groups that are associated with VPC
`vpc-1a2b3c4d`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeSecurityGroups",
 "ec2:CreateSecurityGroup",
 "ec2:DescribeVpcs"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DeleteSecurityGroup",
 "ec2:AuthorizeSecurityGroupIngress",
 "ec2:AuthorizeSecurityGroupEgress"
 ],
 "Resource": "arn:aws:ec2:`us-east-2`:`111122223333`:security-group/*",
 "Condition":{
 "ArnEquals": {
 "ec2:Vpc": "arn:aws:ec2:`us-east-2`:`111122223333`:vpc/`vpc-1a2b3c4d`"
 }
 }
 }
 ]
}`

```

## Example: Work with Elastic IP addresses

To allow users to view Elastic IP addresses in the Amazon EC2 console, you must
grant users permission to use the `ec2:DescribeAddresses`
action.

To allow users to work with Elastic IP addresses, you can add the following
actions to your policy.

- `ec2:AllocateAddress`: To allocate an Elastic IP address.
- `ec2:ReleaseAddress`: To release an Elastic IP
  address.
- `ec2:AssociateAddress`: To associate an Elastic IP address
  with an instance or a network interface.
- `ec2:DescribeNetworkInterfaces` and
  `ec2:DescribeInstances`: To work with the
  **Associate address** screen. The screen displays
  the available instances or network interfaces to which you can associate
  an Elastic IP address.
- `ec2:DisassociateAddress`: To disassociate an Elastic IP
  address from an instance or a network interface.

The following policy allows users to view, allocate, and associate Elastic IP
addresses with instances. Users cannot associate Elastic IP addresses with
network interfaces, disassociate Elastic IP addresses, or release them.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeAddresses",
 "ec2:AllocateAddress",
 "ec2:DescribeInstances",
 "ec2:AssociateAddress"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Example: Work with Reserved Instances

The following policy allows users to view and modify Reserved Instances in your account, as well as
purchase new Reserved Instances in the AWS Management Console.

This policy allows users to view all the Reserved Instances, as well as On-Demand Instances, in the account. It's
not possible to set resource-level permissions for individual Reserved Instances.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeReservedInstances",
 "ec2:ModifyReservedInstances",
 "ec2:PurchaseReservedInstancesOffering",
 "ec2:DescribeInstances",
 "ec2:DescribeInstanceTypes",
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeReservedInstancesOfferings"
 ],
 "Resource": "*"
 }
 ]
}`

```

The `ec2:DescribeAvailabilityZones` action is necessary to ensure that the
Amazon EC2 console can display information about the Availability Zones in which you can
purchase Reserved Instances. The `ec2:DescribeInstances` action is not required, but
ensures that the user can view the instances in the account and purchase reservations to
match the correct specifications.

You can adjust the API actions to limit user access, for example removing
`ec2:DescribeInstances` and
`ec2:DescribeAvailabilityZones` means the user has read-only
access.
