# Example telemetry event in CloudWatch Lambda Insights

Each invocation of a Lambda function that has Lambda Insights enabled writes a single
log event to the
`/aws/lambda-insights` log group.
Each log event contains metrics in embedded metric format. For more information about embedded metric format,
see [Embedding metrics within logs](CloudWatch_Embedded_Metric_Format.md "CloudWatch_Embedded_Metric_Format.md").

To analyze these log events, you can use the following methods:

- The Lambda Insights section of the CloudWatch console, as explained in
  [Viewing your Lambda Insights metrics](Lambda-Insights-view-metrics.md "Lambda-Insights-view-metrics.md").
- Log event queries using CloudWatch Logs Insights. For more information, see [Analyzing Log Data with CloudWatch Logs
  Insights](../logs/AnalyzingLogData.md "../logs/AnalyzingLogData.md").
- Metrics collected in the `LambdaInsights` namespace, which you graph by using CloudWatch
  metrics.
  The following is an example of a Lambda Insights log event with embedded metric format.

```
{
    "_aws": {
        "Timestamp": 1605034324256,
        "CloudWatchMetrics": [
            {
                "Namespace": "LambdaInsights",
                "Dimensions": [
                    [ "function_name" ],
                    [ "function_name", "version" ]
                ],
                "Metrics": [
                    { "Name": "memory_utilization", "Unit": "Percent" },
                    { "Name": "total_memory", "Unit": "Megabytes" },
                    { "Name": "used_memory_max", "Unit": "Megabytes" },
                    { "Name": "cpu_total_time", "Unit": "Milliseconds" },
                    { "Name": "tx_bytes", "Unit": "Bytes" },
                    { "Name": "rx_bytes", "Unit": "Bytes" },
                    { "Name": "total_network", "Unit": "Bytes" },
                    { "Name": "init_duration", "Unit": "Milliseconds" }
                ]
            }
        ],
        "LambdaInsights": {
            "ShareTelemetry": true
        }
    },
    "event_type": "performance",
    "function_name": "cpu-intensive",
    "version": "Blue",
    "request_id": "12345678-8bcc-42f7-b1de-123456789012",
    "trace_id": "1-5faae118-12345678901234567890",
    "duration": 45191,
    "billed_duration": 45200,
    "billed_mb_ms": 11571200,
    "cold_start": true,
    "init_duration": 130,
    "tmp_free": 538329088,
    "tmp_max": 551346176,
    "threads_max": 11,
    "used_memory_max": 63,
    "total_memory": 256,
    "memory_utilization": 24,
    "cpu_user_time": 6640,
    "cpu_system_time": 50,
    "cpu_total_time": 6690,
    "fd_use": 416,
    "fd_max": 32642,
    "tx_bytes": 4434,
    "rx_bytes": 6911,
    "timeout": true,
    "shutdown_reason": "Timeout",
    "total_network": 11345,
    "agent_version": "1.0.72.0",
    "agent_memory_avg": 10,
    "agent_memory_max": 10
}
```

The following is an example of a Lambda Insights log event for a Lambda function running on Lambda Managed Instances.

```
{
    "total_network": 16443,
    "tmp_free": 531492864,
    "total_memory": 2048,
    "fd_use": 85,
    "tmp_used": 11984896,
    "execution_environment_init": false,
    "version": "3",
    "event_type": "performance",
    "agent_memory_max": 6,
    "fd_max": 1024,
    "function_name": "cpu-intensive",
    "tx_bytes": 8404,
    "memory_utilization": 3,
    "used_memory_max": 73,
    "memory_utilization_max": 3,
    "cpu_system_time": 541,
    "threads_max": 49,
    "tmp_max": 543477760,
    "cpu_utilization_max": 2,
    "agent_memory_avg": 6,
    "cpu_total_time": 815,
    "rx_bytes": 8039,
    "lambda_mode": "managed-instance",
    "agent_version": "1.0.660.0",
    "_aws": {
        "CloudWatchMetrics": [
            {
                "Namespace": "LambdaInsights",
                "Dimensions": [
                    [
                        "function_name"
                    ],
                    [
                        "function_name",
                        "version"
                    ]
                ],
                "Metrics": [
                    {
                        "Name": "cpu_total_time",
                        "Unit": "Milliseconds"
                    },
                    {
                        "Name": "cpu_utilization",
                        "Unit": "Percent"
                    },
                    {
                        "Name": "cpu_utilization_max",
                        "Unit": "Percent"
                    },
                    {
                        "Name": "tx_bytes",
                        "Unit": "Bytes"
                    },
                    {
                        "Name": "rx_bytes",
                        "Unit": "Bytes"
                    },
                    {
                        "Name": "total_network",
                        "Unit": "Bytes"
                    },
                    {
                        "Name": "used_memory_max",
                        "Unit": "Megabytes"
                    },
                    {
                        "Name": "memory_utilization",
                        "Unit": "Percent"
                    },
                    {
                        "Name": "memory_utilization_max",
                        "Unit": "Percent"
                    },
                    {
                        "Name": "total_memory",
                        "Unit": "Megabytes"
                    },
                    {
                        "Name": "tmp_used",
                        "Unit": "Bytes"
                    },
                    {
                        "Name": "tmp_free",
                        "Unit": "Bytes"
                    }
                ]
            }
        ],
        "Timestamp": 1764164871353,
        "LambdaInsights": {
            "ShareTelemetry": true
        }
    },
    "cpu_utilization": 1,
    "cpu_user_time": 273
}
```
