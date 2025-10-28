Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Using Identity-Based Policies

(IAM Policies) for AWS Snowball Edge

This topic provides examples of identity-based policies that demonstrate how an
account administrator can attach permissions policies to IAM identities (that is,
users, groups, and roles). These policies thereby grant permissions to perform
operations on AWS Snowball Edge resources in the AWS Cloud.

###### Important

We recommend that you first review the introductory topics that explain the basic
concepts and options available for you to manage access to your AWS Snowball Edge
resources. For more information, see [Overview of Managing Access Permissions to
Your Resources in the AWS Cloud](authentication-and-access-control.md#access-control-overview "authentication-and-access-control.md#access-control-overview").

The sections in this topic cover the following:

- [Permissions Required to
  Use the AWS Snowball Edge Console](#additional-console-required-permissions "#additional-console-required-permissions")
- [AWS-Managed (Predefined)
  Policies for AWS Snowball Edge](authentication-and-access-control.md#access-policy-examples-aws-managed "authentication-and-access-control.md#access-policy-examples-aws-managed")
- [Customer Managed Policy
  Examples](access-policy-examples-for-sdk-cli.md "access-policy-examples-for-sdk-cli.md")
  The following shows an example of a permissions policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation",
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": "arn:aws:s3:::*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "snowball:*",
 "importexport:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

The policy has two statements:

- The first statement grants permissions for three Amazon S3 actions
  (`s3:GetBucketLocation`, `s3:GetObject`, and
  `s3:ListBucket`) on all Amazon S3 buckets using the _Amazon
  Resource Name (ARN)_ of `arn:aws:s3:::*`. The ARN
  specifies a wildcard character (\*) so the user can choose any or all Amazon S3
  buckets to export data from.
- The second statement grants permissions for all AWS Snowball Edge actions. Because
  these actions don't support resource-level permissions, the policy specifies the
  wildcard character (\*) and the `Resource` value also specifies a wild
  card character.
  The policy doesn't specify the `Principal` element because in an
  identity-based policy you don't specify the principal who gets the permission. When you
  attach a policy to a user, the user is the implicit principal. When you attach a
  permissions policy to an IAM role, the principal identified in the role's trust policy
  gets the permissions.

For a table showing all of the AWS Snowball Edge job management API actions and the
resources that they apply to, see [AWS Snowball Edge API Permissions: Actions,
Resources, and Conditions Reference](access-policy-examples-for-sdk-cli.md#snowball-api-permissions-ref "access-policy-examples-for-sdk-cli.md#snowball-api-permissions-ref").

## Permissions Required to

Use the AWS Snowball Edge Console

The permissions reference table lists the AWS Snowball Edge job management API
operations and shows the required permissions for each operation. For more
information about job management API operations, see [AWS Snowball Edge API Permissions: Actions,
Resources, and Conditions Reference](access-policy-examples-for-sdk-cli.md#snowball-api-permissions-ref "access-policy-examples-for-sdk-cli.md#snowball-api-permissions-ref").

To use the AWS Snow Family Management Console, you need to grant permissions for additional actions as
shown in the following permissions policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation",
 "s3:GetBucketPolicy",
 "s3:ListBucket",
 "s3:ListBucketMultipartUploads",
 "s3:ListAllMyBuckets"
 ],
 "Resource": "arn:aws:s3:::*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucket",
 "s3:PutObject",
 "s3:AbortMultipartUpload",
 "s3:ListMultipartUploadParts",
 "s3:PutObjectAcl"
 ],
 "Resource": "arn:aws:s3:::*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "lambda:GetFunction",
 "lambda:GetFunctionConfiguration"
 ],
 "Resource": "arn:aws:lambda:*::function:*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "lambda:ListFunctions"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:CreateGrant",
 "kms:GenerateDataKey",
 "kms:Decrypt",
 "kms:Encrypt",
 "kms:RetireGrant",
 "kms:ListKeys",
 "kms:DescribeKey",
 "kms:ListAliases"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:CreatePolicy",
 "iam:CreateRole",
 "iam:ListRoles",
 "iam:ListRolePolicies",
 "iam:PutRolePolicy"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::*:role/snowball*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "importexport.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeImages",
 "ec2:ModifyImageAttribute"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "sns:CreateTopic",
 "sns:ListTopics",
 "sns:GetTopicAttributes",
 "sns:SetTopicAttributes",
 "sns:ListSubscriptionsByTopic",
 "sns:Subscribe"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "greengrass:getServiceRoleForAccount"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "snowball:*"
 ],
 "Resource": [
 "*"
 ]
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
 "s3:GetBucketLocation",
 "s3:GetBucketPolicy",
 "s3:ListBucket",
 "s3:ListBucketMultipartUploads",
 "s3:ListAllMyBuckets"
 ],
 "Resource": "arn:aws:s3:::*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucket",
 "s3:PutObject",
 "s3:AbortMultipartUpload",
 "s3:ListMultipartUploadParts",
 "s3:PutObjectAcl"
 ],
 "Resource": "arn:aws:s3:::*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "lambda:GetFunction",
 "lambda:GetFunctionConfiguration"
 ],
 "Resource": "arn:aws:lambda:*:*:function:*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "lambda:ListFunctions"
 ],
 "Resource": "arn:aws:lambda:*:*:*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:CreatePolicy",
 "iam:CreateRole",
 "iam:ListRoles",
 "iam:ListRolePolicies",
 "iam:PutRolePolicy"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::*:role/snowball*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "importexport.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeImages",
 "ec2:ModifyImageAttribute"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "sns:CreateTopic",
 "sns:ListTopics",
 "sns:GetTopicAttributes",
 "sns:SetTopicAttributes",
 "sns:ListSubscriptionsByTopic",
 "sns:Subscribe"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "greengrass:getServiceRoleForAccount"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "snowball:*"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

The AWS Snowball Edge console needs these additional permissions for the following
reasons:

- `ec2:` – These allow the user to describe Amazon EC2-compatible instances
  and modify their attributes for local compute purposes. For more
  information, see [Using Amazon EC2-compatible compute instances on Snowball Edge](using-ec2.md "using-ec2.md").
- `kms:` – These allow the user to create or choose the KMS
  key that will encrypt your data. For more information, see [AWS Key Management Service in AWS Snowball Edge](data-protection.md#kms "data-protection.md#kms").
- `iam:` – These allow the user to create or choose an IAM
  role ARN that AWS Snowball Edge will assume to access the AWS resources
  associated with job creation and processing.
- `sns:` – These allow the user to create or choose the
  Amazon SNS notifications for the jobs they create. For more information, see
  [Notifications for Snowball Edge](notifications.md "notifications.md").
