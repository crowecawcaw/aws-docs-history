**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Sending protection pack (web ACL) traffic logs to an Amazon Simple Storage Service bucket

This topic provides information for sending your protection pack (web ACL) traffic logs to an Amazon S3
bucket.

###### Note

You are charged for logging in addition to the charges for using
AWS WAF. For information, see [Pricing for logging protection pack (web ACL) traffic information](logging-pricing.md "logging-pricing.md").

To send your protection pack (web ACL) traffic logs to Amazon S3, you set up an Amazon S3 bucket
from the same account as you use to manage the protection pack (web ACL), and you name
the bucket starting with `aws-waf-logs-`.
When you enable logging in AWS WAF, you provide the bucket name.
For information about creating a logging bucket, see [Create a Bucket](../../../AmazonS3/latest/userguide/CreatingABucket.md "../../../AmazonS3/latest/userguide/CreatingABucket.md") in the
_Amazon Simple Storage Service User Guide_.

You can access and analyze your Amazon S3 logs using the Amazon Athena interactive query
service. Athena makes it easy to analyze data directly in Amazon S3 using standard SQL.
With a few actions in the AWS Management Console, you can point Athena at data stored in Amazon S3
and quickly begin using standard SQL to run ad-hoc queries and get results. For more
information, see [Querying AWS WAF logs](../../../athena/latest/ug/waf-logs.md "../../../athena/latest/ug/waf-logs.md") in the _Amazon Athena user
guide_. For additional sample Amazon Athena queries, see
[aws-samples/waf-log-sample-athena-queries](https://github.com/aws-samples/waf-log-sample-athena-queries "https://github.com/aws-samples/waf-log-sample-athena-queries") on the GitHub website.

###### Note

AWS WAF supports encryption with Amazon S3 buckets for key type Amazon S3 key (SSE-S3) and for AWS Key Management Service (SSE-KMS) AWS KMS keys. AWS WAF doesn't support encryption for AWS Key Management Service keys that are managed by AWS.

Log files from your protection pack (web ACL) are published to the Amazon S3 bucket at 5-minute intervals.
Each log file contains log records for the traffic recorded in the
previous 5 minutes.

The maximum file size for a log file is 75 MB. If the log file reaches the
file size limit within the 5-minute period, the log stops adding records to it,
publishes it to the Amazon S3 bucket, and then creates a new log file.

The log files are compressed. If you open the files using the Amazon S3 console, Amazon S3
decompresses the log records and displays them. If you download the log files, you
must decompress them to view the records.

A single log file contains interleaved entries with multiple records. To see
all the log files for a protection pack (web ACL), look for entries aggregated by the protection pack (web ACL) name,
Region, and your account ID.

## Naming requirements and syntax

Bucket names for AWS WAF logging must start with `aws-waf-logs-` and
can end with any suffix you want. For example,
`aws-waf-logs-`LOGGING-BUCKET-SUFFIX``.

###### Bucket location

The bucket locations use the following syntax:

```
s3://aws-waf-logs-`LOGGING-BUCKET-SUFFIX`/
```

###### Bucket ARN

The format of the bucket Amazon Resource Name (ARN) is as follows:

```
arn:aws:s3:::aws-waf-logs-`LOGGING-BUCKET-SUFFIX`
```

###### Bucket locations with prefixes

If you use prefixes in your object keys name to organize the data that you
store in your buckets, you can provide your prefixes in your logging bucket
names.

###### Note

This option is not available through the console. Use the AWS WAF APIs, CLI, or AWS CloudFormation.

For information about using prefixes in Amazon S3, see [Organizing objects using
prefixes](../../../AmazonS3/latest/userguide/using-prefixes.md "../../../AmazonS3/latest/userguide/using-prefixes.md") in the _Amazon Simple Storage Service User Guide_.

The bucket locations with prefixes use the following syntax:

```
s3://aws-waf-logs-`LOGGING-BUCKET-SUFFIX`/`KEY-NAME-PREFIX`/
```

###### Bucket folders and file names

Inside your buckets, and following any prefixes that you provide, your AWS WAF logs
are written under a folder structure that's determined by your account ID, the
Region, the protection pack (web ACL) name, and the date and time.

```
AWSLogs/`account-id`/WAFLogs/`Region`/`web-acl-name`/`YYYY`/`MM`/`dd`/`HH`/`mm`
```

Inside the folders, the log file names follow a similar format:

```
`account-id`_waflogs_`Region`_`web-acl-name`_`timestamp`_`hash`.log.gz
```

The time specifications used in the folder structure and in the log file name
adhere to the timestamp format specification `YYYYMMddTHHmmZ`.

The following shows an example log file in an Amazon S3 bucket for a bucket named
`aws-waf-logs-`LOGGING-BUCKET-SUFFIX``. The AWS account is
 `11111111111`. The protection pack (web ACL) is `TEST-WEBACL`and the Region
 is`us-east-1`.

```
s3://aws-waf-logs-`LOGGING-BUCKET-SUFFIX`/AWSLogs/11111111111/WAFLogs/us-east-1/TEST-WEBACL/2021/10/28/19/50/11111111111_waflogs_us-east-1_TEST-WEBACL_20211028T1950Z_e0ca43b5.log.gz
```

###### Note

Your bucket names for AWS WAF logging must start with `aws-waf-logs-`
and can end with any suffix you want.

## Permissions required to publish logs to

Amazon S3

Configuring protection pack (web ACL) traffic logging for an Amazon S3 bucket requires the following
permissions settings. These permissions are set for you when you use one of the
AWS WAF full access managed policies, `AWSWAFConsoleFullAccess` or
`AWSWAFFullAccess`. If you want to further manage access to
your logging and AWS WAF resources, you can set these permissions yourself. For
information about managing permissions, see [Access management for AWS
resources](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md") in the _IAM User Guide_. For
information about the AWS WAF managed policies, see [AWS managed policies for AWS WAF](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

The following permissions allow you to change the protection pack (web ACL) logging
configuration and to configure log delivery to your Amazon S3 bucket. These
permissions must be attached to the user that you use to manage AWS WAF.

###### Note

When you set the permissions listed below, you might see errors in your AWS CloudTrail logs
that indicate access denied, but the permissions are correct for AWS WAF logging.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Action":[
 "wafv2:PutLoggingConfiguration",
 "wafv2:DeleteLoggingConfiguration"
 ],
 "Resource":[
 "*"
 ],
 "Effect":"Allow",
 "Sid":"LoggingConfigurationAPI"
 },
 {
 "Sid":"WebACLLogDelivery",
 "Action":[
 "logs:CreateLogDelivery",
 "logs:DeleteLogDelivery"
 ],
 "Resource": "*",
 "Effect":"Allow"
 },
 {
 "Sid":"WebACLLoggingS3",
 "Action":[
 "s3:PutBucketPolicy",
 "s3:GetBucketPolicy"
 ],
 "Resource": [
 "arn:aws:s3:::aws-waf-logs-`amzn-s3-demo-destination-bucket`-suffix"
 ],
 "Effect":"Allow"
 }
 ]
}`

```

