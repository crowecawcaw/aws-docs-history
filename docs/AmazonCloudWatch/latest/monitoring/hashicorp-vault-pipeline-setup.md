

# CloudWatch pipelines configuration for HashiCorp Vault
<a name="hashicorp-vault-pipeline-setup"></a>

The HashiCorp Vault setup on AWS reads log data from Amazon S3 buckets using Amazon SQS notifications for new object events.

Configure the S3 source with the following parameters:

```
source:
  s3:
    aws:
      region: "us-east-1"
      sts_role_arn: "arn:aws:iam::<account>:role/<role-name>"
    compression: "gzip"
    codec:
      ndjson:
    data_source_name: "hashicorp_vault"
    default_bucket_owner: "123456789012"
    bucket_owners:
      my-bucket: "123456789012"
    disable_bucket_ownership_validation: false
    notification_type: "sqs"
    sqs:
      queue_url: "https://sqs.region.amazonaws.com/<account>/<queue-name>"
```Parameters

`notification_type` (required)  
Specifies the notification mechanism. Must be "sqs" to use SQS for S3 event notifications.

`data_source_name` (required)  
Identifies the data source. Must be "hashicorp\_vault".

`aws.region` (required)  
The AWS region where the S3 bucket and SQS queue are located.

`aws.sts_role_arn` (required)  
The ARN of the IAM role to assume for accessing S3 and SQS resources.

`codec` (required)  
Codec configuration for parsing S3 objects. Supports csv, json, ndjson codecs.

`compression` (optional)  
Compression type of the S3 objects. Valid values are "none", "gzip", "automatic". Defaults to "none".

`sqs.queue_url` (required for SQS)  
The complete SQS queue URL that receives S3 bucket notifications when new objects are created.