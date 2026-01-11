# Export log data to Amazon S3 using the AWS CLI

In the following example, you use an export task to export all data from a CloudWatch Logs log
group named `my-log-group` to an Amazon S3 bucket named
`amzn-s3-demo-bucket`. This example assumes that you have already created a
log group called `my-log-group`.

Exporting log data to S3 buckets that are encrypted by AWS KMS is supported. Exporting
to buckets encrypted with DSSE-KMS is not supported.

The details of how you set up the export depends on whether the Amazon S3 bucket that you
want to export to is in the same account as your logs that are being exported, or in a
different account.

###### Topics

- [Same-account export (CLI)](#ExportSingleAccount-CLI "#ExportSingleAccount-CLI")
- [Cross-account export (CLI)](#ExportCrossAccount-CLI "#ExportCrossAccount-CLI")

## Same-account export (CLI)

If the Amazon S3 bucket is in the same account as the logs that are being exported, use
the instructions in this section.

###### Topics

- [Create an S3 bucket (CLI)](#CreateS3Bucket "#CreateS3Bucket")
- [Set up access
  permissions (CLI)](#CreateIAMUser-With-S3-Access-CLI "#CreateIAMUser-With-S3-Access-CLI")
- [Set permissions on an S3 bucket (CLI)](#S3Permissions "#S3Permissions")
- [(Optional) Exporting to a
  destination Amazon S3 bucket encrypted with SSE-KMS (CLI)](#S3-Export-KMSEncrypted-CLI "#S3-Export-KMSEncrypted-CLI")
- [Create an export task (CLI)](#CreateExportTask "#CreateExportTask")

### Create an S3 bucket (CLI)

We recommend that you use a bucket that was created specifically for CloudWatch Logs.
However, if you want to use an existing bucket, you can skip this procedure.

###### Note

The S3 bucket must reside in the same Region as the log data to export.
CloudWatch Logs doesn't support exporting data to S3 buckets in a different
Region.

###### To create an S3 bucket using the AWS CLI

At a command prompt, run the following [create-bucket](../../../cli/latest/reference/s3api/create-bucket.md "../../../cli/latest/reference/s3api/create-bucket.md")
command, where `LocationConstraint` is the Region where you are
exporting log data.

```
`aws s3api create-bucket --bucket `amzn-s3-demo-bucket` --create-bucket-configuration LocationConstraint=`us-east-2``
```

The following is example output.

```
`{
 "Location": "/`amzn-s3-demo-bucket`"
}`
```

### Set up access

permissions (CLI)

To create the export task later, you'll need to be signed on with the
`AmazonS3ReadOnlyAccess` IAM role and with the following
permissions:

- `logs:CreateExportTask`
- `logs:CancelExportTask`
- `logs:DescribeExportTasks`
- `logs:DescribeLogStreams`
- `logs:DescribeLogGroups`

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

### Set permissions on an S3 bucket (CLI)

By default, all S3 buckets and objects are private. Only the resource owner,
the account that created the bucket, can access the bucket and any objects that
it contains. However, the resource owner can choose to grant access permissions
to other resources and users by writing an access policy.

###### Important

To make exports to S3 buckets more secure, we now require you to specify
the list of source accounts that are allowed to export log data to your S3
bucket.

In the following example, the list of account IDs in the
`aws:SourceAccount` key would be the accounts from which a
user can export log data to your S3 bucket. The `aws:SourceArn`
key would be the resource for which the action is being taken. You may
restrict this to a specific log group, or use a wildcard as shown in this
example.

We recommend that you also include the account ID of the account where the
S3 bucket is created, to allow export within the same account.

###### To set permissions on an S3 bucket

1. Create a file named `policy.json` and add the following
   access policy, changing `amzn-s3-demo-bucket` to the name of
   your S3 bucket and `Principal` to the endpoint of the Region
   where you are exporting log data, such as `us-east-1`. Use a
   text editor to create this policy file. Don't use the IAM
   console.

JSON

```
 `{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowGetBucketAcl",
 "Action": "s3:GetBucketAcl",
 "Effect": "Allow",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "Principal": { "Service": "logs.`us-east-1`.amazonaws.com" },
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": [
 "`123456789012`",
 "`111122223333`"
 ]
 },
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:logs:`us-east-1`:`123456789012`:log-group:*",
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:*"
 ]
 }
 }
 },
 {
 "Sid": "AllowPutObject",
 "Action": "s3:PutObject",
 "Effect": "Allow",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*",
 "Principal": { "Service": "logs.`us-east-1`.amazonaws.com" },
 "Condition": {
 "StringEquals": {
 "s3:x-amz-acl": "bucket-owner-full-control",
 "aws:SourceAccount": [
 "`123456789012`",
 "`111122223333`"
 ]
 },
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:logs:`us-east-1`:`123456789012`:log-group:*",
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:*"
 ]
 }
 }
 }
 ]
}`

```

