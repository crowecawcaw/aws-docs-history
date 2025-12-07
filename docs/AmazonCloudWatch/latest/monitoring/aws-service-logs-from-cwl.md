# AWS service logs from CloudWatch Logs

Intercepts log events from CloudWatch Logs that match the log event metadata
configuration.

###### Important

Pipelines with processors mutate the log events in the original CloudWatch log
group they are intercepted from for logs from AWS services.

###### Configuration

Configure the CloudWatch Logs source with the following parameters:

```
source:
  cloudwatch_logs:
    aws:
      sts_role_arn: "arn:aws:iam::123456789012:role/MyCloudWatchLogsRole"
    log_event_metadata:
      data_source_name: "<data_source_name>"
      data_source_type: "<data_source_type>"
```

###### Parameters

`aws.sts_role_arn` (required)

The ARN of the IAM role to assume for CloudWatch Logs interception.

`log_event_metadata.data_source_name` (required)

Identifies the specific AWS service that generated the log events or a
custom log source name. For custom logs, this can be any string up to 15
characters when `data_source_type` is "default".

`log_event_metadata.data_source_type` (required)

Specifies the category or type of logs within the AWS service, or
"default" for custom logs. Set to "default" to enable custom log source
names.

For more information on data source name and type, see the [CloudWatch Logs User Guide](../logs/data-source-discovery-management.md#how-to-get-started-data-sources "../logs/data-source-discovery-management.md#how-to-get-started-data-sources").

###### Restrictions

The following restrictions apply to CloudWatch Logs sources:

- No two pipelines can use the `cloudwatch_logs` source with
  identical `data_source_name` and `data_source_type`
  metadata criteria.
- When `data_source_name` is `aws_cloudtrail`, only empty
  processors (`[]`) or the `ocsf` processor are
  allowed.
