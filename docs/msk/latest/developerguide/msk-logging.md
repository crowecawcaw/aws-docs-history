# Amazon MSK logging

You can deliver Apache Kafka broker logs to one or more of the following destination
types: Amazon CloudWatch Logs, Amazon S3, Amazon Data Firehose. You can also log Amazon MSK API calls with AWS CloudTrail.

###### Note

Broker logs are not available on Express brokers.

## Broker logs

Broker logs enable you to troubleshoot your Apache Kafka applications and to analyze their communications with your MSK cluster. You can configure your new or existing MSK cluster to deliver INFO-level broker logs to one or more of the following types of destination resources: a CloudWatch log group, an S3 bucket, a Firehose delivery stream. Through Firehose you can then deliver the log data from your delivery stream to OpenSearch Service.

You must create a destination resource before you configure your cluster to deliver broker logs to it. Amazon MSK doesn't create these destination resources for you if they don't already exist. For information about these three types of destination resources and how to create them, see the following documentation:

- [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md")
- [Amazon S3](../../../AmazonS3/latest/dev/Welcome.md "../../../AmazonS3/latest/dev/Welcome.md")
- [Amazon Data Firehose](../../../firehose/latest/dev/what-is-this-service.md "../../../firehose/latest/dev/what-is-this-service.md")

### Required permissions

To configure a destination for Amazon MSK broker logs, the IAM identity that you use
for Amazon MSK actions must have the permissions described in the [AWS managed policy:
AmazonMSKFullAccess](security-iam-awsmanpol-AmazonMSKFullAccess.md "security-iam-awsmanpol-AmazonMSKFullAccess.md") policy.

To stream broker logs to an S3 bucket, you also need the
`s3:PutBucketPolicy` permission. For information about S3 bucket
policies, see [How Do I Add an S3 Bucket Policy?](../../../AmazonS3/latest/user-guide/add-bucket-policy.md "../../../AmazonS3/latest/user-guide/add-bucket-policy.md") in the Amazon S3 User Guide. For
information about IAM policies in general, see [Access
Management](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md") in the IAM User Guide.

### Required KMS key policy for use with SSE-KMS buckets

If you enabled server-side encryption for your S3 bucket using AWS KMS-managed keys (SSE-KMS) with a customer managed key,
add the following to the key policy for your KMS key so that Amazon MSK can write broker files to the bucket.

```
{
  "Sid": "Allow Amazon MSK to use the key.",
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

### Configure broker logs using the AWS Management Console

If you are creating a new cluster, look for the **Broker log
delivery** heading in the **Monitoring** section. You
can specify the destinations to which you want Amazon MSK to deliver your broker logs.

For an existing cluster, choose the cluster from your list of clusters, then
choose the **Properties** tab. Scroll down to the
**Log delivery** section and then choose its
**Edit** button. You can specify the destinations to which
you want Amazon MSK to deliver your broker logs.

### Configure broker logs using the AWS CLI

When you use the `create-cluster` or the `update-monitoring` commands, you can optionally specify the `logging-info` parameter and pass to it a JSON structure like the following example. In this JSON, all three destination types are optional.

###### Note

You must set the `LogDeliveryEnabled` tag to `true`on Firehose streams to set up log delivery. The service-linked role that AWS creates for CloudWatch logs uses this tag to grant permission for all Firehose delivery streams. If you remove this tag, the service-linked role won't be able to deliver logs to the Firehose stream. To see an example of an IAM policy that shows the permissions that the service-linked role includes, see [IAM roles used for resource permissions](../../../AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-Firehose.md "../../../AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-Firehose.md") in the _Amazon CloudWatch User Guide_.

```
{
  "BrokerLogs": {
    "S3": {
      "Bucket": "amzn-s3-demo-bucket",
      "Prefix": "ExamplePrefix",
      "Enabled": true
    },
    "Firehose": {
      "DeliveryStream": "ExampleDeliveryStreamName",
      "Enabled": true
    },
    "CloudWatchLogs": {
      "Enabled": true,
      "LogGroup": "ExampleLogGroupName"
    }
  }
}
```

### Configure broker logs using the API

You can specify the optional `loggingInfo` structure in the JSON that
you pass to the [CreateCluster](../../1.0/apireference/clusters.md#CreateCluster "../../1.0/apireference/clusters.md#CreateCluster") or [UpdateMonitoring](../../1.0/apireference/clusters-clusterarn-monitoring.md#UpdateMonitoring "../../1.0/apireference/clusters-clusterarn-monitoring.md#UpdateMonitoring") operations.

###### Note

By default, when broker logging is enabled, Amazon MSK logs `INFO` level logs to the specified
destinations. However, users of Apache Kafka 2.4.X and later can dynamically set the broker log level to any of the
[log4j log levels](https://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/Level.html "https://logging.apache.org/log4j/1.2/apidocs/org/apache/log4j/Level.html"). For
information about dynamically setting the broker log level, see
[KIP-412: Extend Admin API to support dynamic application log levels](https://cwiki.apache.org/confluence/display/KAFKA/KIP-412%3A+Extend+Admin+API+to+support+dynamic+application+log+levels "https://cwiki.apache.org/confluence/display/KAFKA/KIP-412%3A+Extend+Admin+API+to+support+dynamic+application+log+levels").
If you dynamically set the log level to `DEBUG` or `TRACE`, we recommend using Amazon S3 or Firehose
as the log destination. If you use CloudWatch Logs as a log destination and you dynamically enable `DEBUG`
or `TRACE` level logging, Amazon MSK may continuously deliver a sample of logs. This can significantly impact
broker performance and should only be used when the `INFO` log level is not verbose enough to determine
the root cause of an issue.
