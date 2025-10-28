# AWS Transit Gateway Flow Logs records in Amazon S3

Flow logs can publish flow log data to Amazon S3.

When publishing to Amazon S3, flow log data is published to an existing Amazon S3 bucket that
you specify. Flow log records for all of the monitored transit gateways are published to a series
of log file objects that are stored in the bucket.

Data ingestion and archival charges are applied by Amazon CloudWatch for
vended logs when you publish flow logs to Amazon S3. For more information on CloudWatch pricing for
vended logs, open [Amazon CloudWatch
Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/"), choose **Logs**, and then find **Vended
Logs**.

To create an Amazon S3 bucket for use with flow logs, see [Create a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the
_Amazon S3 User Guide_.

For more information about multiple account logging, see [Central Logging](https://aws.amazon.com/solutions/implementations/centralized-logging/ "https://aws.amazon.com/solutions/implementations/centralized-logging/") in the
AWS Solutions Library.

For more information about CloudWatch Logs, see [Logs sent to Amazon S3](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-S3 "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-S3") in the _Amazon CloudWatch Logs User
Guide_.

###### Contents

- [Flow log files](#flow-logs-s3-path "#flow-logs-s3-path")
- [IAM policy for IAM principals that publish
  flow logs to Amazon S3](#flow-logs-s3-iam "#flow-logs-s3-iam")
- [Amazon S3 bucket permissions for flow
  logs](#flow-logs-s3-permissions "#flow-logs-s3-permissions")
- [Required key policy for use with
  SSE-KMS](#flow-logs-s3-cmk-policy "#flow-logs-s3-cmk-policy")
- [Amazon S3 log file permissions](#flow-logs-file-permissions "#flow-logs-file-permissions")
- [Create the source account role](flowlog-s3-create-source.md "flowlog-s3-create-source.md")
- [Create a Flow Log that publishes
  to Amazon S3](flowlog-s3-create.md "flowlog-s3-create.md")
- [View Flow Logs records](view-flow-log-records-s3.md "view-flow-log-records-s3.md")
- [Processed AWS Transit Gateway Flow Logs records in Amazon S3](#process-records-s3 "#process-records-s3")

## Flow log files

VPC Flow Logs is a feature that collects flow log records, consolidates them into
log files, and then publishes the log files to the Amazon S3 bucket at 5-minute
intervals. Each log file contains flow log records for the IP traffic recorded in
the previous five minutes.

The maximum file size for a log file is 75 MB. If the log file reaches the file
size limit within the 5-minute period, the flow log stops adding flow log records to
it. Then it publishes the flow log to the Amazon S3 bucket, and creates a new log
file.

In Amazon S3, the **Last modified** field for the flow log file
indicates the date and time when the file was uploaded to the Amazon S3 bucket. This is
later than the timestamp in the file name, and differs by the amount of time taken
to upload the file to the Amazon S3 bucket.

###### Log file format

You can specify one of the following formats for the log files. Each file is
compressed into a single Gzip file.

- **Text** – Plain text. This is the
  default format.
- **Parquet** – Apache Parquet is a
  columnar data format. Queries on data in Parquet format are 10 to 100 times
  faster compared to queries on data in plain text. Data in Parquet format
  with Gzip compression takes 20 percent less storage space than plain text
  with Gzip compression.

###### Log file options

You can optionally specify the following options.

- **Hive-compatible S3 prefixes** –
  Enable Hive-compatible prefixes instead of importing partitions into your
  Hive-compatible tools. Before you run queries, use the **MSCK REPAIR
  TABLE** command.
- **Hourly partitions** – If you have a
  large volume of logs and typically target queries to a specific hour, you
  can get faster results and save on query costs by partitioning logs on an
  hourly basis.

###### Log file S3 bucket structure

Log files are saved to the specified Amazon S3 bucket using a folder structure that
is based on the flow log's ID, Region, creation date, and destination
options.

By default, the files are delivered to the following location.

```
`bucket-and-optional-prefix`/AWSLogs/`account_id`/vpcflowlogs/`region`/`year`/`month`/`day`/
```

If you enable Hive-compatible S3 prefixes, the files are delivered to the
following location.

```
`bucket-and-optional-prefix`/AWSLogs/aws-account-id=`account_id`/service=vpcflowlogs/aws-region=`region`/year=`year`/month=`month`/day=`day`/
```

If you enable hourly partitions, the files are delivered to the following
location.

```
`bucket-and-optional-prefix`/AWSLogs/`account_id`/vpcflowlogs/`region`/`year`/`month`/`day`/`hour`/
```

If you enable Hive-compatible partitions and partition the flow log per hour, the
files are delivered to the following location.

```
`bucket-and-optional-prefix`/AWSLogs/aws-account-id=`account_id`/service=vpcflowlogs/aws-region=`region`/year=`year`/month=`month`/day=`day`/hour=`hour`/
```

###### Log file names

The file name of a log file is based on the flow log ID, Region, and creation
date and time. File names use the following format.

```
`aws_account_id`_vpcflowlogs_`region`_`flow_log_id`_`YYYYMMDD`T`HHmm`Z_`hash`.log.gz
```

The following is an example of a log file for a flow log created by AWS account
123456789012, for a resource in the us-east-1
Region, on June 20, 2018 at 16:20 UTC. The file
contains the flow log records with an end time between 16:20:00 and
16:24:59.

```
123456789012_vpcflowlogs_us-east-1_fl-1234abcd_20180620T1620Z_fe123456.log.gz
```

## IAM policy for IAM principals that publish

flow logs to Amazon S3

The IAM principal that creates the flow log must have the following permissions,
which are required to publish flow logs to the destination Amazon S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogDelivery",
 "logs:DeleteLogDelivery"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Amazon S3 bucket permissions for flow

logs

By default, Amazon S3 buckets and the objects they contain are private. Only the bucket
owner can access the bucket and the objects stored in it. However, the bucket owner
can grant access to other resources and users by writing an access policy.

If the user creating the flow log owns the bucket and has
`PutBucketPolicy` and `GetBucketPolicy` permissions for the
bucket, we automatically attach the following policy to the bucket. This new
auto-generated policy is appended to the original policy.

Otherwise, the bucket owner must add this policy to the bucket, specifying the
AWS account ID of the flow log creator, or flow log creation fails. For more
information, see [Bucket policies](../../../AmazonS3/latest/userguide/bucket-policies.md "../../../AmazonS3/latest/userguide/bucket-policies.md")
in the _Amazon Simple Storage Service User Guide_.

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
 "Resource": "arn:aws:s3:::bucket_name/*",
 "Condition": {
 "StringEquals": {
 "s3:x-amz-acl": "bucket-owner-full-control",
 "aws:SourceAccount": "123456789012"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:logs:us-east-1:123456789012:*"
 }
 }
 },
 {
 "Sid": "AWSLogDeliveryCheck",
 "Effect": "Allow",
 "Principal": {
 "Service": "delivery.logs.amazonaws.com"
 },
 "Action": [
 "s3:GetBucketAcl"
 ],
 "Resource": "arn:aws:s3:::bucket_name",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "123456789012"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:logs:us-east-1:123456789012:*"
 }
 }
 }
 ]
}`

```

The ARN that you specify for `my-s3-arn` depends on
whether you use Hive-compatible S3 prefixes.

- Default prefixes

```
arn:aws:s3:::`bucket_name`/`optional_folder`/AWSLogs/`account_id`/*
```

- Hive-compatible S3 prefixes

```
arn:aws:s3:::`bucket_name`/`optional_folder`/AWSLogs/aws-account-id=`account_id`/*
```

As a best practice, we recommend that you grant these permissions to the log
delivery service principal instead of individual AWS account ARNs. It is also a
best practice to use the `aws:SourceAccount` and
`aws:SourceArn` condition keys to protect against [the confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md").
The source account is the owner of the flow log and the source ARN is the wildcard
(\*) ARN of the logs service.

## Required key policy for use with

SSE-KMS

You can protect the data in your Amazon S3 bucket by enabling either Server-Side
Encryption with Amazon S3-Managed Keys (SSE-S3) or Server-Side Encryption with KMS Keys
(SSE-KMS). For more information, see [Protecting data using
server-side encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md") in the _Amazon S3 User
Guide_.

With SSE-KMS, you can use either an AWS managed key or a customer managed key.
With an AWS managed key, you can't use cross-account delivery. Flow logs are
delivered from the log delivery account, so you must grant access for cross-account
delivery. To grant cross-account access to your S3 bucket, use a customer managed
key and specify the Amazon Resource Name (ARN) of the customer managed key when you
enable bucket encryption. For more information, see [Specifying
server-side encryption with AWS KMS](../../../AmazonS3/latest/userguide/specifying-kms-encryption.md "../../../AmazonS3/latest/userguide/specifying-kms-encryption.md") in the _Amazon S3 User
Guide_.

When you use SSE-KMS with a customer managed key, you must add the following to
the key policy for your key (not the bucket policy for your S3 bucket), so that VPC
Flow Logs can write to your S3 bucket.

###### Note

Using S3 Bucket Keys allows you to save on AWS Key Management Service (AWS KMS) request costs
by decreasing your requests to AWS KMS for Encrypt, GenerateDataKey, and Decrypt
operations through the use of a bucket-level key. By design, subsequent requests that
take advantage of this bucket-level key do not result in AWS KMS API requests or validate
access against the AWS KMS key policy.

```
{
    "Sid": "Allow Transit Gateway Flow Logs to use the key",
    "Effect": "Allow",
    "Principal": {
        "Service": [
            "delivery.logs.amazonaws.com"
        ]
    },
   "Action": [
       "kms:Encrypt",
       "kms:Decrypt",
       "kms:ReEncrypt*",
       "kms:GenerateDataKey*",
       "kms:DescribeKey"
    ],
    "Resource": "*"
}
```

## Amazon S3 log file permissions

In addition to the required bucket policies, Amazon S3 uses access control lists (ACLs)
to manage access to the log files created by a flow log. By default, the bucket
owner has `FULL_CONTROL` permissions on each log file. The log delivery
owner, if different from the bucket owner, has no permissions. The log delivery
account has `READ` and `WRITE` permissions. For more
information, see [Access control list
(ACL) overview](../../../AmazonS3/latest/userguide/acl-overview.md "../../../AmazonS3/latest/userguide/acl-overview.md") in the _Amazon Simple Storage Service User Guide_.

## Processed AWS Transit Gateway Flow Logs records in Amazon S3

The log files are compressed. If you open the log files using the Amazon S3 console,
they are decompressed and the flow log records are displayed. If you download the
files, you must decompress them to view the flow log records.
