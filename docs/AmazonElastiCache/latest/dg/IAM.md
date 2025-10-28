# Using identity-based policies (IAM policies) for Amazon ElastiCache

This topic provides examples of identity-based policies in which an account
administrator can attach permissions policies to IAM identities (that is, users, groups,
and roles).

###### Important

We recommend that you first read the topics that explain the basic concepts and options to
manage access to Amazon ElastiCache resources. For more information, see [Overview of managing access permissions to your ElastiCache resources](IAM.md "IAM.md").

The sections in this topic cover the following:

- [AWS managed policies for Amazon ElastiCache](IAM.IdentityBasedPolicies.md "IAM.IdentityBasedPolicies.md")
- [Customer-managed policy
  examples](#IAM.IdentityBasedPolicies.CustomerManagedPolicies "#IAM.IdentityBasedPolicies.CustomerManagedPolicies")
  The following shows an example of a permissions policy when using Redis OSS.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowClusterPermissions",
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateServerlessCache",
 "elasticache:CreateCacheCluster",
 "elasticache:DescribeServerlessCaches",
 "elasticache:DescribeReplicationGroups",
 "elasticache:DescribeCacheClusters",
 "elasticache:ModifyServerlessCache",
 "elasticache:ModifyReplicationGroup",
 "elasticache:ModifyCacheCluster"
 ],
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

The following shows an example of a permissions policy when using Memcached.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "AllowClusterPermissions",
 "Effect": "Allow",
 "Action": [
 "elasticache:CreateServerlessCache",
 "elasticache:CreateCacheCluster",
 "elasticache:DescribeServerlessCaches",
 "elasticache:DescribeCacheClusters",
 "elasticache:ModifyServerlessCache",
 "elasticache:ModifyCacheCluster"
 ],
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

- The first statement grants permissions for the Amazon ElastiCache actions
  (`elasticache:Create*`,
  `elasticache:Describe*`,
  `elasticache:Modify*`)
- The second statement grants permissions for the IAM action
  (`iam:PassRole`) on the IAM role name specified at the
  end of the `Resource` value.
  The policy doesn't specify the `Principal` element because in an
  identity-based policy you don't specify the principal who gets the
  permission. When you attach policy to a user, the user is the implicit principal. When
  you attach a permissions policy to an IAM role, the principal identified in the role's
  trust policy gets the permissions.

For a table showing all of the Amazon ElastiCache API actions and the resources that they apply
to, see [ElastiCache API permissions: Actions, resources, and conditions reference](IAM.md "IAM.md").

## Customer-managed policy

examples

If you are not using a default policy and choose to use a custom-managed policy, ensure one
of two things. Either you should have permissions to call
`iam:createServiceLinkedRole` (for more information, see [Example 4: Allow a user to call IAM CreateServiceLinkedRole API](#create-service-linked-role-policy "#create-service-linked-role-policy")). Or you should have created
an ElastiCache service-linked role.

When combined with the minimum permissions needed to use the Amazon ElastiCache console,
the example policies in this section grant additional permissions. The examples are
also relevant to the AWS SDKs and the AWS CLI.

For instructions on setting up IAM users and groups, see [Creating Your First IAM User and Administrators Group](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md") in the _IAM User Guide_.

###### Important

Always test your IAM policies thoroughly before using them in production. Some
ElastiCache actions that appear simple can require other actions to support them
when you are using the ElastiCache console. For example,
`elasticache:CreateCacheCluster` grants permissions to create
ElastiCache clusters. However, to perform this operation, the ElastiCache console uses
a number of `Describe` and `List` actions to populate
console lists.

###### Examples

- [Example 1: Allow a user read-only access to ElastiCache resources](#example-allow-list-current-elasticache-resources "#example-allow-list-current-elasticache-resources")
- [Example 2: Allow a user to perform common ElastiCache system administrator tasks](#example-allow-specific-elasticache-actions "#example-allow-specific-elasticache-actions")
- [Example 3: Allow a user to access all ElastiCache API actions](#allow-unrestricted-access "#allow-unrestricted-access")
- [Example 4: Allow a user to call IAM CreateServiceLinkedRole API](#create-service-linked-role-policy "#create-service-linked-role-policy")
- [Example 5: Allow a user to connect to serverless cache using IAM authentication](#iam-connect-policy "#iam-connect-policy")

### Example 1: Allow a user read-only access to ElastiCache resources

The following policy grants permissions ElastiCache actions that allow a user to list
resources. Typically, you attach this type of permissions policy to a managers group.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[{
 "Sid": "ECReadOnly",
 "Effect":"Allow",
 "Action": [
 "elasticache:Describe*",
 "elasticache:List*"],
 "Resource":"*"
 }
 ]
}`

```

### Example 2: Allow a user to perform common ElastiCache system administrator tasks

Common system administrator tasks include modifying resources. A system administrator may
also want to get information about the
ElastiCache events. The following policy grants a user permissions to perform ElastiCache actions for
these common system administrator tasks. Typically, you attach this type of permissions
policy to the system administrators group.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[{
 "Sid": "ECAllowMutations",
 "Effect":"Allow",
 "Action":[
 "elasticache:Modify*",
 "elasticache:Describe*",
 "elasticache:ResetCacheParameterGroup"
 ],
 "Resource":"*"
 }
 ]
}`

```

### Example 3: Allow a user to access all ElastiCache API actions

The following policy allows a user to access all ElastiCache actions. We recommend that
you grant this type of permissions policy only to an administrator user.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[{
 "Sid": "ECAllowAll",
 "Effect":"Allow",
 "Action":[
 "elasticache:*"
 ],
 "Resource":"*"
 }
 ]
}`

```

### Example 4: Allow a user to call IAM CreateServiceLinkedRole API

The following policy allows user to call the IAM `CreateServiceLinkedRole` API.
We recommend that you grant this type of permissions policy to the user who invokes mutative ElastiCache operations.

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
 "iam:AWSServiceName":"elasticache.amazonaws.com"
 }
 }
 }
 ]
}`

```

### Example 5: Allow a user to connect to serverless cache using IAM authentication

The following policy allows any user to connect to any serverless cache using IAM authentication between 2023-04-01 and 2023-06-30.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement" :
 [
 {
 "Effect" : "Allow",
 "Action" : ["elasticache:Connect"],
 "Resource" : [
 "arn:aws:elasticache:us-east-1:123456789012:serverlesscache:*"
 ],
 "Condition": {
 "DateGreaterThan": {"aws:CurrentTime": "2023-04-01T00:00:00Z"},
 "DateLessThan": {"aws:CurrentTime": "2023-06-30T23:59:59Z"}
 }
 },
 {
 "Effect" : "Allow",
 "Action" : ["elasticache:Connect"],
 "Resource" : [
 "arn:aws:elasticache:us-east-1:123456789012:user:*"
 ]
 }
 ]
}`

```
