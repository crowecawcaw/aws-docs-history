

# Custom log data from CloudWatch Logs or an Amazon S3 bucket
<a name="ingestion-custom-data-sources"></a>

You can create pipelines for custom data sources using the following approaches:

1. **CloudWatch Custom Logs** – Define pipelines on your existing CloudWatch custom log groups by providing:
   + A data source name
   + A data source type

   For more information on data source name and type, see the [CloudWatch Logs User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/data-source-discovery-management.html#how-to-get-started-data-sources).

1. **CloudWatch Logs Syslog service** – Process Syslog messages delivered to a CloudWatch Logs log group. Before creating the pipeline, complete [Setting up syslog ingestion](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_Syslog_Setup.html) and verify that messages are arriving in the destination log group.

   In the console, choose **CloudWatch Logs syslog service** and select RFC 5424, RFC 3164, Cisco, or F5. For API or AWS CLI configuration, use the `cloudwatch_logs` source with `syslog` as the data source name and the corresponding data source type: `rfc5424`, `rfc3164`, `cisco`, or `f5_bigip`.

   ```
   source:
     cloudwatch_logs:
       aws:
         sts_role_arn: "arn:aws:iam::123456789012:role/MyCloudWatchLogsRole"
       log_event_metadata:
         data_source_name: "syslog"
         data_source_type: "rfc5424"
   ```

   A pipeline matches one data source name and type. Create a separate pipeline for each Syslog format that you want to process. Syslog messages are parsed during ingestion, so pipeline processors are optional.

   For the shared source parameter reference and restrictions, see [AWS service logs from CloudWatch Logs](aws-service-logs-from-cwl.md). For pipeline IAM requirements, see [Custom and Syslog data from CloudWatch Logs](pipeline-iam-reference.md#custom-data-cloudwatch-logs).

1. **S3 Custom Sources** – Process arbitrary logs stored in S3 buckets by configuring source for the pipeline:

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
**Note**  
The CSV processor can't be used with S3 custom sources. Instead, use the CSV codec in the S3 source.

**Parameters**  
`notification_type` (required)  
Specifies the notification mechanism. Must be "sqs" to use SQS for S3 event notifications.  
`data_source_name`  
Identifies the data source. This can be any string value that represents your data source. Example: "my\_custom\_logs".  
`aws.region` (required)  
The AWS region where the S3 bucket and SQS queue are located.  
`aws.sts_role_arn` (required)  
The ARN of the IAM role to assume for accessing S3 and SQS resources.  
`codec` (required)  
Codec configuration for parsing S3 objects. Supports `csv`, `json`, `ndjson` codecs.  
`compression` (optional)  
Compression type of the S3 objects. Valid values are "none", "gzip", "automatic". Defaults to "none".  
`sqs.queue_url` (required for SQS)  
The complete SQS queue URL that receives S3 bucket notifications when new objects are created.  
`on_error` (optional)  
Determines how to handle errors in Amazon SQS. Can be either `retain_messages` or `delete_messages`. Default is `retain_messages`.

**Custom source configuration**

When creating a pipeline for custom sources:
+ A parser must be the first processor in the pipeline if the data source is CloudWatch Logs
+ You can specify any supported processor for custom log pipelines

**Topics**
+ [Configuring Custom S3 Bucket Sources](configuring-custom-s3-bucket-sources.md)