When actions are permitted on all AWS resources, it's indicated in the
policy with a `"Resource"` setting of `"*"`. This means
that the actions are permitted on all AWS resources _that each action
supports_. For example, the action
`wafv2:PutLoggingConfiguration` is supported only for
`wafv2` logging configuration resources.

By default, Amazon S3 buckets and the objects that they contain are private. Only
the bucket owner can access the bucket and the objects stored in it. The bucket
owner, however, can grant access to other resources and users by writing an
access policy.

If the user creating the log owns the bucket, the service automatically
attaches the following policy to the bucket to give the log permission to
publish logs to it:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AWSLogDeliveryWrite",
 "Effect": "Allow",
 "Principal": {
 "Service": "delivery.logs.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::aws-waf-logs-`amzn-s3-demo-destination-bucket`-suffix/AWSLogs/`123456789012`/*",
 "Condition": {
 "StringEquals": {
 "s3:x-amz-acl": "bucket-owner-full-control",
 "aws:SourceAccount": ["`123456789012`"]
 },
 "ArnLike": {
 "aws:SourceArn": ["arn:aws:logs:`us-east-2`:`123456789012`:*"]
 }
 }
 },
 {
 "Sid": "AWSLogDeliveryAclCheck",
 "Effect": "Allow",
 "Principal": {
 "Service": "delivery.logs.amazonaws.com"
 },
 "Action": "s3:GetBucketAcl",
 "Resource": "arn:aws:s3:::aws-waf-logs-`amzn-s3-demo-destination-bucket`-suffix",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": ["`123456789012`"]
 },
 "ArnLike": {
 "aws:SourceArn": ["arn:aws:logs:`us-east-2`:`123456789012`:*"]
 }
 }
 }
 ]
}`

```

