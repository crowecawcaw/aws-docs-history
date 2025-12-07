# Export log data to Amazon S3 using the console

In the following examples, you use the Amazon CloudWatch console to export all data from an
Amazon CloudWatch Logs log group named `my-log-group` to an Amazon S3 bucket named
`my-exported-logs`.

Exporting log data to S3 buckets that are encrypted by SSE-KMS is supported. Exporting
to buckets encrypted with DSSE-KMS is not supported.

The details of how you set up the export depends on whether the Amazon S3 bucket that you
want to export to is in the same account as your logs that are being exported, or in a
different account.

###### Topics

- [Same-account export (console)](#ExportSingleAccount "#ExportSingleAccount")
- [Cross-account export (console)](#ExportCrossAccount "#ExportCrossAccount")

## Same-account export (console)

If the Amazon S3 bucket is in the same account as the logs that are being exported, use
the instructions in this section.

###### Topics

- [Create an Amazon S3 bucket (console)](#CreateS3BucketConsole "#CreateS3BucketConsole")
- [Set up access
  permissions (console)](#CreateIAMUser-With-S3-Access "#CreateIAMUser-With-S3-Access")
- [Set permissions on an Amazon S3
  bucket (console)](#S3PermissionsConsole "#S3PermissionsConsole")
- [(Optional) Exporting to a
  bucket encrypted with SSE-KMS (console)](#S3-Export-KMSEncrypted "#S3-Export-KMSEncrypted")
- [Create an export task (console)](#CreateExportTaskConsole "#CreateExportTaskConsole")

### Create an Amazon S3 bucket (console)

We recommend that you use a bucket that was created specifically for CloudWatch Logs.
However, if you want to use an existing bucket, you can skip to step 2.

###### Note

The Amazon S3 bucket must reside in the same Region as the log data to export.
CloudWatch Logs doesn't support exporting data to Amazon S3 buckets in a different
Region.

###### To create an Amazon S3 bucket

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. If necessary, change the Region. From the navigation bar, choose the
   Region where your CloudWatch Logs reside.
3. Choose **Create Bucket**.
4. For **Bucket Name**, enter a name for the
   bucket.
5. For **Region**, select the Region where your CloudWatch Logs
   data resides.
6. Choose **Create**.

### Set up access

permissions (console)

To create the export task, you'll need to be signed on with the
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

### Set permissions on an Amazon S3

bucket (console)

By default, all Amazon S3 buckets and objects are private. Only the resource owner,
the AWS account that created the bucket, can access the bucket and any objects
that it contains. However, the resource owner can choose to grant access
permissions to other resources and users by writing an access policy.

When you set the policy, we recommend that you include a randomly generated
string as the prefix for the bucket, so that only intended log streams are
exported to the bucket.

###### Important

To make exports to Amazon S3 buckets more secure, we now require you to specify
the list of source accounts that are allowed to export log data to your S3
bucket.

In the following example, the list of account IDs in the
`aws:SourceAccount` key would be the accounts from which a
user can export log data to your Amazon S3 bucket. The `aws:SourceArn`
key would be the resource for which the action is being taken. You may
restrict this to a specific log group, or use a wildcard as shown in this
example.

We recommend that you also include the account ID of the account where the
S3 bucket is created, to allow export within the same account.

###### To set permissions on an Amazon S3 bucket

1. In the Amazon S3 console, choose the bucket that you created.
2. Choose **Permissions**, **Bucket
   policy**.
3. In the **Bucket Policy Editor**, add the following
   policy. Change `my-exported-logs` to the name of your S3
   bucket. Be sure to specify the correct Region endpoint, such as
   `us-west-1`, for **Principal**.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCloudWatchLogsGetBucketAcl",
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
 "Sid": "AllowCloudWatchLogsPutObject",
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

4. Choose **Save** to set the policy that you just added
   as the access policy on your bucket. This policy enables CloudWatch Logs to export
   log data to your Amazon S3 bucket. The bucket owner has full permissions on
   all of the exported objects.

###### Warning

If the existing bucket already has one or more policies attached
to it, add the statements for CloudWatch Logs access to that policy or
policies. We recommend that you evaluate the resulting set of
permissions to be sure that they're appropriate for the users who
will access the bucket.

### (Optional) Exporting to a

bucket encrypted with SSE-KMS (console)

This step is necessary only if you are exporting to an Amazon S3 bucket that uses
server-side encryption with AWS KMS keys. This encryption is known as
SSE-KMS.

###### To export to a bucket encrypted with SSE-KMS

1. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the left navigation bar, choose **Customer managed
   keys**.

Choose **Create Key**. 4. For **Key type**, choose
**Symmetric**. 5. For **Key usage**, choose **Encrypt and
decrypt** and then choose **Next**. 6. Under **Add labels**, enter an alias for the key and
optionally add a description or tags. Then choose
**Next**. 7. Under **Key administrators**, select who can
administer this key, and then choose **Next**. 8. Under **Define key usage permissions**, make no
changes and choose **Next**. 9. Review the settings and choose **Finish**. 10. Back at the **Customer managed keys** page, choose
the name of the key that you just created. 11. Choose the **Key policy** tab and choose
**Switch to policy view**. 12. In the **Key policy** section, choose
**Edit**. 13. Add the following statement to the key policy statement list. When you
do, replace `Region` with the Region of your
logs and replace `account-ARN` with the ARN of
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

14. Choose **Save changes**.
15. Open the Amazon S3 console at
    [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
16. Find the bucket that you created in [Create an S3 bucket (CLI)](S3ExportTasks.md#CreateS3Bucket "S3ExportTasks.md#CreateS3Bucket") and choose the bucket name.
17. Choose the **Properties** tab. Then, under
    **Default Encryption**, choose
    **Edit**.
18. Under **Server-side Encryption**, choose
    **Enable**.
19. Under **Encryption type**, choose **AWS Key Management Service
    key (SSE-KMS)**.
20. Choose **Choose from your AWS KMS keys** and find the
    key that you created.
21. For **Bucket key**, choose
    **Enable**.
22. Choose **Save changes**.

### Create an export task (console)

In this procedure, you create the export task for exporting logs from a log
group.

###### To export data to Amazon S3 using the CloudWatch console

1. Sign in with sufficient permissions as documented in [Set up access
   permissions (console)](#CreateIAMUser-With-S3-Access "#CreateIAMUser-With-S3-Access").
2. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
3. In the navigation pane, choose **Log groups**.
4. On the **Log Groups** screen, choose the name of the
   log group.
5. Choose **Actions**, **Export data to
   Amazon S3**.
6. On the **Export data to Amazon S3** screen, under
   **Define data export**, set the time range for the
   data to export using **From** and
   **To**.
7. If your log group has multiple log streams, you can provide a log
   stream prefix to limit the log group data to a specific stream. Choose
   **Advanced**, and then for **Stream
   prefix**, enter the log stream prefix.
8. Under **Choose S3 bucket**, choose the account
   associated with the S3 bucket.
9. For **S3 bucket name**, choose an &S3;
   bucket.
10. For **S3 Bucket prefix**, enter the randomly
    generated string that you specified in the bucket policy.
11. Choose **Export** to export your log data to
    Amazon S3.
12. To view the status of the log data that you exported to Amazon S3, choose
    **Actions** and then **View all exports to
    Amazon S3**.

## Cross-account export (console)

If the Amazon S3 bucket is in a different account than the logs that are being
exported, use the instructions in this section.

###### Topics

- [Create an Amazon S3
  bucket for cross-account export (console)](#CreateS3BucketConsole-crossaccount "#CreateS3BucketConsole-crossaccount")
- [Set up
  access permissions for cross-account export (console)](#CreateIAMUser-With-S3-Access-crossaccount "#CreateIAMUser-With-S3-Access-crossaccount")
- [Set permissions on
  an S3 bucket for cross-account export (console)](#S3PermissionsConsole-crossaccount "#S3PermissionsConsole-crossaccount")
- [(Optional) Exporting to a bucket encrypted with SSE-KMS for cross-account export (console)](#S3-Export-KMSEncrypted-crossaccount "#S3-Export-KMSEncrypted-crossaccount")
- [Create an export
  task for cross-account export (console)](#CreateExportTaskConsole-crossaccount "#CreateExportTaskConsole-crossaccount")

### Create an Amazon S3

bucket for cross-account export (console)

We recommend that you use a bucket that was created specifically for CloudWatch Logs.
However, if you want to use an existing bucket, you can skip this procedure.

###### Note

The Amazon S3 bucket must reside in the same Region as the log data to export.
CloudWatch Logs doesn't support exporting data to Amazon S3 buckets in a different
Region.

###### To create an Amazon S3 bucket

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. If necessary, change the Region. From the navigation bar, choose the
   Region where your CloudWatch Logs reside.
3. Choose **Create Bucket**.
4. For **Bucket Name**, enter a name for the
   bucket.
5. For **Region**, select the Region where your CloudWatch Logs
   data resides.
6. Choose **Create**.

### Set up

access permissions for cross-account export (console)

First, you must create a new IAM policy to enable CloudWatch Logs to have the
`s3:PutObject` action for the destination Amazon S3 bucket in the
destination account.

The additional actions included in the policy depend on whether the destination bucket uses
AWS KMS encryption or has ACLs enabled using the [S3 Object
Ownership](../../../AmazonS3/latest/userguide/about-object-ownership.md "../../../AmazonS3/latest/userguide/about-object-ownership.md") setting.

- If using KMS encryption, add the `GenerateDataKey` and `Decrypt` actions for the key resource
- If ACLs are enabled on the bucket add the `s3:PutObjectAcl` action for the bucket resource

###### To create an IAM policy to export logs to an Amazon S3 bucket

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left, choose
   **Policies**.
3. Choose **Create policy**.
4. In the **Policy editor** section, choose
   **JSON**.
5. If the destination bucket does not use AWS KMS encryption, paste the
   following policy into the editor.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`my-exported-logs`/*"
 }
 ]
}`

```

If the destination bucket does use AWS KMS encryption, paste the
following policy into the editor.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
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

6. Choose **Next**.
7. Enter a policy name. You will use this name to attach the policy to
   your IAM role.
8. Choose **Create policy** to save the new
   policy.

To create the export task, you'll need to be signed in with the
`AmazonS3ReadOnlyAccess` IAM role. You must also be signed in
with the IAM policy that you just created, and also with the following
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

### Set permissions on

an S3 bucket for cross-account export (console)

By default, all S3 buckets and objects are private. Only the resource owner,
the AWS account that created the bucket, can access the bucket and any objects
that it contains. However, the resource owner can choose to grant access
permissions to other resources and users by writing an access policy.

When you set the policy, we recommend that you include a randomly generated
string as the prefix for the bucket, so that only intended log streams are
exported to the bucket.

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

###### To set permissions on an Amazon S3 bucket

1. In the Amazon S3 console, choose the bucket that you created.
2. Choose **Permissions**, **Bucket
   policy**.
3. In the **Bucket Policy Editor**, add the following
   policy. Change `my-exported-logs` to the name of your S3
   bucket. Be sure to specify the correct Region endpoint, such as
   `us-west-1`, for **Principal**.

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
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`role_name`"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*",
 "Condition": {
 "StringEquals": {
 "s3:x-amz-acl": "bucket-owner-full-control"
 }
 }
 }
 ]
}`

```

4. Choose **Save** to set the policy that you just added
   as the access policy on your bucket. This policy enables CloudWatch Logs to export
   log data to your S3 bucket. The bucket owner has full permissions on all
   of the exported objects.

###### Warning

If the existing bucket already has one or more policies attached
to it, add the statements for CloudWatch Logs access to that policy or
policies. We recommend that you evaluate the resulting set of
permissions to be sure that they're appropriate for the users who
will access the bucket.

### (Optional) Exporting to a bucket encrypted with SSE-KMS for cross-account export (console)

This procedure is necessary only if you are exporting to an S3 bucket that uses
server-side encryption with AWS KMS keys. This encryption is known as
SSE-KMS.

###### To export to a bucket encrypted with SSE-KMS

1. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the left navigation bar, choose **Customer managed
   keys**.

Choose **Create Key**. 4. For **Key type**, choose
**Symmetric**. 5. For **Key usage**, choose **Encrypt and
decrypt** and then choose **Next**. 6. Under **Add labels**, enter an alias for the key and
optionally add a description or tags. Then choose
**Next**. 7. Under **Key administrators**, select who can
administer this key, and then choose **Next**. 8. Under **Define key usage permissions**, make no
changes and choose **Next**. 9. Review the settings and choose **Finish**. 10. Back at the **Customer managed keys** page, choose
the name of the key that you just created. 11. Choose the **Key policy** tab and choose
**Switch to policy view**. 12. In the **Key policy** section, choose
**Edit**. 13. Add the following statement to the key policy statement list. When you
do, replace `Region` with the Region of your
logs and replace `account-ARN` with the ARN of
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
 "Service": "logs.`us-east-1`.amazonaws.com"
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
 },
 {
 "Sid": "Enable IAM Role Permissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`role_name`"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`key-id`"
 }
 ]
}`

```

14. Choose **Save changes**.
15. Open the Amazon S3 console at
    [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
16. Find the bucket that you created in [Create an S3 bucket (CLI)](S3ExportTasks.md#CreateS3Bucket "S3ExportTasks.md#CreateS3Bucket") and choose the bucket name.
17. Choose the **Properties** tab. Then, under
    **Default Encryption**, choose
    **Edit**.
18. Under **Server-side Encryption**, choose
    **Enable**.
19. Under **Encryption type**, choose **AWS Key Management Service
    key (SSE-KMS)**.
20. Choose **Choose from your AWS KMS keys** and find the
    key that you created.
21. For **Bucket key**, choose
    **Enable**.
22. Choose **Save changes**.

### Create an export

task for cross-account export (console)

In this procedure, you create the export task for exporting logs from a log
group.

###### To export data to Amazon S3 using the CloudWatch console

1. Sign in with sufficient permissions as documented in [Set up access
   permissions (console)](#CreateIAMUser-With-S3-Access "#CreateIAMUser-With-S3-Access").
2. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
3. In the navigation pane, choose **Log groups**.
4. On the **Log Groups** screen, choose the name of the
   log group.
5. Choose **Actions**, **Export data to
   Amazon S3**.
6. On the **Export data to Amazon S3** screen, under
   **Define data export**, set the time range for the
   data to export using **From** and
   **To**.
7. If your log group has multiple log streams, you can provide a log
   stream prefix to limit the log group data to a specific stream. Choose
   **Advanced**, and then for **Stream
   prefix**, enter the log stream prefix.
8. Under **Choose S3 bucket**, choose the account
   associated with the S3 bucket.
9. For **S3 bucket name**, choose an S3 bucket.
10. For **S3 Bucket prefix**, enter the randomly
    generated string that you specified in the bucket policy.
11. Choose **Export** to export your log data to
    Amazon S3.
12. To view the status of the log data that you exported to Amazon S3, choose
    **Actions** and then **View all exports to
    Amazon S3**.
