# Sinks

Sinks define the destination where processed log data is sent. Each pipeline must have
exactly one sink. Currently, only CloudWatch Logs sink is supported.

| Sink behavior by source type | Source Type           | Log Group Configuration                          | Behavior |
| ---------------------------- | --------------------- | ------------------------------------------------ | -------- |
| CloudWatch Logs              | Must use `@original`  | Events are sent back to their original log group |
| S3                           | Custom log group path | Events are sent to the specified log group       |
| Third-party APIs             | Custom log group path | Events are sent to the specified log group       |

###### Configuration

Configure the sink with the following parameters:

###### Example Non-CloudWatch Logs source configuration

```
sink:
  cloudwatch_logs:
    log_group: "/aws/my-application/logs"
```

###### Example CloudWatch Logs source configuration

```
sink:
  cloudwatch_logs:
    log_group: "@original"
```

###### Parameters

`log_group` (required)

The name of the CloudWatch Logs log group where processed events will be sent. For
pipelines with non-`cloudwatch_logs` sources, this must be an
existing log group name. For pipelines using the `cloudwatch_logs`
source, the ONLY allowed value is `@original`.

## Requirements and limitations

Log group existence

If created using the AWS Management Console, CloudWatch will attempt to create the
specified log group and appropriate resource policy if it does not exist
when using a non-CloudWatch logs source. Otherwise, the specified log group
must exist before creating the pipeline.

Event size

Each log event cannot exceed 256 KB in size after processing.

Log group retention

The pipeline uses the retention settings configured on the destination log
group.

Log group resource policy

CloudWatch Logs resource policies are required for pipelines that write to
log groups, except for pipelines using the `cloudwatch_logs`
source. When you use the AWS Management Console to configure the pipeline, CloudWatch
will attempt to add the resource policy if needed. If you are creating the
pipeline using the AWS CLI or an API, you must create the policy manually and
add it using the `logs:PutResourcePolicy` request. For more
information, see [Resource policies](pipeline-iam-reference.md#resource-policies "pipeline-iam-reference.md#resource-policies").

Cross-Region support

The destination log group must be in the same Region as the
pipeline.

###### Important

For pipelines using the `cloudwatch_logs` source type:

- You must use `@original` as the log group value.
- Events are always sent back to their original log group.
- The original log group must exist throughout the pipeline's
  lifecycle.
- Pipelines with processors mutate the log events in the original CloudWatch log group they are intercepted from for logs from AWS services.

###### Note

Log events are subject to CloudWatch Logs quotas and limitations.
