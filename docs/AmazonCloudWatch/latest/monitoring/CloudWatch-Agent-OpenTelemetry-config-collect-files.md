

# Collect log files

The `files` source collects log files from the host and sends them to the CloudWatch Logs OTLP logs endpoint. It contains one field, `collect_list`.
+ `collect_list` – Required if `files` is included. Contains an array of entries, each of which specifies one set of log files to collect. The array must contain at least one entry. Each entry can include the following fields:
  + `file_path` – Required. Specifies the path or glob pattern of the log files to collect. The maximum length is 4096 characters.
  + `log_group_name` – Optional. Specifies the log group name to use in CloudWatch Logs. The maximum length is 512 characters. You can use `{instance_id}`, `{hostname}`, `{local_hostname}`, and `{ip_address}` as variables within the name. If you omit this field, the agent uses `/aws/cwagent/files`. On Kubernetes, the agent includes the cluster name, as in `/aws/cwagent/{cluster_name}/files`.
  + `log_stream_name` – Optional. Specifies the log stream name to use in CloudWatch Logs. The maximum length is 512 characters. This field supports the same variables as `log_group_name`. If you omit this field, the agent uses the host identifier and the log file name, separated by a slash (for example, `i-0123456789abcdef0/app.log`).
  + `multi_line_start_pattern` – Optional. Specifies a regular expression that marks the start of a new log entry. The agent appends lines that don't match the pattern to the previous entry. Specify the value `{timestamp_format}` to derive the pattern from `timestamp_format`.
  + `timestamp_format` – Optional. Specifies the format used to parse timestamps from log lines. For example, `%Y-%m-%d %H:%M:%S`.
  + `timezone` – Optional. Specifies the time zone to use when parsing timestamps. Valid values are `UTC` and `Local`. The default value is `Local`.
  + `encoding` – Optional. Specifies the encoding of the log files. If you omit this field, the agent uses the default `utf-8`.

The following `opentelemetry` section collects application log files:

```json
{
  "opentelemetry": {
    "collect": {
      "files": {
        "collect_list": [
          {
            "file_path": "/var/log/app/*.log",
            "log_group_name": "/app/logs",
            "log_stream_name": "{instance_id}"
          }
        ]
      }
    }
  }
}
```

For how the agent stores log files in CloudWatch Logs, see [How the agent stores logs](CloudWatch-Agent-OpenTelemetry-config.md#CloudWatch-Agent-OpenTelemetry-config-logs). For the prerequisites, see [Prerequisites](CloudWatch-Agent-OpenTelemetry-config.md#CloudWatch-Agent-OpenTelemetry-config-prereqs). For how to start the agent and verify data, see [Start the agent and verify data](CloudWatch-Agent-OpenTelemetry-config.md#CloudWatch-Agent-OpenTelemetry-config-start).