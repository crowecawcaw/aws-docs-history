# Sending AWS Network Firewall logs to Amazon Simple Storage Service

To send your firewall logs to Amazon S3, you need to set up an Amazon S3 bucket as the destination for the
logs. In your bucket configuration for the firewall, you can optionally include
a prefix, to immediately follow the bucket name. When you enable logging to Amazon S3 in
Network Firewall, you provide the bucket name and, if you are using one, the
prefix. For information about creating your logging bucket, see [Create a Bucket](../../../AmazonS3/latest/userguide/CreatingABucket.md "../../../AmazonS3/latest/userguide/CreatingABucket.md") in the
_Amazon Simple Storage Service User Guide_.

###### Note

Network Firewall supports encryption with Amazon S3 buckets for key type Amazon S3 key (SSE-S3) and for AWS Key Management Service (SSE-KMS) AWS KMS keys. Network Firewall doesn't support encryption for AWS Key Management Service keys that are managed by AWS.

###### Note

For information about the fees associated with sending logs to Amazon S3, see [Pricing for AWS Network Firewall logging](firewall-logging-pricing.md "firewall-logging-pricing.md").

###### Important

If you enable detailed monitoring for a firewall that sends alert or flow logs to Amazon S3,
Network Firewall uses Amazon Athena to create tables as required in your account.
These tables process log data and are used exclusively for populating firewall monitoring dashboards and are managed by the Network Firewall console.
For more information on how Amazon S3 integrates with Amazon Athena,
see [https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-inventory-athena-query.html](../../../AmazonS3/latest/userguide/storage-inventory-athena-query.md "../../../AmazonS3/latest/userguide/storage-inventory-athena-query.md").

###### Important

To use the firewall monitoring dashboard functionality with S3 logging destinations:

- The Amazon S3 bucket storing the logs must be in the same region as the firewall.
  This is required for Amazon Athena to process the logs, as cross-region processing is not supported.
- If you specify a prefix for your S3 bucket, ensure it does not begin with a forward slash (`/`).
  Prefixes starting with (`/`) are not compatible with Amazon Athena processing
  and will prevent the dashboard from functioning correctly.
  Network Firewall collects log records, consolidates them into log files, and then
  publishes the log files to the Amazon S3 bucket at 5-minute intervals. Each log file
  contains log records for the network traffic recorded in the previous five
  minutes.

The maximum file size for a log file is 75 MB. If the log file reaches the
file size limit within the 5-minute period, the log stops adding records to it,
publishes it to the Amazon S3 bucket, and then creates a new log file.

A single log file contains interleaved entries with multiple connection identifier (source IP address, source port, destination IP address, destination port, and protocol) records.
To see all the log files for your firewall, look for entries aggregated by the
firewall name and your account ID.

Log files are saved in the specified Amazon S3 bucket using a folder structure
that's determined by the log's ID, Region, Network Firewall log type, and the date.
The bucket folder structure uses the following format:

```
`s3-bucket-name``/optional-s3-bucket-prefix`/AWSLogs/`aws-account-id`/network-firewall/`log-type`/`Region`/`firewall-name`/`timestamp`/
```

Similarly, the log file name is determined by the flow log's ID, Region, and
the date and time it was created. File names use the following format:

```
`aws-account-id`_network-firewall_`log-type`_`Region_`firewall-name`_timestamp_hash`.log.gz
```

In the specification of the folder and file name, the following apply:

- The log type is either `alert`, `flow`, or
  `tls`.
- The timestamp uses the `YYYYMMDDTHHmmZ` format.
- If you don't provide a specification for the S3 bucket prefix, the log
  file bucket folder structure will be similar to the following:

```
`s3-bucket-name`/AWSLogs/`aws-account-id`
```

- If you specify slash (`/`) for the S3 bucket prefix, or
  provide a prefix that begins with a slash, the log file bucket folder
  structure will contain a double slash (`//`), like the
  following for a prefix set to a single slash:

```
`s3-bucket-name`//AWSLogs/`aws-account-id`
```

The following shows an example flow log file in Amazon S3 for AWS account
`11111111111`, firewall name `test-firewall`, bucket
name `s3://amzn-s3-demo-bucket`, and bucket prefix
`flow-logs`.

```
s3://amzn-s3-demo-bucket/flow-logs/AWSLogs/11111111111/network-firewall/flow/us-east-1/test-firewall/2020/10/01/19/11111111111_network-firewall_flow_us-east-1_test-firewall_202010011920_44442222.log.gz
```

## Permissions to publish logs to

Amazon S3

