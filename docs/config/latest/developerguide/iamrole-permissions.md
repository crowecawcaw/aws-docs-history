# Permissions for the IAM Role Assigned to AWS Config

An IAM role lets you define a set of permissions. AWS Config assumes the role that you assign to
it to write to your S3 bucket, publish to your SNS topic, and make `Describe` or
`List` API requests to get configuration details for your AWS resources. For more
information about IAM roles, see [IAM
Roles](../../../IAM/latest/UserGuide/WorkingWithRoles.md "../../../IAM/latest/UserGuide/WorkingWithRoles.md") in the _IAM User Guide_.

When you use the AWS Config console to create or update an IAM role, AWS Config automatically attaches
the required permissions for you. For more information, see [Setting Up AWS Config with the Console](gs-console.md "gs-console.md").

###### Policies and compliance results

[IAM policies](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md")
and [other policies managed in AWS Organizations](../../../organizations/latest/userguide/orgs_manage_policies.md "../../../organizations/latest/userguide/orgs_manage_policies.md")
can impact whether AWS Config
has permissions to record configuration changes for your resources.
Additionally, rules directly evaluate the configuration of a resource and rules don't take into account these policies when running evaluations. Make sure that the policies in effect align with how you intend to use AWS Config.

###### Contents

- [Creating IAM Role Policies](iamrole-permissions.md#iam-role-policies "iamrole-permissions.md#iam-role-policies")
  - [Adding an IAM Trust Policy to your Role](iamrole-permissions.md#iam-trust-policy "iamrole-permissions.md#iam-trust-policy")
  - [IAM Role Policy for your S3 Bucket](iamrole-permissions.md#iam-role-policies-S3-bucket "iamrole-permissions.md#iam-role-policies-S3-bucket")
  - [IAM Role Policy for KMS Key](iamrole-permissions.md#iam-role-policies-S3-kms-key "iamrole-permissions.md#iam-role-policies-S3-kms-key")
  - [IAM Role Policy for Amazon SNS Topic](iamrole-permissions.md#iam-role-policies-sns-topic "iamrole-permissions.md#iam-role-policies-sns-topic")
  - [IAM Role Policy for Getting
    Configuration Details](iamrole-permissions.md#iam-role-policies-describe-apis "iamrole-permissions.md#iam-role-policies-describe-apis")
  - [Managing Permissions for S3
    Bucket Recording](iamrole-permissions.md#troubleshooting-recording-s3-bucket-policy "iamrole-permissions.md#troubleshooting-recording-s3-bucket-policy")

## Creating IAM Role Policies

When you use the AWS Config console to create an IAM role, AWS Config automatically attaches the
required permissions to the role for you.

If you are using the AWS CLI to set up AWS Config or you are updating an existing IAM role, you
must manually update the policy to allow AWS Config to access your S3 bucket, publish to your SNS
topic, and get configuration details about your resources.

### Adding an IAM Trust Policy to your Role

You can create an IAM trust policy that enables AWS Config to assume a role and use it to
track your resources. For more information about trust policies, see [Roles terms and concepts](../../../IAM/latest/UserGuide/d_roles_terms-and-concepts.md "../../../IAM/latest/UserGuide/d_roles_terms-and-concepts.md") in the*IAM User Guide*.

The following is an example trust policy for AWS Config roles:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "config.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "AWS:SourceAccount": "`sourceAccountID`"
 }
 }
 }
 ]
}`

```

You can use the `AWS:SourceAccount` condition in the IAM Role Trust
relationship above to restrict the Config service principal to only interact with the AWS
IAM Role when performing operations on behalf of specific accounts.

AWS Config also supports the `AWS:SourceArn` condition which restricts the Config
service principal to only assume the IAM Role when performing operations on behalf of the
owning account. When using the AWS Config service principal, the `AWS:SourceArn`
property will always be set to `arn:aws:config:sourceRegion:sourceAccountID:*`
where `sourceRegion` is the region of the customer managed configuration recorder and
`sourceAccountID` is the ID of the account containing the customer managed configuration recorder.

For example, add the following condition restrict the Config service principal to only
assume the IAM Role only on behalf of a customer managed configuration recorder in the
`us-east-1` region in the account `123456789012`: `"ArnLike":
 {"AWS:SourceArn": "arn:aws:config:us-east-1:123456789012:*"}`.

### IAM Role Policy for your S3 Bucket

The following example policy grants AWS Config permission to access your S3 bucket:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "s3:PutObject",
 "s3:PutObjectAcl"
 ],
 "Resource":[
 "arn:aws:s3:::`amzn-s3-demo-bucket`/`prefix`/AWSLogs/`myAccountID`/*"
 ],
 "Condition":{
 "StringLike":{
 "s3:x-amz-acl":"bucket-owner-full-control"
 }
 }
 },
 {
 "Effect":"Allow",
 "Action":[
 "s3:GetBucketAcl"
 ],
 "Resource":"arn:aws:s3:::`amzn-s3-demo-bucket`"
 }
 ]
}`

```

### IAM Role Policy for KMS Key

The following example policy grants AWS Config permission to use KMS-based encryption on new
objects for S3 bucket delivery:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012"
 }
 ]
}`

```

### IAM Role Policy for Amazon SNS Topic

The following example policy grants AWS Config permission to access your SNS topic:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [
 {
 "Effect":"Allow",
 "Action":"sns:Publish",
 "Resource":"arn:aws:sns:us-east-1:123456789012:MyTopic"
 }
 ]
}`

```

If your SNS topic is encrypted for additional setup instructions, see [Configuring
AWS KMS Permissions](../../../sns/latest/dg/sns-server-side-encryption.md#sns-what-permissions-for-sse "../../../sns/latest/dg/sns-server-side-encryption.md#sns-what-permissions-for-sse") in the _Amazon Simple Notification Service Developer Guide_.

### IAM Role Policy for Getting

Configuration Details

It is recommended to use the AWS Config service-linked role: `AWSServiceRoleForConfig`. Service-linked roles are predefined and include all the permissions that AWS Config requires to call other AWS services. The AWS Config service-linked role is required for service-linked configuration recorders.
For more information, see [Using Service-Linked Roles for AWS Config](using-service-linked-roles.md "using-service-linked-roles.md").

If you create or update a role with the console, AWS Config attaches the **AWSServiceRoleForConfig** for you.

If you use the AWS CLI, use the `attach-role-policy` command and specify the
Amazon Resource Name (ARN) for **AWSServiceRoleForConfig**:

```
$ `aws iam attach-role-policy --role-name `myConfigRole` --policy-arn arn:aws:iam::aws:policy/aws-service-role/AWSServiceRoleForConfig`
```

### Managing Permissions for S3

Bucket Recording

AWS Config records and delivers notifications when an S3 bucket is created, updated, or
deleted.

It is recommended to use the AWS Config service-linked role: `AWSServiceRoleForConfig`. Service-linked roles are predefined and include all the permissions that AWS Config requires to call other AWS services. The AWS Config service-linked role is required for service-linked configuration recorders.
For more information, see [Using Service-Linked Roles for AWS Config](using-service-linked-roles.md "using-service-linked-roles.md").
