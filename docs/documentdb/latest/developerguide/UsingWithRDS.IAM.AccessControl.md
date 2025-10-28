# Using identity-based policies (IAM policies) for Amazon DocumentDB

###### Important

For certain management features, Amazon DocumentDB uses operational technology that is shared with Amazon RDS. Amazon DocumentDB console, AWS CLI, and API calls are logged as calls made to the Amazon RDS API.

We recommend that you first review the introductory topics that explain the basic concepts and options available for you to manage access to your Amazon DocumentDB resources. For more information, see [Managing access permissions to your Amazon DocumentDB resources](UsingWithRDS.IAM.AccessControl.md "UsingWithRDS.IAM.AccessControl.md").

This topic provides examples of identity-based policies in which an account administrator can attach permissions policies to IAM identities (that is, users, groups, and roles).

The following is an example of an IAM policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCreateDBInstanceOnly",
 "Effect": "Allow",
 "Action": [
 "rds:CreateDBInstance"
 ],
 "Resource": [
 "arn:aws:rds:*:123456789012:db:test*",
 "arn:aws:rds:*:123456789012:pg:cluster-pg:default*",
 "arn:aws:rds:*:123456789012:subgrp:default"
 ]
 }
 ]
}`

```

The policy includes a single statement that specifies the following permissions for the IAM user:

- The policy allows the IAM user to create an instance using the [CreateDBInstance](API_CreateDBInstance.md "API_CreateDBInstance.md") action (this also applies to the
  [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") AWS CLI operation and the AWS Management Console).
- The `Resource` element specifies that the user can perform actions on or with resources. You specify resources using an Amazon Resource Name (ARN). This ARN includes the name of the service that the resource belongs to (`rds`), the AWS Region (`*` indicates any Region in this example), the user account number (`123456789012` is the user ID in this example), and the type of resource.

The `Resource` element in the example specifies the following policy constraints on resources for the user:

    + The instance identifier for the new instance must begin with `test` (for example, `testCustomerData1`,
     `test-region2-data`).
    + The cluster parameter group for the new instance must begin with `default`.
    + The subnet group for the new instance must be the `default` subnet group.

The policy doesn't specify the `Principal` element because in an identity-based policy you don't specify the principal who gets the permission. When you attach policy to a user, the user is the implicit principal. When you attach a permissions policy to an IAM role, the principal identified in the role's trust policy gets the permissions.

For a table showing all of the Amazon DocumentDB API operations and the resources that they apply to, see [Amazon DocumentDB API permissions: actions, resources, and conditions reference](UsingWithRDS.IAM.md "UsingWithRDS.IAM.md").

## Permissions required to use the Amazon DocumentDB console

For a user to work with the Amazon DocumentDB console, that user must have a minimum set of permissions. These permissions allow the user to describe the Amazon DocumentDB resources for their AWS account and to provide other related information, including Amazon EC2 security and network information.

If you create an IAM policy that is more restrictive than the minimum required permissions, the console won't function as intended for users
with that IAM policy. To ensure that those users can still use the Amazon DocumentDB console, also attach the `AmazonDocDBConsoleFullAccess`
managed policy to the user, as described in [AWS managed policies for Amazon DocumentDB](docdb-managed-policies.md "docdb-managed-policies.md").

You don't need to allow minimum console permissions for users that are making calls only to the AWS CLI or the Amazon DocumentDB API.

## Customer managed policy examples

In this section, you can find example user policies that grant permissions for various Amazon DocumentDB actions. These policies work when you are using Amazon DocumentDB API actions, AWS SDKs, or the AWS CLI. When you are using the console, you need to grant additional permissions specific to the console, which is discussed in [Permissions required to use the Amazon DocumentDB console](#UsingWithRDS.IAM.RequiredPermissions.Console "#UsingWithRDS.IAM.RequiredPermissions.Console").

For certain management features, Amazon DocumentDB uses operational technology that is shared with Amazon Relational Database Service (Amazon RDS) and Amazon Neptune.

###### Note

All examples use the US East (N. Virginia) Region (`us-east-1`) and contain fictitious account IDs.

###### Examples

- [Example 1: Allow a user to perform any describe action on any Amazon DocumentDB resource](#IAMPolicyExamples-RDS-perform-describe-action "#IAMPolicyExamples-RDS-perform-describe-action")
- [Example 2: Prevent a user from deleting an instance](#IAMPolicyExamples-RDS-prevent-db-deletion "#IAMPolicyExamples-RDS-prevent-db-deletion")
- [Example 3: Prevent a user from creating a cluster unless storage encryption is enabled](#IAMPolicyExamples-Prevent-Cluster "#IAMPolicyExamples-Prevent-Cluster")

### Example 1: Allow a user to perform any describe action on any Amazon DocumentDB resource

The following permissions policy grants permissions to a user to run all of the actions that begin with `Describe`. These actions show information about an Amazon DocumentDB resource, such as an instance.
The wildcard character (\*) in the `Resource` element indicates that the actions are allowed for all Amazon DocumentDB resources that are owned by the account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"AllowRDSDescribe",
 "Effect":"Allow",
 "Action":"rds:Describe*",
 "Resource":"*"
 }
 ]
}`

```

### Example 2: Prevent a user from deleting an instance

The following permissions policy grants permissions to prevent a user from deleting a specific instance. For example, you might want to deny the ability to delete your production instances to any user that is not an administrator.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"DenyDelete1",
 "Effect":"Deny",
 "Action":"rds:DeleteDBInstance",
 "Resource":"arn:aws:rds:us-east-1:123456789012:db:my-db-instance"
 }
 ]
}`

```

### Example 3: Prevent a user from creating a cluster unless storage encryption is enabled

The following permissions policy denies permissions to a user from creating an Amazon DocumentDB cluster unless storage encryption is enabled.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PreventUnencryptedDocumentDB",
 "Effect": "Deny",
 "Action": "RDS:CreateDBCluster",
 "Condition": {
 "Bool": {
 "rds:StorageEncrypted": "false"
 },
 "StringEquals": {
 "rds:DatabaseEngine": "docdb"
 }
 },
 "Resource": "*"
 }
 ]
}`

```
