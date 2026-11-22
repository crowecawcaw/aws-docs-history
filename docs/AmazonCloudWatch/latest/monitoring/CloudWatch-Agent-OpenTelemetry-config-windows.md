

# Collect Windows event logs

The `windows_events` source collects events from the Windows Event Log and sends them to the CloudWatch Logs OTLP logs endpoint. This source is available only on servers running Windows Server. It contains one field, `collect_list`.
+ `collect_list` – Required if `windows_events` is included. Contains an array of entries, each of which specifies one Windows Event Log channel to collect. The array must contain at least one entry. Each entry can include the following fields:
  + `event_name` – Required. Specifies the Windows Event Log channel to collect from, such as `System` or `Application`. The maximum length is 255 characters.
  + `event_levels` – Optional. Specifies the event severity levels to collect. Valid values are `CRITICAL`, `ERROR`, `WARNING`, `INFORMATION`, and `VERBOSE`. If you omit this field, the agent collects events of all levels.
  + `event_ids` – Optional. Specifies a list of specific event IDs to collect. Each ID must be between 0 and 65535.
  + `event_format` – Optional. Specifies the output format. Valid values are `xml`, which sends the raw XML of the event, and `text`, which sends a structured representation. If you omit this field, the agent uses `text`.
  + `log_group_name` – Optional. Specifies the log group name to use in CloudWatch Logs. The maximum length is 512 characters. If you omit this field, the agent uses `/aws/cwagent/windows_events`.
  + `log_stream_name` – Optional. Specifies the log stream name to use in CloudWatch Logs. The maximum length is 512 characters. If you omit this field, the agent uses the host identifier and the event channel name, separated by a slash.

The following `opentelemetry` section collects error and warning events from the System and Application event logs. If you don't specify `log_group_name`, the agent sends events to the `/aws/cwagent/windows_events` log group, with one log stream for each instance and event channel.

```json
{
  "opentelemetry": {
    "collect": {
      "windows_events": {
        "collect_list": [
          { "event_name": "System", "event_levels": ["ERROR", "WARNING"] },
          { "event_name": "Application", "event_levels": ["ERROR"] }
        ]
      }
    }
  }
}
```

For how the agent stores Windows events in CloudWatch Logs, see [How the agent stores logs](CloudWatch-Agent-OpenTelemetry-config.md#CloudWatch-Agent-OpenTelemetry-config-logs). For the prerequisites, see [Prerequisites](CloudWatch-Agent-OpenTelemetry-config.md#CloudWatch-Agent-OpenTelemetry-config-prereqs). For how to start the agent and verify data, see [Start the agent and verify data](CloudWatch-Agent-OpenTelemetry-config.md#CloudWatch-Agent-OpenTelemetry-config-start).