2. Set the policy that you just added as the access policy on your bucket
   by using the [put-bucket-policy](../../../cli/latest/reference/s3api/put-bucket-policy.md "../../../cli/latest/reference/s3api/put-bucket-policy.md") command. This policy enables CloudWatch Logs to
   export log data to your S3 bucket. The bucket owner will have full
   permissions on all of the exported objects.

```
`aws s3api put-bucket-policy --bucket amzn-s3-demo-bucket --policy file://policy.json`
```

###### Warning

If the existing bucket already has one or more policies attached
to it, add the statements for CloudWatch Logs access to that policy or
policies. We recommend that you evaluate the resulting set of
permissions to be sure that they're appropriate for the users who
will access the bucket.

### (Optional) Exporting to a

destination Amazon S3 bucket encrypted with SSE-KMS (CLI)

This procedure is necessary only if you are exporting to an S3 bucket that uses
server-side encryption with AWS KMS keys. This encryption is known as
SSE-KMS.

###### To export to a bucket encrypted with SSE-KMS

1. Use a text editor to create a file named
   `key_policy.json` and add the following access
   policy. When you add the policy, make the following changes:
   - Replace `Region` with the Region of
     your logs.
   - Replace `account-ARN` with the ARN of
     the account that owns the KMS key.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow CWL Service Principal usage",
 "Effect": "Allow",
 "Principal": {
 "Service": "logs.`Region`.amazonaws.com"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "*"
 },
 {
 "Sid": "Enable IAM User Permissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`account-ARN`"
 },
 "Action": [
 "kms:GetKeyPolicy*",
 "kms:PutKeyPolicy*",
 "kms:DescribeKey*",
 "kms:CreateAlias*",
 "kms:ScheduleKeyDeletion*",
 "kms:Decrypt"
 ],
 "Resource": "*"
 }
 ]
}`

