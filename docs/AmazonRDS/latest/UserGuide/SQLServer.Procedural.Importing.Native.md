# Setting up for native backup and restore

To set up for native backup and restore, you need three components:

1. An Amazon S3 bucket to store your backup files.

You must have an S3 bucket to use for your backup files and then upload backups you want
to migrate to RDS. If you already have an Amazon S3 bucket, you can use that. If you don't, you can
[create a bucket](../../../AmazonS3/latest/userguide/CreatingaBucket.md "../../../AmazonS3/latest/userguide/CreatingaBucket.md"). Alternatively, you can
choose to have a new bucket created for you when you add the `SQLSERVER_BACKUP_RESTORE`
option by using the AWS Management Console.

For information on using S3, see the [Amazon Simple Storage Service User Guide](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md") 2. An AWS Identity and Access Management (IAM) role to access the bucket.

If you already have an IAM role, you can use that. You can choose to have a new IAM role created for you when you add the
`SQLSERVER_BACKUP_RESTORE` option by using the AWS Management Console. Alternatively, you can create a new one
manually.

If you want to create a new IAM role manually, take the approach discussed in the next section. Do the same if you want to
attach trust relationships and permissions policies to an existing IAM role. 3. The `SQLSERVER_BACKUP_RESTORE` option added to an option group on your DB instance.

To enable native backup and restore on your DB instance, you add the `SQLSERVER_BACKUP_RESTORE`
option to an option group on your DB instance. For more information and instructions, see
[Support for native backup and restore in SQL Server](Appendix.SQLServer.Options.md "Appendix.SQLServer.Options.md").

## Manually creating an IAM role for native backup and restore

If you want to manually create a new IAM role to use with native backup and restore, you can do so. In this case, you create a
role to delegate permissions from the Amazon RDS service to your Amazon S3 bucket. When you create an IAM role, you attach a trust
relationship and a permissions policy. The trust relationship allows RDS to assume this role. The permissions policy defines
the actions this role can perform. For more information about creating the role, see
[Creating a role to delegate permissions to an AWS
service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md").

For the native backup and restore feature, use trust relationships and permissions policies similar to the examples in this
section. In the following example, we use the service principal name `rds.amazonaws.com` as an alias for all
service accounts. In the other examples, we specify an Amazon Resource Name (ARN) to identify another account, user, or role
that we're granting access to in the trust policy.

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and
[`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource-based trust relationships to limit
the service's permissions to a specific resource. This is the most effective way to protect against the [confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md").

You might use both global condition context keys and have the `aws:SourceArn` value contain the account ID. In
this case, the `aws:SourceAccount` value and the account in the `aws:SourceArn` value must use the
same account ID when used in the same statement.

- Use `aws:SourceArn` if you want cross-service access for a single resource.
- Use `aws:SourceAccount` if you want to allow any resource in that account to be associated with the
  cross-service use.

In the trust relationship, make sure to use the `aws:SourceArn` global condition context key with the full ARN
of the resources accessing the role. For native backup and restore, make sure to include both the DB option group and the DB
instances, as shown in the following example.

###### Example of trust relationship with global condition context key for native backup and restore

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "rds.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": [
 "arn:aws:rds:`Region`:`0123456789`:db:`db_instance_identifier`",
 "arn:aws:rds:`Region`:`0123456789`:og:`option_group_name`"
 ],
 "aws:SourceAccount": "`0123456789`"
 }
 }
 }
 ]
}`

```

The following example uses an ARN to specify a resource. For more information on using
ARNs, see [Amazon resource
names (ARNs)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

###### Example of permissions policy for native backup and restore without encryption support

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [
 {
 "Effect": "Allow",
 "Action":
 [
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`"
 },
 {
 "Effect": "Allow",
 "Action":
 [
 "s3:GetObjectAttributes",
 "s3:GetObject",
 "s3:PutObject",
 "s3:ListMultipartUploadParts",
 "s3:AbortMultipartUpload"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 }
 ]
}`

```

###### Example permissions policy for native backup and restore with encryption support

If you want to encrypt your backup files, include an encryption key in your permissions policy. For more information about encryption keys, see [Getting started](../../../kms/latest/developerguide/getting-started.md "../../../kms/latest/developerguide/getting-started.md") in the _AWS Key Management Service Developer Guide_.

###### Note

You must use a symmetric encryption KMS key to encrypt your backups. Amazon RDS doesn't support asymmetric KMS keys. For more
information, see [Creating symmetric encryption KMS keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS Key Management Service Developer Guide_.

The IAM role must also be a key user and key administrator for the KMS key, that is, it must be specified in the key policy.
For more information, see [Creating symmetric encryption
KMS keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS Key Management Service Developer Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAccessToKey",
 "Effect": "Allow",
 "Action": [
 "kms:DescribeKey",
 "kms:GenerateDataKey",
 "kms:Encrypt",
 "kms:Decrypt"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`123456789012`:key/`key-id`"
 },
 {
 "Sid": "AllowAccessToS3",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`"
 },
 {
 "Sid": "GetS3Info",
 "Effect": "Allow",
 "Action": [
 "s3:GetObjectAttributes",
 "s3:GetObject",
 "s3:PutObject",
 "s3:ListMultipartUploadParts",
 "s3:AbortMultipartUpload"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 }
 ]
}`

```

###### Example permissions policy for native backup and restore using access points without encryption support

The actions required to use S3 access points are the same as for S3 buckets. The resource path is updated to match the S3 access point ARN pattern.

###### Note

Access points must be configured to use **Network origin:
Internet** as RDS does not publish private VPCs. S3 traffic
from RDS instances does not go through the public internet since it goes
through private VPCs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:`us-east-1`:`111122223333`:accesspoint/amzn-s3-demo-ap",
 "arn:aws:s3:::`underlying-bucket`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObjectAttributes",
 "s3:GetObject",
 "s3:PutObject",
 "s3:ListMultipartUploadParts",
 "s3:AbortMultipartUpload"
 ],
 "Resource": [
 "arn:aws:s3:`us-east-1`:`111122223333`:`accesspoint/amzn-s3-demo-ap/*`",
 "arn:aws:s3:::underlying-bucket/*"
 ]
 }
 ]
}`

```
