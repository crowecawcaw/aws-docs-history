# Configuring and using flow logs in AWS Global Accelerator

Flow logs enable you to capture information about the IP address traffic going to and from network interfaces in
your accelerator in AWS Global Accelerator. Flow log data is published to Amazon S3, where you can retrieve and view your data after you've
created a flow log.

###### Note

You must view CloudWatch metrics and logs for Global Accelerator in the US West (Oregon) Region, both in the
console or when using the AWS CLI. When you use the AWS CLI, specify the US West (Oregon) Region
for your command by including the following parameter: `--region us-west-2`.

Flow logs can help you with a number of tasks. For example, you can troubleshoot why
specific traffic is not reaching an endpoint, which in turn helps you diagnose overly
restrictive security group rules. You can also use flow logs as a security tool to
monitor the traffic that is reaching your endpoints.

A flow log record represents a network flow in your flow log. Each record captures the network flow for a specific
5-tuple, for a specific capture window. A 5-tuple is a set of five different values that specify the source,
destination, and protocol for an IP flow. The capture window is a duration of time during which the flow logs service
aggregates data before publishing flow log records. The capture window is up to 1 minute. That is, logs might
be published more frequently than every minute, but will be published at least every minute.

CloudWatch Logs charges apply when using flow logs, even when logs are published directly to Amazon S3. For
more information, see _Vended Logs_ under the _Logs_ tab at
[Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

###### Tip

Using Amazon Athena and Amazon Quick Suite with your Global Accelerator flow log data can help you troubleshoot reachability
issues for your application, identify security vulnerabilities, and get an overview of how users access
your application. To learn more, see the following AWS blog post:
[Analyzing and visualizing AWS Global Accelerator flow logs using Amazon Athena and Quick Suite](https://aws.amazon.com/blogs/networking-and-content-delivery/analyzing-and-visualizing-aws-global-accelerator-flow-logs-using-amazon-athena-and-amazon-quicksight/ "https://aws.amazon.com/blogs/networking-and-content-delivery/analyzing-and-visualizing-aws-global-accelerator-flow-logs-using-amazon-athena-and-amazon-quicksight/").

###### Contents

- [Enable flow logs](#monitoring-global-accelerator.flow-logs-publishing-S3.enable "#monitoring-global-accelerator.flow-logs-publishing-S3.enable")
- [Process flow log records](#monitoring-global-accelerator.flow-logs-publishing-S3.processing "#monitoring-global-accelerator.flow-logs-publishing-S3.processing")
- [Publishing to Amazon S3](#monitoring-global-accelerator.flow-logs-publishing-S3 "#monitoring-global-accelerator.flow-logs-publishing-S3")
- [Timing of log files](#monitoring-global-accelerator.flow-logs.timing "#monitoring-global-accelerator.flow-logs.timing")
- [Flow log record syntax](#monitoring-global-accelerator.flow-logs.records.syntax "#monitoring-global-accelerator.flow-logs.records.syntax")

## Enable

publishing flow logs to Amazon S3

To enable flow logs in AWS Global Accelerator, follow the steps in this procedure. Additional sections in this chapter
provide the steps to configure your Amazon S3 bucket and set up permissions, so that flow logs can be published
and accessed.

## To enable flow logs in

AWS Global Accelerator

1. Create an Amazon S3 bucket for your flow logs in your AWS account.
2. Add the required IAM policy for the AWS user who is enabling the flow logs. For
   more information, see [IAM roles for
   publishing flow logs to Amazon S3](#monitoring-global-accelerator.flow-logs-publishing-S3.roles "#monitoring-global-accelerator.flow-logs-publishing-S3.roles").
3. Run the following AWS CLI command, with the Amazon S3 bucket name and prefix that you want to use for
   your log files:

```
aws globalaccelerator update-accelerator-attributes
       --accelerator-arn arn:aws:globalaccelerator::`012345678901`:accelerator/`1234abcd-abcd-1234-abcd-1234abcdefgh`
       --region us-west-2
       --flow-logs-enabled
       --flow-logs-s3-bucket `s3-bucket-name`
       --flow-logs-s3-prefix `s3-bucket-prefix`
```

## Processing

flow log records in Amazon S3

The log files are compressed. If you open the log files using the Amazon S3 console, they are decompressed and
the flow log records are displayed. If you download the files, you must decompress them to view the flow log
records.

## Publishing flow logs to Amazon S3

Flow logs for AWS Global Accelerator are published to Amazon S3 to an existing S3 bucket that you specify. Flow log records are
published to a series of log file objects that are stored in the bucket.

To create an Amazon S3 bucket for use with flow logs, see [Create your first
S3 bucket](../../../AmazonS3/latest/userguide/CreatingABucket.md "../../../AmazonS3/latest/userguide/CreatingABucket.md") in the _Amazon Simple Storage Service User Guide_.

### Flow logs files

Flow logs collect flow log records, consolidate them into log files, and then publish the log files to the
Amazon S3 bucket at 5-minute intervals. That is, log files are written every five minutes, and each log file contains
flow log records for the IP address traffic recorded in the previous five minutes.

The maximum file size for a log file is 75 MB. If the log file reaches the file size limit within the
5-minute period, the flow log stops adding flow log records to it, publishes it to the Amazon S3 bucket, and then
creates a new log file.

Log files are saved to the specified Amazon S3 bucket using a folder structure that is determined by the flow
log's ID, Region, and the date on which they are created. The bucket folder structure uses the following
format:

```
`s3-bucket_name`/`s3-bucket-prefix`/AWSLogs/`aws_account_id`/globalaccelerator/`region`/`yyyy/mm/dd`/
```

Similarly, the log file name is determined by the flow log's ID, Region, and the date and
time it was created. File names use the following format:

```
`aws_account_id`_globalaccelerator_`accelerator_id`_`flow_log_id_timestamp_hash`.log.gz
```

Note the following about the folder and file name structure for log files:

- The timestamp uses the `YYYYMMDDTHHmmZ` format.
- If you specify slash (/) for the S3 bucket prefix, the log file bucket folder structure will include a double slash (//), like the following:

```
`s3-bucket_name`//AWSLogs/`aws_account_id`
```

The following example shows the folder structure and file name of a log file for a flow
log created by AWS account `123456789012` for an accelerator
with an ID of `1234abcd-abcd-1234-abcd-1234abcdefgh`, on November 23,
2018 at 00:05 UTC:

```
amzn-s3-demo-bucket/prefix1/AWSLogs/123456789012/globalaccelerator/us-west-2/2018/11/23/123456789012_globalaccelerator_1234abcd-abcd-1234-abcd-1234abcdefgh_20181123T0005Z_1fb1234.log.gz
```

A single flow log file contains interleaved entries with multiple 5-tuple records; that
is, `client_ip`, `client_port`, `accelerator_ip`,
`accelerator_port`, `protocol`. To see all the flow log files
for your accelerator, look for entries aggregated by the
`accelerator_id` and your `account_id`.

### IAM roles for

publishing flow logs to Amazon S3

An IAM principal, such as an IAM role or user, must have sufficient permissions to publish flow logs to the Amazon S3
bucket. The IAM policy must include the following permissions. To learn more about how to create policies, including
where and how to add JSON similar to the following to an IAM policy, see [Identity-based policy
examples for AWS Global Accelerator](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md")

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DeliverLogs",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogDelivery",
 "logs:DeleteLogDelivery"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowGlobalAcceleratorService",
 "Effect": "Allow",
 "Action": [
 "globalaccelerator:*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "s3Perms",
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketPolicy",
 "s3:PutBucketPolicy"
 ],
 "Resource": "*"
 }
 ]
}`

```

###

Amazon S3 bucket permissions for flow logs

By default, Amazon S3 buckets and the objects that they contain are private. Only the bucket
owner can access the bucket and the objects stored in it. The bucket owner,
however, can grant access to other resources and users by writing an access
policy.

If the user creating the flow log owns the bucket, the service automatically attaches the
following policy to the bucket to give the flow log permission to publish logs
to it:

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
 "Resource": "arn:aws:s3:::`bucket_name/optional_folder`/AWSLogs/`account_id`/*",
 "Condition": {"StringEquals": {"s3:x-amz-acl": "bucket-owner-full-control"}}
 },
 {
 "Sid": "AWSLogDeliveryAclCheck",
 "Effect": "Allow",
 "Principal": {"Service": "delivery.logs.amazonaws.com"},
 "Action": "s3:GetBucketAcl",
 "Resource": "arn:aws:s3:::`bucket_name`"
 }
 ]
}`

```

If the user creating the flow log does not own the bucket, or does not have the
`GetBucketPolicy` and `PutBucketPolicy` permissions
for the bucket, the flow log creation fails. In this case, the bucket owner must
manually add the preceding policy to the bucket and specify the flow log
creator's AWS account ID. For more information, see [Adding a bucket policy by using the Amazon S3 console](../../../AmazonS3/latest/userguide/add-bucket-policy.md "../../../AmazonS3/latest/userguide/add-bucket-policy.md") in the _Amazon Simple Storage Service User Guide_. If the bucket
receives flow logs from multiple accounts, add a `Resource` element
entry to the `AWSLogDeliveryWrite` policy statement for each account.

For example, the following bucket policy allows AWS accounts 123123123123 and
456456456456 to publish flow logs to a folder named `flow-logs` in a
bucket named `log-bucket`:

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
 "arn:aws:s3:::log-bucket/flow-logs/AWSLogs/123123123123/*",
 "arn:aws:s3:::log-bucket/flow-logs/AWSLogs/456456456456/*"
 ],
 "Condition": {"StringEquals": {"s3:x-amz-acl": "bucket-owner-full-control"}}
 },
 {
 "Sid": "AWSLogDeliveryAclCheck",
 "Effect": "Allow",
 "Principal": {"Service": "delivery.logs.amazonaws.com"},
 "Action": "s3:GetBucketAcl",
 "Resource": "arn:aws:s3:::log-bucket"
 }
 ]
}`

```