```

2. Enter the following command:

```
aws kms create-key --policy file://key_policy.json
```

The following is example output from this command:

```
{
    "KeyMetadata": {
        "AWSAccountId": "`account_id`",
        "KeyId": "`key_id`",
        "Arn": "arn:aws:kms:us-east-2:`account-ARN`:key/`key_id`",
        "CreationDate": "`time`",
        "Enabled": true,
        "Description": "",
        "KeyUsage": "ENCRYPT_DECRYPT",
        "KeyState": "Enabled",
        "Origin": "AWS_KMS",
        "KeyManager": "CUSTOMER",
        "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
        "KeySpec": "SYMMETRIC_DEFAULT",
        "EncryptionAlgorithms": [
            "SYMMETRIC_DEFAULT"
        ],
        "MultiRegion": false
    }

```

3. Use a text editor to create a file called
   `bucketencryption.json` with the following
   contents.

```
{
  "Rules": [
    {
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "aws:kms",
        "KMSMasterKeyID": "{KMS Key ARN}"
      },
      "BucketKeyEnabled": true
    }
  ]
}
```

4. Enter the following command, replacing
   `amzn-s3-demo-bucket` with the name of the bucket
   that you are exporting logs to.

```
aws s3api put-bucket-encryption --bucket `amzn-s3-demo-bucket` --server-side-encryption-configuration file://bucketencryption.json
```

If the command doesn't return an error, the process is
successful.

### Create an export task (CLI)

Use the following command to create the export task. After you create it, the
export task might take anywhere from a few seconds to a few hours, depending on
the size of the data to export.

###### To export data to Amazon S3 using the AWS CLI

1. Sign in with sufficient permissions as documented in [Set up access
   permissions (CLI)](#CreateIAMUser-With-S3-Access-CLI "#CreateIAMUser-With-S3-Access-CLI").
2. At a command prompt, use the following [create-export-task](../../../cli/latest/reference/logs/create-export-task.md "../../../cli/latest/reference/logs/create-export-task.md") command to create the export
   task.

```
`aws logs create-export-task --profile CWLExportUser --task-name "`my-log-group-09-10-2015`" --log-group-name "`my-log-group`" --from `1441490400000` --to `1441494000000` --destination "`amzn-s3-demo-bucket`" --destination-prefix "`export-task-output`"`
```

The following is example output.

```
`{
 "taskId": "`cda45419-90ea-4db5-9833-aade86253e66`"
}`
```

## Cross-account export (CLI)

If the Amazon S3 bucket is in a different account than the logs that are being
exported, use the instructions in this section.

###### Topics

- [Create an S3
  bucket for cross-account export (CLI)](#CreateS3Bucket-CLI-crossaccount "#CreateS3Bucket-CLI-crossaccount")
- [Set up
  access permissions for cross-account export (CLI)](#CreateIAMUser-With-S3-Access-CLI-crossaccount "#CreateIAMUser-With-S3-Access-CLI-crossaccount")
- [Set permissions on an
  S3 bucket for cross-account export (CLI)](#S3Permissions-CLI-crossaccount "#S3Permissions-CLI-crossaccount")
- [(Optional)
  Exporting to a destination Amazon S3 bucket encrypted with SSE-KMS for cross-account export (CLI)](#S3-Export-KMSEncrypted-CLI-crossaccount "#S3-Export-KMSEncrypted-CLI-crossaccount")
- [Create an export
  task for cross-account export (CLI)](#CreateExportTask-CLI-crossaccount "#CreateExportTask-CLI-crossaccount")

### Create an S3

bucket for cross-account export (CLI)

We recommend that you use a bucket that was created specifically for CloudWatch Logs.
However, if you want to use an existing bucket, you can skip to step 2.

###### Note

The S3 bucket must reside in the same Region as the log data to export.
CloudWatch Logs doesn't support exporting data to S3 buckets in a different
Region.

###### To create an S3 bucket using the AWS CLI

At a command prompt, run the following [create-bucket](../../../cli/latest/reference/s3api/create-bucket.md "../../../cli/latest/reference/s3api/create-bucket.md")
command, where `LocationConstraint` is the Region where you are
exporting log data.

```
`aws s3api create-bucket --bucket `amzn-s3-demo-bucket` --create-bucket-configuration LocationConstraint=`us-east-2``
```

The following is example output.

```
`{
 "Location": "/`amzn-s3-demo-bucket`"
}`
```

### Set up

access permissions for cross-account export (CLI)

First, you must create a new IAM policy to enable CloudWatch Logs to have the
`s3:PutObject` action for the destination Amazon S3 bucket in the
destination account.

Along with `s3:PutObject` action, additional actions included in the
policy depend on whether the destination bucket uses AWS KMS encryption or has ACLs
enabled using the [S3 Object
Ownership](../../../AmazonS3/latest/userguide/about-object-ownership.md "../../../AmazonS3/latest/userguide/about-object-ownership.md") setting.

- If using KMS encryption, add the `kms:GenerateDataKey` and `kms:Decrypt` actions for the key resource
- If ACLs are enabled on the bucket add the `s3:PutObjectAcl` action for the bucket resource

Change `amzn-s3-demo-bucket` to the name of your destination S3 bucket in the following policies.

The policy that you create depends on whether the destination bucket uses
AWS KMS encryption. If it does not use AWS KMS encryption, create a policy with the
following contents.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 }
 ]
}`

