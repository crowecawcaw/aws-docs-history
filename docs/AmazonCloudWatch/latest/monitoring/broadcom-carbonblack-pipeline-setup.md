# CloudWatch pipelines configuration for Broadcom Carbon Black

Collects endpoint detection and response data from Broadcom Carbon Black through Amazon S3 bucket ingestion.

Configure the Broadcom Carbon Black source with the following parameters:

```
source:
  s3:
    notification_type: sqs
    data_source_name: broadcom_carbonblack
    codec:
      ndjson:
    sqs:
      queue_url: "https://sqs.us-east-1.amazonaws.com/123456789012/carbon-black-queue"
    aws:
      region: "us-east-1"
      sts_role_arn: "arn:aws:iam::123456789012:role/PipelineRole"
```

###### Parameters

`notification_type` (required)

Must be `sqs`.

`data_source_name` (required)

Must be `broadcom_carbonblack`.

`codec` (required)

Must be `ndjson` for Carbon Black event exports.

`sqs.queue_url` (required)

The Amazon SQS queue URL that receives Amazon S3 event notifications when new Carbon Black export files are created.

`aws.region` (required)

The AWS Region where the Amazon S3 bucket and Amazon SQS queue are located.

`aws.sts_role_arn` (required)

The ARN of the IAM role that the pipeline assumes to read from the Amazon S3 bucket and Amazon SQS queue.
