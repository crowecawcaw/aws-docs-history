

# Create a CloudWatch agent configuration for OpenTelemetry

With the `opentelemetry` section of the agent configuration file, one agent collects metrics, logs, and traces from your servers and applications and sends them to the CloudWatch OpenTelemetry Protocol (OTLP) endpoints. The agent sets the endpoints, the Region, and request signing for you. You query the metrics with PromQL.

Configure one source topic for each kind of telemetry that you collect. Each source topic lists the fields of the source and shows a focused example. The prerequisites, how to start the agent and verify data, and how to split the configuration across files in this topic apply to every source. For a summary of the `opentelemetry` section structure, see [CloudWatch agent configuration file: OpenTelemetry section](CloudWatch-Agent-Configuration-File-OpenTelemetrysection.md). To compare this model with Classic metrics, see [Choose a configuration model for the CloudWatch agent](CloudWatch-Agent-config-model.md). For common customizations and the Classic settings they replace, see [Common customizations](CloudWatch-Agent-config-model.md#CloudWatch-Agent-OpenTelemetry-config-customize).

**Note**  
The configuration wizard doesn't create an `opentelemetry` section. Create the configuration file manually.

Each signal comes from one or more sources in the `collect` section:


| Signal | Sources | Destination | 
| --- | --- | --- | 
| Metrics | host\_metrics (CPU, memory, disk, file system, network, processes), prometheus (Prometheus targets), otlp (applications), and database\_insights | CloudWatch OTLP metrics endpoint, queried with PromQL | 
| Logs | files (log files), windows\_events (Windows event logs), and otlp (applications) | CloudWatch Logs OTLP logs endpoint | 
| Traces | otlp (applications) | X-Ray OTLP traces endpoint, viewed in Transaction Search | 

## Prerequisites
<a name="CloudWatch-Agent-OpenTelemetry-config-prereqs"></a>
+ Install CloudWatch agent version 1.300070.0 or later. To check the installed version on Linux, run `cat /opt/aws/amazon-cloudwatch-agent/bin/CWAGENT_VERSION`. On Windows Server, read `C:\Program Files\Amazon\AmazonCloudWatchAgent\CWAGENT_VERSION`.
+ Complete the IAM and network prerequisites. For more information, see [Prerequisites](prerequisites.md).
+ If you send traces, enable Transaction Search. For more information, see [Transaction Search](CloudWatch-Transaction-Search.md).

## Example: On-premises servers and macOS
<a name="CloudWatch-Agent-OpenTelemetry-config-onprem"></a>

On servers outside Amazon EC2, such as on-premises servers and Mac computers, the agent can't detect resource attributes that identify the host. Host metrics don't include `@resource.host.id` or `@resource.host.name`, so metrics from different servers can't be told apart. Set an identifier for each server with `resource_attributes`.

The following configuration sets `host.name`, collects host metrics and log files, and receives metrics, logs, and traces from applications over OTLP. The `{hostname}` variable names each log stream after the server.

```json
{
  "opentelemetry": {
    "resource_attributes": {
      "host.name": "{{server-01}}",
      "deployment.environment.name": "production"
    },
    "collect": {
      "host_metrics": {},
      "files": {
        "collect_list": [
          {
            "file_path": "/var/log/app/*.log",
            "log_group_name": "/app/logs",
            "log_stream_name": "{hostname}"
          }
        ]
      },
      "otlp": {}
    }
  }
}
```

Start the agent with `-m onPremise`. The agent uses the credentials and Region from the `AmazonCloudWatchAgent` profile. For more information, see [(Installing on an on-premises server) Specify IAM credentials and AWS Region](install-CloudWatch-Agent-on-premise.md#install-CloudWatch-Agent-iam_user-SSM-onprem).

## Start the agent and verify data
<a name="CloudWatch-Agent-OpenTelemetry-config-start"></a>

1. Start the agent with your configuration file. The following command is for an Amazon EC2 instance running Linux.

   ```
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:{{/path/to/config.json}} -s
   ```

   For other platforms, see [Starting the CloudWatch agent](start-CloudWatch-Agent-on-premise-SSM-onprem.md).

   If the command doesn't return, the agent might be unable to reach the Amazon EC2 API. For more information, see [Network requirements](prerequisites.md#CloudWatch-Agent-network-requirements).

1. Confirm that the agent is running:

   ```
   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a status
   ```

1. In the CloudWatch console, open Query Studio and run a PromQL query for a host metric from the server. For example, on an Amazon EC2 instance:

   ```
   {"system.memory.utilization", "@resource.host.id"="{{i-1234567890abcdef0}}"}
   ```

   On an on-premises server or Mac computer, filter on the `resource_attributes` that you set, such as `@resource.host.name`. Metrics typically appear within 1–2 minutes. A PromQL selector must include a metric name, so you can't select all metrics for an instance by label alone. To check a metric that receives data points infrequently, use `last_over_time`, for example `last_over_time({"{{my_metric}}"}[15m])`. For more information, see [Running PromQL queries in Query Studio](CloudWatch-PromQL-QueryStudio.md).

1. For log files and Windows events, open the log group in the CloudWatch Logs console and confirm that the log streams exist.

## How the agent stores logs
<a name="CloudWatch-Agent-OpenTelemetry-config-logs"></a>

The agent sends log files and Windows events to CloudWatch Logs as OpenTelemetry log records. Each log event is a JSON object with the following fields:
+ `body` — The original log line. For Windows events, a JSON object that contains the event fields, such as `channel`, `level`, and `provider`.
+ `resource.attributes` — Attributes that identify the source, such as `host.id`, `host.name`, `log.file.name`, and any `resource_attributes` that you set.
+ `severityText` and `severityNumber` — For Windows events, the event level.
+ `timeUnixNano` and `observedTimeUnixNano` — The event time and the time that the agent read the event. For log files, `timeUnixNano` is `0` unless you set `timestamp_format`.

To work with the original log line in CloudWatch Logs Logs Insights, query the `body` field.

## Split the configuration across files
<a name="CloudWatch-Agent-OpenTelemetry-config-multiple"></a>

You can split an `opentelemetry` configuration across multiple files and combine them with the `append-config` option. The agent merges the sources under `collect` from each file. For example, one file can configure `host_metrics` and `files` for all servers, and a second file can add `otlp` and `prometheus` on servers that run instrumented applications.

Each source can appear in only one file. If two files configure the same source, such as `files`, the agent fails to merge them with the error `Different values are specified for files`. Put all entries for a source in the same file. For more information about multiple configuration files, see [Creating multiple CloudWatch agent configuration files](create-cloudwatch-agent-configuration-file.md#CloudWatch-Agent-multiple-config-files).