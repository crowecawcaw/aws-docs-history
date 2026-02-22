# Using identity-based policies (IAM policies) for MemoryDB

This topic provides examples of identity-based policies in which an account
administrator can attach permissions policies to IAM identities (that is, users, groups,
and roles).

###### Important

We recommend that you first read the topics that explain the basic concepts and options to
manage access to MemoryDB resources. For more information, see [Overview of managing access permissions to your MemoryDB resources](iam.md "iam.md").

The sections in this topic cover the following:

- [Permissions required to use the MemoryDB console](#iam.identitybasedpolicies.minconpolicies "#iam.identitybasedpolicies.minconpolicies")
- [AWS-managed (predefined) policies
  for MemoryDB](security-iam-awsmanpol.md#iam.identitybasedpolicies.predefinedpolicies "security-iam-awsmanpol.md#iam.identitybasedpolicies.predefinedpolicies")
- [Customer-managed policy
  examples](#iam.identitybasedpolicies.customermanagedpolicies "#iam.identitybasedpolicies.customermanagedpolicies")
  The following shows an example of a permissions policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "AllowClusterPermissions",
 "Effect": "Allow",
 "Action": [
 "memorydb:CreateCluster",
 "memorydb:DescribeClusters",
 "memorydb:UpdateCluster"],
 "Resource": "*"
 },
 {
 "Sid": "AllowUserToPassRole",
 "Effect": "Allow",
 "Action": [ "iam:PassRole" ],
 "Resource": "arn:aws:iam::123456789012:role/EC2-roles-for-cluster"
 }
 ]
}`

```

The policy has two statements:

- The first statement grants permissions for the MemoryDB actions
  (`memorydb:CreateCluster`,
  `memorydb:DescribeClusters`, and
  `memorydb:UpdateCluster`) on any cluster owned by
  the account.
- The second statement grants permissions for the IAM action
  (`iam:PassRole`) on the IAM role name specified at the
  end of the `Resource` value.
  The policy doesn't specify the `Principal` element because in an
  identity-based policy you don't specify the principal who gets the
  permission. When you attach policy to a user, the user is the implicit principal. When
  you attach a permissions policy to an IAM role, the principal identified in the role's
  trust policy gets the permissions.

For a table showing all of the MemoryDB API actions and the resources that they apply
to, see [MemoryDB API permissions: Actions, resources, and conditions reference](iam.md "iam.md").

## Permissions required to use the MemoryDB console

The permissions reference table lists the MemoryDB API operations and shows the required permissions
for each operation. For more information about MemoryDB API operations, see [MemoryDB API permissions: Actions, resources, and conditions reference](iam.md "iam.md").

To use the MemoryDB console, first grant permissions for additional actions as shown in
the following permissions policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "MinPermsForMemDBConsole",
 "Effect": "Allow",
 "Action": [
 "memorydb:Describe*",
 "memorydb:List*",
 "ec2:DescribeAvailabilityZones",
 "ec2:DescribeVpcs",
 "ec2:DescribeAccountAttributes",
 "ec2:DescribeSecurityGroups",
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:DescribeAlarms",
 "s3:ListAllMyBuckets",
 "sns:ListTopics",
 "sns:ListSubscriptions" ],
 "Resource": "*"
 }
 ]
}`

```

The MemoryDB console needs these additional permissions for the following reasons:

- Permissions for the MemoryDB actions enable the console to display MemoryDB
  resources in the account.
- The console needs permissions for the `ec2` actions to query Amazon EC2 so it
  can display Availability Zones, VPCs, security groups, and account
  attributes.
- The permissions for `cloudwatch` actions enable the console to retrieve Amazon CloudWatch metrics
  and alarms, and display them in the console.
- The permissions for `sns` actions enable the console to retrieve Amazon Simple Notification Service (Amazon SNS) topics and
  subscriptions, and display them in the console.

## Customer-managed policy

examples

