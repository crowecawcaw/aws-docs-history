

# Sinks
<a name="pipeline-sinks"></a>

Sinks define the destination where processed data is sent. Logs pipelines use the `cloudwatch_logs` sink and can route events among multiple log groups. Metrics pipelines use exactly one `cloudwatch_metrics` sink.

## CloudWatch Logs sink (`cloudwatch_logs`)
<a name="cloudwatch-logs-sink"></a>

For logs pipelines, the `cloudwatch_logs` sink sends processed log events to a CloudWatch Logs log group.


| Source Type | Log group configuration | Behavior | 
| --- | --- | --- | 
| CloudWatch Logs | Use @original for a pipeline with one sink, or configure conditional sinks for routing | Events are returned to their original log group or routed to the selected destination log group | 
| S3 | Custom log group path | Events are sent to the specified log group | 
| Third-party APIs | Custom log group path | Events are sent to the specified log group | 

**Configuration**  
Configure the sink with the following parameters:

**Example Non-CloudWatch Logs source configuration**  

```
sink:
  cloudwatch_logs:
    log_group: "/aws/my-application/logs"
```

**Example CloudWatch Logs source configuration**  

```
sink:
  cloudwatch_logs:
    log_group: "@original"
```Parameters

`log_group` (required)  
The name of the CloudWatch Logs log group where processed events will be sent. For pipelines with non-`cloudwatch_logs` sources, this must be an existing log group name. For a pipeline that has one `cloudwatch_logs` sink and uses a `cloudwatch_logs` source, the value must be `@original`. A pipeline that uses conditional routing can use `@original` or another destination log group in any route.

`when` (optional)  
An expression that selects events for this route. Conditions are evaluated in sink order, and the first matching route is used. The expression can contain up to 4,096 characters. For syntax, see [Expression syntax for conditional processing](conditional-processing.md).

`is_default` (optional)  
Set to `true` on exactly one sink when the pipeline has multiple sinks. This route receives events that don't match an earlier `when` expression. Place the default route last.

`include_original` (optional)  
When present, stores a copy of each raw log event before any transformation takes place in the `@original_message` system field of the event. This preserves the original data for audit or compliance purposes. Specify as an empty object (`{}`). Available only for pipelines with `cloudwatch_logs` sources. At least one processor must be configured when this option is enabled.

**Example CloudWatch Logs sink with original log preservation**  

```
sink:
  - cloudwatch_logs:
      log_group: "@original"
      include_original: {}
```

### Route logs to multiple log groups
<a name="cloudwatch-logs-sink-routing"></a>

A logs pipeline can contain up to 10 `cloudwatch_logs` sinks, including the default route. Define a `when` expression on each conditional route and set `is_default: true` on exactly one fallback route. Each event is delivered to one destination only.

**Example Route by log level and return unmatched events to the source log group**  

```
sink:
  - cloudwatch_logs:
      log_group: "/app/errors"
      when: 'level == "ERROR"'
  - cloudwatch_logs:
      log_group: "/app/warnings"
      when: 'level == "WARN"'
  - cloudwatch_logs:
      log_group: "@original"
      is_default: true
```

For an S3 source, a destination log group can contain one template variable. Use `{s3.path.N}` to select the Nth segment of the S3 object key, starting at 1, or use a field beneath `{@pipeline_metadata.source.s3}`, such as `{@pipeline_metadata.source.s3.bucket}`. For example, `/customers/{s3.path.1}` routes an object with the key `customer-a/audit.json` to `/customers/customer-a`.

A resolved template value must contain 1–64 letters, numbers, periods, underscores, or hyphens. Each template route can resolve to at most five distinct destination log groups for one input batch. Events that exceed this limit, or whose template can't be resolved, use the configured default route. Static routes don't count toward this template limit.

### Requirements and limitations
<a name="sink-requirements"></a>

Log group existence  
If created using the AWS Management Console, CloudWatch will attempt to create the specified log group and appropriate resource policy if it does not exist when using a non-CloudWatch logs source. Otherwise, the specified log group must exist before creating the pipeline. For conditional routing, a physical default-route log group must exist before you create the pipeline. Conditional destination log groups are created when first used. The `@original` alias resolves to the source log group and is not created.

Event size  
Each log event cannot exceed 256 KB in size after processing.

Log group retention  
The pipeline uses the retention settings configured on the destination log group.

Log group resource policy  
CloudWatch Logs resource policies are required for the direct destination of S3-based and third-party API pipelines. For a `cloudwatch_logs` source, the `@original` destination does not require a resource policy. Additional named conditional and templatized destinations use the pipeline source role. When you use the AWS Management Console to configure the pipeline, CloudWatch will attempt to add the direct-destination resource policy if needed. If you create the pipeline using the AWS CLI or an API, you must create the policy manually. For more information, see [Resource policies](pipeline-iam-reference.md#resource-policies) and [Permissions for routed destinations](pipeline-iam-reference.md#routed-destination-permissions).

Cross-Region support  
The destination log group must be in the same Region as the pipeline.

**Important**  
For pipelines using the `cloudwatch_logs` source type:  
A pipeline with one sink must use `@original` as the log group value. Conditional routing can use other destination log groups.
Use `@original` in any route that should return matching events to their source log group.
The original log group must exist throughout the pipeline's lifecycle.
Pipelines with processors mutate the log events in the original CloudWatch log group they are intercepted from for logs from AWS services. To preserve the original data, enable `include_original` in the sink configuration. The original log copy is stored in the `@original_message` system field of the event.

**Note**  
Log events are subject to CloudWatch Logs quotas and limitations.

## CloudWatch Metrics sink (`cloudwatch_metrics`)
<a name="cloudwatch-metrics-sink"></a>

For metrics pipelines, the `cloudwatch_metrics` sink stores processed metrics in CloudWatch. Processed metrics are queryable through PromQL in Query Studio and fully compatible with CloudWatch Alarms, Anomaly Detection, and Dashboards.

**Configuration**  
The `cloudwatch_metrics` sink has no parameters:

```
sink:
  - cloudwatch_metrics: {}
```