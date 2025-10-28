# Troubleshoot VPC Flow Logs

The following are possible issues you might have when working with flow logs.

###### Issues

- [Incomplete flow log records](#flow-logs-troubleshooting-incomplete-records "#flow-logs-troubleshooting-incomplete-records")
- [Flow log is active, but no
  flow log records or log group](#flow-logs-troubleshooting-no-log-group "#flow-logs-troubleshooting-no-log-group")
- ['LogDestinationNotFoundException'
  or 'Access Denied for LogDestination' error](#flow-logs-troubleshooting-not-found "#flow-logs-troubleshooting-not-found")
- [Exceeding the Amazon S3 bucket policy limit](#flow-logs-troubleshooting-policy-limit "#flow-logs-troubleshooting-policy-limit")
- [LogDestination undeliverable](#flow-logs-troubleshooting-kms-id "#flow-logs-troubleshooting-kms-id")
- [Flow logs data size mismatch with billing data](#flow-logs-data-size-mismatch "#flow-logs-data-size-mismatch")

## Incomplete flow log records

###### Problem

Your flow log records are incomplete or are no longer being published.

###### Cause

There might be a problem delivering the flow logs to the CloudWatch Logs log group or
[SkipData entries may be present](flow-logs-records-examples.md#flow-log-example-no-data "flow-logs-records-examples.md#flow-log-example-no-data").

###### Solution

Check the **Flow logs** tab for the VPC, subnet, or network
interface. Note that you can't describe flow logs for a VPC or subnet that was
shared with you, but you can describe flow logs for a network interface that you
create in a VPC or subnet that was shared with you. If there are any errors,
they appear in the **Status** column. Alternatively, use the
[describe-flow-logs](../../../cli/latest/reference/ec2/describe-flow-logs.md "../../../cli/latest/reference/ec2/describe-flow-logs.md")
command, and check the value that's returned in the `DeliverLogsErrorMessage`
field.

The following are possible error values for the status:

- `Rate limited`: This error can occur if CloudWatch Logs throttling has
  been applied — when the number of flow log records for a network
  interface is higher than the maximum number of records that can be published
  within a specific timeframe. This error can also occur if you've reached the
  quota for the number of CloudWatch Logs log groups that you can create. For more
  information, see [CloudWatch
  service quotas](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_limits.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_limits.md") in the
  _Amazon CloudWatch User Guide_.
- `Access error`: This error can occur for one of the following
  reasons:

      + The IAM role for your flow log does not have sufficient
       permissions to publish flow log records to the CloudWatch log group
      + The IAM role does not have a trust relationship with the flow
       logs service
      + The trust relationship does not specify the flow logs service as
       the principal

  For more information, see [IAM role for publishing flow logs to CloudWatch Logs](flow-logs-iam-role.md "flow-logs-iam-role.md").

- `Unknown error`: An internal error has occurred in the flow
  logs service.

## Flow log is active, but no

flow log records or log group

###### Problem

You created a flow log, and the Amazon VPC or Amazon EC2 console displays the flow
log as `Active`. However, you cannot see any log streams in CloudWatch Logs or
log files in your Amazon S3 bucket.

###### Possible causes

- The flow log is still being created. In some cases, it can take ten
  minutes or more after you create the flow log for the log group to be
  created, and for data to be displayed.
- There has been no traffic recorded for your network interfaces yet. The
  log group in CloudWatch Logs is only created when traffic is recorded.

###### Solution

Wait a few minutes for the log group to be created, or for traffic to be
recorded.

## 'LogDestinationNotFoundException'

or 'Access Denied for LogDestination' error

###### Problem

You get a `Access Denied for LogDestination` or a
`LogDestinationNotFoundException` error when you create a
flow log.

###### Possible causes

- When creating a flow log that publishes data to an Amazon S3 bucket, this error
  indicates that the specified S3 bucket could not be found or that the bucket
  policy does not allow logs to be delivered to the bucket.
- When creating a flow log that publishes data to Amazon CloudWatch Logs, this error indicates
  that the IAM role does not allow logs to be delivered to the log group.

###### Solution

- When publishing to Amazon S3, ensure that you have specified the ARN for an existing
  S3 bucket, and that the ARN is in the correct format. If you do not own the S3 bucket,
  verify that the [bucket policy](flow-logs-s3-permissions.md "flow-logs-s3-permissions.md") has
  the required permissions and uses the correct account ID and bucket name in the ARN.
- When publishing to CloudWatch Logs, verify that the [IAM role](flow-logs-iam-role.md "flow-logs-iam-role.md")
  has the required permissions.

## Exceeding the Amazon S3 bucket policy limit

###### Problem

You get the following error when you try to create a flow log:
`LogDestinationPermissionIssueException`.

###### Possible causes

Amazon S3 bucket policies are limited to 20 KB in size.

Each time that you create a flow log that publishes to an Amazon S3 bucket, we
automatically add the specified bucket ARN, which includes the folder path, to the
`Resource` element in the bucket's policy.

Creating multiple flow logs that publish to the same bucket could cause you to
exceed the bucket policy limit.

###### Solution

- Clean up the bucket policy by removing the flow log entries that are no
  longer needed.
- Grant permissions to the entire bucket by replacing the individual flow
  log entries with the following.

```
arn:aws:s3:::`bucket_name/*`
```

If you grant permissions to the entire bucket, new flow log subscriptions
do not add new permissions to the bucket policy.

## LogDestination undeliverable

###### Problem

You get the following error when you try to create a flow log:
`LogDestination <bucket name> is undeliverable`.

###### Possible causes

The target Amazon S3 bucket is encrypted using server-side encryption with AWS KMS
(SSE-KMS) and the default encryption of the bucket is a KMS key ID.

###### Solution

The value must be a KMS key ARN. Change the default S3 encryption type from
KMS key ID to KMS key ARN. For more information, see [Configuring
default encryption](../../../AmazonS3/latest/userguide/default-bucket-encryption.md "../../../AmazonS3/latest/userguide/default-bucket-encryption.md") in the
_Amazon Simple Storage Service User Guide_.

## Flow logs data size mismatch with billing data

###### Problem

The total data size of your flow logs does not match the size reported by billing data.

###### Possible causes

There may be SKIPDATA entries in your flow logs. See [No data and skipped records](flow-logs-records-examples.md#flow-log-example-no-data "flow-logs-records-examples.md#flow-log-example-no-data") for an explanation of SKIPDATA entries.

###### Solution

Confirm that SKIPDATA entries are present in your log entries by querying your logs for different entries in the log-status field.

Sample queries to check for SKIPDATA:

CW Insights:

````
fields @timestamp, @message, @logStream, @log
| filter interfaceId = 'eni-123'
| stats count(*) by interfaceId, logStatus
| sort by interfaceId, logStatus ``` Athena: ``` SELECT log_status, interface_id, count(1) FROM vpc_flow_logs WHERE interface_id IN ('eni-1', 'eni-2', 'eni-3') GROUP BY log_status, interface_id ```
````
