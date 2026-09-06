

# CloudWatch pipelines configuration for Broadcom Carbon Black
<a name="broadcom-carbonblack-pipeline-setup"></a>

The Broadcom Carbon Black setup on AWS reads log data from Amazon S3 buckets using Amazon SQS notifications for new object events.

Configure the Broadcom Carbon Black source with the following parameters:

```
source:
  s3:
    aws:
      region: "<aws_region>"
      sts_role_arn: "arn:aws:iam::<account_id>:role/<role-name>"
    compression: "gzip"
    codec:
      ndjson:
    data_source_name: "broadcom_carbonblack"
    default_bucket_owner: "<account_id>"
    bucket_owners:
      my-bucket: "<account_id>"
    disable_bucket_ownership_validation: false
    notification_type: "sqs"
    sqs:
      queue_url: "https://sqs.<aws_region>.amazonaws.com/<account_id>/<queue-name>"
    on_error: "retain_messages"
```Parameters

`notification_type` (required)  
Specifies the notification mechanism. Must be `sqs` to use Amazon SQS for Amazon S3 event notifications.

`data_source_name` (required)  
Identifies the data source. This can be any string value that represents your data source. Example: `broadcom_carbonblack`.

`aws.region` (required)  
The AWS Region where the Amazon S3 bucket and Amazon SQS queue are located.

`aws.sts_role_arn` (required)  
The ARN of the IAM role to assume for accessing Amazon S3 and Amazon SQS resources.

`codec` (required)  
Codec configuration for parsing Amazon S3 objects. Supports `csv`, `json`, `ndjson` codecs.

`compression` (optional)  
Compression type of the Amazon S3 objects. Valid values are `none`, `gzip`, `automatic`. Defaults to `none`.

`sqs.queue_url` (required)  
The complete Amazon SQS queue URL that receives Amazon S3 bucket notifications when new objects are created.

`on_error` (optional)  
Determines how to handle errors in Amazon SQS. Can be either `retain_messages` or `delete_messages`. Default is `retain_messages`.