###### Note

We recommend that you grant the `AWSLogDeliveryAclCheck` and `AWSLogDeliveryWrite`
permissions to the log delivery service principal instead of individual AWS account ARNs.

### Required CMK key policy

for use with SSE-KMS buckets

If you enabled server-side encryption for your Amazon S3 bucket using AWS KMS-managed keys
(SSE-KMS) with a customer-managed CMK, you must add the
following to the key policy for your CMK so that flow logs can write log files
to the bucket:

```
{
    "Sid": "Allow AWS Global Accelerator Flow Logs to use the key",
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

###

Amazon S3 log file permissions

In addition to the required bucket policies, Amazon S3 uses access control lists (ACLs) to manage access to the
log files created by a flow log. By default, the bucket owner has `FULL_CONTROL` permissions on
each log file. The log delivery owner, if different from the bucket owner, has no permissions. The log
delivery account has `READ` and `WRITE` permissions. For more information, see [Access control list (ACL) overview](../../../AmazonS3/latest/userguide/acl-overview.md "../../../AmazonS3/latest/userguide/acl-overview.md") in the
_Amazon Simple Storage Service User Guide_.

## Timing of log file delivery

AWS Global Accelerator delivers log files for your configured accelerator up to several times an hour. In
general, a log file contains information about the requests that your accelerator
received during a given time period. Global Accelerator usually delivers the log file for that
time period to your Amazon S3 bucket within an hour of the events that appear in the log.
Some or all log file entries for a time period can sometimes be delayed by up to 24
hours. When log entries are delayed, Global Accelerator saves them in a log file for which the
file name includes the date and time of the period in which the requests occurred,
not the date and time when the file was delivered.

When creating a log file, Global Accelerator consolidates information for your accelerator from all the
edge locations that received requests during the time period that the log file
covers.

Global Accelerator begins to reliably deliver log files about four hours after you enable logging. You might get a few log
files before that time.

###### Note

If no users connect to your accelerator during the time period, you don't receive any log files for that
period.

## Flow log record syntax

A flow log record is a space-separated string that has the following format:

`<version> <aws_account_id> <accelerator_id> <client_ip> <client_port>
 <accelerator_ip> <accelerator_port> <endpoint_ip> <endpoint_port> <protocol>
 <ip_address_type> <packets> <bytes> <start_time> <end_time> <action>
 <log-status> <globalaccelerator_source_ip> <globalaccelerator_source_port> <endpoint_region>
 <globalaccelerator_region> <direction> <vpc_id> <reject_reason>`

The Version 1.0 format does not include the VPC identifier, `vpc_id`. The Version 2.0 format,
which includes `vpc_id`, is generated when Global Accelerator sends traffic to an endpoint with client
IP address preservation.

The following table describes the fields of a flow log record.

| Field                           | Description                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `version`                       | The flow logs version.                                                                                                                                                                                                                                                                                                                                              |
| `aws_account_id`                | The AWS account ID for the flow log.                                                                                                                                                                                                                                                                                                                                |
| `accelerator_id`                | The ID of the accelerator for which the traffic is recorded.                                                                                                                                                                                                                                                                                                        |
| `client_ip`                     | The source IPv4 or IPv6 address.                                                                                                                                                                                                                                                                                                                                    |
| `client_port`                   | The source port.                                                                                                                                                                                                                                                                                                                                                    |
| `accelerator_ip`                | The accelerator's IP address.                                                                                                                                                                                                                                                                                                                                       |
| `accelerator_port`              | The accelerator's port.                                                                                                                                                                                                                                                                                                                                             |
| `endpoint_ip`                   | The destination IP address of the traffic.                                                                                                                                                                                                                                                                                                                          |
| `endpoint_port`                 | The destination port of the traffic.                                                                                                                                                                                                                                                                                                                                |
| `protocol`                      | The IANA protocol number of the traffic. For more information, see [Assigned Internet Protocol Numbers](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml "https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml").                                                                                                       |
| `ip_address_type`               | IPv4 or IPv6.                                                                                                                                                                                                                                                                                                                                                       |
| `packets`                       | The number of packets transferred during the capture window. When the number of packets is 0 (zero), the flow is alive but no packets were seen in that direction during a capture window.                                                                                                                                                                          |
| `bytes`                         | The number of bytes transferred during the capture window.                                                                                                                                                                                                                                                                                                          |
| `start_time`                    | The time, in Unix seconds, of the start of the capture window.                                                                                                                                                                                                                                                                                                      |
| `end_time`                      | The time, in Unix seconds, of the end of the capture window.                                                                                                                                                                                                                                                                                                        |
| `action`                        | The action associated with the traffic: <br>• `ACCEPT`: The recorded traffic was permitted by the security groups or network ACLs. The value is currently always ACCEPT.                                                                                                                                                                                            |
| `log-status`                    | The logging status of the flow log: <br>• `OK`: Data is logging normally to the chosen destinations. <br>• `SKIPDATA`: Some flow log records were skipped during the capture window. This can be because of an internal capacity constraint, or an internal error.                                                                                                  |
| `globalaccelerator_source_ip`   | The IP address used by the Global Accelerator network interface. If client IP address preservation is enabled, this value is set to - (hyphen). For more information, see [Preserve client IP addresses in AWS Global Accelerator](preserve-client-ip-address.md "preserve-client-ip-address.md").                                                                  |
| `globalaccelerator_source_port` | The port used by the Global Accelerator network interface. If client IP address preservation is enabled, this value is set to 0 (zero). For more information, see [Preserve client IP addresses in AWS Global Accelerator](preserve-client-ip-address.md "preserve-client-ip-address.md").                                                                          |
| `endpoint_region`               | The AWS Region where the endpoint is located.                                                                                                                                                                                                                                                                                                                       |
| `globalaccelerator_region`      | The edge location (point of presence) that served the request. Each edge location has a three-letter code and an arbitrarily assigned number, for example, DFW3. The three-letter code typically corresponds with the International Air Transport Association airport code for an airport near the edge location. (These abbreviations might change in the future.) |
| `direction`                     | The direction of the traffic. Denotes traffic coming into the Global Accelerator network (`INGRESS`) or returning to the client (`EGRESS`).                                                                                                                                                                                                                         |
| `vpc_id`                        | The VPC identifier. Included with Version 2.0 flow logs when Global Accelerator sends traffic to an endpoint with client IP address preservation.                                                                                                                                                                                                                   |
| `reject_reason`                 | The reason traffic was not served. The value is `BPA` if traffic was not served due to VPC Block Public Access feature settings. Otherwise, the field is empty.                                                                                                                                                                                                     | If a field does not apply for a specific record, the record displays a '-' symbol for that entry. |
