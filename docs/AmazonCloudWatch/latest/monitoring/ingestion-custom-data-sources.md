# Custom log data from CloudWatch Logs or an Amazon S3 bucket

You can create pipelines for custom data sources using the following
approaches:

1.  **CloudWatch Custom Logs** – Define
    pipelines on your existing CloudWatch custom log groups by providing:

        * A data source name
        * A data source type

    For more information on data source name and type, see the [CloudWatch Logs User Guide](../logs/data-source-discovery-management.md#how-to-get-started-data-sources "../logs/data-source-discovery-management.md#how-to-get-started-data-sources").

2.  **S3 Custom Sources** – Process arbitrary
    logs stored in S3 buckets by configuring source for the pipeline:

```
source:
  s3:
    aws:
      region: "us-east-1"
      sts_role_arn: "arn:aws:iam::<account>:role/<role-name>"
    compression: "gzip"
    codec:
      ndjson:
    data_source_name: "my_custom_logs"
    default_bucket_owner: "123456789012"
    bucket_owners:
      my-bucket: "123456789012"
    disable_bucket_ownership_validation: false
    notification_type: "sqs"
    sqs:
      queue_url: "https://sqs.region.amazonaws.com/<account>/<queue-name>"
    on_error: "retain_messages"
```

###### Note

The CSV processor can’t be used with S3 custom sources. Instead, use the
CSV codec in the S3 source.

###### Parameters

`notification_type` (required)

Specifies the notification mechanism. Must be "sqs" to use SQS for
S3 event notifications.

`data_source_name`

Identifies the data source. This can be any string value that
represents your data source. Example: "my_custom_logs".

`aws.region` (required)

The AWS region where the S3 bucket and SQS queue are
located.

`aws.sts_role_arn` (required)

The ARN of the IAM role to assume for accessing S3 and SQS
resources.

`codec` (required)

Codec configuration for parsing S3 objects. Supports
`csv`, `json`, `ndjson`
codecs.

`compression` (optional)

Compression type of the S3 objects. Valid values are "none",
"gzip", "automatic". Defaults to "none".

`sqs.queue_url` (required for SQS)

The complete SQS queue URL that receives S3 bucket notifications
when new objects are created.

`on_error` (optional)

Determines how to handle errors in Amazon SQS. Can be either
`retain_messages` or `delete_messages`.
Default is `retain_messages`.
**Custom source configuration**

When creating a pipeline for custom sources:

- A parser must be the first processor in the pipeline if the data source is CloudWatch Logs
- You can specify any supported processor for custom log pipelines