```

If the destination bucket uses AWS KMS encryption, create a policy with the
following contents.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`123456789012`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`"
 }
 ]
}`

```

If the ACLs are enabled on destination bucket then add s3:PutObjectAcl
to s3:PutObject Action block in the above policies.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:PutObjectAcl"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 }
 ]
}`

```

To create an export task, you must be signed in with a IAM role that has the
`AmazonS3ReadOnlyAccess` managed policy attached, the IAM policy created above,
and also with the following permissions:

- `logs:CreateExportTask`
- `logs:CancelExportTask`
- `logs:DescribeExportTasks`
- `logs:DescribeLogStreams`
- `logs:DescribeLogGroups`

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

### Set permissions on an

S3 bucket for cross-account export (CLI)

By default, all S3 buckets and objects are private. Only the resource owner,
the account that created the bucket, can access the bucket and any objects that
it contains. However, the resource owner can choose to grant access permissions
to other resources and users by writing an access policy.

###### Important

To make exports to S3 buckets more secure, we now require you to specify
the list of source accounts that are allowed to export log data to your S3
bucket.

In the following example, the list of account IDs in the
`aws:SourceAccount` key would be the accounts from which a
user can export log data to your S3 bucket. The `aws:SourceArn`
key would be the resource for which the action is being taken. You may
restrict this to a specific log group, or use a wildcard as shown in this
example.

We recommend that you also include the account ID of the account where the
S3 bucket is created, to allow export within the same account.

###### To set permissions on an S3 bucket