You must have the following permissions settings to configure your
firewall to send logs to Amazon S3.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "logs:CreateLogDelivery",
 "logs:GetLogDelivery",
 "logs:UpdateLogDelivery",
 "logs:DeleteLogDelivery",
 "logs:ListLogDeliveries"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow",
 "Sid": "FirewallLogging"
 },
 {
 "Sid": "FirewallLoggingS3",
 "Action": [
 "s3:PutBucketPolicy",
 "s3:GetBucketPolicy"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket-name`"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

By default, Amazon S3 buckets and the objects that they contain are private.
Only the bucket owner can access the bucket and the objects stored in it.
The bucket owner, however, can grant access to other resources and users by
writing an access policy.

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
 "Principal": {"Service": "delivery.logs.amazonaws.com"},
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`bucket-name/optional-folder`/AWSLogs/`123456789012`/*",
 "Condition": {"StringEquals": {"s3:x-amz-acl": "bucket-owner-full-control"}}
 },
 {
 "Sid": "AWSLogDeliveryAclCheck",
 "Effect": "Allow",
 "Principal": {"Service": "delivery.logs.amazonaws.com"},
 "Action": "s3:GetBucketAcl",
 "Resource": "arn:aws:s3:::`bucket-name`"
 }
 ]
}`

```

If the user creating the log doesn't own the bucket, or doesn't have the
`GetBucketPolicy` and `PutBucketPolicy`
permissions for the bucket, the log creation fails. In this case, the bucket
owner must manually add the preceding policy to the bucket and specify the
log creator's AWS account ID. For more information, see [How Do I Add an S3 Bucket
Policy?](../../../AmazonS3/latest/userguide/add-bucket-policy.md "../../../AmazonS3/latest/userguide/add-bucket-policy.md") in the _Amazon Simple Storage Service User Guide_. If the
bucket receives logs from multiple accounts, add a `Resource`
element entry to the `AWSLogDeliveryWrite` policy statement for
each account.

For example, the following bucket policy allows AWS accounts
`111122223333` and
`444455556666` to publish logs to a folder named
`flow-logs` in a bucket named
`amzn-s3-demo-bucket`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AWSLogDeliveryWrite",
 "Effect": "Allow",
 "Principal": {"Service": "delivery.logs.amazonaws.com"},
 "Action": "s3:PutObject",
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket:/flow-logs/AWSLogs/111122223333/",
 "arn:aws:s3:::amzn-s3-demo-bucket:/flow-logs/AWSLogs/444455556666/"
 ],
 "Condition": {"StringEquals": {"s3:x-amz-acl": "bucket-owner-full-control"}}
 },
 {
 "Sid": "AWSLogDeliveryAclCheck",
 "Effect": "Allow",
 "Principal": {"Service": "delivery.logs.amazonaws.com"},
 "Action": "s3:GetBucketAcl",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket"
 }
 ]
}`

```

## (Optional) Permissions to access Amazon S3 log metrics in Network Firewall using Amazon Athena

In addition to your existing Amazon S3 permissions, you must have the following permissions for flow or alert log metrics to populate the firewall monitoring dashboard.

###### Important

When you enable firewall monitoring for a firewall that sends logs to Amazon S3, Network Firewall uses Amazon Athena to create tables and metadata files (including CSV files) in your S3 bucket. To optimize storage costs, we recommend periodically cleaning up these metadata files when they are no longer needed.

If you haven't already verified that your account has the baseline logging permissions, go do that now. For more information, see [Permissions to configure AWS Network Firewall logging](firewall-logging-permissions.md "firewall-logging-permissions.md").

###### Important

Additional fees are incurred when Network Firewall uses Amazon Athena to query Amazon S3 logs for the detailed monitoring dashboard.
For best practices to minimize additional cost, see [Working with the firewall monitoring dashboard](nwfw-using-dashboard.md "nwfw-using-dashboard.md").

```
{
            "Effect": "Allow",
            "Action": [
                "athena:StartQueryExecution",
                "athena:GetQueryExecution",
                "athena:GetQueryResults"
            ],
            "Resource": "*"
        },
{
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:GetBucketLocation",
                "s3:ListBuckets",
                "s3:ListBucket"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "glue:GetTable",
                "glue:GetDatabase",
                "glue:GetPartitions",
                "glue:CreateTable",
                "glue:DeleteTable"
            ],
            "Resource": "*"
        }

```

If you're using CloudWatch Logs as a logging destination, you'll need additional permissions. For more information, see [Permissions to publish logs to CloudWatch Logs](logging-cw-logs.md#logging-cw-logs-permissions "logging-cw-logs.md#logging-cw-logs-permissions").

The following view shows both standard Amazon S3 permissions and the additional Athena permissions needed for detailed monitoring.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "FirewallLogging",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogDelivery",
 "logs:GetLogDelivery",
 "logs:UpdateLogDelivery",
 "logs:DeleteLogDelivery",
 "logs:ListLogDeliveries"
 ],
 "Resource": "*"
 },
 {
 "Sid": "FirewallLoggingS3",
 "Effect": "Allow",
 "Action": [
 "s3:PutBucketPolicy",
 "s3:GetBucketPolicy",
 "s3:PutObject",
 "s3:GetObject",
 "s3:GetBucketLocation",
 "s3:ListAllMyBuckets",
 "s3:ListBucket"
 ],
 "Resource": "*"
 },
 {
 "Sid": "FirewallLoggingAthena",
 "Effect": "Allow",
 "Action": [
 "athena:StartQueryExecution",
 "athena:GetQueryExecution",
 "athena:GetQueryResults"
 ],
 "Resource": "*"
 },
 {
 "Sid": "FirewallLoggingGlue",
 "Effect": "Allow",
 "Action": [
 "glue:GetTable",
 "glue:GetDatabase",
 "glue:GetPartitions",
 "glue:CreateTable",
 "glue:DeleteTable"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Amazon S3 log file access

In addition to the required bucket policies, Amazon S3 uses access control
lists (ACLs) to manage access to the log files created by a Network Firewall
log. By default, the bucket owner has `FULL_CONTROL` permissions
on each log file. The log delivery owner, if different from the bucket
owner, has no permissions. The log delivery account has `READ`
and `WRITE` permissions. For more information, see [Access Control List (ACL)
Overview](../../../AmazonS3/latest/userguide/acl-overview.md "../../../AmazonS3/latest/userguide/acl-overview.md") in the _Amazon Simple Storage Service User Guide_.

The log files are compressed. If you open the files using the Amazon S3
console, Amazon S3 decompresses the log records and displays them. If you
download the log files, you must decompress them to view the records.
