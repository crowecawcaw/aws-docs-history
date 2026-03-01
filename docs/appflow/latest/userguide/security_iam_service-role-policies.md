# Service role policies for Amazon AppFlow

A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

###### Warning

Changing the permissions for a service role might break Amazon AppFlow functionality. Edit
service roles only when Amazon AppFlow provides guidance to do so.

###### Topics

- [Allow Amazon AppFlow to access the AWS Glue Data Catalog](#access-gdc "#access-gdc")
- [Allow Amazon AppFlow to access Amazon Redshift databases with the Data API](#access-redshift "#access-redshift")
- [Allow Amazon Redshift to access your Amazon AppFlow data in Amazon S3](#redshift-access-s3 "#redshift-access-s3")

## Allow Amazon AppFlow to access the AWS Glue Data Catalog

Before you can create a flow that catalogs its output data in the AWS Glue Data Catalog, you
must grant Amazon AppFlow the required permissions. Amazon AppFlow requires permissions to create
Data Catalog tables, databases, and partitions. To grant the required permissions, you
provide an IAM role that contains the following permissions policy and trust policy.
You provide this role to Amazon AppFlow in the settings for your flows.

###### Example permissions policy

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "glue:BatchCreatePartition",
 "glue:CreatePartitionIndex",
 "glue:DeleteDatabase",
 "glue:GetTableVersions",
 "glue:GetPartitions",
 "glue:BatchDeletePartition",
 "glue:DeleteTableVersion",
 "glue:UpdateTable",
 "glue:DeleteTable",
 "glue:DeletePartitionIndex",
 "glue:GetTableVersion",
 "glue:CreatePartition",
 "glue:UntagResource",
 "glue:UpdatePartition",
 "glue:TagResource",
 "glue:UpdateDatabase",
 "glue:CreateTable",
 "glue:BatchUpdatePartition",
 "glue:GetTables",
 "glue:BatchGetPartition",
 "glue:GetDatabases",
 "glue:GetPartitionIndexes",
 "glue:GetTable",
 "glue:GetDatabase",
 "glue:GetPartition",
 "glue:CreateDatabase",
 "glue:BatchDeleteTableVersion",
 "glue:BatchDeleteTable",
 "glue:DeletePartition"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Example trust policy

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal":
 {
 "Service": "appflow.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

## Allow Amazon AppFlow to access Amazon Redshift databases with the Data API

Before you can create a flow that transfers data to an Amazon Redshift database by using the Amazon Redshift
Data API, you must grant Amazon AppFlow the required permissions. Amazon AppFlow requires permissions
to do the following with your Amazon Redshift database:

- Gain access through temporary credentials
- Run SQL statements

To grant those permissions, you create an IAM role that contains the permissions
policy and trust policy below. You provide this role to Amazon AppFlow in the settings for your Amazon Redshift
connections.

###### Example permissions policy

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DataAPIPermissions",
 "Effect": "Allow",
 "Action": [
 "redshift-data:ExecuteStatement",
 "redshift-data:GetStatementResult",
 "redshift-data:DescribeStatement"
 ],
 "Resource": "*"
 },
 {
 "Sid": "GetCredentialsForAPIUser",
 "Effect": "Allow",
 "Action": "redshift:GetClusterCredentials",
 "Resource": [
 "arn:aws:redshift:*:*:dbname:*/*",
 "arn:aws:redshift:*:*:dbuser:*/*"
 ]
 },
 {
 "Sid": "GetCredentialsForServerless",
 "Effect": "Allow",
 "Action": "redshift-serverless:GetCredentials",
 "Resource": "*",
 "Condition":
 {
 "StringLike":
 {
 "aws:ResourceTag/RedshiftDataFullAccess": "*"
 }
 }
 },
 {
 "Sid": "DenyCreateAPIUser",
 "Effect": "Deny",
 "Action": "redshift:CreateClusterUser",
 "Resource": [
 "arn:aws:redshift:*:*:dbuser:*/*"
 ]
 },
 {
 "Sid": "ServiceLinkedRole",
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/redshift-data.amazonaws.com/AWSServiceRoleForRedshift",
 "Condition":
 {
 "StringLike":
 {
 "iam:AWSServiceName": "redshift-data.amazonaws.com"
 }
 }
 }
 ]
}`

```

###### Tag condition for Amazon Redshift Serverless resources

In the example permissions policy, the statement that grants the
`redshift-serverless:GetCredentials` action has the following condition
block:

```
"Condition":
{
  "StringLike":
  {
    "aws:ResourceTag/RedshiftDataFullAccess": "*"
  }
}
```

In IAM policies, `condition` is an optional element that specifies
conditions for when a policy is in effect. With this condition block, the policy allows
Amazon AppFlow to get temporary credentials for only those Amazon Redshift Serverless resources that meet the
condition. To meet the condition, the resources must be tagged with the key
`RedshiftDataFullAccess`. Therefore, to use this policy, you must apply that
tag to the appropriate workgroup.

For more information about tagging resources in Amazon Redshift Serverless, see [Tagging resources overview](../../../redshift/latest/mgmt/serverless-tagging-resources.md "../../../redshift/latest/mgmt/serverless-tagging-resources.md") in the _Amazon Redshift Management
Guide_.

###### Example trust policy

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal":
 {
 "Service": "appflow.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

For more information about authorizing access to the Data API, see [Authorizing access to
the Amazon Redshift Data API](../../../redshift/latest/mgmt/data-api-access.md "../../../redshift/latest/mgmt/data-api-access.md") in the _Amazon Redshift Management
Guide_.

## Allow Amazon Redshift to access your Amazon AppFlow data in Amazon S3

When you run a flow that transfers data to an Amazon Redshift database, Amazon AppFlow first stores the data
in an S3 bucket that you provide. Then, Amazon Redshift gets the data from the S3 bucket. For the flow to
run successfully, you must authorize Amazon Redshift to get and decrypt the data. To grant those
permission, you create an IAM role that contains the permissions policies and trust policy
below.

You provide the IAM role in the settings when you create an Amazon Redshift connection in
Amazon AppFlow.

You must also associate the role with the Amazon Redshift cluster that receives the data that you
transfer with Amazon AppFlow. For the steps to associate the role, see [Associating IAM roles with clusters](../../../redshift/latest/mgmt/copy-unload-iam-role.md#copy-unload-iam-role-associating-with-clusters "../../../redshift/latest/mgmt/copy-unload-iam-role.md#copy-unload-iam-role-associating-with-clusters") in the _Amazon Redshift
Management Guide_.

###### Example permissions policies

To provide the required permissions to Amazon Redshift, you can attach the following permissions
policies to the IAM role:

- The AWS managed policy AmazonS3ReadOnlyAccess. This policy is owned and maintained
  by AWS. It grants read-only access to Amazon S3. To view the permissions for this policy, see
  [AmazonS3ReadOnlyAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess$jsonEditor "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess$jsonEditor") in the AWS Management Console.
- A policy that permits Amazon Redshift to decrypt the encrypted data that Amazon AppFlow stores in Amazon S3,
  such as the following example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "kms:Decrypt",
 "Resource": "*"
 }
 ]
}`

```

###### Example trust policy

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal":
 {
 "Service": "redshift.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```