1. Create a file named `policy.json` and add the following
   access policy, changing `amzn-s3-demo-bucket` to the name of
   your destination S3 bucket, `Principal` to the endpoint of the Region
   where you are exporting log data, such as `us-west-1`. Use a
   text editor to create this policy file. Don't use the IAM
   console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "s3:GetBucketAcl",
 "Effect": "Allow",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "Principal": { "Service": "logs.`us-east-1`.amazonaws.com" },
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": [
 "`123456789012`",
 "`111122223333`"
 ]
 },
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:logs:`us-east-1`:`123456789012`:log-group:*",
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:*"
 ]
 }
 }
 },
 {
 "Action": "s3:PutObject" ,
 "Effect": "Allow",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*",
 "Principal": { "Service": "logs.`us-east-1`.amazonaws.com" },
 "Condition": {
 "StringEquals": {
 "s3:x-amz-acl": "bucket-owner-full-control",
 "aws:SourceAccount": [
 "`123456789012`",
 "`111122223333`"
 ]
 },
 "ArnLike": {
 "aws:SourceArn": [
 "arn:aws:logs:`us-east-1`:`123456789012`:log-group:*",
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:*"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`role_name`"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::>amzn-s3-demo-bucket/*",
 "Condition": {
 "StringEquals": {
 "s3:x-amz-acl": "bucket-owner-full-control"
 }
 }
 }
 ]
}`

```

2. Set the policy that you just added as the access policy on your bucket
   by using the [put-bucket-policy](../../../cli/latest/reference/s3api/put-bucket-policy.md "../../../cli/latest/reference/s3api/put-bucket-policy.md") command. This policy enables CloudWatch Logs to
   export log data to your S3 bucket. The bucket owner will have full
   permissions on all of the exported objects.

```
`aws s3api put-bucket-policy --bucket amzn-s3-demo-bucket --policy file://policy.json`
```

###### Warning

If the existing bucket already has one or more policies attached
to it, add the statements for CloudWatch Logs access to that policy or
policies. We recommend that you evaluate the resulting set of
permissions to be sure that they're appropriate for the users who
will access the bucket.

### (Optional)

Exporting to a destination Amazon S3 bucket encrypted with SSE-KMS for cross-account export (CLI)

This procedure is necessary only if you are exporting to an S3 bucket that uses
server-side encryption with AWS KMS keys. This encryption is known as
SSE-KMS.

###### To export to a bucket encrypted with SSE-KMS

1. Use a text editor to create a file named
   `key_policy.json` and add the following access
   policy. When you add the policy, make the following changes:
   - Replace `us-east-1` with the Region of
     your logs.
   - Replace `account-ARN` with the ARN of
     the account that owns the KMS key.
   - Replace `123456789012` with the
     account number that owns the KMS key.
   - `key_id` with the kms-key Id.
   - `role_name` with the role used for
     creating export task.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCWLServicePrincipalUsage",
 "Effect": "Allow",
 "Principal": {
 "Service": "logs.`us-east-1`.amazonaws.com"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "*"
 },
 {
 "Sid": "EnableIAMUserPermissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`account-ARN`"
 },
 "Action": [
 "kms:GetKeyPolicy*",
 "kms:PutKeyPolicy*",
 "kms:DescribeKey*",
 "kms:CreateAlias*",
 "kms:ScheduleKeyDeletion*",
 "kms:Decrypt"
 ],
 "Resource": "*"
 },
 {
 "Sid": "EnableIAMRolePermissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`role_name`"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`123456789012`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`"
 }
 ]
}`

```

2. Enter the following command:

```
aws kms create-key --policy file://key_policy.json
```

The following is example output from this command:

```
{
    "KeyMetadata": {
        "AWSAccountId": "`account_id`",
        "KeyId": "`key_id`",
        "Arn": "arn:aws:kms:us-east-1:`123456789012`:key/`key_id`",
        "CreationDate": "`time`",
        "Enabled": true,
        "Description": "",
        "KeyUsage": "ENCRYPT_DECRYPT",
        "KeyState": "Enabled",
        "Origin": "AWS_KMS",
        "KeyManager": "CUSTOMER",
        "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
        "KeySpec": "SYMMETRIC_DEFAULT",
        "EncryptionAlgorithms": [
            "SYMMETRIC_DEFAULT"
        ],
        "MultiRegion": false
    }

```

3. Use a text editor to create a file called
   `bucketencryption.json` with the following
   contents.

```
{
  "Rules": [
    {
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "aws:kms",
        "KMSMasterKeyID": "{KMS Key ARN}"
      },
      "BucketKeyEnabled": true
    }
  ]
}
```

4. Enter the following command, replacing
   `amzn-s3-demo-bucket` with the name of the bucket
   that you are exporting logs to.

```
aws s3api put-bucket-encryption --bucket `amzn-s3-demo-bucket` --server-side-encryption-configuration file://bucketencryption.json
```

If the command doesn't return an error, the process is
successful.

### Create an export

task for cross-account export (CLI)

Use the following command to create the export task. After you create it, the
export task might take anywhere from a few seconds to a few hours, depending on
the size of the data to export.

###### To export data to Amazon S3 using the AWS CLI

1. Sign in with sufficient permissions as documented in [Set up access
   permissions (CLI)](#CreateIAMUser-With-S3-Access-CLI "#CreateIAMUser-With-S3-Access-CLI").
2. At a command prompt, use the following [create-export-task](../../../cli/latest/reference/logs/create-export-task.md "../../../cli/latest/reference/logs/create-export-task.md") command to create the export
   task.

```
`aws logs create-export-task --profile CWLExportUser --task-name "`my-log-group-09-10-2015`" --log-group-name "`my-log-group`" --from `1441490400000` --to `1441494000000` --destination "`amzn-s3-demo-bucket`" --destination-prefix "`export-task-output`"`
```

The following is example output.

```
`{
 "taskId": "`cda45419-90ea-4db5-9833-aade86253e66`"
}`
```
