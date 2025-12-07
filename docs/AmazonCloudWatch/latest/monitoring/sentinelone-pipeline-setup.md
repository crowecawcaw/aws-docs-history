# CloudWatch pipelines configuration for SentinelOne

The SentinelOne setup on AWS reads log data from Amazon S3 buckets using Amazon SQS
notifications for new object events.

Configure the Zscalar source using the following parameters:

```
source:
  s3:
    aws:
      region: "us-east-1"
      sts_role_arn: "arn:aws:iam::<account>:role/<role-name>"
    compression: "gzip"
    codec:
      ndjson:
    data_source_name: "sentinelone_endpointsecurity"
    default_bucket_owner: "123456789012"
    bucket_owners:
      my-bucket: "123456789012"
    disable_bucket_ownership_validation: false
    notification_type: "sqs"
    sqs:
      queue_url: "https://sqs.region.amazonaws.com/<account>/<queue-name>"
    on_error: "retain_messages"

```

###### Parameters

`notification_type` (required)

Specifies the notification mechanism. Must be "sqs" to use SQS for
S3 event notifications.

`data_source_name` (required)

Identifies the data source. This can be any string value that represents
your data source. Example: "sentinelone_endpointsecurity".

`aws.region` (required)

The AWS region where the S3 bucket and SQS queue are
located.

`aws.sts_role_arn` (required)

The ARN of the IAM role to assume for accessing S3 and SQS
resources.

`codec` (required)

Codec configuration for parsing S3 objects. Supports csv, json,
ndjson codecs.

`compression` (optional)

Compression type of the S3 objects. Valid values are "none",
"gzip", "automatic". Defaults to "none".

`sqs.queue_url` (required for SQS)

The complete SQS queue URL that receives S3 bucket notifications
when new objects are created.

`on_error` (optional)

Determines how to handle errors in Amazon SQS. Can be either
retain_messages or delete_messages. Default is
retain_messages.