If you are not using a default policy and choose to use a custom-managed policy, ensure one
of two things. Either you should have permissions to call
`iam:createServiceLinkedRole` (for more information, see [Example 4: Allow a user to call IAM CreateServiceLinkedRole API](#create-service-linked-role-policy "#create-service-linked-role-policy")). Or you should have created
a MemoryDB service-linked role.

When combined with the minimum permissions needed to use the MemoryDB console,
the example policies in this section grant additional permissions. The examples are
also relevant to the AWS SDKs and the AWS CLI. For more information about what
permissions are needed to use the MemoryDB console, see
[Permissions required to use the MemoryDB console](#iam.identitybasedpolicies.minconpolicies "#iam.identitybasedpolicies.minconpolicies").

For instructions on setting up IAM users and groups, see [Creating Your First IAM User and Administrators Group](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md") in the _IAM User Guide_.

###### Important

Always test your IAM policies thoroughly before using them in production. Some
MemoryDB actions that appear simple can require other actions to support them
when you are using the MemoryDB console. For example,
`memorydb:CreateCluster` grants permissions to create
MemoryDB clusters. However, to perform this operation, the MemoryDB console uses
a number of `Describe` and `List` actions to populate
console lists.

###### Examples

- [Example 1: Allow a user read-only access to MemoryDB resources](#example-allow-list-current-memorydb-resources "#example-allow-list-current-memorydb-resources")
- [Example 2: Allow a user to perform common MemoryDB system administrator tasks](#example-allow-specific-memorydb-actions "#example-allow-specific-memorydb-actions")
- [Example 3: Allow a user to access all MemoryDB API actions](#allow-unrestricted-access "#allow-unrestricted-access")
- [Example 4: Allow a user to call IAM CreateServiceLinkedRole API](#create-service-linked-role-policy "#create-service-linked-role-policy")

### Example 1: Allow a user read-only access to MemoryDB resources

The following policy grants permissions for MemoryDB actions that allow a user to list
resources. Typically, you attach this type of permissions policy to a managers group.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[{
 "Sid": "MemDBUnrestricted",
 "Effect":"Allow",
 "Action": [
 "memorydb:Describe*",
 "memorydb:List*"],
 "Resource":"*"
 }
 ]
}`

```

### Example 2: Allow a user to perform common MemoryDB system administrator tasks

Common system administrator tasks include modifying clusters, parameters, and
parameter groups. A system administrator may also want to get information about the
MemoryDB events. The following policy grants a user permissions to perform MemoryDB actions for
these common system administrator tasks. Typically, you attach this type of permissions
policy to the system administrators group.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "MDBAllowSpecific",
 "Effect": "Allow",
 "Action": [
 "memorydb:UpdateCluster",
 "memorydb:DescribeClusters",
 "memorydb:DescribeEvents",
 "memorydb:UpdateParameterGroup",
 "memorydb:DescribeParameterGroups",
 "memorydb:DescribeParameters",
 "memorydb:ResetParameterGroup"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Example 3: Allow a user to access all MemoryDB API actions

The following policy allows a user to access all MemoryDB actions. We recommend that
you grant this type of permissions policy only to an administrator user.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[{
 "Sid": "MDBAllowAll",
 "Effect":"Allow",
 "Action":[
 "memorydb:*" ],
 "Resource":"*"
 }
 ]
}`

```

### Example 4: Allow a user to call IAM CreateServiceLinkedRole API

The following policy allows user to call the IAM `CreateServiceLinkedRole` API.
We recommend that you grant this type of permissions policy to the user who invokes mutative MemoryDB operations.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"CreateSLRAllows",
 "Effect":"Allow",
 "Action":[
 "iam:CreateServiceLinkedRole"
 ],
 "Resource":"*",
 "Condition":{
 "StringLike":{
 "iam:AWSServiceName":"memorydb.amazonaws.com"
 }
 }
 }
 ]
}`

```