###### Note

Your bucket names for AWS WAF logging must start with `aws-waf-logs-`
and can end with any suffix you want.

If the user creating the log doesn't own the bucket, or doesn't have the
`GetBucketPolicy` and `PutBucketPolicy` permissions
for the bucket, the log creation fails. In this case, the bucket owner must
manually add the preceding policy to the bucket and specify the log creator's
AWS account ID. For more information, see [How Do I Add an S3 Bucket
Policy?](../../../AmazonS3/latest/userguide/add-bucket-policy.md "../../../AmazonS3/latest/userguide/add-bucket-policy.md") in the _Amazon Simple Storage Service User Guide_. If the bucket
receives logs from multiple accounts, add a `Resource` element entry
to the `AWSLogDeliveryWrite` policy statement for each account.

For example, the following bucket policy allows AWS account
`111122223333` to publish logs to a bucket named `aws-waf-logs-`LOGGING-BUCKET-SUFFIX``:

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "AWSLogDeliveryWrite20150319",
 "Statement": [
 {
 "Sid": "AWSLogDeliveryWrite",
 "Effect": "Allow",
 "Principal": {
 "Service": "delivery.logs.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::aws-waf-logs-`amzn-s3-demo-destination-bucket`-suffix/AWSLogs/111122223333/*",
 "Condition": {
 "StringEquals": {
 "s3:x-amz-acl": "bucket-owner-full-control",
 "aws:SourceAccount": ["111122223333"]
 },
 "ArnLike": {
 "aws:SourceArn": ["arn:aws:logs:us-east-1:`111122223333`:*"]
 }
 }
 },
 {
 "Sid": "AWSLogDeliveryAclCheck",
 "Effect": "Allow",
 "Principal": {
 "Service": "delivery.logs.amazonaws.com"
 },
 "Action": "s3:GetBucketAcl",
 "Resource": "arn:aws:s3:::aws-waf-logs-`amzn-s3-demo-destination-bucket`-suffix",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": ["111122223333"]
 },
 "ArnLike": {
 "aws:SourceArn": ["arn:aws:logs:us-east-1:`111122223333`:*"]
 }
 }
 }
 ]
}`

```

###### Note

In some cases, you may see `AccessDenied` errors in
AWS CloudTrail if the `s3:ListBucket` permission has not been
granted to `delivery.logs.amazonaws.com`. To avoid these
errors in your CloudTrail logs, you must grant the `s3:ListBucket`
permission to `delivery.logs.amazonaws.com` and you must
include the `Condition` parameters shown with the
`s3:GetBucketAcl` permission set in the preceding bucket
policy. To make this simpler, instead of creating a new
`Statement`, you can directly update the
`AWSLogDeliveryAclCheck` to be `“Action”:
 [“s3:GetBucketAcl”, “s3:ListBucket”]`.

## Permissions for using

AWS Key Management Service with a KMS key

If your logging destination uses server-side encryption with keys that are
stored in AWS Key Management Service (SSE-KMS) and you use a customer managed key (KMS key), you must
give AWS WAF permission to use your KMS key. To do this, you add a key
policy to the KMS key for your chosen destination. This permits AWS WAF
logging to write your log files to your destination.

Add the following key policy to your KMS key to allow AWS WAF to log to your
Amazon S3 bucket.

```
{
    "Sid": "Allow AWS WAF to use the key",
    "Effect": "Allow",
    "Principal": {
        "Service": [
            "delivery.logs.amazonaws.com"
        ]
    },
    "Action": "kms:GenerateDataKey*",
    "Resource": "*"
}
```

## Permissions required to access

Amazon S3 log files

Amazon S3 uses access control
lists (ACLs) to manage access to the log files created by an AWS WAF
log. By default, the bucket owner has `FULL_CONTROL` permissions
on each log file. The log delivery owner, if different from the bucket
owner, has no permissions. The log delivery account has `READ`
and `WRITE` permissions. For more information, see [Access Control List (ACL)
Overview](../../../AmazonS3/latest/userguide/acl-overview.md "../../../AmazonS3/latest/userguide/acl-overview.md") in the _Amazon Simple Storage Service User Guide_.
