# CloudWatch pipelines configuration for Cisco FTD

The Cisco FTD setup reads log data from Amazon S3 buckets using Amazon SQS notifications for new object events.

Configure the Cisco FTD source with the following parameters:

```
source:
  s3:
    aws:
      region: "<region>"
      sts_role_arn: "arn:aws:iam::<account>:role/<role-name>"
    compression: "gzip"
    codec:
      newline:
    data_source_name: "cisco_ftd"
    default_bucket_owner: "<account-id>"
    bucket_owners:
      <bucket-name>: "<account-id>"
    notification_type: "sqs"
    sqs:
      queue_url: "https://sqs.<region>.amazonaws.com/<account>/<queue-name>"
```

###### Parameters

`sqs.queue_url` (required)

Amazon SQS queue receiving Amazon S3 event notifications.

`data_source_name` (required)

Set to `cisco_ftd`.

`aws.region` (required)

Region of Amazon S3 and Amazon SQS.

`aws.sts_role_arn` (required)

IAM role to assume for Amazon S3/Amazon SQS access.

`notification_type` (required)

Set to `sqs`.

`codec` (required)

Codec for parsing Amazon S3 objects. Cisco FTD uses `newline`.

`bucket_owners` (optional)

Mapping of Amazon S3 bucket to AWS account ID.

`default_bucket_owner` (optional)

Default AWS account ID.

`compression` (optional)

Default `none`.

###### Note

The `sts_role_arn` role must have permissions to read from Amazon S3 and receive/delete Amazon SQS messages. See the [pipeline IAM reference](pipeline-iam-reference.md#source-specific-iam-policies "pipeline-iam-reference.md#source-specific-iam-policies") for the required trust policy and permissions policy.
