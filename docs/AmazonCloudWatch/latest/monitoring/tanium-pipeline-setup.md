

# CloudWatch pipelines configuration for Tanium
<a name="tanium-pipeline-setup"></a>

The Tanium setup on AWS reads log data from Amazon S3 buckets using Amazon SQS notifications for new object events.

Configure the S3 source with the following parameters:

```
source:
  s3:
    acknowledgments: true
    sqs:
      queue_url: "https://sqs.us-east-1.amazonaws.com/1234567890/tanium-sqs"
      maximum_messages: '10'
      visibility_duplication_protection: true
      visibility_timeout: 180s
    aws:
      region: "us-east-1"
    notification_type: sqs
    notification_source: s3
    bucket_owners:
      tanium-test-logs-test: '1234567890'
    default_bucket_owner: '1234567890'
    codec:
      ndjson: {}
    compression: none
```Parameters

`acknowledgments` (required)  
Prevents data loss by only considering logs successfully processed after they are received by the sink. Set to `true` to enable.

`sqs.queue_url` (required)  
The Amazon SQS queue URL that receives Amazon S3 event notifications when new objects land.

`sqs.maximum_messages` (optional)  
Max number of Amazon SQS messages to pull per poll (batch size, up to Amazon SQS max of 10).

`sqs.visibility_duplication_protection` (optional)  
Uses Amazon SQS visibility timeout to prevent duplicate processing of the same message by multiple workers.

`sqs.visibility_timeout` (optional)  
How long (in seconds) a message stays invisible to other consumers after being picked up, giving the worker time to process it.

`aws.region` (required)  
AWS region where the Amazon SQS queue and Amazon S3 bucket live.

`notification_type` (required)  
`sqs` – Tells the plugin to expect notifications through Amazon SQS.

`notification_source` (optional)  
`s3` – Indicates the Amazon SQS notifications originate from Amazon S3 event notifications.

`bucket_owners` (required)  
Maps specific bucket names to their owning AWS account IDs, needed for cross-account access.

`default_bucket_owner` (required)  
Fallback AWS account ID used for any bucket not explicitly listed in `bucket_owners`.

`codec` (required)  
`ndjson` – Parses each Amazon S3 object as newline-delimited JSON (one JSON record per line).

`compression` (required)  
`none` – Indicates the Amazon S3 objects are not compressed, so no decompression is applied before parsing.